import csv
from dataclasses import dataclass
import classes
from classes import *

@dataclass
class Producto :
    id: int
    nombre: str
    tipo: str
    masa: str
    peso: int

def csvx (x):
    with open(x, 'r') as c:
        line = csv.reader(c)
        lista = list(line)
        array = []
        
        for i in lista:
            id = int(i[0]) ; nombre = i[1] ; tipo = i[2]
            masa = i[3]    ; peso = int(i[4])

            producto = [id, nombre, tipo, masa, peso]
            array.append(producto)            

        for x in range(len(array)):
            tupla = (array[x][0], array[x][4])

            if array[x][2] == "normal":

                if array[x][3] in Contenedor_NP.carga and array[x][4] <= Contenedor_NP.capacidad:
                    Contenedor_NP.productos.append(tupla)
                    array[x] = []
                
                elif array[x][3] in Contenedor_RG.carga and array[x][4] <= Contenedor_RG.capacidad:
                    Contenedor_NG.productos.append(tupla)
                    array[x] = []

                elif array[x][3] in Estanque.carga:
                    Estanque.productos.append(tupla)
                    array[x] = []

            elif array[x][2] == "refrigerado":

                if array[x][3] in Contenedor_RP.carga and array[x][4] <= Contenedor_RP.capacidad:
                    Contenedor_RP.productos.append(tupla)
                    array[x] = []
                
                elif array[x][3] in Contenedor_RG.carga and array[x][4] <= Contenedor_RG.capacidad:
                    Contenedor_RG.productos.append(tupla)
                    array[x] = []
            
            elif array[x][2] == "inflamable":

                if array[x][3] in Estanque_I.carga:
                    Estanque_I.productos.append(tupla)
                    array[x] = [] 
            
        print (f"C.Normal_Grande {Contenedor_NG.productos}\n C.Normal_Pequeno {Contenedor_NP.productos}\n C.Refrigerado_Grande {Contenedor_RG.productos}\n C.Refrigerado_Pequeno {Contenedor_RP.productos}\n Estanque {Estanque.productos}\n Estanque_Inflamable {Estanque_I.productos}")

if __name__ == "__main__":
    csvx("Lista.csv")


