import csv
from dataclasses import dataclass
import classes
from classes import *

@dataclass
class Producto :

    id: int ; nombre: str ; tipo: str
    masa: str ; peso: int

def csvx (x):
    with open(x, 'r') as c:
        line = csv.reader(c)
        lista = list(line)
        productos = []

        for i in lista:
            id = int(i[0]) ; nombre = i[1] ; tipo = i[2]
            masa = i[3]    ; peso = int(i[4])

            producto = [id, nombre, tipo, masa, peso]

            productos.append(producto) 

        return productos

def main(productos):

    contenedores = [0, 0, 0, 0, 0, 0] #[0] = NP, [1] = NG, [2] = RP, [3] = RG, [4] = E, [5] = E_I
    
    for x in range(len(productos)):
        
        tupla = (productos[x][0], productos[x][1], productos[x][2], productos[x][3], productos[x][4])

        if productos[x][2] == "normal":

            if productos[x][3] in Contenedor_NP.carga and productos[x][4] <= Contenedor_NP.capacidad:
                Contenedor_NP.productos.append(tupla)
                contenedores[0] += productos[x][4]
                productos[x] = []

            elif productos[x][3] in Contenedor_NG.carga and productos[x][4] > Contenedor_NP.capacidad:
                Contenedor_NG.productos.append(tupla)
                contenedores[1] += productos[x][4]
                productos[x] = []

            elif productos[x][3] in Estanque.carga:
                Estanque.productos.append(tupla)
                contenedores[4] += productos[x][4]
                productos[x] = []

        elif productos[x][2] == "refrigerado":

            if productos[x][3] in Contenedor_RP.carga and productos[x][4] <= Contenedor_RP.capacidad:
                Contenedor_RP.productos.append(tupla)
                contenedores[2] += productos[x][4]
                productos[x] = []

            elif productos[x][3] in Contenedor_RG.carga and productos[x][4] > Contenedor_RP.capacidad:
                Contenedor_RG.productos.append(tupla)
                contenedores[3] += productos[x][4]
                productos[x] = []

        elif productos[x][2] == "inflamable":

            if productos[x][3] in Estanque_I.carga:
                Estanque_I.productos.append(tupla)
                contenedores[5] += productos[x][4]
                productos[x] = []

    return contenedores

def cantidad_c(contenedores):

    if contenedores[0] == 0:
        cantNP = 0
    else:
        cantNP = contenedores[0]//Contenedor_NP.capacidad + 1

    if contenedores[1] == 0:
        cantNG = 0
    else:
        cantNG = contenedores[1]//Contenedor_NG.capacidad + 1

    if contenedores[2] == 0:
        cantRP = 0
    else:
        cantRP = contenedores[2]//Contenedor_RP.capacidad + 1

    if contenedores[3] == 0:
        cantRG = 0
    else:
        cantRG = contenedores[3]//Contenedor_RG.capacidad + 1

    if contenedores[4] == 0:
        cantE = 0
    else:
        cantE = contenedores[4]//Estanque.capacidad  + 1

    if contenedores[5] == 0:
        cantEI = 0
    else:
        cantEI = contenedores[5]//Estanque_I.capacidad + 1

    cant_total = cantNP*0.5 + cantNG + cantRP*0.5 + cantRG + cantE + cantEI

    print(f"Se necesitan {cantNP} contenedores normales pequeños")
    print(f"Se necesitan {cantNG} contenedores normales grandes")
    print(f"Se necesitan {cantRP} contenedores refrigerados pequeños")
    print(f"Se necesitan {cantRG} contenedores refrigerados grandes")
    print(f"Se necesitan {cantE} estanques normales")
    print(f"Se necesitan {cantEI} estanques inflamables \n")

    return cant_total

def cantidad_v(cant_total):

    Capacidades = [Barco.capacidad, Avion.capacidad, Camion.capacidad, Tren.capacidad]

    if cant_total <= Capacidades[0]:
        print("Se puede transportar por un barco")
    else: 
        B_necesarios = int(cant_total//Capacidades[0] + 1)
        print(f"Se necesitan {B_necesarios} barcos para transportar todo")

    if cant_total <= Capacidades[1]:
        print("Se puede transportar por un avion")

    else:
        A_necesarios = int(cant_total//Capacidades[1] + 1)
        print(f"Se necesitan {A_necesarios} aviones para transportar todo")
    
    if cant_total <= Capacidades[2]:
        print("Se puede transportar por un camion")
    else:
        C_necesarios = int(cant_total//Capacidades[2] + 1)
        print(f"Se necesitan {C_necesarios} camiones para transportar todo")

    if cant_total <= Capacidades[3]:
        print("Se puede transportar por un tren")

    else:
        T_necesarios = int(cant_total//Capacidades[3] + 1)
        print(f"Se necesitan {T_necesarios} trenes para transportar todo")

    necesarios = [B_necesarios, A_necesarios, C_necesarios, T_necesarios]

    return necesarios


def costos(necesarios):

    B_costo = necesarios[0]*Barco.costo
    A_costo = necesarios[1]*Avion.costo
    C_costo = necesarios[2]*Camion.costo
    T_costo = necesarios[3]*Tren.costo

    costos = [B_costo, A_costo, C_costo, T_costo]
    print (costos)

if __name__ == "__main__":


    (csvx("MOCK_DATA.csv"))
    main(csvx("MOCK_DATA.csv"))
    cantidad_c(main(csvx("MOCK_DATA.csv")))
    cantidad_v(cantidad_c(main(csvx("MOCK_DATA.csv"))))
    costos(cantidad_v(cantidad_c(main(csvx("MOCK_DATA.csv")))))