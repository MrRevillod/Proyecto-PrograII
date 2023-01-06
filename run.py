from main import *

def run_Lis_Cont(lista, lis_Cont_N, lis_Cont_R, lis_Cont_I):
	llenar_lista_Contenedores(lista, lis_Cont_N, 0, "normal", "solida", 24000)
	llenar_lista_Contenedores(lista, lis_Cont_N, 1, "normal", "liquida", 24000)
	llenar_lista_Contenedores(lista, lis_Cont_N, 2, "normal", "gas", 24000)
	llenar_lista_Contenedores(lista, lis_Cont_R, 0, "refrigerada", "solida", 20000)
	llenar_lista_Contenedores(lista, lis_Cont_R, 1, "refrigerada", "liquida", 20000)
	llenar_lista_Contenedores(lista, lis_Cont_R, 2, "refrigerada", "gas", 20000)
	llenar_lista_Contenedores(lista, lis_Cont_I, 0, "inflamable", "solida", 22000)
	llenar_lista_Contenedores(lista, lis_Cont_I, 1, "inflamable", "liquida", 22000)
	llenar_lista_Contenedores(lista, lis_Cont_I, 2, "inflamable", "gas", 22000)

def run_Cont_Total(lis_Cont_N, lis_Cont_R, lis_Cont_I):
	cantidad_Total = float(0)
	lista = []
	n, lisN =  cont_Totales(lis_Cont_N)
	r, lisR = cont_Totales(lis_Cont_R)
	i, lisI = cont_Totales(lis_Cont_I)
	cantidad_Total += n + r + i
	for x in lisN:
		lista.append(x)
	for x in lisR:
		lista.append(x)
	for x in lisI:
		lista.append(x)
	return [cantidad_Total, lista]