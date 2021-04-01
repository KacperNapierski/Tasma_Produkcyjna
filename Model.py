import control
from control import matlab
import numpy as np
from scipy import signal
from scipy import integrate as spi
from matplotlib import pyplot as plt
from numpy import min


# Dane katalogowe
Km = 0.1
Rw=2
Lw=0.2
Ke=0.1
B=0.5
J=0.1
Ob = 20.0

# Nastawy
Polozenie_Kp=5
Predkosc_Kp=0.1
Predkosc_Ki=5


# Wyprowadzenia
s = control.matlab.tf('s')

G_obiektu = Km/(J*Lw*(s**2)+(Rw*J+B*Lw)*s+Rw*B+Km*Ke)
G1 = G_obiektu*((Ob+Predkosc_Kp)*s + Predkosc_Kp*Predkosc_Ki)
G2 = G1/s
G3 = G2/(1+G2)
G_predkosci = G3*Polozenie_Kp
G4 =G3/s
G_polozenia = G4/(G4+1)
print(G_polozenia)


#step responce
fig, (ax1, ax2) =plt.subplots(2)

t1,y1=control.step_response(G_polozenia,60)
t2,y2=control.step_response(G_predkosci,60)
ax1.plot(t1, y1)
ax2.plot(t2, y2)
#plt.grid()
plt.show()
#print(len(y))

