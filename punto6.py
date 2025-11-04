import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import cumtrapz


k = 1.380649e-23   # J/K
q = 1.602176634e-19 # C

def punto6(Na,Nd,ni,T ,Wp,Wn,Va):
    
    Vth = (k*T)/q
    
    delta_n_xp = (ni)*np.exp(Va/(2*Vth))

    delta_p_xn =  (ni)*np.exp(Va/(2*Vth))

    print("\n\nPunto 6:\n Calcular el exceso de portadores minoritarios en los bordes de la zona de carga espacial (SCR). ¿Se verifica la hipótesis de bajo nivel de inyección?")

    print("--- Exceso de Portadores Minoritarios en los Bordes (cm⁻³) ---")
    print(f"Exceso de Electrones en el borde del lado P (Δn(xp)): {delta_n_xp*1e-10:.2f}  x10^10 cm^{-3} ")
    print(f"Exceso de Huecos en el borde del lado N (Δp(xn)): {delta_p_xn*1e-10:.2f} x10^10 cm^{-3} ")
    print("----------------------------------------------------------------")

    return