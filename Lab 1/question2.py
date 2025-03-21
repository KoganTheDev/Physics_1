import numpy as np

def zero_cross(ar_of_a_sampled_f):
    """
    Identifies the indices where the sign of the input array changes.

    Parameters:
    ar_of_a_sampled_f (numpy.ndarray): A 1D numpy array of sampled function values.

    Returns:
    numpy.ndarray: An array of indices where the sign of the input array changes.
    """
    ar_of_sign_change_indxs = np.sign(ar_of_a_sampled_f)
    ar_of_sign_change_indxs = np.diff(ar_of_sign_change_indxs)
    ar_of_sign_change_indxs = np.nonzero(ar_of_sign_change_indxs)[0]
    return ar_of_sign_change_indxs

# Input: initial velocity
v0 = float(input("Enter the initial velocity (m/s): "))

# Constants
g = 9.8  # Acceleration due to gravity (m/s^2)
t = np.arange(0, 5, 0.01)  # Time array from 0 to 5 seconds with 0.01s intervals
y = -0.3 + v0 * t - 0.5 * g * t**2  # Position array based on the given equation

# Find the indices where the object changes direction (ascends and descends)
ascent, descent = zero_cross(y)[0], zero_cross(y)[1]

# Calculate the time of flight
time_of_flight = t[descent] - t[ascent]

# Output the time of flight
print(f'Time of flight: {time_of_flight:.5g} s')