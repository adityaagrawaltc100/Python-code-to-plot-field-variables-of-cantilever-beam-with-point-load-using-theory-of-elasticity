import numpy as np
import matplotlib.pyplot as plt
Q = 1000
l = 100
d = 1
b = 10
e = 10000
k = 0.3
xlist = np.linspace(0.0, 100.0, 20)
ylist = np.linspace(-5.0, 5.0, 10)
x,y = np.meshgrid(xlist, ylist)
z = ((12*Q)/(e*d*b**3))*(0.5*k*y**2*(l-x) + 0.5*l*x**2 - (x**3/6) + 0.25*x*b**2*(1+k))
fig, ax = plt.subplots(1,1)
cp = ax.contourf(x,y,z)
plt.show()