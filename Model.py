from scipy import signal
from scipy import integrate as spi
from matplotlib import pyplot as plt
from numpy import min
from scipy import linspace


# Dane katalogowe
J_obiektu = 9.82*(10**(-7))
Kt = 0.0146
Ob = 20.0

# Nastawy
Predkosc_Kp = 0.01
Predkosc_Ki = 0.125
Polozenie_Kp = 60.0

# Wyprowadzenia
#num_predkosc = [-0.005*Ob, Predkosc_Kp*Kt-Ob, Predkosc_Ki*Kt]
#den_predkosc = [J_obiektu*0.005, J_obiektu -0.005*Ob, Predkosc_Kp*Kt-Ob, Predkosc_Ki*Kt]
#G_predkosc=signal.TransferFunction(num_predkosc, den_predkosc)

num=[-0.005*Polozenie_Kp*Ob, Polozenie_Kp*(Kt*Predkosc_Kp-Ob), Predkosc_Ki*Kt*Polozenie_Kp]
den=[0.005*J_obiektu, J_obiektu-0.005*Ob, Predkosc_Kp*Kt-Ob-0.005*Polozenie_Kp*Ob, Predkosc_Ki*Kt+Predkosc_Kp*Kt-Ob*Polozenie_Kp, Predkosc_Ki*Kt*Polozenie_Kp]
Gc = signal.TransferFunction(num, den)
#Gc= signal.lti(num, den)


#step responce
t, y = signal.step2(Gc)
plt.plot(t, y)
plt.grid()
plt.show()