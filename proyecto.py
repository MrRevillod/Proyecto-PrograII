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

        print(f"\n{contenedores}\n")

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
        print(f"Se necesitan {cantEI} estanques inflamables")

        return cant_total





if __name__ == "__main__":
    (csvx("MOCK_DATA.csv"))
    main(csvx("MOCK_DATA.csv"))
    cantidad_c(main(csvx("MOCK_DATA.csv")))








"""     Rentabilidad_cont_por_Vehiculo((csvx("Lista.csv")))
    Contar_Vehiculos() """

""" def Rentabilidad_cont_por_Vehiculo(total_containt):
    # Se saca la rentabilidad para cada vehículo en base a la cantidad
    # total de contenedores
    Valor_Barco  = Barco.costo // (Barco.capacidad //total_containt)
    Valor_Tren   = Tren.costo  // (Tren.capacidad  //total_containt)
    Valor_Avion  = Avion.costo // (Avion.capacidad //total_containt)
    Valor_Camion = Camion.costo// (Camion.capacidad//total_containt)

    Vehículo_Óptimo = []
    # lleva el id con su nombre y el valor para saber cual es el
    # vehículo mas rentable

    matrix = [["Barco",Valor_Barco],["Tren",Valor_Tren]
                        ,["Avion",Valor_Avion],["Camion",Valor_Camion]]
    # recorre la "matrix" verificando el menor valor posible iterando
    # la rentabilidad de cada vehículo, esto lo hace con el valor del
    # vehículo actual(x) y el valor del siguiente vehículo(x+1). 
    # Por ultimo lo agrega a la lista Vehículo_Óptimo
    for x in range(len(matrix)):
        if (x+2) <= len(matrix):
            if matrix[x][1] <= matrix[x+1][1]:
                tupla = (matrix[x][0], matrix[x][1])
                Vehículo_Óptimo.append(tupla)

        else: break
    # Cuando el vehículo óptimo concide con el tipo de barco, primero
    # le suma 1 a la cantidad de vehículos de ese tipo, luego imprime
    # el costo del vehículo en específico y por último suma ese costo
    # a el valor total de todo el transporte
    Costo_Total_Transporte = 0
    if Vehículo_Óptimo[-1][0] == "Barco":
        Barco.cantidad += 1
        print(f"El total de transporte en barcos es: ${Barco.costo}")
        Costo_Total_Transporte += Barco.costo
    if Vehículo_Óptimo[-1][0] == "Tren":
        Tren.cantidad += 1
        print(f"El total de transporte  en trenes es: ${Tren.costo}")
        Costo_Total_Transporte += Tren.costo
    if Vehículo_Óptimo[-1][0] == "Avion":
        Avion.cantidad += 1
        print(f"El total de transporte en aviones es: ${Avion.costo}")
        Costo_Total_Transporte += Avion.costo
    if Vehículo_Óptimo[-1][0] == "Camion":
        Camion.cantidad += 1
        print(f"El total de transporte en camiones es: ${Camion.costo}")
        Costo_Total_Transporte += Camion.costo
    print(f"costo para el barco  es: ${Valor_Barco} ")
    print(f"costo para el tren   es: ${Valor_Tren}  ")
    print(f"costo para el avion  es: ${Valor_Avion} ")
    print(f"costo para el camion es: ${Valor_Camion}")
    print(f"El costo total de transporte es: ${Costo_Total_Transporte}")

def Contar_Vehiculos():
    # Se imprimen la cantidad de vehículos en particular y en conjunto total
    Total_Vehículos = Barco.cantidad+Tren.cantidad+Avion.cantidad+Camion.cantidad
    print(f"La cantidad total de vehículos es: {Total_Vehículos}")
    print(f"Se deben usar {Barco.cantidad} barcos")
    print(f"Se deben usar {Tren.cantidad} tren")
    print(f"Se deben usar {Avion.cantidad} aviones")
    print(f"Se deben usar {Camion.cantidad} camiones")

# no se instancia la clase Producto() como objeto producto y tampoco de Vehiculos() """