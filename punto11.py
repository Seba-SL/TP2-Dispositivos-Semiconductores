import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import cumtrapz


from punto10 import punto10
from punto8 import punto8
from punto7 import punto7
from punto5 import obtener_porcentajes_Jn_Jp

from punto1 import movilidades_y_difusion

k = 1.380649e-23   # J/K
q = 1.602176634e-19 # C
e_o = 88.5e-15 # C/(V cm)
e_s = 11.9*e_o


def Graficar_corrientes_diodo(
    J_nP_arr, J_pN_arr,
    J_nN_arr, J_pP_arr,
    J_nN_dif, J_pP_dif,
    J_nP_dif, J_pN_dif,
    Wn, Wp, xp, xn
):
    """
    Grafica las corrientes de arrastre y difusión en una juntura PN
    separando minoritarios y mayoritarios en QNR-P, SCR y QNR-N.
    """

    fig, ax = plt.subplots(figsize=(9, 5))

    # Regiones
    ax.axvspan(-Wp, -xp, color='lightcoral', alpha=0.4)
    ax.axvspan(-xp, xn, color='white', alpha=0.8)
    ax.axvspan(xn, Wn, color='lightblue', alpha=0.4)

    ax.axvline(-xp, color='k', linestyle='--', lw=1)
    ax.axvline(xn, color='k', linestyle='--', lw=1)

    ax.text(-Wp/2, 1.8, "QNR–P", ha='center', fontsize=12)
    ax.text(0, 1.8, "SCR", ha='center', fontsize=12)
    ax.text(Wn/2, 1.8, "QNR–N", ha='center', fontsize=12)

    # ---------- Función auxiliar para flechas ----------
    def flecha(x, y, sentido, J, color, etiqueta):
        """Dibuja una flecha proporcional a |J| con dirección según su signo"""
        dx = 0.5 * np.sign(sentido)
        lw = 1.5 + 5 * abs(J) / max(1e-12, max_magnitud)
        ax.arrow(x, y, dx, 0, 
                 head_width=0.1, head_length=0.1,
                 fc=color, ec=color, lw=lw,
                 alpha=0.9, length_includes_head=True)
        ax.text(x, y + 0.15, etiqueta, fontsize=10, ha='center')

    # ---------- Calcular magnitud máxima para escalar grosor ----------
    corrientes = [
        J_nP_arr, J_pN_arr, J_nN_arr, J_pP_arr,
        J_nN_dif, J_pP_dif, J_nP_dif, J_pN_dif
    ]
    max_magnitud = max(abs(np.array(corrientes)))

    # ---------- QNR-P ----------
    y_base = 1.0
    # Minoritarios (electrones)
    flecha(-Wp*0.6, y_base, 1, J_nP_dif, 'blue',  r'$J_{nP}^{dif}$')
    flecha(-Wp*0.6, y_base-0.3, 1, J_nP_arr, 'navy',  r'$J_{nP}^{arr}$')
    # Mayoritarios (huecos)
    flecha(-Wp*0.3, y_base, 1, J_pP_dif, 'red',   r'$J_{pP}^{dif}$')
    flecha(-Wp*0.3, y_base-0.3, 1, J_pP_arr, 'darkred', r'$J_{pP}^{arr}$')

    # ---------- SCR ----------
    flecha(0, y_base-0.6, -1, 0.5*(J_nP_dif + J_pN_dif), 'black', r'$J_{SCR}$')

    # ---------- QNR-N ----------
    # Minoritarios (huecos)
    flecha(Wn*0.3, y_base, -1, J_pN_dif, 'red',  r'$J_{pN}^{dif}$')
    flecha(Wn*0.3, y_base-0.3, -1, J_pN_arr, 'darkred',  r'$J_{pN}^{arr}$')
    # Mayoritarios (electrones)
    flecha(Wn*0.6, y_base, -1, J_nN_dif, 'blue',  r'$J_{nN}^{dif}$')
    flecha(Wn*0.6, y_base-0.3, -1, J_nN_arr, 'navy',  r'$J_{nN}^{arr}$')

    # ---------- Ejes y formato ----------
    ax.text(-Wp*0.8, y_base+0.4, "Minoritarios", fontsize=10)
    ax.text(-Wp*0.2, y_base+0.4, "Mayoritarios", fontsize=10)
    ax.text(Wn*0.2, y_base+0.4, "Mayoritarios", fontsize=10)
    ax.text(Wn*0.8, y_base+0.4, "Minoritarios", fontsize=10)

    ax.set_xlim(-Wp, Wn)
    ax.set_ylim(0, 2)
    ax.set_xlabel("x (posición)", fontsize=12)
    ax.set_ylabel("Corrientes", fontsize=12)
    ax.set_title("Densidades de corriente de arrastre y difusión", fontsize=13)
    ax.grid(alpha=0.3)
    plt.tight_layout()
    plt.show()




def punto11(ni,Na,Nd,Wp,Wn,Va,T):

    print("\nRealizar un gráfico del diodo PN que contenga todas las corrientes de las tres regiones de la aproximación de vaciamiento, indicando módulo y sentido (usar los valores calculados en los ı́tems anteriores) y si son de mayoritarios o minoritarios.")
    
    coeficientes = movilidades_y_difusion(Na,Nd,T)

    #corrientes de arrastre minoritarios
    J_nP_arr , j_pN_arr = punto10(ni,Na,Nd,Wp,Wn,Va,T,False)

    #corrientes de arrastre mayoritarios
    J_nN_arr, J_pP_arr = punto8(ni,Na,Nd,Wp,Wn,Va,T,False)

    #Corrientes de Difusión Mayoritarios
    J_nN_dif, j_pP_dif = punto7(ni,Na,Nd,Wp,Wn,Va,T,False)

    #Corrientes de Difusión Minoritarios
    J_nP_dif,j_pN_dif = obtener_porcentajes_Jn_Jp(ni,Na,Nd,Wp,Wn,coeficientes,Va,T)

    # Corrientes en lado P 
    #Minoritario
    #J_nP_dif =
    #J_nP_arr =
    #Mayoritarios
    #j_pP_dif = 
    #j_pP_arr = 

    # Corrientes en lado N
    #Minoritario
    #j_pN_dif = 
    #j_pN_arr = 

    #Mayoritarios
    #J_nN_dif =
    #J_nN_arr =
   



    J_arr = {'n': 0.04, 'p': 1}

    J_dif = {'n': 10, 'p': 0.4}
    
    Graficar_corrientes_diodo(J_nP_arr, j_pN_arr,J_nN_arr, J_pP_arr,J_nN_dif, j_pP_dif,J_nP_dif, j_pN_dif,Wn*1e6, Wp*1e6, xp = 2, xn=2)

    return