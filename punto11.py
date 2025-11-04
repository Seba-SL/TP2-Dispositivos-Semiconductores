import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import cumtrapz

k = 1.380649e-23   # J/K
q = 1.602176634e-19 # C
e_o = 88.5e-15 # C/(V cm)
e_s = 11.9*e_o


def punto11():

    print("\nRealizar un gráfico del diodo PN que contenga todas las corrientes de las tres regiones de la aproximación de vaciamiento, indicando módulo y sentido (usar los valores calculados en los ı́tems anteriores) y si son de mayoritarios o minoritarios.")
    return