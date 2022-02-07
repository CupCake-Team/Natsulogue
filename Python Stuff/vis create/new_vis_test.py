import librosa, os, sys
import numpy as np
from tinytag import TinyTag

sa = "just.ogg"

#name = TinyTag.get(sys.argv[1])

name = TinyTag.get(sa)

mlen = name.duration

RATE = 44100

#time_series, sample_rate = librosa.load(sys.argv[1])

time_series, sample_rate = librosa.load(sa)

stft = np.abs(librosa.stft(time_series, hop_length=512, n_fft=2048*4))

spectrogram = librosa.amplitude_to_db(stft, ref=np.max)

frequencies = librosa.core.fft_frequencies(n_fft=2048*4) #10724

times = librosa.core.frames_to_time(np.arange(spectrogram.shape[1]), sr=RATE, hop_length=512, n_fft=2048*4)

time_index_ratio = len(times)/times[len(times) - 1]

frequencies_index_ratio = len(frequencies)/frequencies[len(frequencies)-1]

#new_s = spectrogram * 0.8 * (spectrogram / 20)

new_s = 80 + spectrogram


def get_decibel(target_time, freq):
    k = new_s[int(freq*frequencies_index_ratio)][int(target_time*time_index_ratio)]
    return str(k)

deltime = 0.0167
delfreq = 200
ctime = 0
cfreq = 0

print(mlen)
print(time_index_ratio)

with open("data.txt", "w") as d:
    while True:
        try:
            
            d.write(get_decibel(ctime, cfreq))
            d.write(" ")
            
            if cfreq >= 10000:
                cfreq = 0
                ctime = ctime + deltime
                d.write("\n")
            else:
                cfreq = cfreq + delfreq
        except:
            break

            
        


