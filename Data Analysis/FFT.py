import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft
from matplotlib.ticker import (AutoMinorLocator, MultipleLocator)
s = 2000  # number of samples
f = 1000  # Sampling Freq


[t41,v41] = np.loadtxt('C:\\Users\\achil\\OneDrive\\Documents\\Fall 2019\\MAE 157\\Hot Wire\\LabData\\_41in.csv', delimiter = ',', unpack = True)
[t99,v99] = np.loadtxt('C:\\Users\\achil\\OneDrive\\Documents\\Fall 2019\\MAE 157\\Hot Wire\\LabData\\_99in.csv', delimiter = ',', unpack = True)
[t159,v159] = np.loadtxt('C:\\Users\\achil\\OneDrive\\Documents\\Fall 2019\\MAE 157\\Hot Wire\\LabData\\1_59in.csv', delimiter = ',', unpack = True)

freq = np.arange(s) * f / s  # Discretizing the frequency axis
int = np.fft.fft(v41)
int2 = np.fft.fft(v99)
int3 = np.fft.fft(v159)


f, (p41,p99,p159) = plt.subplots(3,1, sharex = True)

p41.set_title('(a)')
p99.set_title('(b)')
p159.set_title('(c)')
p99.set_ylabel('Normalized Response')
p159.set_xlabel('Frequency [hz]')
p41.xaxis.set_minor_locator(AutoMinorLocator(2))
p41.xaxis.set_major_locator(MultipleLocator(20))
p99.xaxis.set_minor_locator(AutoMinorLocator(2))
p159.xaxis.set_minor_locator(AutoMinorLocator(2))
p41.tick_params(which = 'both',direction="in")
p99.tick_params(which = 'both',direction="in")
p159.tick_params(which = 'both',direction="in")
p41.set_ylim([0,30])
p99.set_ylim([0,40])
p159.set_ylim([0,30])
p41.set_xlim([10,100])
p99.set_xlim([10,100])
p159.set_xlim([10,100])

p41.plot(freq,int.real)
p99.plot(freq,int2.real)
p159.plot(freq,int3.real)

plt.show()
