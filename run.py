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

# Ejecutar programa
insert_to_db(read_csv("MOCK_DATA_CHICO.csv"))
lista_Contenedores(get_list_to_db(), lista_Cont)
num_Total_Depositos, lista_All_Dep = cont_Totales(lista_Cont)
list_precios_buena = precio_mayor(get_precio())
# cant_Vh(num_Total_Depositos, list_precios_buena)