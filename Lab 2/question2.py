import numpy as np
#import matplotlib.pyplot as plt

def zero_cross(ar):
    #returns an array of indices where ar changes sign
    H1t=np.sign(ar)
    H1s=np.abs(H1t[:-1]-H1t[1:])
    return np.nonzero(H1s)[0]

#input
T1=float(input('enter T_one: '))
T2=float(input('enter T_two: '))
qn=int(input('enter question no.: '))

# your code
R=40
t1=T1/6
X1=R*np.cos(2*np.pi*t1/T1)
Y1=R*np.sin(2*np.pi*t1/T1)
X2=R*np.cos(2*np.pi*t1/T2)
Y2=R*np.sin(2*np.pi*t1/T2)

d=np.sqrt((X1-X2)**2+(Y1-Y2)**2)
s=R*(2*np.pi*t1/T1-2*np.pi*t1/T2)

"""
fig1, ax1 = plt.subplots()
ax1.set_title("Race")
ax1.set_xlabel("x (meters)")
ax1.set_ylabel("y (meters)")
ax1.plot(R*np.cos(t),R*np.sin(t), label="Path")
ax1.plot(X1, Y1, "go", label="Car 1")
ax1.plot(X2, Y2, "ro", label="Car 2")
ax1.legend()

plt.show()
"""
# T1=42
# T2=50
dt = 10*T2/10000
t=np.linspace(0,10*T2,10000)
x1=R*np.cos(2*np.pi*t/T1)
y1=R*np.sin(2*np.pi*t/T1)
x2=R*np.cos(2*np.pi*t/T2)
y2=R*np.sin(2*np.pi*t/T2)
D=np.sqrt((x1-x2)**2+(y1-y2)**2)
time=zero_cross(np.gradient(D, dt))[1]
T3_numeric=t[time]
"""
fig2, ax2 = plt.subplots()
ax2.set_title("Distance between cars over time")
ax2.set_xlabel("time (seconds)")
ax2.set_ylabel("distance (meters)")
ax2.plot(t3range, D, label="Distance over time")
ax2.legend()

plt.show()
"""

T3_analytic=(T1*T2)/(T2-T1)

#output
if qn==1:
    print(f'{X1:.5g},{Y1:.5g} m')
if qn==2:
    print(f'{d:.5g} m')
if qn==3:
    print(f'{s:.5g} m')
if qn==4:
    print(f'{T3_numeric:.5g}')
if qn==5:
    print(f'{T3_analytic:.5g}')