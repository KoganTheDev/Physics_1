import numpy as np
from numpy.polynomial import Polynomial
from numpy.polynomial.polynomial import polyval
# import matplotlib.pyplot as plt

def simple(x0,v0,dt,t_last, k, m, power):
    t = np.arange(0, t_last, dt)
    x = np.zeros_like(t)+x0
    v = np.zeros_like(t)+v0
    for i in range(0, int(t_last/dt)-1):
        v[i+1] = -(k/m)*x[i]**power*dt+v[i]
        x[i+1] = v[i+1]*dt+x[i]
    return t, x, v

def zero_cross(ar):
    #returns an array of indices where ar changes sign
    H1t=np.sign(ar)
    H1s=np.abs(H1t[:-1]-H1t[1:])
    return np.nonzero(H1s)[0]

#input
f_in=float(input('Enter frequncy (Hz): '))

#your code
k = 20
kapa = 5
m = 1
dt = 1e-3
t_last = 10
v0 = 0
x0 = np.arange(1, 2.1, 0.2)
x0 = np.round(x0, 2)
T = np.zeros_like(x0)
f = np.zeros_like(x0)

# fig1, ax1 = plt.subplots()
# fig2, ax2 = plt.subplots()
# fig3, ax3 = plt.subplots()
for i in range(0, len(x0)):
    # get the graph for each start condition
    t1, x1, v1 = simple(x0[i], v0, dt, t_last, k, m, 1)
    t2, x2, v2 = simple(x0[i], v0, dt, t_last, kapa, m, 3)
    # get cycle time
    time = zero_cross(x2)
    T[i] = (time[4] - time[2])*dt
    # get frequency
    f[i] = 1/T[i]

    # ax1.plot(t1, x1)
    # ax2.plot(t2, x2)

# ax3.plot(f, x0)
# plt.show()

p_fit = Polynomial.fit(f ,x0 , deg=3)

# plt.plot(f, x0, 'o')
x, y = p_fit.linspace(50)
# plt.plot(x, y)
# plt.show()

p_coef = p_fit.convert().coef
A_of_f = polyval(f_in, p_coef)

#ouput
print(f'{A_of_f:.4g}')