import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import cumtrapz

from punto2 import obtener_e_max,x_,obtener_tension_contacto
from punto1 import movilidades_y_difusion
from punto4 import x_,obtener_tension_contacto
from punto5 import obtener_porcentajes_Jn_Jp 

k = 1.380649e-23   # J/K
q = 1.602176634e-19 # C
e_o = 88.5e-15 # C/(V cm)
e_s = 11.9*e_o


def punto7(ni,Na,Nd,Wp,Wn,Va,T,imprimir_enunciado):

    if(imprimir_enunciado):
        print("\nPunto 7: \nCalcular la corriente de difusión de mayoritarios de cada lado de la juntura, suponiendo válida la hipótesis de cuasi-neutralidad en las regiones cuasi-neutrales (QNRs), ¿En qué sentido se difunden los portadores mayoritarios? ¿Es consistente con la corriente calculada en el ı́tem 5?\n\n")
   
    coeficientes = movilidades_y_difusion(Na,Nd,T)

    D_nN  = coeficientes['D_nN']
    D_pN  = coeficientes['D_pN']
    D_nP  = coeficientes['D_nP']  # ¡Asegúrate de que esta clave exista en tu dict!
    D_pP  = coeficientes['D_pP']

    J_nP,J_pN = obtener_porcentajes_Jn_Jp(ni,Na,Nd,Wp,Wn,coeficientes,Va,T)


    J_nN = (D_nN/D_pN)*J_nP

    J_pP = (D_pP/D_nP)*J_pN


    print(f"Corrientes de Difusión Mayoritarios: J_nN = {J_nN*1e6:.3f}  u A/cm^2  J_pP = {J_pP*1e6:.3f} u A/cm^2 ")
   
    return J_nN , J_pP

