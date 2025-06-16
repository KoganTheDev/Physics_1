import numpy as np
import matplotlib.pyplot as plt

# Prompt the user to enter the question number and acceleration
qn = int(input('Enter question number: '))
a = float(input('Enter acceleration (m/s^2): '))
print()

if qn == 2:
    # Question 2: Calculate velocity given acceleration and time
    t = float(input('Enter time (s): '))
    v = a * t  # Velocity calculation
    print(f'v={v:.5g} m/s')  # Output the velocity

if qn == 3:
    # Question 3: Calculate displacement given acceleration and time
    t = float(input('Enter time (s): '))
    x = (a * t ** 2) / 2  # Displacement calculation
    print(f'x={x:.5g} m')  # Output the displacement

if qn == 4:
    # Question 4: Calculate displacement given acceleration and velocity
    v = float(input('Enter velocity (m/s): '))
    t = v / a  # Time calculation
    x = 0.5 * a * t ** 2  # Displacement calculation
    print(f'x={x:.5g} m')  # Output the displacement

if qn == 7:
    # Question 7: Output a predefined answer
    ANS = False
    print(ANS)