import numpy as np
import pyaudiowpatch as pyaudio
import socket
import struct

FORMAT = pyaudio.paInt16
CHANNELS = 2
FPB = 1024
plotsAmt = 512

p = pyaudio.PyAudio()

wasapi_info = p.get_host_api_info_by_type(pyaudio.paWASAPI)
default_speakers = p.get_device_info_by_index(wasapi_info["defaultOutputDevice"])
if not default_speakers["isLoopbackDevice"]:
    for loopback in p.get_loopback_device_info_generator():
        if default_speakers["name"] in loopback["name"]:
            default_speakers = loopback
            break

input_device_index = default_speakers["index"]

RATE = int(default_speakers["defaultSampleRate"])

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                frames_per_buffer=FPB,
                input=True,
                input_device_index=input_device_index)

def quadBezier(p0, p2, c, n, extra=False):
    x = []
    samples = n

    if extra: samples = n + 1
    for i in range(samples):
        t = i / n
        x.append((1 - t) * ((1-t) * p0 + t * c) + t * ((1-t) * c + t * p2))

    return x

def dataPlotter(values, step, limit):
    maxNum = int(values[0])
    plottedList = [maxNum]

    for i in range(1, len(values)):
        minNum = maxNum
        maxNum = step * round(values[i]/step)

        if values[i - 1] <= values[i]:
            if maxNum - minNum <= 0:
                maxNum = minNum + step
        else:
            if minNum - maxNum <= 0:
                maxNum = minNum - step

        if maxNum > max(values):
            maxNum = round(max(values) - step)
        if maxNum < 0:
            maxNum = step
        if maxNum > limit:
            maxNum = limit - step
        if minNum == maxNum:
            maxNum += step

        plottedList.append(maxNum)

    return plottedList

def savitzkyGolay(y, window_size, order, deriv=0, rate=1):
    from math import factorial
    y = np.array(y)

    window_size = np.abs(int(window_size))
    order = np.abs(int(order))

    order_range = range(order+1)
    half_window = (window_size -1) // 2

    b = np.mat([[k**i for i in order_range] for k in range(-half_window, half_window+1)])
    m = np.linalg.pinv(b).A[deriv] * rate**deriv * factorial(deriv)

    firstvals = y[0] - np.abs( y[1:half_window+1][::-1] - y[0] )
    lastvals = y[-1] + np.abs(y[-half_window-1:-1][::-1] - y[-1])
    y = np.concatenate((firstvals, y, lastvals))
    return np.convolve( m[::-1], y, mode='valid')

def get_audio_data(n):
    i = 0
    buffer = plotsAmt * 4
    dataArr, dataArr2, plotValues, audio_vals = [], [], [], []
    pointsList = [1000, 0.66, 1, 12000]
    curveList = [5, 10, 15] #почти без сглаживания, идеальное, слишком сглажено
    w = curveList[1]

    while (i < buffer-1):
        data = stream.read(1, exception_on_overflow=False)
        dataArr.append(sum(struct.unpack("2h", data)[:1]))   
        dataArr2.append(sum(struct.unpack("2h", data)[1:]))
        i += 1

    dataList = (np.array(dataArr) + np.array(dataArr2))/2
    
    plot = RATE / (buffer*2)
    
    midPoint = pointsList[0] / plot

    midPointPos = int(round(plotsAmt * pointsList[1]))

    endCurve = midPoint * pointsList[2]

    endPoint = pointsList[3] / plot

    startScale = quadBezier(0, midPoint, 0, midPointPos)
    endScale = quadBezier(midPoint, endPoint, endCurve, plotsAmt - midPointPos, True)
    plots = startScale + endScale
    plotsList = list(map(int, dataPlotter(plots, 1, (buffer*2) // 2)))

    fft_data = np.fft.rfft(dataList, len(dataList), norm="ortho")
    fft_data = np.abs(fft_data)

    for z in range(len(plotsList)-1):
        minNum = plotsList[z]
        maxNum = plotsList[z+1]

        if maxNum > minNum:
            plotValues.append(int(max(fft_data[minNum:maxNum], default=0)))
        else:
            plotValues.append(int(max(fft_data[maxNum:minNum], default=0)))

    if (w % 2) == 0: w += 1

    filtered = savitzkyGolay(plotValues, w, 3)

    #indecies

    step = (32000 - 1) / n
    frequencies = np.linspace(1, 32000, 512)

    indices = []
    for i in range(n):
        freq = 1 + i * step
        index = np.argmin(np.abs(frequencies - freq))
        indices.append(index)

    for i in indices:
        audio_vals.append(int(filtered[i]))
    
    return audio_vals

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 3030)) 
s.listen(1)
conn, addr = s.accept()

while 1:
    data = conn.recv(1024)
    if not data:
        break
    num_bar = int(data.decode('utf-8'))

    f = get_audio_data(num_bar)

    data_str = ""

    for ind, i in enumerate(f):
        if ind < len(f)-1:
            data_str += str(i) + " "
        else:
            data_str += str(i)

    conn.send(data_str.encode())

conn.close()