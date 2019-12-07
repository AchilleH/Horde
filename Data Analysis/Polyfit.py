#Program to fit data to 5th order polynomial
import numpy as np
import matplotlib.pyplot as plt
import numpy.polynomial.polynomial as poly
from matplotlib.ticker import (AutoMinorLocator, MultipleLocator)

#################################################
# Calibration Data Reduction
#################################################
#Voltage
E = np.array([1.687,1.759,1.812,1.851,1.88,1.908,1.929,1.948])
#Freestream Velocity
U = np.array([10.34580108,14.02308097,17.35491861,19.95675324,22.25647771,24.59421883,26.54135641,28.26717531])
#This will return the coefficients of the polynomial in descending order: 5th,4th,3rd,2nd,...
p = np.polyfit(E,U,5)
py = np.poly1d(p)
x = np.arange(1.65,2,0.01)

print('Polynomial Coefficients in Descending Order:\n')
print(p)

#################################################
# Constant Re, Different hot wire positions
#################################################
vpos = [6,5,4,3,2,1.5,1,0.5,0]
volt = [1.866,1.865,1.86,1.852,1.851,1.847,1.841,1.838,1.832]
print('Velocity values(6in - 0 in)')
print(py(volt))

plt.figure(1)
plt.scatter(E,U,color='k')
plt.plot(x,py(x),color='k')
plt.xlabel('Voltage[V]')
plt.ylabel('Velocity[m/s]')
plt.tick_params(which = 'major',direction="in")
plt.tick_params(which = 'minor',direction="in")

plt.figure(2)
plt.scatter(py(volt),vpos, color='k')
plt.xlabel('Velocity[m/s]')
plt.ylabel('Vertical Pos[in]')
plt.tick_params(which = 'major',direction="in")
plt.tick_params(which = 'minor',direction="in")

plt.show()
