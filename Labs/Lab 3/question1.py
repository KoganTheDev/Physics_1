import numpy as np

# Input values
m1 = float(input())
m2 = float(input())
F0 = float(input())
v0 = float(input())
qn = int(input())

# Time setup
dt = 0.01
t = np.arange(0, 10, dt)

# Forces
force_2 = F0 * np.sin(2 * t)
force_1 = -force_2  # Assuming Newton's third law (action-reaction)

# Initial velocities
velocity_2 = np.zeros(len(t))
velocity_1 = np.zeros(len(t))
velocity_1[0] = v0

# Compute acceleration
acceleration_1 = force_1 / m1
acceleration_2 = force_2 / m2

# Compute velocity using numerical integration
velocity_1[1:] = v0 + np.cumsum(acceleration_1[:-1]) * dt
velocity_2[1:] = np.cumsum(acceleration_2[:-1]) * dt

# Compute total momentum (assuming P = p1 + p2, where p = m * v)
p1 = m1 * velocity_1
p2 = m2 * velocity_2
P = p1 + p2

# Answers for qn 4, 5, 6 (unclear, keeping as they are)
ANS4 = 'no'
ANS5 = 'yes'
ANS6 = 'yes'

# Output
if qn == 1:
    print(p1[:10])
elif qn == 2:
    print(p2[:10])
elif qn == 3:
    print(P[:10])
elif qn == 4:
    print(ANS4)
elif qn == 5:
    print(ANS5)
elif qn == 6:
    print(ANS6)
