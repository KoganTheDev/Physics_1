#imports and def
import numpy as np
#import matplotlib.pyplot as plt

def zero_cross(ar):
    #returns an array of indices where ar changes sign
    sign_ar=np.sign(ar)
    sign_change_ar=np.abs(sign_ar[:-1]-sign_ar[1:])
    return np.nonzero(sign_change_ar)[0]

#input
sn=int(input())
v0=float(input())
m=float(input())
b=float(input())

#your code
dt = 0.001
t = np.arange(0, 3, dt)
g = 9.8
a = np.zeros_like(t)+g
r0 = 0
v = np.concatenate(([v0], np.cumsum(a)*dt+v0))

f = v - b*v*dt/m - g*dt
for i in range(0, (int)(3/dt)):
    if i == 0:
        v[0] = v0
    else:
        v[i] = v[i-1]*(1-b*dt/m)-g*dt

r = np.concatenate(([r0], np.cumsum(v)*dt+r0))

time = zero_cross(v)
t1 = t[time[0]]
time = zero_cross(r)
t2 =  t[time[1]] - t1

"""
fig, ax = plt.subplots()
ax.plot(t, v[0:-1], "blue", label="v(t)")
ax.plot(t, r[0:-2], "red", label="r(t)")
ax.legend()
ax.set_xlabel("time (second)")
plt.show()
"""

#output
if sn==1:
    print(t1)
if sn==2:
    print(t2)