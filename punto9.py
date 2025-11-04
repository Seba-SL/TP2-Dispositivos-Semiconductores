import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import cumtrapz

k = 1.380649e-23   # J/K
q = 1.602176634e-19 # C
e_o = 88.5e-15 # C/(V cm)
e_s = 11.9*e_o


def punto9():

    print("\nPunto 9 :A partir de la corriente de arrastre de mayoritarios calculada en el ı́tem anterior y suponiendo que se puede considerar la distribución de mayoritarios homogénea en las QNRs, ¿cuál debe ser la intensidad del E en cada QNR que da lugar a esas corrientes? ¿Cómo se comparan con Emáx ? ¿Es correcto suponer que las QNRs son cuasi neutrales?")

    return