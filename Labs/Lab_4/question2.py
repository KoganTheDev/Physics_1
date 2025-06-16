import numpy as np

def zero_cross(ar):
    #returns an array of indices where ar changes sign
    H1t=np.sign(ar)
    H1s=np.abs(H1t[:-1]-H1t[1:])
    return np.nonzero(H1s)[0]


#input
V=float(input('enter V: '))
alpha=float(input('enter alpha: '))
qn=int(input('enter question no.: '))


# consts
rho=1.3 # kg/m^3 (air density)
A=18 # m^2 (wing area)

# your code
mAir = -rho*A*np.sin(np.deg2rad(alpha))*V
Fy = -mAir*V*np.sin(2*np.deg2rad(alpha))
Fx = mAir*V*np.cos(2*np.deg2rad(alpha))-mAir*V

t = np.arange(0, 90, 0.01)
mAir = -rho*A*np.sin(np.deg2rad(t))*V
fy = -mAir*V*np.sin(2*np.deg2rad(t))
fx = mAir*V*np.cos(2*np.deg2rad(t))-mAir*V
d = fy - 10*fx
alpha = t[zero_cross(d)[1]]

V = np.arange(0, 200, 0.01)
mAir = rho*A*np.sin(np.deg2rad(alpha))*V
fy = mAir*V*np.sin(2*np.deg2rad(alpha))
m = 1000
g = -10
f = fy + m*g
V4 = V[zero_cross(f)[0]]



Answers=[0,Fy,Fx,alpha,V4]
print(f'{Answers[qn]:.5g}')
