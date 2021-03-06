from scipy import signal

# Dane katalogowe
J_obiektu = 9.82*(10**(-7))
Kt = 0.0146
Ob = 0.0

# nastawy
Predkosc_Kp = 0.01
Predkosc_Ki = 0.125
Polozenie_Kp = 60.0

# Wybrowadzenia
num_predkosc = [-0.005*Ob, Predkosc_Kp*Kt-Ob, Predkosc_Ki*Kt]
den_predkosc = [J_obiektu*0.005, J_obiektu -0.005*Ob, Predkosc_Kp*Kt-Ob, Predkosc_Ki*Kt]

G_predkosc=signal.TransferFunction(num_predkosc, den_predkosc)

#num = [Polozenie_Kp*G_predkosc]
#den = [1, Polozenie_Kp*G_predkosc]
num=[-0.005*Polozenie_Kp*Ob, Polozenie_Kp*(Kt*Predkosc_Kp-Ob), Predkosc_Ki*Kt]
den=[0.005*J_obiektu, J_obiektu-0.005*Ob, Predkosc_Kp*Kt-Ob-0.005*Polozenie_Kp*Ob, Predkosc_Ki*Kt+Predkosc_Kp*Kt-Ob*Polozenie_Kp, Predkosc_Ki*Kt]
Gc = signal.TransferFunction(num, den)
