import matplotlib.pyplot as plt
import numpy as np

from punto1 import punto1
from punto2 import punto2
from punto3 import punto3
from punto4 import punto4
from punto5 import punto5
from punto6 import punto6
from punto7 import punto7
from punto8 import punto8
from punto9 import punto9
from punto10 import punto10
from punto11 import punto11

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

#punto1(ni,Na,Nd,T , tao_n ,tao_po ,Va, Wn, Wp)

#punto2(Na,Nd,ni,T ,e_s)

#punto3(Na,Nd,ni,T,e_s,Va )

#punto4(Na,Nd,ni,T,Va)

#punto5(Na,Nd,ni,T ,Wp,Wn,Va)

#punto6(Na,Nd,ni,T ,Wp,Wn,Va)

punto7(ni,Na,Nd,Wp,Wn,Va,T,True)
   
#punto8(ni,Na,Nd,Wp,Wn,Va,T,True)

#punto9(ni,Na,Nd,Wp,Wn,Va,T,True)

#punto10(ni,Na,Nd,Wp,Wn,Va,T,True)

punto11(ni,Na,Nd,Wp,Wn,Va,T)