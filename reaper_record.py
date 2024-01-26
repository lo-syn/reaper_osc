from pythonosc.udp_client import SimpleUDPClient
from scipy.io import wavfile
from lib_reaper_cmds import *
import time
import glob
import numpy as np
import os

reaper_dir = str(r"C:\Program Files\REAPER (x64)\reaper.exe")

process = reaper_start(reaper_dir, True)
time.sleep(5)
client = reaper_client_setup(port = 8000)

time.sleep(1) # Required to let UDP Client initialise
reaper_record(client)
time.sleep(2)
reaper_stop(client)
time.sleep(1)
process.terminate()
print("Terminated")

SCALE_V = 11 / (2**15)
SCALE_I = 3 / (2**15)

file = glob.glob('./reaper_osc/Media/*.wav')

samplerate, data = wavfile.read(file[0])
test = os.listdir('./reaper_osc/Media/')

for item in test:
    if item.endswith(".wav") or item.endswith(".reapeaks"):
        os.remove(os.path.join('./reaper_osc/Media/', item))

length = data.shape[0] / samplerate
time = np.linspace(0., length, data.shape[0])
convert_16bit = float(2**15)
export_data = []
export_data.append(time)
for i in range(data.shape[1]):
    plot_data = (data[:, i] / (convert_16bit))
    plot_data = list(plot_data * SCALE_V)
    export_data.append(plot_data)
export_data = np.array(export_data)
export_data = np.transpose(export_data)
np.savetxt("Voltage.txt", export_data, delimiter=",")