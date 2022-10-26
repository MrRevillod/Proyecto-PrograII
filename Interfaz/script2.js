"use strict";

let Trenesjson = "./Interfaz/JSON/Trenes.json";
let Avionesjson = "./Interfaz/JSON/Aviones.json";
let Camionjson = "./Interfaz/JSON/Camiones.json";

let resultados = document.getElementsByClassName("resultado");
let botones = document.getElementsByClassName("div");

let jsons = [Trenesjson, Avionesjson, Camionjson];
let jstring = ["Trenes", "Aviones", "Camiones"];

const I = async (jsons) => {

    let arraylength = []; 
    let cont = 0;

    for (let j = 0; j < jsons.length; j++) {

        const response = await fetch(jsons[j]);
        const data = await response.json();
        
        let long = data.length;
        arraylength.push(long);
    
    }

    for (let i = 0; i < arraylength.length; i++) {

        cont = cont + arraylength[i];
    }

    console.log(cont); 
}


const II = async (jsons, jstring) => {

    let arraylength = [];

    for (let j = 0; j < jsons.length; j++) {

        const response = await fetch(jsons[j]);
        const data = await response.json();

        let long = data.length;
        arraylength.push(long, jstring[j]);

    }

    console.log(arraylength); 
}

const III = async (jsons, jstring, resultados) => {
    for (let i = 0; i < jsons.length; i++) {
        let button = document.createElement("button");
        button.setAttribute("class", "button3");
        resultados[2].appendChild(button);
    }
    let buttons3 = document.getElementsByClassName("button3");

    for (let j = 0 ; j < buttons3.length ; j++ ) {
        buttons3[j].setAttribute("id", jstring[j]);

        buttons3[j].addEventListener("click", async function(e) {
            console.log("click");

            e.preventDefault();

            const response = await fetch(jsons[j]);
            const data = await response.json();
            console.log(data);
        }

    )}
}


for (let i = 0; i < botones.length; i++) {

    botones[i].addEventListener("click", async function (event) {

        event.preventDefault();

        if ( i === 0) {
            await I(jsons);
        } else if (i === 1) {
            await II(jsons, jstring);
        } else if (i === 2) {
            await III(jsons, jstring);
        }
    })
}

