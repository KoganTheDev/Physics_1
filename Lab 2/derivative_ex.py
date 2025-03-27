import numpy as np
import matplotlib.pyplot as plt

t, dt = 10, 0.01

t = np.arange(0, t, dt)
f = np.sin(t)

# definition of a limit: f(t + dt) - f(t) / dt
# this is the derivative of f(t) with respect to t

#fdot = (f[1:] - f[:-1]) / dt
# np.gradient does the same as the line above

#fdot = np.gradient(f)/ dt

f = np.exp(t)
fDot = np.gradient(f) / dt

'''
Example: that np.gradient isn`t the accurate but will do.

print(t[100])
print(fDot[100])
print(np.exp(1))
'''

plt.plot(t, fDot)
plt.show()