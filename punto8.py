import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import cumtrapz

k = 1.380649e-23   # J/K
q = 1.602176634e-19 # C
e_o = 88.5e-15 # C/(V cm)
e_s = 11.9*e_o


def punto8():

    print("\nPunto 8 :\nDeterminar la corriente de arrastre de mayoritarios usando los valores de las corrientes netas de electrones y huecos calculadas en el ı́tem 5.\n")

    return