import matplotlib.pyplot as plt
import numpy as np



k = 1.380649e-23   # J/K
q = 1.602176634e-19 # C
e_o = 88.5e-15 # C/(V cm)
e_s = 11.9*e_o


def  imprimir_concentraciones(ni,Na,Nd,T,Va):

    # Convertir μm -> cm
    W = 22 * 1e-4

    # Dividir la región en P y N
    x = np.linspace(-W/2, W/2, 1000)

    # Regiones
    x_p = x[x < 0]
    x_n = x[x >= 0]

    # Concentraciones
    p_p = Na
    n_p = (ni**2) / Na
    n_n = Nd
    p_n = (ni**2) / Nd

    # Crear arrays del mismo tamaño
    p = np.where(x < 0, p_p, p_n)
    n = np.where(x < 0, n_p, n_n)

    # Graficar
    plt.figure(figsize=(8,5))
    plt.semilogy(x*1e4, p, label="Huecos p(x)", color='red',linewidth = 5,alpha = 0.8)
    plt.semilogy(x*1e4, n, label="Electrones n(x)", color='blue',linewidth = 5,alpha = 0.8)
    plt.axvline(0, color='k', linestyle='--', label="Unión")
    plt.xlabel("Posición x [μm]")
    plt.ylabel("Concentración [1/cm³]")
    plt.title(f"Distribución de portadores en un diodo de {22} μm")


    # Indicar regiones P y N
    plt.text(-22/4, max(Na, Nd)*0.7, "Lado P (x < 0)", color='black', fontsize=11, fontweight='bold')
    plt.text(22/4, max(Na, Nd)*0.7, "Lado N (x > 0)",  color='black', fontsize=11, fontweight='bold')

    plt.legend()
    plt.grid(True, which="both")
    plt.show()

    return

def datos_enunciado(ni,Na, Nd, T, tao_n , tao_po , Va):
    Vth = (k*T)/q
    print(f"Temperatura: {T:.4g} K")
    print(f"Dopajes: Na = {Na:.2g} cm^-3, Nd = {Nd:.2g} cm^-3")
    print(f"Permitividad Electrica : {e_o*e_s:.2g}  C/(V cm) ")
    print(f"Tensión Termica : Vth = {Vth:.2g} V")
    print(f"Tensión Termica : tao_n = {tao_n:.3g} s")
    print(f"Tensión Termica : tao_po = {tao_po:.3g} s")
    print(f"Tensión de polarización :  { Va:.9g}" )

    imprimir_concentraciones(ni,Na,Nd,T,Va)


def movilidades_y_difusion(Na, Nd, T):

    """
    Devuelve un diccionario con:
      mu_nN, mu_pP, mu_nP, mu_pN  (cm^2 / V s)
      D_nN, D_pP, D_nP, D_pN     (cm^2 / s)
    NA: concentración región P [cm^-3]
    ND: concentración región N [cm^-3]
    T : temperatura [K]
    """
    Tn = T / 300.0
    Vt = k * T / q  # V

    # parámetros empíricos (electrones)
    mu_min_e = 88.0 * Tn**(-0.57)
    mu1_e    = 1250.0 * Tn**(-2.33)
    Nref_e   = 1.26e17 * Tn**(2.4)
    alpha_e  = 0.88 * Tn**(-0.146)

    # parámetros empíricos (huecos)
    mu_min_h = 54.3 * Tn**(-0.57)
    mu1_h    = 407.0 * Tn**(-2.23)
    Nref_h   = 2.35e17 * Tn**(2.4)
    alpha_h  = 0.88 * Tn**(-0.146)

    def mu_e(N):
        return mu_min_e + mu1_e / (1.0 + (N / Nref_e)**alpha_e)

    def mu_h(N):
        return mu_min_h + mu1_h / (1.0 + (N / Nref_h)**alpha_h)

    # movilidades (cm^2 / V s)
    mu_nN = mu_e(Nd)  # electrones en region N
    mu_pP = mu_h(Na)  # huecos en region P
    mu_nP = mu_e(Na)  # electrones en region P (minoritarios)
    mu_pN = mu_h(Nd)  # huecos en region N (minoritarios)

    # difusiones (cm^2 / s) : D = mu * Vt ; Vt en V, mu en cm^2/Vs => D en cm^2/s
    D_nN = mu_nN * Vt
    D_pP = mu_pP * Vt
    D_nP = mu_nP * Vt
    D_pN = mu_pN * Vt

    return {
        'mu_nN': mu_nN, 'mu_pP': mu_pP, 'mu_nP': mu_nP, 'mu_pN': mu_pN,
        'D_nN': D_nN,   'D_pP': D_pP,   'D_nP': D_nP,   'D_pN': D_pN
    }


def imprimir_parametros_u_D(parametros):
    """
    Imprime los parámetros con formato controlado para que sea legible.
    """
    print("\n--- Parámetros del Diodo Calculados ---")

    # Bucle para imprimir cada par clave:valor del diccionario
    for clave, valor in parametros.items():
        # Aplicamos el formato según el tipo de valor:

        if clave.startswith('mu') or clave.startswith('D_'):
            # Para movilidades (mu) y difusividades (D), usamos 2 decimales para claridad
            print(f"- {clave:<6s}: {valor:^10.2f}")
        
        elif clave == 'Vt':
            # Para el voltaje térmico (Vt), usamos 4 decimales o notación científica
            print(f"- {clave:<6s}: {valor:^10.4f} V")
        
        else:
            # Opción por defecto
            print(f"- {clave:<6s}: {valor:^10g}")

    print("\n")
   

def longitud_caracteristica(parametros , tao_n , tao_po ):

    D_nN  = parametros['D_nN']
    D_pN  = parametros['D_pN']
    D_nP  = parametros['D_nP']  # ¡Asegúrate de que esta clave exista en tu dict!
    D_pP  = parametros['D_pP']

    # Longitudes para electrones (n) en región N (N) o P (P)
    L_nN = np.sqrt(D_nN * tao_n) # Error común: Debería ser np.sqrt(D_n / tau_n)

    # Longitud de arrastre (ejemplo) para huecos (p) en región N (N)
    L_pN =np.sqrt(D_pN * tao_po)

    # Longitud para electrones (n) en región P (P)
    L_nP = np.sqrt(D_nP * tao_n) 
    
    # Longitud para huecos (p) en región P (P)
    L_pP = np.sqrt(D_pP * tao_po) 

    # NOTA: En la física de semiconductores, la longitud de difusión L 
    # se calcula típicamente como L = sqrt(D * tau)
    
    return  {
        'L_nN': L_nN, # Longitud de electrón en región N
        'L_pN': L_pN, # Longitud de hueco en región N
        'L_nP': L_nP, # Longitud de electrón en región P
        'L_pP': L_pP, # Longitud de hueco en región P
    }


def imprimir_longitudes(datos):
    """
    Imprime las longitudes características con notación científica ('.2e').
    """
    print("\n--- Longitudes Características Calculadas ---")
    
    # Iterar e imprimir con formato alineado
    for clave, valor in datos.items():
        # :<6s -> Clave alineada a la izquierda, 6 caracteres de ancho
        # :.2e -> Valor en notación científica, 2 decimales de precisión
        print(f"- {clave:<6s}: {valor:.2e} cm")

    print("\n")
   



def condicion_diodo_corto(parametros,Wn, Wp ):

    cumple = True

    L_nN  = parametros['L_nN']

    if( L_nN < Wn ):
        cumple = False

    L_pN  = parametros['L_pN']

    if( L_pN < Wp ):
        cumple = False


    L_nP  = parametros['L_nP'] 
    if( L_nP < Wn ):
        cumple = False

    L_pP  = parametros['L_pP']


    if( L_pP < Wp ):
       cumple = False





    return cumple



def punto1(ni,Na,Nd,T , tao_n ,tao_po ,Va, Wn, Wp):

    print("\nPunto 1: \n Hallar las movilidades y coeficientes de difusión para electrones y huecos de ambos lados de la juntura usando los datos de dopaje de la Tabla 1. Además, estimar la longitud caracterı́stica de difusión de los portadores minoritarios y determinar si es válida la hipótesis de diodo corto.\n\n")

    datos_enunciado(ni,Na, Nd, T,tao_n , tao_po , Va)

    movilidades_coeficientesD = movilidades_y_difusion(Na, Nd, T)

    imprimir_parametros_u_D(movilidades_coeficientesD)

    longitudes_de_difusion = longitud_caracteristica(movilidades_coeficientesD, tao_n, tao_po)

    imprimir_longitudes(longitudes_de_difusion)



    if(condicion_diodo_corto(longitudes_de_difusion, Wn ,Wp)):
        print("Cumple la condición de Diodo Corto")

    else:
        print("No cumple la condición de Diodo Corto")


    return 