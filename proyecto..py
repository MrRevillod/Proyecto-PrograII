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
        for i in lista:
            id = int(i[0])
            nombre = i[1]
            tipo = i[2]
            masa = i[3]
            peso = int(i[4])
            producto = Producto(id, nombre, tipo, masa, peso)
            #print(f"Producto: {producto.nombre} - Tipo: {producto.tipo} - Masa: {producto.masa} - Peso: {producto.peso}")
            

            #verificar si el producto es de tipo normal

            if tipo == "normal":
                if peso <= 12000:
                    for x in Contenedor_NP.carga:
                        if masa in Contenedor_NP.carga:
                            Contenedor_NP.productos.append(id)
                            break
                        
                elif peso > 12000:
                    for x in Contenedor_NG.carga:
                        if masa in Contenedor_NG.carga:
                            Contenedor_NG.productos.append(id)
                            break

            elif tipo == "refrigerado":
                if peso <= 10000:
                    for x in Contenedor_RP.carga:
                        if masa in Contenedor_RP.carga:
                            Contenedor_RP.productos.append(id)
                            break
                        
                elif peso > 10000:
                    for x in Contenedor_RG.carga:
                        if masa in Contenedor_RG.carga:
                            Contenedor_RG.productos.append(id)
                            break

            elif tipo == "normal":
                if masa == "liquido":
                    for x in Estanque.carga:
                        if masa in Estanque.carga:
                            Estanque.productos.append(id)
                            break
            
            elif tipo == "inflamable":
                    for x in Estanque_I.carga:
                        if masa in Estanque_I.carga:
                            Estanque_I.productos.append(id)
                            break
                        
        print (f"C.Normal_Grande {Contenedor_NG.productos}")
        print (f"C.Normal_Pequeno {Contenedor_NP.productos}")
        print (f"C.Refrigerado_Grande {Contenedor_RG.productos}")
        print (f"C.Refrigerado_Pequeno {Contenedor_RP.productos}")
        print (f"Estanque {Estanque.productos}")
        print (f"Estanque_Inflamable {Estanque_I.productos}")
        

if __name__ == "__main__":
    csvx("prueba.csv")

