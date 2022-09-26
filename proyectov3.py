import dataclasses
import csv
from classes import *

cont_NS = [] ; cont_NL = [] ; cont_NG = []
cont_RS = [] ; cont_RL = [] ; cont_RG = [] 
cont_IS = [] ; cont_IL = [] ; cont_IG = [] 

pesos_normales      =   [cont_NS, cont_NL, cont_NG]
pesos_refrigerados  =   [cont_RS, cont_RL, cont_RG]
pesos_inflamables   =   [cont_IS, cont_IL, cont_IG]

lista_tipo_cont  = [[pesos_normales,"normal"], [pesos_refrigerados,"refrigerado"], [pesos_inflamables,"inflamable"]]
lista_tipo_cont2 = [pesos_normales, pesos_refrigerados, pesos_inflamables]

sumas_Totales = []

strings_for_prints = ["solida", "liquida", "gaseosa"]

cant_cont = []

# Leer el archivo csv (retorna una matriz con cada producto como una lista
#                        con sus respectivos atributos)
def read_csv (x):
    with open(x, 'r') as c:
        line = csv.reader(c)
        lista = list(line)
    return lista

# Asigna la cantidad de contenedores a cada tipo de contenedor
# (pesos_normales, pesos_refrigerados, pesos_inflamables)
def main(lista, lista_pesos, tipo_prod):
    for i in range(len(lista)):
        if lista[i][2] == tipo_prod:
            if lista[i][3] == "solida":
                lista_pesos[0].append(int(lista[i][4]))

            elif lista[i][3] == "liquida":
                lista_pesos[1].append(int(lista[i][4]))

            elif lista[i][3] == "gas":
                lista_pesos[2].append(int(lista[i][4]))

# Muestra la cantidad de contenedores por tipo de contenedor, la masa de
# de los productos y el tamaño del contenedor
def Total_Contenedores(total_c, peso_max, tipo_C, masa):
    cont_g = 0; cont_p = 0
    if total_c >= peso_max:
        cont_g += int(total_c / peso_max)
        resto = total_c % peso_max 
        if resto > (peso_max/2):
            cont_p += 1
            resto_menor = resto % (peso_max/2)
        if resto <= (peso_max/2) or resto_menor <= (peso_max/2):
            cont_p += 1
    elif total_c > (peso_max/2):
        cont_p += 1
        resto_menor = total_c % (peso_max/2)
        if resto <= (peso_max/2) or resto_menor <= (peso_max/2):
            cont_p += 1

    if cont_p == 0:
        cont_t = int(cont_g)
    elif (cont_p%2) == 0:
        cont_t = int(cont_g + (cont_p/2))
    elif (cont_p%2) != 0:
        cont_t = cont_g + (cont_p/2)
    # print(f"Contenedores {tipo_C} grandes con masa {masa}: {cont_g}")
    # print(f"Contenedores {tipo_C} pequeños con masa {masa}: {cont_p}")
    return cont_t