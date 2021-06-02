import os
import matplotlib.pyplot as plt
from thinkdsp import read_wave
from thinkdsp import decorate
from IPython.display import display
from ipywidgets import interact, fixed
from thinkdsp import SinSignal

wave3 = read_wave('D:/123/18871__zippi1__sound-bell-440hz.wav')
wave3.normalize()
wave3.make_audio()

def stretch(wave, factor):
    wave.ts *= factor
    wave.framerate /= factor

stretch(wave3, 0.5)
wave3.make_audio()
wave3.plot()

wave3.write(filename='output.wav')
plt.show()