import csv
from dataclasses import dataclass
from sys import api_version
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
        return lista

def Enlistar_Contenedores(lista):
    productos = []
    for i in lista:
        id = int(i[0]) ; nombre = i[1] ; tipo = i[2]
        masa = i[3]    ; peso = int(i[4])

        producto = [id, nombre, tipo, masa, peso]

        productos.append(producto) 

    contenedores = [0, 0, 0, 0, 0, 0] 
    #[0] = NP, [1] = NG, [2] = RP, [3] = RG, [4] = E, [5] = E_I
    
    for x in range(len(productos)):
        
        tupla = (productos[x][0], productos[x][4])

        if productos[x][2] == "normal":

            if productos[x][3] in Contenedor_NP.carga and productos[x][4] <= Contenedor_NP.capacidad:
                Contenedor_NP.productos.append(tupla)
                contenedores[0] += productos[x][4]
                productos[x] = []

            elif productos[x][3] in Contenedor_NG.carga and productos[x][4] <= Contenedor_NG.capacidad:
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

            elif productos[x][3] in Contenedor_RG.carga and productos[x][4] <= Contenedor_RG.capacidad:
                Contenedor_RG.productos.append(tupla)
                contenedores[3] += productos[x][4]
                productos[x] = []

        elif productos[x][2] == "inflamable":

            if productos[x][3] in Estanque_I.carga:
                Estanque_I.productos.append(tupla)
                contenedores[5] += productos[x][4]
                productos[x] = []

    print(f"\n{contenedores}\n")

    cantNP = contenedores[0]//12000 + 1
    cantNG = contenedores[1]//24000 + 1
    cantRP = contenedores[2]//10000 + 1
    cantRG = contenedores[3]//20000 + 1
    cantE = contenedores[4]//24000 + 1
    cantEI = contenedores[5]//20000 + 1
    Cant_total = cantNP*0.5+cantNG+cantRP*0.5+cantRG+cantE+cantEI

    print(f"Contenedor NP: {Contenedor_NP.productos} Cantidad de contenedores: {cantNP}")
    print(f"Contenedor NG: {Contenedor_NG.productos} Cantidad de contenedores: {cantNG}")
    print(f"Contenedor RP: {Contenedor_RP.productos} Cantidad de contenedores: {cantRP}")
    print(f"Contenedor RG: {Contenedor_RG.productos} Cantidad de contenedores: {cantRG}")
    print(f"Estanque: {Estanque.productos} Cantidad de contenedores: {cantE}")
    print(f"Estanque I: {Estanque_I.productos} Cantidad de contenedores: {cantEI}")
    print(f"La cantidad total de contenedores es: {Cant_total}")
    return Cant_total

def Contar_Vehiculos():
    Total_Vehículos = Barco.cantidad+Tren.cantidad+Avión.cantidad+Camión.cantidad
    print(f"La cantidad total de vehículos es: {Total_Vehículos}")
    print(f"Se deben usar {Barco.cantidad} barcos")
    print(f"Se deben usar {Tren.cantidad} tren")
    print(f"Se deben usar {Avión.cantidad} aviones")
    print(f"Se deben usar {Camión.cantidad} camiones")

def Rentabilidad_cont_por_Vehiculo(total_containt):

    Valor_Barco  = Barco.costo // (Barco.capacidad //total_containt)
    Valor_Tren   = Tren.costo  // (Tren.capacidad  //total_containt)
    Valor_Avión  = Avión.costo // (Avión.capacidad //total_containt)
    Valor_Camión = Camión.costo// (Camión.capacidad//total_containt)

    Vehículo_Óptimo = []
    matrix = [["Barco",Valor_Barco],["Tren",Valor_Tren]
                        ,["Avión",Valor_Avión],["Camión",Valor_Camión]]
    for x in range(len(matrix)):
        if (x+2) <= len(matrix):
            if matrix[x][1] <= matrix[x+1][1]:
                tupla = (matrix[x][0], matrix[x][1])
                Vehículo_Óptimo.append(tupla)

        else: break
    
    Costo_Total_Transporte = 0

    if Vehículo_Óptimo[-1][0] == "Barco":
        Barco.cantidad += 1
        print(f"El total de transporte en barcos es: ${Barco.costo}")
        Costo_Total_Transporte += Barco.costo
    if Vehículo_Óptimo[-1][0] == "Tren":
        Tren.cantidad += 1
        print(f"El total de transporte  en trenes es: ${Tren.costo}")
        Costo_Total_Transporte += Tren.costo
    if Vehículo_Óptimo[-1][0] == "Avión":
        Avión.cantidad += 1
        print(f"El total de transporte en aviónes es: ${Avión.costo}")
        Costo_Total_Transporte += Avión.costo
    if Vehículo_Óptimo[-1][0] == "Camión":
        Camión.cantidad += 1
        print(f"El total de transporte en camiones es: ${Camión.costo}")
        Costo_Total_Transporte += Camión.costo
    print(f"El costo total de transporte es: ${Costo_Total_Transporte}")

    print(f"costo para el barco  es: ${Valor_Barco} ")
    print(f"costo para el tren   es: ${Valor_Tren}  ")
    print(f"costo para el avión  es: ${Valor_Avión} ")
    print(f"costo para el camión es: ${Valor_Camión}")
    # print(f"El vehículo más óptimo es el: {Vehículo_Óptimo[-1][0]}")


def Total_Transporte():


    pass

def Procesar_Contenedores(total_containt):

    pass

# no se instancia la clase Producto() como objeto producto y tampoco de Vehiculos()

# if __name__ == "__main__":
#     Enlistar_Contenedores(csvx("Lista.csv"))

if __name__ == "__main__":
    Rentabilidad_cont_por_Vehiculo(Enlistar_Contenedores(csvx("Lista.csv")))


if __name__ == "__main__":
    Contar_Vehiculos()

""" 1,planchas_cobre,normal,solida,10000
2,carne_roja,refrigerado,solida,1000
3,gas_licuado,inflamable,gas,25000
4,aceite_cocina,inflamable,liquido,3000
5,leche,refrigerado,liquido,15000
6,carne_blanca,refrigerado,solida,20000
7,verduras,refrigerado,solida,5000
8,agua,normal,liquido,100000
9,helio,normal,gas,10000
10,planchas_cobre,normal,solida,10000 """