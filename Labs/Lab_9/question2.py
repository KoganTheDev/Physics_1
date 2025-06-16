import numpy as np

k = 9e9
N = 10_000

lam = float(input())
L  = float(input())
qn = int(input())

def E_field(x0, y0, lam, L, N=N):
    dx  = L / N
    x_p = np.linspace(-L/2, L/2 - dx, N)
    Rx  = x0 - x_p
    Ry  = y0
    R3  = (Rx**2 + Ry**2)**1.5
    Ex  = k * lam * np.sum(Rx / R3) * dx
    Ey  = k * lam * np.sum(Ry / R3) * dx
    return Ex, Ey

_format = lambda v: f'{v:.5g}'

Ex1, Ey1 = E_field(2*L, 3*L, lam, L)
Ex2, Ey2 = E_field(0.0,   L,  lam, L)
Ey3      = E_field(0.0, 100*L, lam, L)[1]

ANS4 = round(100 * abs(k*lam*L/(100*L)**2 - Ey3) / Ey3, 1)

Ey5  = E_field(0.0, 0.01*L, lam, L)[1]
ANS6 = round(100 * abs(2*k*lam/(0.01*L) - Ey5) / Ey5, 1)

if qn == 1:
    print(f'{_format(Ex1)},{_format(Ey1)}')
elif qn == 2:
    print(f'{_format(Ex2)},{_format(Ey2)}')
elif qn == 3:
    print(f'{_format(Ey3)}')
elif qn == 4:
    print(ANS4)
elif qn == 5:
    print(f'{_format(Ey5)}')
elif qn == 6:
    print(ANS6)
