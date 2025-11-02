import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import cumtrapz

from punto2 import obtener_e_max,x_,obtener_tension_contacto
from punto1 import movilidades_y_difusion
from punto4 import x_,obtener_tension_contacto

k = 1.380649e-23   # J/K
q = 1.602176634e-19 # C
e_o = 88.5e-15 # C/(V cm)
e_s = 11.9*e_o


def obtener_Js(ni,Na,Nd,Wp,Wn,coeficientes,Va,T):

  
    D_pN  = coeficientes['D_pN']
    D_nP  = coeficientes['D_nP']  

    phi_bi = obtener_tension_contacto(Na,Nd,ni,T)

    xna = x_(phi_bi - Va, Na, Nd, e_s)
    xpa = x_(phi_bi - Va, Nd, Na, e_s)
   
    A_p = (1/Na)*(D_nP/(Wp - xpa))
    B_n = (1/Nd)*(D_pN/(Wn - xna))


    Js = q*(ni*ni)*(A_p + B_n)


   
    return Js

def obtener_porcentajes_Jn_Jp(ni,Na,Nd,Wp,Wn,coeficientes,Va,T):

    Vth = (k*T)/q

    D_pN  = coeficientes['D_pN']
    D_nP  = coeficientes['D_nP']  

    phi_bi = obtener_tension_contacto(Na,Nd,ni,T)

    xna = x_(phi_bi - Va, Na, Nd, e_s)
    xpa = x_(phi_bi - Va, Nd, Na, e_s)
   
    A_p = (1/Na)*(D_nP/(Wp - xpa))
    B_n = (1/Nd)*(D_pN/(Wn - xna))


    Js = q*(ni*ni)*(A_p + B_n)

    J = Js*( np.exp(Va/Vth) - 1 )

    J_n = q*(ni*ni)*(A_p)*( np.exp(Va/Vth) - 1 )

    J_n_porcentaje = (J_n/J)*100
    
    J_p = q*(ni*ni)*(B_n)*( np.exp(Va/Vth) - 1 )

    J_p_porcentaje = (J_p/J)*100


    print(f"Jn = {J_n_porcentaje:.2f} %  | Jp = {J_p_porcentaje:.2f} %")

    return 


def punto5(Na,Nd,ni,T ,Wp,Wn,Va):

    print("\n\nPunto 5: \nCalcular la densidad de corriente que circula por el diodo cuando se aplica Va . ¿Qué porcentaje de la corriente corresponde a electrones y huecos?")

    Vth = (k*T)/q

    coeficientes = movilidades_y_difusion(Na, Nd, T)

    Js = obtener_Js(ni,Na,Nd,Wp,Wn,coeficientes,Va,T)

    print(f"Js =  {Js*1e9:.2f}   n A/cm^2")

    J = Js*( np.exp(Va/Vth) - 1 )

    print(f"J (Va = {Va*1e3:.2f} mV)=  {J*1e6:.2f} \mu A/cm^2"  )

    obtener_porcentajes_Jn_Jp(ni,Na,Nd,Wp,Wn,coeficientes,Va,T)

    return J