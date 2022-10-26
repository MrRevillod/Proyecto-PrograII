"use strict";

let Trenesjson = "./Interfaz/JSON/Trenes.json";
let Avionesjson = "./Interfaz/JSON/Aviones.json";
let Camionjson = "./Interfaz/JSON/Camiones.json";

let resultados = document.getElementsByClassName("resultado");
let botones = document.getElementsByClassName("div");

let jsons = [Trenesjson, Avionesjson, Camionjson];
let jstring = ["Trenes", "Aviones", "Camiones"];
 

function read(jsons) {

    var array = [];

    for (let i = 0 ; i < jsons.length ; i++){

        const xhttp = new XMLHttpRequest();

        xhttp.open("GET", jsons[i], true);
        xhttp.send();

        xhttp.onreadystatechange = function () {

            if (this.readyState == 4 && this.status == 200) {
    
                var datos = JSON.parse(this.responseText);
                console.log(datos[0]["nom_Vh"]);
                array.push(datos);

            }
        }
        
    }
    console.log(array[0]);
    return array;
    
}

read(jsons);


const EnunciadoI = (array) => {

    let Contador = 0;
    /* console.log(array); */

    let lista = [1,2,3,4,5,6,7,8,9,10];
    /* console.log(lista); */
 
    for (let i = 0 ; i < array.length ; i++) {

        Contador += array[i].length;
        console.log(array[i].length); 
    }
    console.log("Cantidad de vehiculos: " + Contador); 
    
}

/* EnunciadoI(read(jsons)); */






















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