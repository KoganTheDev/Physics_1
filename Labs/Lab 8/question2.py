import numpy as np
#import matplotlib.pyplot as plt

def zero_cross(arr):
    arr = np.sign(arr)
    arr = np.diff(arr)
    arr = np.nonzero(arr)
    return arr[0]

#input
v0x = float(input())
v0y = float(input()) # test using v0x=0 v0y=4e6 m/s #
x0 = float(input()) # x0=1.51e-11 m    y0=0
y0 = float(input())

# your code
k = 9e+9
e = 1.6e-19
m = 9.1e-31
q1 = e
q2 = -e

dt = 1e-20
t = np.arange(0, 3300*dt, dt)

x = np.zeros_like(t)+x0
y = np.zeros_like(t)+y0
vx = np.zeros_like(t)+v0x
vy = np.zeros_like(t)+v0y

Fx = (-k*e**2*x0)/((x0**2+y0**2)**(3/2))
Fy = (-k*e**2*y0)/((x0**2+y0**2)**(3/2))

ax = Fx/m
ay = Fy/m

for i in range(0, len(t)-1):
    Fx = (-k*e**2*x[i])/((x[i]**2+y[i]**2)**(3/2))
    ax = Fx/m
    vx[i+1] = ax*dt + vx[i]
    x[i+1] = vx[i+1]*dt + x[i]

    Fy = (-k*e**2*y[i])/((x[i]**2+y[i]**2)**(3/2))
    ay = Fy/m
    vy[i+1] = ay*dt + vy[i]
    y[i+1] = vy[i+1]*dt + y[i]


tx = zero_cross(vx)
ty = zero_cross(vy)

al = x[tx[1]] - x[tx[0]]
be = y[ty[1]] - y[ty[0]]

e = np.sqrt(1-(be**2)/(al**2))

# fig, ax = plt.subplots()
# ax.plot(x, y)
# ax.axis('equal')
# plt.show()

# output
print(f'{e:.5g}')