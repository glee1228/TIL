import numpy as np
from matplotlib import pyplot as plt

def expectation
x = np.linspace(-100,500,1000)

#print(x)
p = np.zeros_like(x)
p[(0 < x) & (x <= 360 )] = 1/360
#print(p)
xp = x*p
#print(xp)

plt.subplot(121)
plt.plot(x,p)
plt.xticks([0, 180, 360])
plt.title('$p(x)$')
plt.xlabel('$x$ (deg.)')

plt.subplot(122)
plt.plot(x,xp)
plt.xticks([0,180,360])
plt.title('$xp(x)$')
plt.xlabel('$x$ (deg.)')

plt.show()

