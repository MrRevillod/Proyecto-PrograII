from dataclasses import dataclass
@dataclass
class Barco:
    costo: int = 1000000000
    capacidad: int = 24000
    
@dataclass
class Tren:
    costo: int = 100000000
    capacidad: int = 10000

@dataclass
class Avion:
    costo: int = 10000000
    capacidad: int = 1000

@dataclass
class Camion:
    costo: int = 5000000
    capacidad: int = 100
@dataclass
class Contenedor_NP:
    capacidad: int = 12000
    tipo = "normal"
    carga = ["solida","inerte"]
    productos  = []
@dataclass
class Contenedor_NG:
    capacidad: int = 24000
    tipo = "normal"
    carga = ["solida", "inerte"]
    productos  = []
@dataclass
class Contenedor_RG:
    capacidad: int = 20000
    tipo = "refrigerada"
    carga = ["solida", "normal", "liquido", "inerte"]
    productos = []
@dataclass
class Contenedor_RP:
    capacidad: int = 10000
    tipo = "refrigerada"
    carga = ["solida", "normal", "liquido", "inerte"]
    productos = []
@dataclass
class Estanque:
    capacidad: int = 24000
    tipo = "normal"
    carga = ["gas", "liquido"]
    productos  = []
@dataclass
class Estanque_I:
    capacidad: int = 20000
    tipo = "inflamable"
    carga = ["gas", "liquido"]
    productos  = []