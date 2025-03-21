import numpy as np

def zero_cross(ar_of_a_sampled_f):
    ar_of_sign_change_indxs = np.sign(ar_of_a_sampled_f)
    ar_of_sign_change_indxs = np.diff(ar_of_sign_change_indxs)
    ar_of_sign_change_indxs = np.nonzero(ar_of_sign_change_indxs)[0]
    return ar_of_sign_change_indxs



# input 
v0=float(input())
# const
g=9.8 # m/s^2
t=np.arange(0,5,0.01)
y=-0.3+v0*t-0.5*g*t**2

# My code
ascent, decent = zero_cross(y)[0], zero_cross(y)[1]

time_of_flight= t[decent] - t[ascent]

#output
print(f'time of flight: {time_of_flight:.5g} s')