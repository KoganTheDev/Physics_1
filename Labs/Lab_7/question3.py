import numpy as np
# import matplotlib.pyplot as plt

x0 = float(input("initial position: "))
v0 = float(input("initial velocity: "))
t = float(input("time: "))

dt = 1e-3
t_array = np.arange(0, 10, dt)

b = 5
m = 2
k = 40
rho = b/(2*m)
w0 = np.sqrt(k/m)

# fig, ax = plt.subplots()
# ax.set_title("322855909 - 206680753")

# numeric
x = np.zeros_like(t_array)+x0
v = np.zeros_like(t_array)+v0

for i in range(0, len(t_array)-1):
    v[i+1] = -2*rho*v[i]*dt-w0**2*x[i]*dt+v[i]
    x[i+1] = v[i+1]*dt+x[i]

print(f"{v[int(np.round(t/dt, 0))]:.5g}")

# ax.plot(t_array, x, "blue", label="numeric")

# analytic
w = np.sqrt(w0**2+rho**2)

phi = np.arctan((v0+x0*rho)/(-x0*w))
A = x0/np.cos(phi)
x = A*np.exp(-rho*t_array)*np.cos(w*t_array+phi)

# ax.plot(t_array, x, "red", label="analytic")

# ax.legend()
# plt.show()