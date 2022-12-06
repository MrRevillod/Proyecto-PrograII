from main import *

# def run_program(lista_Cont, lista_Vh):
# 	insert_to_db(read_csv("MOCK_DATA_CHICO.csv"))
# 	lista_Contenedores(get_list_to_db(), lista_Cont)
# 	num_Total_Depositos, lista_All_Dep = cont_Totales(lista_Cont)
# 	num_Vh = cant_Vh(num_Total_Depositos)
# 	Dep_en_Vh(num_Vh, lista_All_Dep, lista_Vh)

# run_program(lista_Cont, lista_Vh)


def precio_mayor(list_precios):
	list_precios_buena = [[],[],[0,0,0,0]]
	for x in range(4):
		nmin = min(list_precios[0]) ; nindex = list_precios[0].index(nmin)
		print(list_precios[2])
		print(nindex)
		max_Peso_Vh = list_precios[1][nindex] ; nom_Vh = list_precios[2][nindex]
		list_precios[0].pop(nindex) ; list_precios[1].pop(nindex); list_precios[2].pop(nindex)
		list_precios_buena[0].append(max_Peso_Vh)
		list_precios_buena[1].append(nom_Vh)
	return list_precios_buena

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
	n =  cont_Totales(lis_Cont_N)
	r = cont_Totales(lis_Cont_R)
	i = cont_Totales(lis_Cont_I)
	cantidad_Total += n[0] + r[0] + i[0]
	for x in n[1]:
		lista.append(x)
	for x in r[1]:
		lista.append(x)
	for x in i[1]:
		lista.append(x)
	return [cantidad_Total, lista]

Pbarco = 1000000000 ; Ptren = 10000000 ; Pavion = 1000000 ; Pcamion = 500000000000

# Ejecutar programa
# insert_to_db(read_csv("MOCK_DATA.csv"))
# lista = get_list_to_db()
lista = read_csv("MOCK_DATA.csv")
run_Lis_Cont(lista, lis_Cont_N, lis_Cont_R, lis_Cont_I)
cantidad_Total, lista_All_Dep = run_Cont_Total(lis_Cont_N, lis_Cont_R, lis_Cont_I)
cant_Vhs = cant_Vh(cantidad_Total, Pbarco, Ptren, Pavion, Pcamion)
Dep_en_Vh(cant_Vhs[0][0], 24000, 0, cant_Vhs,  lista_All_Dep, lista_Vh)
Dep_en_Vh(cant_Vhs[1][0], 250,   1, cant_Vhs,  lista_All_Dep, lista_Vh)
Dep_en_Vh(cant_Vhs[2][0], 10,    2, cant_Vhs,  lista_All_Dep, lista_Vh)
Dep_en_Vh(cant_Vhs[3][0], 1,     3, cant_Vhs,  lista_All_Dep, lista_Vh)