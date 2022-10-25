"use strict";

let Trenesjson = "./Interfaz/JSON/Trenes.json";
let Avionesjson = "./Interfaz/JSON/Aviones.json";
let Camionjson = "./Interfaz/JSON/Camiones.json";

let resultados = document.getElementsByClassName("resultado");

let jsons = [Trenesjson, Avionesjson, Camionjson];
let jstring = ["Trenes", "Aviones", "Camiones"];
 
const readjson = (jsons, jstring) => {

    let cantidad = [];
    
    for (let j = 0; j < jsons.length; j++) {

        let contador = 0;

        fetch(jsons[j])
            .then(response => response.json())
            .then(data => {
                
                for (let i = 0; i < data.length; i++) {
                    let vehiculo = data[i];
                    contador += 1;
                }
                cantidad.push([contador, jstring[j]]);
            })
            .catch(error => console.log(error));
        }
    }

let main = readjson(jsons, jstring);


/* const EnunciadoI = (cantidad) => {

    console.log(cantidad);

    let total = 0;

    for (let i = 0; i < cantidad.length; i++) {
        total += cantidad[i][0];
    }

    console.log("El total de vehiculos es: " + total);
} */ 


/* const EnunciadoII = (cantidad, resultados) => {

    for (let i = 0; i < cantidad.length; i++) {
        
        let num = cantidad[i][0];
        let tipo = cantidad[i][1];

        let div = document.createElement("div");
        let h3 = document.createElement("h3");
        let ul = document.createElement("ul");
        ul.setAttribute("id", tipo);

        let li = document.createElement("li*" + num);
        li.setAttribute("class", "img-li");

        let imgclass = document.getElementsByClassName("img-li");

        for (let j = 0; j < imgclass.length; j++) {
            imgclass[j].style.backgroundImage = "url(./Interfaz/img/" + tipo + ".png)";
            tipo.appendChild(imgclass[j]);
        }

        h3.innerHTML = "Cantidad de" + tipo + ":" + num;

        div.appendChild(h3);
        div.appendChild(ul);
        
        resultados[1].appendChild(div);
    }
} */

/* EnunciadoI(main); */

readjson(jsons, jstring);
