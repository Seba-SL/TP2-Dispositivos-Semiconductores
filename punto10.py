import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import cumtrapz

k = 1.380649e-23   # J/K
q = 1.602176634e-19 # C
e_o = 88.5e-15 # C/(V cm)
e_s = 11.9*e_o


def punto10():

    print("\nPunto 10 :¿Cuánto es la corriente de arrastre de minoritarios para los E calculados en las QNRs? (Calcular en los bordes de la SCR, donde la densidad de minoritarios es máxima). ¿Es compa- rable esta corriente de arrastre con la corriente de difusión de minoritarios en las QNRs?")

    return