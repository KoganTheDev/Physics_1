import numpy as np

#inputs
x0=float(input('x coordinate:'))
y0=float(input('y coordinate:'))
qn=int(input('qn:'))
#your code
k = 9e9
q = (1/9)*1e-9
Exx0y0_1 = x0*k*q/((x0**2+y0**2)**(3/2))
Eyx0y0_1 = y0*k*q/((x0**2+y0**2)**(3/2))

def get_index(lower,upper,delta,target):
    ret = (target - lower) / delta
    if lower<=target:
        return int(np.round(ret,0))
    return 0

dx=dy=0.1
X, Y =np.meshgrid(np.arange(-4,4,dx),np.arange(-4,4,dy))
Ex = X*k*q/((X**2+Y**2)**(3/2))
Ey = Y*k*q/((X**2+Y**2)**(3/2))

Exx0y0_2=Ex[get_index(-4,4,dy,y0)][get_index(-4,4,dx,x0)]
Eyx0y0_2=Ey[get_index(-4,4,dy,y0)][get_index(-4,4,dx,x0)]

dx=dy=0.01
X, Y =np.meshgrid(np.arange(-4,4,dx),np.arange(-4,4,dy))
Ex = X*k*q/((X**2+Y**2)**(3/2))
Ey = Y*k*q/((X**2+Y**2)**(3/2))
phi = k*q/(X**2+Y**2)**0.5
E = -np.array([np.gradient(phi,dx,axis=0),np.gradient(phi,dy,axis=1)])

Eyx0y0_3=E[0][get_index(-4,4,dy,y0)][get_index(-4,4,dx,x0)]
Exx0y0_3=E[1][get_index(-4,4,dy,y0)][get_index(-4,4,dx,x0)]


#ouput
if qn==1:
    print(f"Output={Exx0y0_1:.5g}\n{Eyx0y0_1:.5g}")
if qn==2:
    print(f"Output={Exx0y0_2:.5g}\n{Eyx0y0_2:.5g}")
if qn==3:
    print(f"Output={Exx0y0_3:.5g}\n{Eyx0y0_3:.5g}")