import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import cumtrapz

from punto2 import obtener_e_max,x_,obtener_tension_contacto

k = 1.380649e-23   # J/K
q = 1.602176634e-19 # C
e_o = 88.5e-15 # C/(V cm)
e_s = 11.9*e_o


def densidad_de_carga(Na, Nd, phi_bi, Va):
    # Longitudes de agotamiento
    x_n0 = x_(phi_bi, Na, Nd, e_s)
    x_p0 = x_(phi_bi, Nd, Na, e_s)
    x_na = x_(phi_bi - Va, Na, Nd, e_s)
    x_pa = x_(phi_bi - Va, Nd, Na, e_s)

    # --- Mismo rango de eje X para todos los gráficos ---
    x_lim_max = 1.5 * max(x_n0 + x_p0, x_na + x_pa) / 2   # [cm]
    x_um = x_lim_max * 1e4                                # [μm]

    rho_Na = -q * Na
    rho_Nd = q * Nd

    fig, ax = plt.subplots(figsize=(10, 6))
    x_etd = np.array([-x_lim_max, -x_p0, -x_p0, 0, 0, x_n0, x_n0, x_lim_max])
    rho_etd = np.array([0, 0, rho_Na, rho_Na, rho_Nd, rho_Nd, 0, 0])
    ax.step(x_etd * 1e4, rho_etd, 'blue', alpha=0.7, linewidth=5, label='Equilibrio (ETD)')

    x_polarizado = np.array([-x_lim_max, -x_pa, -x_pa, 0, 0, x_na, x_na, x_lim_max])
    rho_polarizado = np.array([0, 0, rho_Na, rho_Na, rho_Nd, rho_Nd, 0, 0])
    ax.step(x_polarizado * 1e4, rho_polarizado, 'red', alpha=0.7, linewidth=5, label=f'$V_a = {Va*1000:.0f} \\,mV$')

    ax.axhline(0, color='k', linewidth=0.8)
    ax.axvline(0, color='k', linestyle='--', linewidth=0.9, label='Unión metalúrgica')
    # # # Etiquetas de posiciones # 
    marcas_x = np.array([-x_p0* 1e4, -x_pa* 1e4, 0, x_n0* 1e4, x_na* 1e4]) # 
    etiquetas_x = [r'$-x_{p0}$', r'$-x_{pa}$', '0', r'$x_{n0}$', r'$x_{na}$'] # 
    plt.xticks(marcas_x, etiquetas_x, fontsize=12)

    ax.set_xlim(-x_um, x_um)  # mismo límite que campo eléctrico
    ax.set_xlabel('Posición $x$ [nm]')
    ax.set_ylabel('Densidad de Carga [C/cm³]')
    ax.set_title('Densidad de Carga en una Unión p–n')
    ax.grid(True, linestyle='--', alpha=0.6)
    ax.legend()
    plt.tight_layout()
    plt.show()

    return x_lim_max  # <--- devolvemos el límite para reutilizarlo


def campo_electrico(Na, Nd, phi_bi, Va, x_lim_max):
    xn0 = x_(phi_bi, Na, Nd, e_s)
    xp0 = x_(phi_bi, Nd, Na, e_s)
    xna = x_(phi_bi - Va, Na, Nd, e_s)
    xpa = x_(phi_bi - Va, Nd, Na, e_s)

    x = np.linspace(-x_lim_max, x_lim_max, 5000)
    E_o = np.zeros_like(x)

    mask_p = (x > -xp0) & (x <= 0)
    E_o[mask_p] = -q * Na / e_s * (x[mask_p] + xp0)
    mask_n = (x > 0) & (x <= xn0)
    E_o[mask_n] = q * Nd / e_s * (x[mask_n] - xn0)

    E_a = E_o * np.sqrt(1 - Va / phi_bi)

    plt.figure(figsize=(10, 6))
    plt.plot(x * 1e4, E_o / 1e3, color='blue', linewidth=5, alpha=0.8, label=r'$\mathcal{E}_0(x)$')
    plt.plot(x * 1e4, E_a / 1e3, color='red', linewidth=5, alpha=0.8, label=rf'$\mathcal{{E}}_a(x)$ ({Va*1000:.0f} mV)')

    plt.axhline(0, color='k', linewidth=0.8)
    plt.axvline(0, color='k', linestyle='--', linewidth=0.9, label='Unión metalúrgica')

    plt.xlim(-x_lim_max * 1e4, x_lim_max * 1e4)
    plt.xlabel('Posición $x$ [nm]')
    plt.ylabel('Campo eléctrico $\mathcal{E}(x)$ [kV/cm]')
    plt.title('Campo eléctrico en una unión p–n')
    plt.grid(True, linestyle='--', alpha=1)
    plt.legend()
    plt.yticks(np.arange(-1, -13, -1))  # de -1 a -12, paso -1
    plt.tight_layout()
    plt.show()
    
    return 



def potencial_electrico(ni,Na,Nd,phi_bi,T, Va, x_lim_max ):

    Vth = (k*T)/q 

    xn0 = x_(phi_bi, Na, Nd, e_s)
    xp0 = x_(phi_bi, Nd, Na, e_s)
    xna = x_(phi_bi - Va, Na, Nd, e_s)
    xpa = x_(phi_bi - Va, Nd, Na, e_s)

    x = np.linspace(-x_lim_max, x_lim_max, 5000)
    phi_o = np.zeros_like(x)
    
    phi_n = Vth*np.log(Nd/ni)
    phi_p = -Vth*np.log(Na/ni)

     # Lado p negativo
    mask1 = x < -xp0
    phi_o[mask1] = phi_p

    mask4 = x > xn0
    phi_o[mask4] = phi_n

    mask2 = (x >= -xp0) & (x < 0)
    phi_o[mask2] = phi_p + q * Na / (2 * e_s) * (x[mask2] + xp0)**2
    
    mask3 = (x >= 0) & (x <= xn0)
    phi_o[mask3] = phi_n - q * Nd / (2 * e_s) * (x[mask3] - xn0)**2
    
    polarizacion_label = f"Potencial con polarización $V_a = {Va*1000:.0f}$ mV | ($\phi_0 + V_a$)"

    phi_con_va = np.zeros_like(x)
    mask1_a = x < -xpa
    mask2_a = (x >= -xpa) & (x < 0)
    mask3_a = (x >= 0) & (x <= xna)
    mask4_a = x > xna

    phi_con_va[mask1_a] = phi_p + Va
    phi_con_va[mask2_a] = (phi_p + Va) + q * Na / (2 * e_s) * (x[mask2_a] + xpa)**2
    phi_con_va[mask3_a] =  (phi_n)  - q * Nd / (2 * e_s) * (x[mask3_a] - xna)**2
    phi_con_va[mask4_a] = phi_n

    plt.figure(figsize=(10, 6))
    plt.plot(x*1e4, phi_o*1e3, linewidth = 5 ,alpha = 0.8 ,label= "Potencial de Equilibrio ($\phi_0$)")  # eje x en µm
    plt.plot(x*1e4,phi_con_va*1e3,color = "red", linewidth = 5 ,alpha = 0.8, label=polarizacion_label)  # eje x en µm
    plt.xlabel("x [nm]")
    plt.ylabel("Potencial φ(x) [mV]")

    plt.legend(loc='upper left', frameon=True, fancybox=True, shadow=True, borderpad=1) # 'frameon=True' para el recuadro, 'shadow' para una sombra, 'borderpad' para el espacio interno

    plt.title('Potencial eléctrico [mV] en función de la distancia [nm]')
    plt.grid(True)
    plt.show()

    return 


def punto4(Na,Nd,ni,T,Va):
    
    print("\nPunto 4 : \nConfeccionar los gráficos de la densidad de carga, el campo eléctrico y la función potencial eléctrica en función de la distancia (en total son tres gráficos). Cada uno debe tener dos curvas (ETD y tensión aplicada) y estar destacado como varı́a la zona de vaciamiento. \n")
    
    phi_bi = obtener_tension_contacto(Na,Nd,ni,T)

    x_lim_max = densidad_de_carga(Na,Nd,phi_bi, Va)

    campo_electrico(Na,Nd,phi_bi, Va, x_lim_max )


    potencial_electrico(ni,Na,Nd,phi_bi,T, Va, x_lim_max )
    
    return