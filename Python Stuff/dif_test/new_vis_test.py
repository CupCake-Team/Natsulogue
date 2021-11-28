import librosa, os, shutil, cv2
import numpy as np
import imageio as io
from PIL import Image



strokes = [3, 5, 7, 10, 12, 14, 17, 19, 21, 24, 26, 28, 30, 33, 35, 37, 40, 42, 44, 47, 49, 51, 54, 56, 58, 61, 63, 65, 68, 70, 72, 75, 77, 79, 82, 84, 86, 89, 91, 93, 96, 98, 100, 103, 105, 107, 110, 112, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127]

RATE = 44100

c_t = 0

num = 0

frames = []

cdr = Image.new("RGBA", (452, 160))

v_img = Image.open("visbar.png")

v_img = v_img.resize((3,160))

os.makedirs("cadres")

time_series, sample_rate = librosa.load("herewego.ogg")

stft = np.abs(librosa.stft(time_series, hop_length=512, n_fft=2048*8))

spectrogram = librosa.amplitude_to_db(stft, ref=np.max)

frequencies = librosa.core.fft_frequencies(n_fft=2048*8)

times = librosa.core.frames_to_time(np.arange(spectrogram.shape[1]), sr=RATE, hop_length=512, n_fft=2048*8)

time_index_ratio = len(times)/times[len(times) - 1]

frequencies_index_ratio = len(frequencies)/frequencies[len(frequencies)-1]

new_s = spectrogram * 0.8 * (spectrogram / 20)



def get_decibel(target_time, freq):
    k = (new_s[int(freq*frequencies_index_ratio)][int(target_time*time_index_ratio)])
    return int(k)



def create_cadre(cur_time, save_num):
    global v_img, cdr
    f_n = 1
    hz = 100
    x = 0
    while f_n < 69:
        cdr.paste(v_img, (x, get_decibel(cur_time, hz)))
        f_n = f_n + 1
        x = x + 7
        if hz <= 1000:
            hz = hz + 20    #40
        if hz > 1000 and hz <= 5000:
            hz = hz + 85    #170
        if hz > 5000:
            hz = hz + 132   #235
    cdr.save("cadres/c"+str(save_num)+".png")
    cdr.close()



while True:
    try:
        create_cadre(c_t, num)
        c_t = c_t + 0.02
        num = num + 1
        cdr = Image.new("RGBA", (452, 160))
    except:
        cdr.close()
        v_img.close()
        break


#with io.get_writer('test.gif', mode='I', fps=25) as writer:
  #  for c in range (0, len(os.listdir('cadres'))-1):
   #     image = io.imread("cadres\\c" + str(c) + ".png")
   #     writer.append_data(image)



image_folder = 'cadres'

video_name = 'video.avi'

arr = []

for imgnum in range (len(os.listdir(image_folder))-1):
    frame = cv2.imread(image_folder + "/c" + str(imgnum) + ".png")
    height, width, layers = frame.shape
    size = (width,height)
    arr.append(frame)
    
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
video = cv2.VideoWriter(video_name, fourcc, 25, size)

for k in range (len(arr)):
    video.write(arr[k])
#cv2.destroyAllWindows()
video.release()

        
#shutil.rmtree("cadres")


