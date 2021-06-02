import os
import matplotlib.pyplot as plt
import thinkdsp as dsp
from thinkdsp import read_wave
from thinkdsp import decorate
from IPython.display import display
from ipywidgets import interact, fixed

wave = read_wave('D:/123/18871__zippi1__sound-bell-440hz.wav')
wave.normalize()
wave.make_audio()

segment = wave.segment(start=1.1, duration=5.0)

spectrum = segment.make_spectrum()

spectrum.low_pass(2000,0.3)
spectrum.make_wave().make_audio()
spectrum.plot()

wave.write(filename='output.wav')
plt.show()