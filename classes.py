from dataclasses import dataclass

@dataclass
class Producto :
    id: int
    nombre: str
    tipo: str
    masa: str
    peso: int

@dataclass
class Vehículo:
    costo: int
    capacidad: int

@dataclass
class Contenedores:
    carga: int
    tipo: str
    masa: list
    prod: list

# Vehiculos

Barco = Vehículo(1000000000, 24000)
Tren = Vehículo(10000000, 250)
Avión = Vehículo(1000000, 10)
Camión = Vehículo(500000, 1)

# Contenedores

C_np  = Contenedores(12000, "normal", ["normal","inerte","sólida"], [])
C_ng  = Contenedores(24000, "normal", ["normal","inerte","sólida"], [])
C_rp  = Contenedores(10000, "refrigerado", ["normal","refrigerada","inerte","sólida"], [])
C_rg  = Contenedores(20000, "refrigerado", ["normal","refrigerada","inerte", "sólida"], [])
C_el  = Contenedores(24000, "líquidos", ["inerte","líquida","gas"], [])
C_eli = Contenedores(20000, "líq.inflamable", ["inerte","inflamable","líquida","gas"], [])