def total_Por_Vh(root,  lista_Vh, vhs, main):
    ClearMainCont(main)

    SideBar(root, lista_Vh, vhs, main)

    img_tren = PhotoImage(file=r"./img/Tren.png")
    img_avion = PhotoImage(file=r"./img/Avion.png")
    img_camion = PhotoImage(file=r"./img/Camion.png")
    img_barco = PhotoImage(file=r"./img/Barco.png")

    lista_img = [img_tren, img_avion, img_camion, img_barco]

    lbl_title = Label(main, text="Cantidad total de cada tipo de vehiculo",
                      bg="grey", padx=0, pady=0, font=("Arial", 10))
    lbl_title.grid(row=0, column=0, columnspan=4, sticky="nsew")

    for x in range(0, len(vhs)):
        lbl_text = Label(
            main, text=f"{vhs[x]} : {len(lista_Vh[x])}", padx=10, pady=10)
        lbl_text.grid(row=1, column=x, sticky="nsew")

        lbl_img = Label(main, image=lista_img[x])
        lbl_img.grid(row=2, column=x, sticky="nsew")
    root.mainloop()


# ========================================================================#
# ================ indice 3 :Al seleccionar un vehiculo ==================#
# ========================================================================#

def select_vh(root,  lista_Vh, vhs, main):
    ClearMainCont(main)

    SideBar(root, lista_Vh, vhs, main)

    lbl_sel = Label(root, text="Elige un vehiculo : ", width=100, bg="#0088b6",
                    height=5, font=("Arial", 13))
    lbl_sel.grid(row=0, column=0, columnspan=4)

    # barco = Button(root, text= "Barco", width= 30, height= 2)
    # barco.grid(row= 1, column= 0)

    tren = Button(root, text="Tren", width=30, height=2, font=("Arial", 13),
                  command=lambda: vh_selected(0, root, lista_Vh, vhs, lis_Wid_2), bg="#0088b6")
    tren.grid(row=1, column=0)

    avion = Button(root, text="Avion", width=30, height=2, font=("Arial", 13),
                   command=lambda: vh_selected(1, root, lista_Vh, vhs, lis_Wid_2), bg="#0088b6")
    avion.grid(row=1, column=1)

    camion = Button(root, text="Camion", width=30, height=2, font=("Arial", 13),
                    command=lambda: vh_selected(2, root, lista_Vh, vhs, lis_Wid_2), bg="#0088b6")
    camion.grid(row=1, column=2)

    lis_Wid_2 = [lbl_sel, tren, avion, camion]

# ========================================================================#
# ====== Mostrar Cantidad de vehiculos para el tipo seleccionado =========#
# ========================================================================#


def vh_selected(index, root, lista_Vh, vhs, lis_Wid_2):
    cant_Vh = len(lista_Vh[index])
    var_Response = IntVar()
    lbl_quest = Label(root, font=("Arial", 13), bg="#0088b6",
                      text=f"Hay {cant_Vh} {vhs[index]}\nQue numero de vehiculo deseas elegir: ", justify=CENTER)
    lbl_quest.grid(row=2, column=1)
    lis_Wid_2.append(lbl_quest)

    response = Entry(root, font=("Arial", 13), bg="#0088b6",
                     textvariable=var_Response)
    response.grid(row=3, column=1)
    lis_Wid_2.append(response)

    but_get = Button(root, text="Obtener datos del vehiculo", font=("Arial", 13),
                     command=lambda: print_Vh(root,
                                              index,
                                              var_Response.get(),
                                              lista_Vh,
                                              lis_Wid_2), bg="#0088b6")
    but_get.grid(row=4, column=1)
    lis_Wid_2.append(but_get)


def print_Vh(root, index, index_2, lista_Vh, lis_Wid_2):
    vh = lista_Vh[index][index_2 - 1]

    vh.punto_3_1(root)
    vh.punto_3_2(root)
    vh.punto_3_3(root)
    vh.punto_3_4(root)
    vh.punto_3_5(root)

# ========================================================================#
# ================ indice 4.1 :Costo total de transporte =================#
# ========================================================================#


def indice_4_1(root,  lista_Vh, main):

    SideBar(root, lista_Vh, vhs, main)

    total_Transporte = 0
    for x in range(len(lista_Vh)):
        for y in range(len(lista_Vh[x])):
            total_Transporte += lista_Vh[x][y].costo
    lbl_text = Label(root, font=("Arial", 13), bg="#0088b6",
                     text=f"El costo total de transporte es :"
                     f"{total_Transporte}")
    lbl_text.pack()

# ========================================================================#
# ============= indice 4.2 :Costo total por tipo de transporte ===========#
# ========================================================================#


def indice_4_2(root, lista_Vh, vhs, main):
    l_Total_Por_Tipo_Vh = [0, 0, 0]
    for x in range(len(lista_Vh)):
        for y in range(len(lista_Vh[x])):
            l_Total_Por_Tipo_Vh[x] += lista_Vh[x][y].costo
    for x in range(len(l_Total_Por_Tipo_Vh)):
        lbl_text = Label(root, font=("Arial", 13), bg="#0088b6",
                         text=f"El costo total por {vhs[x]} es :"
                         f" {l_Total_Por_Tipo_Vh[x]}")
        lbl_text.pack()

# ========================================================================#
# ====================== Limpiar ventana de Widgets ======================#
# ========================================================================#


# ========================================================================#
# =================== Inicialización de funciones ========================#
# ========================================================================#


if __name__ == "__main__":
    lista = read_csv("MOCK_DATA.csv")
    lista_Contenedores(lista, lista_Cont)
    cant_Vhs = cant_Vh(cont_Totales(lista_Cont)[0])
    Dep_en_Vh(cant_Vhs, cont_Totales(lista_Cont)[1], lista_Vh)
