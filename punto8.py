from punto7 import punto7
from punto5 import obtener_porcentajes_Jn_Jp 
from punto1 import movilidades_y_difusion

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import cumtrapz

k = 1.380649e-23   # J/K
q = 1.602176634e-19 # C
e_o = 88.5e-15 # C/(V cm)
e_s = 11.9*e_o


def punto8(ni,Na,Nd,Wp,Wn,Va,T,imprimir_enunciado):

    if(imprimir_enunciado):
        print("\nPunto 8 :\nDeterminar la corriente de arrastre de mayoritarios usando los valores de las corrientes netas de electrones y huecos calculadas en el ı́tem 5.\n")

     
    coeficientes = movilidades_y_difusion(Na,Nd,T)

    D_nN  = coeficientes['D_nN']
    D_pN  = coeficientes['D_pN']
    D_nP  = coeficientes['D_nP']  # ¡Asegúrate de que esta clave exista en tu dict!
    D_pP  = coeficientes['D_pP']


    #Corrientes de difusion de mayoritarios
    J_nN, J_pP = punto7(ni,Na,Nd,Wp,Wn,Va,T,False)

    #Corrientes J_n , J_p totales , aproximadamente la de los minoritarios de difusion
    J_nP,J_pN = obtener_porcentajes_Jn_Jp(ni,Na,Nd,Wp,Wn,coeficientes,Va,T)


    J_nN_arr = J_nP - J_nN

    J_pP_arr = J_pN - J_pP

    

    print(f"Corrientes de Arrastre Mayoritarios: J_nN = {J_nN_arr*1e6:.3f}  u A/cm^2  J_pP = {J_pP_arr*1e6:.3f} u A/cm^2 ")

    return J_nN_arr, J_pP_arr