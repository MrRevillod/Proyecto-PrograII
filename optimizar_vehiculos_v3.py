from classes import *
from proyectov3 import *

def optimizar_vh(contenedores):
    cont_T = sum(contenedores)
    cant_barco  = 0; cant_tren   = 0; cant_avion  = 0; cant_camion = 0
    if cont_T >= 250:
        cant_tren += int(cont_T/250)
        resto = cont_T % 250
        if resto > 90 and resto < 250:
            cant_tren += 1
        elif resto <= 90: 
            cant_avion += int(resto/10)
            resto = resto % 10
            if resto < 10 and resto > 1:
                cant_avion += 1
            elif resto <= 1:
                cant_camion += 1
    print(f"Barcos: {cant_barco}")
    print(f"Trenes: {cant_tren}")
    print(f"Avión : {cant_avion}")
    print(f"Camión: {cant_camion}")

if __name__ == "__main__":
    productos= read_csv("MOCK_DATA.csv")

    # Sirve para asignar especificamente los pesos de cada producto en cada tipo
    # de contenedor por masa (solida, liquida, gaseosa)
    for x in range(len(lista_tipo_cont)):
        main(productos, lista_tipo_cont[x][0], lista_tipo_cont[x][1])

    # Suma los valores de las listas (tipos de contenedores con su respectiva masa)
    # y las asigna a la lista sumas_Totales []
    for c in range(len(lista_tipo_cont2)):
        for v in range(len(lista_tipo_cont2[c])):
            sumas_Totales.append((sum(lista_tipo_cont2[c][v])/1000))

    # cada for es para imprima cada tipo de contenedor con su masa recorriendo
    # la lista sumas_Totales
    for x in range(0, 3):
        cant_cont.append(Total_Contenedores(sumas_Totales[x], 24, "normales",strings_for_prints[x]))
    for x in range(3, 6):
        cant_cont.append(Total_Contenedores(sumas_Totales[x], 20, "refrigerados", strings_for_prints[x-3]))
    for x in range(6, 9):
        cant_cont.append(Total_Contenedores(sumas_Totales[x], 22, "inflamables", strings_for_prints[x-6]))

    optimizar_vh(cant_cont)