from dataclasses import dataclass
import csv


@dataclass

class Barco:

    costo: int = 1000000000 #USD
    capacidad: int = 24000  #Contenedores Estandar


@dataclass

class Tren:
    
    costo: int = 10000000 #USD
    capacidad: int = 250  #Contenedores Estandar

@dataclass

class Avion:
    
    costo: int = 1000000 #USD
    capacidad: int = 10  #Contenedores Estandar

@dataclass

class Camion:
    
    costo: int = 500000 #USD
    capacidad: int = 1  #Contenedores Estandar


@dataclass

class Contenedor_N:

    capacidad: int 
    carga: str
    productos: int

N_Pequeño = Contenedor_N(12000, ["Normal, Inerte, Solida"], []) #Contenedores Estandar / 2
N_Grande = Contenedor_N(24000, ["Normal, Inerte, Solida"], [])  #Contenedores Estandar

@dataclass

class Contenedor_R:

    capacidad: int
    carga: str
    productos: int

R_Pequeño = Contenedor_R(10000, ["Normal, Inerte, Solida, Refrigerada"], []) #Contenedores Estandar / 2
R_Grande = Contenedor_R(20000, ["Normal, Inerte, Solida, Refrigerada"], []) #Contenedores Estandar


@dataclass

class Estanque:

    capacidad: int
    carga: str
    productos: int

E_Liquidos = Estanque(24000, ["Inerte, Liquida, Gas"], []) #Contenedores Estandar
E_Liquidos_I = Estanque(24000, ["Inerte, Liquida, Gas, Inflamable"], []) #Contenedores Estandar


def readcsv (x):
    with open(x, 'r') as c:
        line = csv.reader(c)
        lista = list(line)
        return lista 

def Extraer_Peso(csv):
    for x in csv:
        for y in x:
            if y.isdigit():
                print(x[4])
                break

def Encontrar_Rentabilidad():
    profit_1 = 1000000000/24000
    profit_2 = 10000000/250
    profit_3 = 1000000/10
    profit_4 = 500000
    print()
    print(profit_1)
    print()
    print(profit_2)
    print()
    print(profit_3)
    print()
    print(profit_4)
    print()

# if __name__ == "__main__":
#     Extraer_Peso(readcsv("Lista.csv"))

if __name__ == "__main__":
    Encontrar_Rentabilidad()