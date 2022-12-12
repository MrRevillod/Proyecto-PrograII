
class Deposito:
	def __init__(self, id, tipo, masa):
		self.id_P = id
		self.tipo_C = tipo
		self.masa_P = masa

	def print_Atr(self):
		print(f"{self.__dict__}")

	def tipo_Deposito(self):

		if self.masa_P != "solida":
			self.tipo_Dep = "Estanque"

		else: self.tipo_Dep = "Contenedor"

		print(f"El tipo de deposito que deberia ser es un {self.tipo_Dep} porque la masa del producto que transporto es {self.masa_P}\n")

class Contenedor(Deposito):
	pass

class Estanque(Deposito):
	pass

deposito1 = Deposito(15, "refrigerado", "liquida")
contenedor1 = Contenedor(1, "normal", "solida")
estanque1 = Estanque(200, "Inflamable", "gas")

print(type(deposito1).__name__)
deposito1.print_Atr()
deposito1.tipo_Deposito()

print("=====================================================")

print(type(contenedor1).__name__)
contenedor1.print_Atr()
contenedor1.tipo_Deposito()

print("=====================================================")

print(type(estanque1).__name__)
estanque1.print_Atr()
estanque1.tipo_Deposito()