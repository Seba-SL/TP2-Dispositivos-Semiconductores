import matplotlib.pyplot as plt
import numpy as np

from punto1 import datos_enunciado,movilidades_y_difusion, imprimir_parametros_u_D,longitud_caracteristica,imprimir_longitudes,condicion_diodo_corto

# Parámetros del diodo
Na = 2e15  # cm^-3
Nd = 1e15   # cm^-3
T = 300 # Kellllvin
tao_n = 8e-6 # segundos
tao_po = 440e-6 #s
Va = 210e-3 # V
Wn = 11e-6  # m 
Wp = 11e-6 # m 

datos_enunciado(Na, Nd, T,tao_n , tao_po , Va)

movilidades_coeficientesD = movilidades_y_difusion(Na, Nd, T)

imprimir_parametros_u_D(movilidades_coeficientesD)

longitudes_de_difusion = longitud_caracteristica(movilidades_coeficientesD, tao_n, tao_po)

imprimir_longitudes(longitudes_de_difusion)



if(condicion_diodo_corto(longitudes_de_difusion, Wn ,Wp)):
    print("Cumple la condición de Diodo Corto")

else:
    print("No cumple la condición de Diodo Corto")

