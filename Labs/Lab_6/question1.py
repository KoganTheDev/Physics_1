import numpy as np
#import matplotlib.pyplot as plt

# inputs
a=float(input("a:"))
b=float(input("b:"))
sn=int(input("sn:"))

# Question 1
dt = pow(10, -4)
t = np.arange(-np.pi/2, np.pi/2, dt)
radius = 1 # m

x = radius * np.sin(t)
y = -radius * np.cos(t)
angle = np.radians(30)

dxdt = np.gradient(x,dt)
dydt = np.gradient(y,dt) 

F_x = a*np.cos(angle)
F_y = a*np.sin(angle)

force = F_x * dxdt + F_y * dydt
work = np.sum(force) * dt

# Question 2
f_x = b*y / radius
f_y = - b*x / radius
work_q2 = np.sum(f_x * dxdt * dt) + np.sum(f_y * dydt *dt)

f_x_new = -a * np.power(y,2) 
f_y_new = b*np.power(x,3)*y
work_new = np.sum(f_x_new * dxdt * dt) + np.sum(f_y_new * dydt *dt)


if sn==1:
    print(work)
elif sn==2:
    print(work_q2)
elif sn==3:
    print(work_new)
elif sn==4:
    print('0')
elif sn==5:
    print('2')
