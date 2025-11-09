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
    mostrando claramente cuáles son mayoritarios/minoritarios
    y distinguiendo por color y tipo de corriente.
    """

    um = 1e-6
    Wn_um, Wp_um, xn_um, xp_um = Wn/um, Wp/um, xn/um, xp/um

    fig, ax = plt.subplots(figsize=(13, 6))

    # ----- Regiones -----
    ax.axvspan(-Wp_um, -xp_um, color='#ffc8c8', alpha=0.4, label='QNR–P')
    ax.axvspan(-xp_um, xn_um+2*45*10000, color='#fdfdfd', alpha=0.9, label='SCR')
    ax.axvspan(xn_um, Wn_um, color='#b3d9ff', alpha=0.4, label='QNR–N')

    # ----- Líneas divisorias -----
    ax.axvline(-xp_um, color='k', linestyle='--', lw=1)
    ax.axvline(xn_um, color='k', linestyle='--', lw=1)
    ax.axvline(0, color='k', lw=0.8)

    # ----- Etiquetas de regiones -----
    ax.text(-Wp_um/2, 2.7, "QNR–P", ha='center', fontsize=16, fontweight='bold')
    ax.text(0.15, 2.7, "SCR", ha='center', fontsize=16, fontweight='bold')
    ax.text(Wn_um/2, 2.7, "QNR–N", ha='center', fontsize=16, fontweight='bold')

    # ---------- Flecha auxiliar ----------
    def flecha(x, y, sentido, J, color, estilo, etiqueta):
        dx = 2*0.8 * np.sign(sentido)
        lw = 3 + 5 * abs(J*2) / max(1e-12, max_magnitud)
        ax.arrow(x, y, dx, 0, head_width=0.15, head_length=0.25,fc=color, ec=color, lw=lw, alpha=0.9, linestyle=estilo, length_includes_head=True)
        ax.text(x, y + 0.25, etiqueta, fontsize=12, ha='center', color=color, fontweight='bold')

    # ---------- Magnitud máxima ----------
    corrientes = [J_nP_arr, J_pN_arr, J_nN_arr, J_pP_arr,J_nN_dif, J_pP_dif, J_nP_dif, J_pN_dif]
    max_magnitud = max(abs(np.array(corrientes)))

    y_base = 1.0

    # ===== QNR–P =====
    # Minoritarios: electrones (azul)
    flecha(-Wp_um*0.7, y_base, 1,  J_nP_dif, 'blue', '-',  rf'$\mathbf{{J_{{nP,dif}}}}$ = {J_nP_dif*1e6:.2f} μA/cm²')
    flecha(-Wp_um*0.7, y_base-0.6, 1,  J_nP_arr, 'darkblue', '-', rf'$\mathbf{{J_{{nP,arr}}}}$ = {J_nP_arr*1e15:.3f} fA/cm²')

    # Mayoritarios: huecos (rojo)
    flecha(-Wp_um*0.25, y_base, -1, J_pP_dif, 'red', '-',  rf'$\mathbf{{J_{{pP,dif}}}}$ = {J_pP_dif*1e6:.2f} μA/cm²')
    flecha(-Wp_um*0.3, y_base-0.6, 1, J_pP_arr, 'darkred', '-', rf'$\mathbf{{J_{{pP,arr}}}}$ = {J_pP_arr*1e6:.2f} μA/cm²')

    # ===== QNR–N =====
    # Minoritarios: huecos (rojo)
    flecha(Wn_um*0.35, y_base, 1, J_pN_dif, 'red', '-', rf'$\mathbf{{J_{{pN,dif}}}}$ = {J_pN_dif*1e6:.2f} μA/cm²')
    flecha(Wn_um*0.35, y_base-0.6, 1, J_pN_arr, 'darkred', '-', rf'$\mathbf{{J_{{pN,arr}}}}$ = {J_pN_arr*1e15:.3f} f A/cm²')

    # Mayoritarios: electrones (azul)
    flecha(Wn_um*0.8, y_base, -1, J_nN_dif, 'blue', '-', rf'$\mathbf{{J_{{nN,dif}}}}$ = {J_nN_dif*1e6:.2f} μA/cm²')
    flecha(Wn_um*0.7, y_base-0.6, 1, J_nN_arr, 'darkblue', '-', rf'$\mathbf{{J_{{nN,arr}}}}$ = {J_nN_arr*1e6:.2f} μA/cm²')

    # ===== Etiquetas globales =====
    ax.text(-Wp_um*0.7, y_base+1.0, "n: Minoritarios", fontsize=15, color='navy', ha='center', fontweight='bold')
    ax.text(-Wp_um*0.2, y_base+1.0, "p: Mayoritarios", fontsize=15, color='darkred', ha='center', fontweight='bold')
    ax.text(Wn_um*0.25, y_base+1.0, "p: Minoritarios", fontsize=15, color='darkred', ha='center', fontweight='bold')
    ax.text(Wn_um*0.75, y_base+1.0, "n: Mayoritarios", fontsize=15, color='navy', ha='center', fontweight='bold')

    # ===== Leyenda =====
    legend_elements = [
        plt.Line2D([0], [0], color='blue', lw=3, label='Difusión (electrones)'),
        plt.Line2D([0], [0], color='darkblue', lw=3, linestyle='-', label='Arrastre (electrones)'),
        plt.Line2D([0], [0], color='red', lw=3, label='Difusión (huecos)'),
        plt.Line2D([0], [0], color='darkred', lw=3, linestyle='-', label='Arrastre (huecos)'),
    ]
    ax.legend(handles=legend_elements, loc='upper right', fontsize=10, frameon=True)

    # ===== Ejes =====
    ax.set_xlim(-Wp_um, Wn_um)
    ax.set_ylim(0, 3.2)
    ax.set_xlabel("Posición x [μm]", fontsize=13)
    ax.set_ylabel("Intensidad relativa de corriente", fontsize=13)
    ax.set_title("Densidades de Corrientes en el diodo PN con polarización Va = 210 mV", fontsize=15, fontweight='bold')
    ax.grid(alpha=0.25)
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