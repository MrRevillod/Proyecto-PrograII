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

        contenedores = [0, 0, 0, 0, 0, 0] 
        #[0] = NP, [1] = NG, [2] = RP, [3] = RG, [4] = E, [5] = E_I
        
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

        if contenedores[0] == 0:
            cantNP = 0
        else:
            cantNP = contenedores[0]//12000 + 1

        if contenedores[1] == 0:
            cantNG = 0
        else:
            cantNG = contenedores[1]//24000 + 1

        if contenedores[2] == 0:
            cantRP = 0
        else:
            cantRP = contenedores[2]//10000 + 1

        if contenedores[3] == 0:
            cantRG = 0
        else:
            cantRG = contenedores[3]//20000 + 1

        if contenedores[4] == 0:
            cantE = 0
        else:
            cantE = contenedores[4]//24000  + 1

        if contenedores[5] == 0:
            cantEI = 0
        else:
            cantEI = contenedores[5]//20000 + 1

        

    

    print(f"Contenedor NP: {Contenedor_NP.productos} Cantidad de contenedores: {cantNP}")
    print(f"Contenedor NG: {Contenedor_NG.productos} Cantidad de contenedores: {cantNG}")
    print(f"Contenedor RP: {Contenedor_RP.productos} Cantidad de contenedores: {cantRP}")
    print(f"Contenedor RG: {Contenedor_RG.productos} Cantidad de contenedores: {cantRG}")
    print(f"Estanque: {Estanque.productos} Cantidad de contenedores: {cantE}")
    print(f"Estanque I: {Estanque_I.productos} Cantidad de contenedores: {cantEI}")

if __name__ == "__main__":
    csvx("MOCK_DATA.csv")
