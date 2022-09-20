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

    matriz  =  [
        [0,Contenedor_NP.capacidad],    # cant_NP
        [0,Contenedor_NG.capacidad],    # cant_NG
        [0,Contenedor_RP.capacidad],    # cant_RP
        [0,Contenedor_RG.capacidad],    # cant_RG
        [0,Estanque.capacidad],         # cant_E
        [0,Estanque_I.capacidad]]       # cant_EI

    for x in range(len(contenedores)):
        if contenedores[x] == 0:
            matriz[x][0] = 0
        else:
            matriz[x][0] = contenedores[x]//matriz[x][1] + 1

    cant_total = float(matriz[0][0]*0.5 + matriz[1][0] + matriz[2][0]*0.5 +
                    matriz[3][0] + matriz[4][0] + matriz[5][0])

    print(f"Se necesitan {matriz[0][0]} contenedores normales pequeños")
    print(f"Se necesitan {matriz[1][0]} contenedores normales grandes")
    print(f"Se necesitan {matriz[2][0]} contenedores refrigerados pequeños")
    print(f"Se necesitan {matriz[3][0]} contenedores refrigerados grandes")
    print(f"Se necesitan {matriz[4][0]} estanques normales")
    print(f"Se necesitan {matriz[5][0]} estanques inflamables \n")

    return cant_total


def cantidad_v(cant_total):    

    Capacidades = [Barco.capacidad, Tren.capacidad, Avion.capacidad, Camion.capacidad]

    V_necesarios = [[0,"barco"],[0,"tren"],[0,"avión"],[0,"camión"]]

    for x in range(len(Capacidades)):
        if cant_total <= Capacidades[x]:
            V_necesarios[x][0] = cant_total/Capacidades[x]
            print(f"Se puede transportar por un {V_necesarios[x][1]}")
        else:
            V_necesarios[x][0] = int(cant_total/Capacidades[x] + 1)
            print(f"Se necesitan {V_necesarios[x][0]} {V_necesarios[x][1]} para transportar todo")

    necesarios = [V_necesarios[0][0],V_necesarios[1][0],V_necesarios[2][0],
                    V_necesarios[3][0]]

    return necesarios


def costos(necesarios):

    Presupuesto = [[0,Barco.costo],[0,Tren.costo],[0,Avion.costo],[0,Camion.costo]]

    Vehiculos = ["barcos","trenes","aviones","camiones"]

    Costos = []

    for x in range(len(necesarios)):
        if necesarios[x] <= 1:
            Presupuesto[x][0] = Presupuesto[x][1]
            print(f"El costo total al utilizar {Vehiculos[x]} es: "  "{:,.0f}".format(Presupuesto[x][0]).replace(",","@").replace(".",",").replace("@","."))
            lista = [Vehiculos[x],Presupuesto[x][0]]
            Costos.append(lista)

        else:
            Presupuesto[x][0] = int(necesarios[x]*Presupuesto[x][1])
            print(f"El costo total al utilizar {Vehiculos[x]} es: "  "{:,.0f}".format(Presupuesto[x][0]).replace(",","@").replace(".",",").replace("@","."))
            lista = [Vehiculos[x],Presupuesto[x][0]]
            Costos.append(lista)
    return Costos


def print_mayor_rentabilidad(Costos):
    rentable = 0
    for x in range(len(Costos)):
        if rentable <= Costos[x][1]:
            rentable = rentable
        else:
            pass


if __name__ == "__main__":

    costos(cantidad_v(cantidad_c(main(csvx("MOCK_DATA.csv")))))