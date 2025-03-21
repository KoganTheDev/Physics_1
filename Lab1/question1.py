import numpy as np
import matplotlib.pyplot as plt

qn=int(input('enter question number: '))
a=float(input('enter acceleration: '))
print()

if qn==2:
    t=float(input('enter t: '))
    ## your answer
    v = a * t
    
    ## output
    print(f'v={v:.5g} m/s')

if qn==3:
    t=float(input('enter t: '))
    ## your answer
    
    x= (a * t ** 2)/2
    
    ## output
    print(f'x={x:.5g} m')
    
if qn==4:
    v=float(input('enter v: '))
    ## your answer
    
    t = v / a
    x= 0.5*a*t**2
    
    ## output
    print(f'x={x:.5g} m')

if qn==7:
    ANS= False
    print(ANS)