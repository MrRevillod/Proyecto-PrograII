import csv
from dataclasses import dataclass
import classes
from classes import *

def csvx (x):
    with open(x, 'r') as c:
        line = csv.reader(c)
        lista = list(line)
        for i in lista:
            id = int(i[0])
            nombre = i[1]
            tipo = i[2]
            masa = i[3]
            peso = int(i[4])
            producto = Producto(id, nombre, tipo, masa, peso)
            #print(f"Producto: {producto.nombre} - Tipo: {producto.tipo} - Masa: {producto.masa} - Peso: {producto.peso}")

        # print (f"C.Normal_Grande {Contenedor_NG.productos}")
        # print (f"C.Normal_Pequeno {Contenedor_NP.productos}")
        # print (f"C.Refrigerado_Grande {Contenedor_RG.productos}")
        # print (f"C.Refrigerado_Pequeno {Contenedor_RP.productos}")

if __name__ == "__main__":
    csvx("Lista.csv")

