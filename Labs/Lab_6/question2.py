import numpy as np

v1x=float(input("vx_one:\n"))
v1y=float(input("vy_one:\n"))

v2x=float(input("vx_two:\n"))
v2y=float(input("vy_two:\n"))

a=float(input("alpha: "))
qn=int(input("q#:\n"))

#ex2
dt = 1e-2
R = np.array([[np.cos(np.radians(a)), -np.sin(np.radians(a))], [np.sin(np.radians(a)), np.cos(np.radians(a))]])
TR = np.array([[np.cos(np.radians(a)), np.sin(np.radians(a))], [-np.sin(np.radians(a)), np.cos(np.radians(a))]])


if qn==1: 
    # your solution
    u1x = v2x
    u1y = v1y
    u2x = v1x
    u2y = v2y
    
elif qn==2: 
    # your solution
    v1 = np.matmul(TR, np.array([v1x, v1y]))
    v2 = np.matmul(TR, np.array([v2x, v2y]))
    u1x = v2[0]
    u1y = v1[1]
    u2x = v1[0]
    u2y = v2[1]
    u1 = np.matmul(R, np.array([u1x, u1y]))
    u2 = np.matmul(R, np.array([u2x, u2y]))
    u1x = u1[0]
    u1y = u1[1]
    u2x = u2[0]
    u2y = u2[1]

#output    
print(f'{u1x:.5g}\n{u1y:.5g}\n{u2x:.5g}\n{u2y:.5g}')
    