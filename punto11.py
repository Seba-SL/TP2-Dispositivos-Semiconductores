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
    Wn=11e-6, Wp=11e-6, xn=594e-9, xp=297e-9
):
    """
    Grafica las corrientes de arrastre y difusión en un diodo PN
    con escala espacial realista (μm y nm).

    Parámetros:
    ------------
    Todas las J_xx: magnitudes (positivas o negativas)
    Wn, Wp : longitudes de las regiones cuasi neutras [m]
    xn, xp : anchos de la zona de vaciamiento [m]
    """

    # Convertir a micrómetros para mostrar en el eje x
    um = 1e-6
    Wn_um, Wp_um, xn_um, xp_um = Wn/um, Wp/um, xn/um, xp/um

    fig, ax = plt.subplots(figsize=(10, 5))

    # ----- Regiones -----
    ax.axvspan(-Wp_um, -xp_um, color='lightcoral', alpha=0.4)  # QNR-P
    ax.axvspan(-xp_um, xn_um, color='white', alpha=0.9)        # SCR
    ax.axvspan(xn_um, Wn_um, color='lightblue', alpha=0.4)     # QNR-N

    # ----- Líneas de borde -----
    ax.axvline(-xp_um, color='k', linestyle='--', lw=1)
    ax.axvline(xn_um, color='k', linestyle='--', lw=1)
    ax.axvline(0, color='k', lw=0.8)

    # ----- Etiquetas de regiones -----
    ax.text(-Wp_um/2, 2.5, "QNR–P", ha='center', fontsize=20)
    ax.text(0, 2.5, "SCR", ha='center', fontsize=20)
    ax.text(Wn_um/2, 2.5, "QNR–N", ha='center', fontsize=20)

    # ---------- Función auxiliar para flechas ----------
    def flecha(x, y, sentido, J, color, etiqueta):
        """Dibuja una flecha proporcional a |J| con dirección según sentido"""
        dx = 1* np.sign(sentido)
        lw = 4+ 6 * abs(J) / max(1e-12, max_magnitud)
        ax.arrow(x, y, dx, 0, head_width=0.12, head_length=0.12,fc=color, ec=color, lw=lw, alpha=0.9, length_includes_head=True)
        ax.text(x, y + 0.18, etiqueta, fontsize=6, ha='center')

    # ---------- Calcular magnitud máxima para escalar grosor ----------
    corrientes = [
        J_nP_arr, J_pN_arr, J_nN_arr, J_pP_arr,
        J_nN_dif, J_pP_dif, J_nP_dif, J_pN_dif
    ]
    max_magnitud = max(abs(np.array(corrientes)))

    # ---------- QNR–P ----------
    y_base = 1.0
    flecha(-Wp_um*0.7, y_base,     1, J_nP_dif, 'blue', f'J_nP_dif = {J_nP_dif*1e6:.3f}  u A/cm^2')
    flecha(-Wp_um*0.7, y_base-0.5, 1, J_nP_arr, 'navy', f'J_nP_arr = {J_nP_arr*1e6:.3f}  u A/cm^2')
    flecha(-Wp_um*0.35, y_base,     1, J_pP_dif, 'red', f'J_pP_dif = {J_pP_dif*1e6:.3f}  u A/cm^2' )
    flecha(-Wp_um*0.35, y_base-0.5, 1, J_pP_arr, 'darkred',  f'J_pP_arr = {J_pP_arr*1e6:.3f}  u A/cm^2')

    # ---------- SCR ----------
    #flecha(0, y_base-0.6, -1, 0.5*(J_nP_dif + J_pN_dif), 'black', r'$J_{SCR}$')

    # ---------- QNR–N ----------
    flecha(Wn_um*0.35, y_base,    -1, J_pN_dif, 'red',  f'J_pN_dif = {J_pN_dif*1e6:.3f}  u A/cm^2')
    flecha(Wn_um*0.35, y_base-0.5,-1, J_pN_arr, 'darkred', f'J_pN_arr = {J_pN_arr*1e6:.3f}  u A/cm^2')
    flecha(Wn_um*0.7, y_base,     -1, J_nN_dif, 'blue', f'J_nN_dif = {J_nN_dif*1e6:.3f}  u A/cm^2')
    flecha(Wn_um*0.7, y_base-0.5, -1, J_nN_arr, 'navy', f'J_nN_arr = {J_nN_arr*1e6:.3f}  u A/cm^2')

    # ---------- Etiquetas ----------
    ax.text(-Wp_um*0.8, y_base+1,"Minoritarios", fontsize=12)
    ax.text(-Wp_um*0.25, y_base+1, "Mayoritarios", fontsize=12)
    ax.text(Wn_um*0.25, y_base+1, "Minoritarios", fontsize=12)
    ax.text(Wn_um*0.8, y_base+1, "Mayoritarios", fontsize=12)

    # ---------- Ejes ----------
    ax.set_xlim(-Wp_um, Wn_um)
    ax.set_ylim(0, 2.2)
    ax.set_xlabel("x [μm]", fontsize=12)
    ax.set_ylabel("Corrientes", fontsize=12)
    ax.set_title("Distribución de corrientes en el diodo PN (escala real)", fontsize=13)
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

    xn  = 594e-9
    xp = 297e-9
    
    Graficar_corrientes_diodo(J_nP_arr, j_pN_arr,J_nN_arr, J_pP_arr,J_nN_dif, j_pP_dif,J_nP_dif, j_pN_dif,Wn, Wp, xn, xp)

    return