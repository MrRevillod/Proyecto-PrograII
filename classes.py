from dataclasses import dataclass
import random as ra
@dataclass
class Deposito:
	id_Prod = int
	nom_Prod = str
	tipo_Dep = str
	tipo_Carga = str
	masa = str
	peso = int
	porte = str

	def atributos(self, id_Prodx, nom_Prodx, tipo_Cargax, masax, pesox, portex):
		self.id_Prod = id_Prodx
		self.nom_Prod = nom_Prodx
		self.tipo_Carga = tipo_Cargax
		self.masa = masax
		self.peso = pesox
		self.porte = portex
		if masax == "solida":
			self.tipo_Dep = "contenedor"
		else:
			self.tipo_Dep = "estanque"

@dataclass
class Vehiculos:
	nom_Vh = str
	cant_Cont = int
	costo = int
	list_Depositos = []

	def assign_atr(self, cant_Contx):
		self.cant_Cont = cant_Contx
		if cant_Contx >= 250:
			self.nom_Vh = "tren"; self.costo = 10000000
		elif cant_Contx >= 2:
			self.nom_Vh = "avion"; self.costo = 1000000
		elif cant_Contx <= 1:
			self.nom_Vh = "camion"; self.costo = 500000

	def prints_Enunciado_1(self):
		print(f"\nLa cantidad total de contenedores es : \
		{len(self.list_Depositos)}") # cantidad total de contenedores
		tipo_Depo = ["contenedor", "estanque"]
		tipo_Carga = ["normal", "refrigerado", "inflamable"]
		cant_Tipo_Dep = [[0], [0]]; cant_Tipo_Carga = [[0], [0], [0]]
		for x in range(len(self.list_Depositos)):
			for y in range(len(tipo_Depo)):
				(self.list_Depositos[x])
				if self.list_Depositos[x]["tipo_Dep"] == tipo_Depo[y]:
					cant_Tipo_Dep[y][0] += 1
			for t in range(len(tipo_Carga)):
				if self.list_Depositos[x]["tipo_Carga"] == tipo_Carga[t]:
					cant_Tipo_Carga[t][0] += 1
		print(f"Hay {cant_Tipo_Dep[0]} depositos de tipo Contenedor")
		print(f"Hay {cant_Tipo_Dep[1]} depositos de tipo Estanque")
		print(f"Hay {cant_Tipo_Carga[0]} productos de tipo Normal")
		print(f"Hay {cant_Tipo_Carga[1]} productos de tipo Refrigerado")
		print(f"Hay {cant_Tipo_Carga[2]} productos de tipo Inflamable")
		tonelaje_Total = 0
		for x in range(len(self.list_Depositos)):
			tonelaje_Total += self.list_Depositos[x]["peso"]
		print(f"El tonelaje total del vehiculo es : {tonelaje_Total}")