
import numpy as np

#input
F=list(map(float,input().split()))
a=list(map(float,input().split()))
print()

# consts
g=9.8

# your code


p, pcov = np.polyfit(F,a,1, cov=True)

mu= np.round(-p[1]/9.8, 2)
DELTA_mu= round(np.sqrt(pcov[1,1])/9.8,2)



## output
print(f'{mu}\n{DELTA_mu}')