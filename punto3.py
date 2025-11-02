from punto2 import obtener_e_max,x_,obtener_tension_contacto


def imprimir_datos(phi_bi,x_no , x_po, e_max, Va):

    print("Ahora con la tensión de polarización Va")
    print(f"Tensión de Contacto {phi_bi*1000:.5g} mV \n")
    print(f"Tensión de polarización {Va*1000:.5g} mV")

    print(f"x_no =  {x_no*1e6:.3g} um    x_po = {x_po*1e6:.3g} um")
    print(f"E_max = {e_max/1000:.3g} kV/cm")
          
    return 

def punto3(Na,Nd,ni,T,e_s,Va ):
    phi_bi = obtener_tension_contacto(Na,Nd,ni,T)
    x_no = x_(phi_bi - Va, Na , Nd,e_s )
    x_po = x_(phi_bi - Va , Nd , Na ,e_s )
    e_max = obtener_e_max(phi_bi - Va,Na,Nd,e_s)

    imprimir_datos(phi_bi ,x_no , x_po , e_max, Va)
    return 