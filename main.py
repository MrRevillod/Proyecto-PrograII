import csv
from manipular_db import *
from classes import *

# lista ordenada para juntar y organizar los contenedores por tipo y masa
lis_Cont_N = [[],[],[]]
lis_Cont_R = [[],[],[]]
lis_Cont_I = [[],[],[]]

lista_Vh = [[],[],[],[]]
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

def llenar_lista_Contenedores(lista, lista_Cont, index, tipo_Cont, masax, pesom):
	peso_Max = pesom
	for id, nom, tipo_C, masa, pesO	in lista:
		peso = pesO
		num_Dep = cant_Cont(peso, peso_Max)
		if tipo_C == tipo_Cont and masa == masax:
			for x in range(num_Dep[0]):
				obj = Deposito()
				obj.atributos(int(id), nom, tipo_C, masa, peso_Max, "grande")
				lista_Cont[index].append(obj)
			if num_Dep[1][1] != 0:
				if len(num_Dep) == 3:
					obj = Deposito()
					obj.atributos(int(id), nom, tipo_C, masa, num_Dep[1][1], "pequeño")
					lista_Cont[index].append(obj)
				else:
					obj = Deposito()
					obj.atributos(int(id), nom, tipo_C, masa, num_Dep[1][1], "grande")
					lista_Cont[index].append(obj)
	return

# Esta función se utiliza para sacar la cantida de contenedores grandes
# llenos, grandes con resto y/o pequeños con restos, esta implementada
# en la función lista_Contenedores.

def cant_Cont(pesox, pesomax):
	cont_G_llenos = 0; cont_G = 0; cont_P = 0
	if pesox >= pesomax:
		cont_G_llenos += pesox//pesomax
		resto = pesox % pesomax
		if resto >= (pesomax/2):
			cont_G += 1
			lista_G = [cont_G, resto]
			return [cont_G_llenos, lista_G]
		else:
			cont_P += 1
			lista_P = [cont_P, resto]
			return [cont_G_llenos, lista_P, "pequeño"]
	elif pesox >= (pesomax/2) :
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

def cont_Totales(lis_Depositos):
	cantidad_Total = float(0)
	lista = []
	for x in range(len(lis_Depositos)):
		for y in range(len(lis_Depositos[x])):
			lista.append(lis_Depositos[x][y])
			if lis_Depositos[x][y].porte == "pequeño":
				cantidad_Total += 0.5
			elif lis_Depositos[x][y].porte == "grande":
				cantidad_Total += 1
	return [cantidad_Total, lista]

# retorna una lista con la cantidad de vehiculos, si hay un resto
# se le asigna al vehiculo correspondiente, esto se utiliza en la
# función Dep_en_Vh.

def cant_Vh(cont_Totales, Pbarco, Ptren, Pavion, Pcamion):
	PrecioPorDep1 = Pbarco / 24000
	PrecioPorDep2 = Ptren  / 250
	PrecioPorDep3 = Pavion / 10
	PrecioPorDep4 = Pcamion
	NBarco = 0; NTren = 0 ; NAvion = 0 ; NCamion = 0
	lis = ["camion"]
	if Pbarco < Ptren and Pbarco < Pavion and Pbarco < Pcamion:
		resto, NBarco = VhRentable(cont_Totales, 24000, NBarco)
	elif Ptren < Pavion and Ptren < Pcamion:
		resto, NTren = VhRentable(cont_Totales, 250, NTren)
	elif Pavion < Pcamion:
		resto, NAvion = VhRentable(cont_Totales, 10, NAvion)
	elif Pcamion < PrecioPorDep1 and Pcamion < PrecioPorDep2 and Pcamion < PrecioPorDep3 and Pcamion < PrecioPorDep4:
		resto, NCamion = VhRentable(cont_Totales, 1, NCamion)
	else:
		if PrecioPorDep1 < PrecioPorDep2:
				lis.append("barco")
		if PrecioPorDep2 < PrecioPorDep3:
				lis.append("tren")
		if PrecioPorDep3 < PrecioPorDep4:
				lis.append("avion")
		resto, NBarco  = VhRentable2(cont_Totales, 24000, "barco", lis, NBarco)
		resto, NTren   = VhRentable2(resto, 250, "tren", lis, NTren)
		resto, NAvion  = VhRentable2(resto, 10, "avion", lis, NAvion)
		resto, NCamion = VhRentable2(resto, 1, "camion", lis, NCamion)
		resto, NCamion = VhRentable2(resto, 1, "camion", lis, NCamion)
	matriz = [[NBarco, Pbarco], [NTren, Ptren], [NAvion, Pavion], [NCamion, Pcamion]]
	return matriz

def VhRentable(num_Conts, peso_Dep, NumVhs):
	resto = num_Conts
	if resto >= peso_Dep:
		NumVhs += resto // peso_Dep
		resto = resto % peso_Dep
	elif resto > (peso_Dep // 2):
		NumVhs += 1
	return resto, NumVhs

def VhRentable2(num_Conts, peso_Dep, string, lis, NumVhs):
	resto = num_Conts
	if resto >= peso_Dep and string in lis:
		NumVhs += resto // peso_Dep
		resto = resto % peso_Dep
	elif resto > (peso_Dep // 2) and string in lis:
		NumVhs += 1
	return resto, NumVhs

def Dep_en_Vh(NumVhs, peso_Dep, index,  matriz, lista_All_Dep, lista_Vh):
	var = 0
	for x in range(int(NumVhs)):
		obj = Vehiculo()
		obj.list_Depositos = []
		obj.assign_atr(peso_Dep, matriz[index][1])
		for y in range(var, len(lista_All_Dep)):
			if y == (peso_Dep + var):
				var += peso_Dep
				break
			obj.list_Depositos.append(lista_All_Dep[y])
		lista_Vh[index].append(obj)