import numpy as np
import matplotlib.pyplot as plt


def zero_cross(ar):
    #returns an array of indices where ar changes sign
    H1t=np.sign(ar)
    H1s=np.abs(H1t[:-1]-H1t[1:])
    return np.nonzero(H1s)[0]

c=float(input("enter c: "))
qn=int(input("enter qn: "))

b=7e-5
m=2.7/1000
g=9.8
v0=10
alpha=15*np.pi/180

## your code and answers
dt = 1e-4
t = np.arange(0, 1.1, dt)

# Get velocity
vx = np.zeros_like(t)
vx[0] = v0*np.cos(alpha)
vy = np.zeros_like(t)
vy[0] = np.sin(alpha)

# Use euler method to extract the components of the velocity
for i in range(1, len(t)):
    v = (vx[i-1]**2 + vy[i-1]**2)**0.5
    vx[i] = -b*dt/m*vx[i-1]-0*dt/m*vx[i-1]*v+vx[i-1]
    vy[i] = -g*dt-b*dt/m*vy[i-1]-0*dt/m*vy[i-1]*v+vy[i-1]

# Calculate the displacement
x = np.concatenate(([0], np.cumsum(vx)*dt))
y = np.concatenate(([0], np.cumsum(vy)*dt))

landing = zero_cross(y)[1]

plt.plot(x[:landing], y[:landing])

plt.show()





ANS1=0
ANS2=0

#ouput
Answers=[0,ANS1,ANS2]
print(f'{Answers[qn]:.5g}')
