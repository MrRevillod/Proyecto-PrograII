import csv
from manipular_db import *
from classes import *

# lista ordenada para juntar y organizar los contenedores por tipo y masa
lista_Cont = [
    ["normal", ["solida", ], ["liquida", ], ["gas", ]],
    ["refrigerado", ["solida", ], ["liquida", ], ["gas", ]],
    ["inflamable", ["solida", ], ["liquida", ], ["gas", ]]]

lista_Vh = [[],[],[]]
# Leer el archivo csv (retorna una matriz en la que cada sublista
# 											corresponde a un producto con todos
# 											sus atributos). retorna todo como string

def read_csv(x):
	with open(x, 'r') as c:
			line = csv.reader(c)
			lista = list(line)
	return lista

# Crea cada instancia de contenedor y los agrega a la lista de contenedores
# según sus características (tipo de contenedor y masa del producto).

def lista_Contenedores(lista, lista_Cont):
	peso_Max_Por_Tipo_Cont = [
							["normal",24000],
							["refrigerado", 20000],
							["inflamable",22000]]
	for i in range(len(lista)):
		peso_Prod = int(lista[i][4])
		for x in range(len(lista_Cont)):
			if lista[i][2] == lista_Cont[x][0]:
				for j in range(len(lista_Cont[0])):
					if lista[i][3] == lista_Cont[x][j][0]:
						for t in range(len(peso_Max_Por_Tipo_Cont)):
							if lista[i][2] == peso_Max_Por_Tipo_Cont[t][0]:
								pesomax = peso_Max_Por_Tipo_Cont[t][1]
								arr = cant_Cont(peso_Prod, pesomax)
								for g in range(arr[0]):
									obj = Deposito()
									obj.atributos(int(lista[i][0]), lista[i][1],
																lista[i][2], lista[i][3],
																pesomax, "grande")
									lista_Cont[x][j].append(obj)
								if arr[1][1] != 0:
									if len(arr) == 3:
										obj = Deposito()
										obj.atributos(int(lista[i][0]), lista[i][1],
																	lista[i][2], lista[i][3],
																	arr[1][1], "pequeno")
										lista_Cont[x][j].append(obj)
									else:
										obj = Deposito()
										obj.atributos(int(lista[i][0]), lista[i][1],
																	lista[i][2], lista[i][3],
																	arr[1][1], "grande")
										lista_Cont[x][j].append(obj)
						break
			else:
				continue
	return

# Esta función se utiliza para sacar la cantida de contenedores grandes
# llenos, grandes con resto y/o pequeños con restos, esta implementada
# en la función lista_Contenedores.

def cant_Cont(pesox, pesomax):
	cont_G_llenos = 0; cont_G = 0; cont_P = 0
	if pesox >= pesomax:
		cont_G_llenos += pesox//pesomax
		resto = pesox % pesomax
		if resto > (pesomax/2):
			cont_G += 1
			lista_G = [cont_G, resto]
			return [cont_G_llenos, lista_G]
		else:
			cont_P += 1
			lista_P = [cont_P, resto]
			return [cont_G_llenos, lista_P, "pequeño"]
	elif pesox > (pesomax/2) :
		cont_G += 1
		lista_G = [cont_G, pesox]
		return [cont_G_llenos, lista_G]
	else:
		cont_P += 1
		lista_P = [cont_P, pesox]
		return [cont_G_llenos, lista_P, "pequeño"]

# cantidad de contenedores considerando que los pequeños ocupan la
# mitad del espacio que los grandes, por lo que en vez de contar
# como un entero, cada uno vale 0.5 respecto de uno grande

def cont_Totales(lista_Cont):
	cantidad_Total = float(0)
	lista = []
	for x in range(len(lista_Cont)):
		for y in range(1, len(lista_Cont[0])):
			for j in range(1, len(lista_Cont[x][y])):
				lista.append(lista_Cont[x][y][j])
				if lista_Cont[x][y][j].porte == "pequeno":
					cantidad_Total += 0.5
				elif lista_Cont[x][y][j].porte == "grande":
					cantidad_Total += 1
	return [cantidad_Total, lista]

# retorna una lista con la cantidad de vehiculos, si hay un resto
# se le asigna al vehiculo correspondiente, esto se utiliza en la
# función Dep_en_Vh.

def get_precio():
	# Pbarco = input("Precio Barco: ")
	# Ptren = input("Precio Tren: ")
	# Pavion = input("Precio Avion: ")
	# Pcamion = input("Precio Camion: ")
	Pbarco = 1000000000; Ptren = 10000000
	Pavion = 1000000 ; Pcamion = 500000
	div_Pbarco  = Pbarco  / 24000
	div_Ptren   = Ptren   / 250
	div_Pavion  = Pavion  / 10
	div_Pcamion = Pcamion
	return [[div_Pbarco, div_Ptren, div_Pavion, div_Pcamion],
					[24000, 250, 10, 1],
					["barco", "tren", "avion", "camion"]]

def cant_Vh(cont_Totales, list_precios_buena):
	max_Peso_Vh = list_precios_buena[0]
	nom_Vh = list_precios_buena[1]
	cant_Vh = list_precios_buena[2]
	if cont_Totales >= max_Peso_Vh[0]:
		cant_Vh[0] += cont_Totales // max_Peso_Vh[0] ; resto_1 = cont_Totales % max_Peso_Vh[0]
		if resto_1 >= max_Peso_Vh[1]:
			cant_Vh[1] += resto_1 // max_Peso_Vh[1] ; resto_2 = resto_1 % max_Peso_Vh[1]
			if resto_2 >= max_Peso_Vh[2]:
				cant_Vh[2] += resto_2 // max_Peso_Vh[2] ; resto_3 = resto_2 % max_Peso_Vh[2]
				if resto_3 >= max_Peso_Vh[3]:
					cant_Vh[3] += resto_3 // max_Peso_Vh[3] ; resto_4 = resto_3 % max_Peso_Vh[3]
					if resto_4 > 0:
						cant_Vh[3] += 1
				else:
					cant_Vh[3] += 1
			else:
				cant_Vh[2] += 1
		else:
			cant_Vh[1] += 1
	elif cont_Totales >= max_Peso_Vh[1]:
		cant_Vh[1] += cont_Totales// max_Peso_Vh[1] ; resto_1 = cont_Totales % max_Peso_Vh[1]
		if resto_1 >= max_Peso_Vh[2]:
			cant_Vh[2] = resto_1 // max_Peso_Vh[2] ; resto_2 = resto_1 % max_Peso_Vh[2]
			if resto_2 >= max_Peso_Vh[3]:
				cant_Vh[3] += resto_2 // max_Peso_Vh[3] ;resto_3 = resto_2 % max_Peso_Vh[3]
				if resto_3 > 0:
					cant_Vh[3] += 1
			else:
				cant_Vh[3] += 1
		else:
			cant_Vh[2] += 1
	elif cont_Totales >= max_Peso_Vh[2]:
		cant_Vh[2] += cont_Totales // max_Peso_Vh[2] ; resto_1 = cont_Totales % max_Peso_Vh[2]
		if resto_1 >= max_Peso_Vh[3]:
			cant_Vh[3] += resto_1 // max_Peso_Vh[3] ; resto_2 = resto_1 % max_Peso_Vh[3]
			if resto_2 > 0:
				cant_Vh[3] += 1
		else:
			cant_Vh[3] += 1
	elif cont_Totales >= max_Peso_Vh[3]:
		cant_Vh[3] += cont_Totales // max_Peso_Vh[3] ; resto_1 = cont_Totales % max_Peso_Vh[3]
		if resto_1 > 0:
			cant_Vh[3] += 1
	else:
		cant_Vh[3] += 1
	print(cant_Vh)
	print(nom_Vh)
	return [max_Peso_Vh, nom_Vh, cant_Vh]

# Crea las instancias de vehiculos y los agrega a la lista_Vh,
# tambien para cada instancia agrega los contenedores correspondientes
# a cada vehiculo en especifico.

def Dep_en_Vh(cant_Vhs, lista_All_Dep, lista_Vh):
	cant_Total_Vh = [250, 10, 1]
	nom = ["trenes", "aviones", "camiones"]
	for r in range(len(cant_Vhs)):
		var = 0
		for k in range(int(cant_Vhs[r][0])):
			obj = Vehiculo()
			obj.list_Depositos = []
			obj.assign_atr(cant_Total_Vh[r])
			for x in range(var, len(lista_All_Dep)):
				if x == (cant_Total_Vh[r] + var):
					var += cant_Total_Vh[r]
					break
				obj.list_Depositos.append(lista_All_Dep[x])
			lista_Vh[r].append(obj)
	return lista_Vh

def run_program(lista_Cont, lista_Vh):
	insert_to_db(read_csv("MOCK_DATA.csv"))
	lista_Contenedores(get_list_to_db(), lista_Cont)
	num_Total_Depositos, lista_All_Dep = cont_Totales(lista_Cont)
	num_Vh = cant_Vh(num_Total_Depositos)
	Dep_en_Vh(num_Vh, lista_All_Dep, lista_Vh)