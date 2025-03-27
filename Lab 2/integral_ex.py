import numpy as np
import matplotlib.pyplot as plt

T, dt = 1, 0.0001

t = np.arange(0, T, dt)
f = t + 2
F = np.cumsum(f) * dt

# cumsum doesn`t include the first element of the array
# so we need to add it manually
print(F[0])
F = np.concatenate(([1], np.cumsum(f) * dt + 1))