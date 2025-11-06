import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import cumtrapz


from punto8 import punto8
from punto1 import movilidades_y_difusion


k = 1.380649e-23   # J/K
q = 1.602176634e-19 # C
e_o = 88.5e-15 # C/(V cm)
e_s = 11.9*e_o


def punto9(ni,Na,Nd,Wp,Wn,Va,T,imprimir_enunciado):

    if(imprimir_enunciado):
        print("\nPunto 9 :A partir de la corriente de arrastre de mayoritarios calculada en el ı́tem anterior y suponiendo que se puede considerar la distribución de mayoritarios homogénea en las QNRs, ¿cuál debe ser la intensidad del E en cada QNR que da lugar a esas corrientes? ¿Cómo se comparan con Emáx ? ¿Es correcto suponer que las QNRs son cuasi neutrales?")


      
    coeficientes = movilidades_y_difusion(Na,Nd,T)

    mu_nN  = coeficientes['mu_nN']
    mu_pP  = coeficientes['mu_pP']



    J_nN_arr, J_pP_arr = punto8(ni,Na,Nd,Wp,Wn,Va,T, False )


    E_N = (J_nN_arr)/(q*Nd*mu_nN)

    E_P = (J_pP_arr)/(q*Na*mu_pP)

    print(f"Campos en QNR: E_N = {E_N*1e6:.3f}  u V/cm   E_P = {E_P*1e6:.3f} u V/cm ")


    return E_N,E_P


