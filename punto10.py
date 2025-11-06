import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import cumtrapz


from punto9 import punto9
from punto1 import movilidades_y_difusion


k = 1.380649e-23   # J/K
q = 1.602176634e-19 # C
e_o = 88.5e-15 # C/(V cm)
e_s = 11.9*e_o


def punto10(ni,Na,Nd,Wp,Wn,Va,T,imprimir_enunciado):

    if(imprimir_enunciado):
        print("\nPunto 10 :¿Cuánto es la corriente de arrastre de minoritarios para los E calculados en las QNRs? (Calcular en los bordes de la SCR, donde la densidad de minoritarios es máxima). ¿Es compa- rable esta corriente de arrastre con la corriente de difusión de minoritarios en las QNRs?")

    E_N,E_P = punto9(ni,Na,Nd,Wp,Wn,Va,T,False)

        
    coeficientes = movilidades_y_difusion(Na,Nd,T)

    mu_nP  = coeficientes['mu_nP']
    mu_pN  = coeficientes['mu_pN']



    n = (ni*ni)/Na

    p = (ni*ni)/Nd

    J_nP_arr  = q*p*mu_nP*E_P

    J_pN_arr = q*n*mu_pN*E_N

    
    print(f"Corrientes de Arrastre Minoritarios: J_nP_arr = {J_nP_arr*1e6:.3f}  u A/cm^2  J_pN_arr = {J_pN_arr*1e6:.3f} u A/cm^2 ")


    return J_nP_arr, J_pN_arr