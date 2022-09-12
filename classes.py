from dataclasses import dataclass

@dataclass
class Barco:
    costo: int = 1000000000
    capacidad: int = 24000

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
    capacidad: int = 100000
    tipo = "normal"
    carga = ["gas", "liquido"]
    productos  = []

@dataclass
class Estanque_I:
    capacidad: int = 100000
    tipo = "inflamable"
    carga = ["gas", "liquido"]
    productos  = []