from dataclasses import dataclass


@dataclass
class Producto:
	tipo_Cont = str
	tipo_Carga = str
	masa = str
	peso = int
	cont_G = 0
	cont_P = 0

	def atributos(self, tipo_Carga, masax, pesox):
		self.tipo_Carga = tipo_Carga
		self.masa = masax
		self.peso = pesox
		if masax == "solida":
			self.tipo_Cont = "contenedor"
		else:
			self.tipo_Cont = "estanque"
		peso_Max_Por_Carga_Cont = [
													["normal",24000],
													["refrigerado", 20000],
													["inflamable",22000]]
		for x in range(len(peso_Max_Por_Carga_Cont)):
			if tipo_Carga == peso_Max_Por_Carga_Cont[x][0]:
				peso_Max = peso_Max_Por_Carga_Cont[x][1]
				self.cant_Cont(pesox, peso_Max)
				return

	def cant_Cont(self, pesox, pesomax):
		if pesox >= pesomax:
			self.cont_G += pesox//pesomax
			resto = pesox % pesomax
			self.cant_Cont(resto, pesomax)
		elif pesox > (pesomax/2) :
			self.cont_P += 1
			resto = (pesox % pesomax/2)
			self.cant_Cont(resto, pesomax)
		else:
			self.cont_P += 1
		return

@dataclass
class Vehiculos:
	tren = int
	avion = int
	camion = int

	def cantidad(self, cont_Totales):
		if cont_Totales >= 250:
			self.tren += cont_Totales // 250
			resto = cont_Totales % 250
			self.cantidad(resto)
		elif cont_Totales >= 10:
			self.avion += cont_Totales// 10
			resto = cont_Totales % 10
			self.cantidad(resto)
		elif cont_Totales <= 1:
			self.camion += 1
			return
		else:
			self.avion += 1
			return