import matplotlib.pyplot as plt
import numpy as np

from punto1 import punto1
from punto2 import punto2
from punto3 import punto3
from punto4 import punto4

# Parámetros del diodo
Na = 2e15  # cm^-3
Nd = 1e15   # cm^-3
T = 300 # Kellllvin
tao_n = 8e-6 # segundos
tao_po = 440e-6 #s
Va = 210e-3 # V
Wn = 11e-6  # m 
Wp = 11e-6 # m 
ni = 1e10 #cm-3
e_o = 88.5e-15 # C/(V cm)
e_s = 11.9*e_o

punto1(Na,Nd,T , tao_n ,tao_po ,Va, Wn, Wp)

punto2(Na,Nd,ni,T ,e_s)

punto3(Na,Nd,ni,T,e_s,Va )

punto4(Na,Nd,ni,T,Va)
