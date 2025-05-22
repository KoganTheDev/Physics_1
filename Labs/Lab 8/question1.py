import numpy as np
#import matplotlib.pyplot as plt

def zero_cross(ar):
    #returns an array of indices where ar changes sign
    H1t=np.sign(ar)
    H1s=np.abs(H1t[:-1]-H1t[1:])
    return np.nonzero(H1s)[0]

L=float(input("enter L: "))
qn=int(input("enter qn: "))
print()

## your code

ANS1 = 3

m = 1e-3
k = 9e+9
q1 = 10e-6
q2 = 10e-6
Q = 10e-6
y = np.linspace(-L, L, 300)
F = (-2*k*q1*Q/(y**2+(L/2)**2))*(y/np.sqrt(y**2+(L/2)**2))
"""
fig, ax = plt.subplots()
ax.plot(y, F)
"""
y = np.linspace(-0.02*L, 0.02*L, 300)
F = (2*k*q1*Q/(y**2+(L/2)**2))*(y/np.sqrt(y**2+(L/2)**2))
"""
fig, ax = plt.subplots()
ax.plot(y, F)
"""
y = 0.02*L
F = (2*k*q1*Q/(y**2+(L/2)**2))*(y/np.sqrt(y**2+(L/2)**2))
ANS2 = F

dt = 1e-4
t = np.arange(0, 0.2, dt)
y = np.zeros_like(t)+0.01*L
v = np.zeros_like(t)
for i in range(0, len(t)-1):
    F = (-2*k*q1*Q/(y[i]**2+(L/2)**2))*(y[i]/np.sqrt(y[i]**2+(L/2)**2))
    v[i+1] = F*dt/m + v[i]
    y[i+1] = v[i+1]*dt + y[i]
"""
fig, ax = plt.subplots()
ax.plot(t, y)
"""

time = zero_cross(y)
T = t[time[4]] - t[time[2]]
y2=0.01*L*np.cos(2*np.pi/T*t)
"""
ax.plot(t, y2)
"""
ANS4 = "yes"

k_eff=16*k*q1*Q/L**3
w0=np.sqrt(k_eff/m)
T_th=2*np.pi/w0

ANS5 = T_th

# output
ANSWERS=[0,ANS1,ANS2,T,ANS4,ANS5]
if qn!=4:
    print(f'{ANSWERS[qn]:.3e}')
else:
    print(ANS4)