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

	def structure(self):
		return	{ self.tipo_Dep: 
								{
									"self.id_Prod": self.id_Prod, 
									"self.nom_Prod": self.nom_Prod, 
									"self.tipo_Carga": self.tipo_Carga, 
									"self.masa": self.masa, 
									"self.peso": self.peso, 
									"self.porte": self.porte}}

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
