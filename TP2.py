import matplotlib.pyplot as plt
import numpy as np

from punto1 import punto1


# Parámetros del diodo
Na = 2e15  # cm^-3
Nd = 1e15   # cm^-3
T = 300 # Kellllvin
tao_n = 8e-6 # segundos
tao_po = 440e-6 #s
Va = 210e-3 # V
Wn = 11e-6  # m 
Wp = 11e-6 # m 

punto1(Na,Nd,T , tao_n ,tao_po ,Va, Wn, Wp)
