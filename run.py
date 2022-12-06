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

Pbarco = 1000000000 ; Ptren = 10000000 ; Pavion = 1000000 ; Pcamion = 500000

# Ejecutar programa
# insert_to_db(read_csv("MOCK_DATA.csv"))
# lista = get_list_to_db()
# lista = read_csv("MOCK_DATA.csv")
# run_Lis_Cont(lista, lis_Cont_N, lis_Cont_R, lis_Cont_I)
# cantidad_Total, lista_All_Dep = run_Cont_Total(lis_Cont_N, lis_Cont_R, lis_Cont_I)
# cant_Vhs = cant_Vh(cantidad_Total, Pbarco, Ptren, Pavion, Pcamion)
# Dep_en_Vh(cant_Vhs[0][0], 24000, 0, cant_Vhs,  lista_All_Dep, lista_Vh)
# Dep_en_Vh(cant_Vhs[1][0], 250,   1, cant_Vhs,  lista_All_Dep, lista_Vh)
# Dep_en_Vh(cant_Vhs[2][0], 10,    2, cant_Vhs,  lista_All_Dep, lista_Vh)
# Dep_en_Vh(cant_Vhs[3][0], 1,     3, cant_Vhs,  lista_All_Dep, lista_Vh)