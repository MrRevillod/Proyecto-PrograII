from dataclasses import dataclass


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

N_Pequeño = Contenedor_N(12, ["Normal, Inerte, Solida"], []) #Contenedores Estandar / 2
N_Grande = Contenedor_N(24, ["Normal, Inerte, Solida"], [])  #Contenedores Estandar

@dataclass

class Contenedor_R:

    capacidad: int
    carga: str
    productos: int

R_Pequeño = Contenedor_R(10, ["Normal, Inerte, Solida, Refrigerada"], []) #Contenedores Estandar / 2
R_Grande = Contenedor_R(20, ["Normal, Inerte, Solida, Refrigerada"], []) #Contenedores Estandar


@dataclass

class Estanque:

    capacidad: int
    carga: str
    productos: int

E_Liquidos = Estanque(24, ["Inerte, Liquida, Gas"], []) #Contenedores Estandar
E_Liquidos_I = Estanque(24, ["Inerte, Liquida, Gas, Inflamable"], []) #Contenedores Estandar


def readcsv (x):
    with open(x, 'r') as c:
        reader = csv.reader(c)
        lst = list(reader)
        print(lst)


if __name__ == "__main__":
    readcsv("Lista.csv")
"""     main(csv) """

