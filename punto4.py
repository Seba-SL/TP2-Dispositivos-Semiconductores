import matplotlib.pyplot as plt
import numpy as np

from punto2 import obtener_e_max,x_,obtener_tension_contacto

k = 1.380649e-23   # J/K
q = 1.602176634e-19 # C
e_o = 88.5e-15 # C/(V cm)
e_s = 11.9*e_o

def densidad_de_carga(Na, Nd, phi_bi, Va):
   

    # 1. CÁLCULOS PARA EQUILIBRIO (ETD, Va = 0)
    # Longitudes de agotamiento en equilibrio (x_n0 y x_p0)
    constante_0 = 2 * e_s * phi_bi / q
    
    x_n0 =  x_(phi_bi,Na,Nd,e_s )
    x_p0 =  x_(phi_bi, Nd,Na,e_s )

    # 2. CÁLCULOS PARA TENSIÓN APLICADA (Va)
    # Tensión efectiva para el caso polarizado
    phi_eff_a = phi_bi - Va

    if phi_eff_a < 0:
        print("Advertencia: Se ha alcanzado un colapso. Usando 0.001 V para evitar raíz cuadrada negativa.")
        phi_eff_a = 0.001  # Pequeño valor para evitar error en Va > phi_bi (polarización directa excesiva)

    constante_a = 2 * e_s * phi_eff_a / q
    
    x_na =  x_(phi_eff_a,Na,Nd,e_s )
    x_pa = x_(phi_eff_a, Nd,Na,e_s )

    # 3. CREACIÓN DE GRÁFICO

    # Rango total del eje x (para visualizar ambos casos cómodamente)
    x_lim_max = 1.2 * max(x_n0 + x_p0, x_na + x_pa) / 2
    x_lim_max_cm = x_lim_max * 1e4 # Conversión a μm para etiquetas del gráfico
    
  
    # Densidades de Carga
    rho_Na = -q * Na
    rho_Nd = q * Nd

    # Rango del Eje X: 1.2 veces el ancho máximo
    x_lim_max =  max(x_n0 + x_p0, x_na + x_pa) / 2
    
    fig, ax = plt.subplots(figsize=(8, 8))

    # --- Caso 1: Equilibrio (ETD, Línea Discontinua) ---
    x_etd = np.array([-x_lim_max, -x_p0, -x_p0, 0, 0, x_n0, x_n0, x_lim_max])
    rho_etd = np.array([0, 0, rho_Na, rho_Na, rho_Nd, rho_Nd, 0, 0])
    ax.step(x_etd * 1e4, rho_etd, 'orange',alpha = 0.7, where='post', linewidth=3.5, label='Equilibrio (ETD)')

    # --- Caso 2: Tensión Aplicada (Va, Línea Sólida) ---
    x_polarizado = np.array([-x_lim_max, -x_pa, -x_pa, 0, 0, x_na, x_na, x_lim_max])
    rho_polarizado = np.array([0, 0, rho_Na, rho_Na, rho_Nd, rho_Nd, 0, 0])
    ax.step(x_polarizado * 1e4, rho_polarizado, 'green',alpha = 0.7, where='post', linewidth=3.5, label=f'$V_a = {Va*1000:.0f}  \,mV$')

    # 3. FORMATO Y ANOTACIONES
    ax.axhline(0, color='k', linewidth=0.5)
    ax.axvline(0, color='k', linestyle=':', linewidth=0.9, label='Unión metalurgica')
    
    # # Etiquetas de la Unión
    ax.text(x_lim_max * 1e4 / 2, rho_Na * 0.9, f'$-qNd = {rho_Na*1e6:.2f}  \,\mu \;C/cm3$ ' , fontsize=14, ha='center')
    ax.text(x_lim_max * 1e4 / 2, rho_Nd * 0.85, f'$qNa = {rho_Nd*1e6:.2f}  \,\mu \;C/cm3$ ', fontsize=14, ha='center')
    
    # # Etiquetas de la Densidad de Carga
    ax.text(-x_lim_max * 1e4 * 0.09, rho_Nd, '$+qN_d  $', va='center', ha='right', fontsize=12)
    ax.text(x_lim_max * 1e4 * 0.2, rho_Na, '$-qN_a  $'  , va='center', ha='right', fontsize=12)
    
    # Corregido: Uso de r'...' y única pareja de $ para toda la expresión matemática.
    ax.set_xlabel('Posición $x$ [um] ')
    ax.set_ylabel('Densidad de Carga [cm^-3]')
    ax.set_title('Densidad de Carga en una Unión p-n')
    ax.legend()
    ax.grid(True, linestyle='--', alpha=0.6)

    # Marcas de Eje X para destacar la zona de vaciamiento
    marcas_x = sorted(np.unique([0, -x_p0, x_n0, -x_pa, x_na]))
    etiquetas_x = [f'{m*1e4:.2f}' for m in marcas_x] # Valores en µm
    ax.set_xticks(np.array(marcas_x) * 1e4)
    ax.set_xticklabels(etiquetas_x)

    plt.tight_layout()
    plt.show()


def punto4(Na,Nd,ni,T,Va):
    print("\nPunto 4 : \nConfeccionar los gráficos de la densidad de carga, el campo eléctrico y la función potencial eléctrica en función de la distancia (en total son tres gráficos). Cada uno debe tener dos curvas (ETD y tensión aplicada) y estar destacado como varı́a la zona de vaciamiento. \n")
    
    phi_bi = obtener_tension_contacto(Na,Nd,ni,T)

    densidad_de_carga(Na,Nd,phi_bi, Va)
    
    return