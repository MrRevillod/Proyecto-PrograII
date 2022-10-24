import csv
import json
from classes import *

# lista ordenada para juntar y organizar los contenedores por tipo y masa
lista_Cont = [
    ["normal", ["solida", ], ["liquida", ], ["gas", ]],
    ["refrigerado", ["solida", ], ["liquida", ], ["gas", ]],
    ["inflamable", ["solida", ], ["liquida", ], ["gas", ]]]

nom_Vh = ["Trenes.json", "Aviones.json", "Camión.json"]
# cantidad de vehiculos [0] = tren, [1] =avion, [2] = camion
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
def cant_Vh(cont_Totales):
	tren = 0; avion = 0; camion = 0
	lista = [[tren], [avion], [camion]]
	if cont_Totales >= 250:
		lista[0][0] += cont_Totales // 250
		resto = cont_Totales % 250
		if resto >= 10:
			lista[1][0] += resto // 10
			resto_menor = resto % 10
			if resto_menor <= 1:
				lista[2][0] += 1 ; lista[2].append(resto_menor)
			else:
				lista[1][0] += 1 ; lista[1].append(resto_menor)
		elif resto <= 1:
			lista[2][0] += 1 ; lista[2].append(resto)
		else:
			lista[1][0] += 1 ; lista[1].append(resto)
	elif cont_Totales >= 10:
		lista[1][0] += cont_Totales// 10
		resto = cont_Totales % 10
		if resto <= 1:
			lista[2][0] += 1 ; lista[2].append(resto)
		else:
			lista[1][0] += 1 ; lista[1].append(resto)
	elif cont_Totales <= 1:
		lista[2][0] += 1 ; lista[2].append(cont_Totales)
	else:
		lista[1][0] += 1 ; lista[1].append(cont_Totales)
	return lista

# Crea las instancias de vehiculos y los agrega a la lista_Vh,
# tambien para cada instancia agrega los contenedores correspondientes
# a cada vehiculo en especifico.
def Dep_en_Vh(cant_Vhs, cont_Totales, lista_Vh):
	cant_Total_Vh = [250, 10, 1]
	nom = ["trenes", "aviones", "camiones"]
	for r in range(len(cant_Vhs)):
		print(f"Cantidad total de {nom[r]} : ", int(cant_Vhs[r][0])) # cantidad
		# total por tipo de vehiculo
		var = 0
		for k in range(int(cant_Vhs[r][0])):
			obj = Vehiculos()
			obj.list_Depositos = []
			obj.assign_atr(cant_Total_Vh[r])
			for x in range(var, len(cont_Totales)):
				if x == (cant_Total_Vh[r] + var):
					var += cant_Total_Vh[r]
					break
				obj.list_Depositos.append(cont_Totales[x])
			lista_Vh[r].append(obj)
	return lista_Vh

# Crea el archivo json para luego utilizarlo de parte del javascript
def jsonconvert(index, lista_Vh, nom_Vh):
	lista = []
	for x in range(len(lista_Vh[index])):
		l_Dep = lista_Vh[index][x].__dict__
		li = []
		for y in range(len(lista_Vh[index][x].list_Depositos)):
			li.append(lista_Vh[index][x].list_Depositos[y].__dict__)
		l_Dep["list_Depositos"] = li; lista.append(l_Dep)
	with open(nom_Vh[index], "w") as file:
		json.dump(lista, file, indent=4)