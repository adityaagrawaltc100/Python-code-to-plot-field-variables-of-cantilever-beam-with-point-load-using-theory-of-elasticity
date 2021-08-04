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
z = ((12*Q)/(d*b**3))*(x*y - l*y)
fig, ax = plt.subplots(1,1)
cp = ax.contourf(x,y,z)
plt.show()