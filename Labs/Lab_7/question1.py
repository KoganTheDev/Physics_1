import numpy as np
#import matplotlib.pyplot as plt

x0=float(input("initial position: "))
v0=float(input("initial velocity: "))
k=40
m=2
w0=np.sqrt(k/m)

def Simple_HM_A1(x0,v0,dt,t_last):
    t = np.arange(0, t_last, dt)
    x = np.zeros_like(t)+x0
    v = np.zeros_like(t)+v0
    for i in range(0, int(t_last/dt)-1):
        v[i+1] = -w0**2*x[i]*dt+v[i]
        x[i+1] = v[i]*dt+x[i]
    return t, x, v
            
    
def Simple_HM_A2(x0,v0,dt,t_last):
    t = np.arange(0, t_last, dt)
    x = np.zeros_like(t)+x0
    v = np.zeros_like(t)+v0
    for i in range(0, int(t_last/dt)-1):
        v[i+1] = -w0**2*x[i]*dt+v[i]
        x[i+1] = v[i+1]*dt+x[i]
    return t, x, v
    
    
dt=0.01
t_last=10
t,x_A1,v_A1=Simple_HM_A1(x0,v0,dt,t_last)
t,x_A2,v_A2=Simple_HM_A2(x0,v0,dt,t_last)

x_th = (x0/(np.cos(np.arctan(-v0/(x0*w0)))))*np.cos(w0*t+np.arctan(-v0/(x0*w0)))

D1=np.abs(x_th[300]-x_A1[300])
D2=np.abs(x_th[300]-x_A2[300])
"""
fig, ax1 = plt.subplots()
ax1.plot(t, x_A1, "red", label="x_A1")
ax1.legend()
ax1.set_xlabel("t")
ax1.set_ylabel("x")

fig, ax2 = plt.subplots()
ax2.plot(t, x_A2, "blue", label="x_A2")
ax2.legend()
ax2.set_xlabel("t")
ax2.set_ylabel("x")
"""
#output
print(f'{x_A1[300]:.5g}')
print(f'{x_A2[300]:.5g}')
print(f'{D1:.5g}')
print(f'{D2:.5g}')