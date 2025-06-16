import numpy as np
qn=int(input())
# question 1
g = 9.8
earth_radius_squared = pow(6378000, 2)
# question2 
moon_radius = 3.844e8
angular_acceleration = pow(2 * np.pi / (27.3*24*3600), 2) * moon_radius
# question3 
m1 = 158
m2 = 0.73
F = 1.53e-7
dis = pow((225/1000), 2)
G = F/(m1*m2/dis)
# question4 
moon_radius = 3.844e8
angular_acceleration = pow(2 * np.pi / (27.3*24*3600), 2) * moon_radius

# Question 5
T_sun = 365 * 24 * 60 * 60
radius_sum = 1.5e11
angular_acceleration_sun = pow((2 * np.pi / T_sun), 2) * pow(radius_sum, 3)
Ms = angular_acceleration_sun / G

ANS1= g * earth_radius_squared
ANS2= angular_acceleration * pow(moon_radius, 2)
ANS3= G
ANS4= g * earth_radius_squared / G
ANS5= Ms

## output
if qn==1: print(f'{ANS1:.4g}')
if qn==2: print(f'{ANS2:.4g}')
if qn==3: print(f'{ANS3:.4g}')
if qn==4: print(f'{ANS4:.4g}')
if qn==5: print(f'{ANS5:.4g}')
