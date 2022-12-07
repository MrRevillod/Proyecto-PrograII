from dataclasses import dataclass
from tkinter import *

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
class Vehiculo:
	nom_Vh = str
	cant_Cont = int
	costo = int
	list_Depositos = []

#========================================================================#
#================= Asignar atributos a cada vehiculo ====================#
#========================================================================#

	def assign_atr(self, cant_Contx, precio):
		self.cant_Cont = cant_Contx
		if cant_Contx >= 24000:
			self.nom_Vh = "barco" ; self.costo = precio
		elif cant_Contx >= 250:
			self.nom_Vh = "tren"; self.costo = precio
		elif cant_Contx >= 2:
			self.nom_Vh = "avion"; self.costo = precio
		elif cant_Contx <= 1:
			self.nom_Vh = "camion"; self.costo = precio

#========================================================================#
#================= Imprimir enunciados de la entrega 1 ==================#
#========================================================================#

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

#========================================================================#
#============================= Entrega 2 ================================#
#========================================================================#

#========================================================================#
#================ indice 3.1 :Lista de contenedores =====================#
#========================================================================#

	def punto_3_1(self, main):
		l_obj_dict = []
		for x in range(len(self.list_Depositos)):
			l_obj_dict.append(self.list_Depositos[x].__dict__)
		scroll = Scrollbar(main)
		text = Text(main, height= 15, width= 60,bg="grey")
		scroll.pack(side= LEFT, fill= Y)
		text.pack(side= LEFT, fill= Y)
		scroll.config(command= text.yview)
		text.config(yscrollcommand= scroll.set)
		for x in range(len(l_obj_dict)):
			msg = str(l_obj_dict[x]).split(",")
			id = msg[0] ; nom = msg[1] ; t_Carga = msg[2]
			masa = msg[3] ; peso = msg[4]
			porte = msg[5] ; t_Dep = msg[6]
			texto = id + nom + "\n" + t_Carga + masa + "\n" + peso + porte + "\n" + t_Dep + "\n\n\n"
			text.insert(END, texto)

#========================================================================#
#======== indice 3.2 :Cantidad total de cada tipo de contenedor =========#
#========================================================================#

	def punto_3_2(self, root):
		scroll = Scrollbar(root)
		l_cant_por_tipo = [0, 0, 0]
		l_tipo_str = ["normal", "refrigerado", "inflamable"]
		for x in range(len(self.list_Depositos)):
			dep = self.list_Depositos[x]
			for  y in range(len(l_tipo_str)):
				if dep.tipo_Carga == l_tipo_str[y]:
					l_cant_por_tipo[y] += 1
		for x in range(len(l_tipo_str)):
			lbl_print = Label(root, text= f"Hay {l_cant_por_tipo[x]} contenedores"
																		f" de tipo {l_tipo_str[x]}",bg="grey")
			lbl_print.pack(side= TOP)

#========================================================================#
#================ indice 3.3 :Tonelaje total de productos ===============#
#========================================================================#

	def punto_3_3(self, root):
		tonelaje = 0
		for x in range(len(self.list_Depositos)):
			tonelaje += self.list_Depositos[x].peso
		lbl_print_3 = Label(root, text= f"Tonelaje total de"
																		f" productos es : {tonelaje}",bg="grey")
		lbl_print_3.pack(side= TOP)

#========================================================================#
#================ indice 3.4 :Tonelaje por tipo de carga ================#
#========================================================================#

	def punto_3_4(self, root):
		lis_Peso_Por_Carga = [0, 0, 0]
		l_tipo_str = ["normal", "refrigerado", "inflamable"]
		for x in range(len(self.list_Depositos)):
			dep = self.list_Depositos[x]
			for  y in range(len(l_tipo_str)):
				if dep.tipo_Carga == l_tipo_str[y]:
					lis_Peso_Por_Carga[y] += dep.peso
		for x in range(len(l_tipo_str)):
			lbl_print_4 = Label(root, text= f"Tonelaje total para contenedores"
																			f" {l_tipo_str[x]} es :"
																			f" {lis_Peso_Por_Carga[x]}",bg="grey")
			lbl_print_4.pack(side= TOP)

#========================================================================#
#================= indice 3.5 :Tonelaje por masa ========================#
#========================================================================#

	def punto_3_5(self, root):
		l_Peso_Por_Masa = [0, 0, 0]
		l_Str_Por_Masa = ["solida", "liquida", "gas"]
		for x in range(len(self.list_Depositos)):
			dep = self.list_Depositos[x]
			for  y in range(len(l_Str_Por_Masa)):
				if dep.masa == l_Str_Por_Masa[y]:
					l_Peso_Por_Masa[y] += dep.peso
		for x in range(len(l_Str_Por_Masa)):
			lbl_print_5 = Label(root, text= f"Tonelaje total por productos de masa"
																			f" {l_Str_Por_Masa[x]} es :"
																			f" {l_Peso_Por_Masa[x]}",bg="grey")
			lbl_print_5.pack(side= TOP)