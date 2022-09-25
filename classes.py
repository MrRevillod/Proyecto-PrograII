from dataclasses import dataclass

@dataclass
class Containt():
    tipo_carga: str
    masa: str
    tamaño: int

@dataclass
class cP(Containt):
    nombre = "Pequeño"
@dataclass
class cG(Containt):
    nombre = "Grande"