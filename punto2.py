import matplotlib.pyplot as plt
import numpy as np
import math


k = 1.380649e-23   # J/K
q = 1.602176634e-19 # C
e_o = 88.5e-15 # C/(V cm)
e_s = 11.9*e_o
#Calcular los siguientes parámetros para la juntura en equilibrio termodinámico (ETD): ψbi ; xn ;
#xp y Emáx .


def obtener_tension_contacto(Na,Nd,ni,T):

    print (f"tension termica usada : {k*T/q*1000:.4g} mV , conc intri : {ni:.2g}  ,  Na: {Na:.2g} ,  Nd: {Nd:.2g}")

    Vth = (k * T) / q
  
    phi_bi =   Vth*np.log((Na*Nd) / (ni * ni))
    
    return phi_bi


def imprimir_datos(phi_bi,x_no , x_po, e_max):

    print(f"Tensión de Contacto {phi_bi*1000:.5g} mV \n")
    print(f"x_no =  {x_no*1e6:.3g} um    x_po = {x_po*1e6:.3g} um")
    print(f"E_max = {e_max/1000} kV/cm")
          
    return 

def x_(phi_bi, dopaje1 , dopaje2,e_s ):

    return np.sqrt( (2*e_s*phi_bi*dopaje1 )/(q*(dopaje1+dopaje2)*dopaje2) )

      

def obtener_e_max(phi_bi,Na,Nd,e_s):
    return np.sqrt( (2 * q * phi_bi * Na * Nd) / (e_s * (Na + Nd)) )


def punto2(Na,Nd,ni,T,e_s ):
    
    phi_bi = obtener_tension_contacto(Na,Nd,ni,T)
    x_no = x_(phi_bi, Na , Nd,e_s )
    x_po = x_(phi_bi, Nd , Na ,e_s )
    e_max = obtener_e_max(phi_bi,Na,Nd,e_s)

    imprimir_datos(phi_bi,x_no , x_po , e_max)

    return