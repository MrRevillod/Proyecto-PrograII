"use strict";

fetch("./contenedores.json")
    .then((response) => response.json())
    .then((json) => {
        for (let i = 0; i < json.length; i++) {
            let contenedor = json[i];
            console.log(contenedor.id_Prod);
        }
    });