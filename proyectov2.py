import classes
import csv

def leerCsv(archivo):
    with open(archivo,'r') as file:
        reader = csv.reader(file)
        lista = list(reader)
        return lista

def main(productos, tipo_c, peso_max):

    # Contenedores grandes con productos de masa solida
    CGS = 0
    # Contenedores pequeños con productos de masa solida
    CPS = 0

    # x[0]= id ; x[1]=nombre_prod ;x[2]=tipo_c ;x[3]=masa ;x[4]=peso

    for p in productos:
        switch = 1
        resto = int(p[4])
        while switch :
            if p[2] == tipo_c:
                if p[3] == "solida":
                    if resto >= peso_max:
                        CGS += 1
                        resto -= peso_max
                    elif resto > (peso_max/2):
                        CPS += 1
                        resto -= round(peso_max/2)
                    elif resto <= (peso_max/2):
                        CPS += 1
                        resto = 0
                    elif resto <= 0:
                        switch = 0
                else:
                    switch = 0
            else:
                switch = 0
        continue
    print(CGS)
                # if p[3] == "liquida":
                #     if p[4] >= peso_max:
                #         contenedores_NLG.append(p[4])
                # if p[3] == "gas":
                #     if p[4] >= peso_max:
                #         contenedores_NGG.append(p[4])

if __name__ == "__main__":
    productos = leerCsv("MOCK_DATA.csv")
    main(productos, "normal", 24000)
    # main(productos, "refrigerada", 20000)