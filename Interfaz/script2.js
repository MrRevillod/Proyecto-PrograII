"use strict";

let Trenesjson = "./Interfaz/JSON/Trenes.json";
let Avionesjson = "./Interfaz/JSON/Aviones.json";
let Camionjson = "./Interfaz/JSON/Camiones.json";
let Barcosjson = "./Interfaz/JSON/Barcos.json";

let resultados = document.getElementsByClassName("resultado");
let botones = document.getElementsByClassName("div");

let jsons = [Trenesjson, Avionesjson, Camionjson, Barcosjson];
let jstring = ["Trenes", "Aviones", "Camiones", "Barcos"];

/* ----------- ChangeDisplay ---------- */

const changedisplay = (resultados, x, contransporte, conts) => {
    for (let i = 0; i < resultados.length; i++) {
        resultados[i].style.display = "none";
    }

    resultados[x].style.display = "flex";

    for (let i = 0; i < conts.length; i++) {
        conts[i].style.display = "none";
        contransporte.style.display = "flex";
    }
};

/* ------------------------------------- */

/* ------------ Enunciado I ----------- */

const I = async (jsons, resultados) => {
    let arraylength = [];
    let cont = 0;
    let div = resultados[0];
    div.innerHTML = "";

    for (let j = 0; j < jsons.length; j++) {
        const response = await fetch(jsons[j]);
        const data = await response.json();

        let long = data.length;
        arraylength.push(long);
    }

    for (let i = 0; i < arraylength.length; i++) {
        cont = cont + arraylength[i];
    }

    let p = document.createElement("p");
    let resultado = "El total de vehiculos es: " + cont;
    p.innerHTML = resultado;
    div.appendChild(p);
};

/* ------------------------------------- */

/* ------------ Enunciado II ----------- */

const II = async (jsons, jstring, resultados) => {
    let arraylength = [];
    let div = resultados[1];
    div.innerHTML = "";

    let imgsrc = ["./Interfaz/img/Trenes.png", "./Interfaz/img/Avion.png", "./Interfaz/img/Camiones.png", "./Interfaz/img/Barcos.png"];

    for (let j = 0; j < jsons.length; j++) {
        const response = await fetch(jsons[j]);
        const data = await response.json();

        let long = data.length;
        arraylength.push([long, jstring[j]]);
    }

    for (let i = 0; i < arraylength.length; i++) {
        let resultado = "El total de " + arraylength[i][1] + " es: " + arraylength[i][0] + "<br>";
        let p = document.createElement("p");
        let img = document.createElement("img");
        img.setAttribute("src", imgsrc[i]);
        img.setAttribute("class", "img");

        p.innerHTML = resultado;
        div.appendChild(p);
        div.appendChild(img);
    }
};

/* ------------------------------------- */

/* ------------ Enunciado III ---------- */

const III = async (jsons, jstring, resultados) => {
    /* resultados[2].innerHTML = ""; */
    let l = jsons.length;

    let contransporte = document.getElementById("trans-buttons");
    let transporte = document.getElementsByClassName("transporte"); /* botones */
    let conts = document.getElementsByClassName("trans-conts"); /* contenedores */

    for (let i = 0; i < transporte.length; i++) {
        transporte[i].addEventListener("click", async (e) => {
            e.preventDefault();

            contransporte.style.display = "none";
            if ((contransporte.style.display = "none")) {
                conts[i].style.display = "grid";
            }

            const response = await fetch(jsons[i]);
            const data = await response.json();
            let l = data.length;
            console.log(data);

            for (let j = 0; j < l; j++) {
                let form = document.getElementsByClassName("trans-form");
                let submits = document.getElementsByClassName("form-submit");

                submits[i].addEventListener("click", (e) => {
                    e.preventDefault();

                    /* let value = document.getElementsByClassName("form-input").value; */
                    let ul = document.getElementsByClassName("busqueda-ul");
                    let tren = document.getElementById("inputren").value;

                    if (tren === j) {
                        console.log("hola");
                        let li = document.createElement("li");
                        li.innerHTML = data[j].cant_Cont;

                        let li2 = document.createElement("li");
                        li2.innerHTML = data[j].nom_Vh;

                        let li3 = document.createElement("li");
                        li3.innerHTML = data[j].costo;

                        ul[i].appendChild(li, li2, li3);
                        form[i].reset();
                    }
                });
            }
        });
    }
};

/* ------------------------------------- */

/* -------------- Eventos -------------- */

for (let i = 0; i < botones.length; i++) {
    botones[i].addEventListener("click", async function (event) {
        event.preventDefault();

        let contransporte = document.getElementById("trans-buttons");
        let transporte = document.getElementsByClassName("transporte"); /* botones */
        let conts = document.getElementsByClassName("trans-conts"); /* contenedores */

        if (i === 0) {
            await I(jsons, resultados);
            changedisplay(resultados, 0, contransporte, conts);
        } else if (i === 1) {
            await II(jsons, jstring, resultados);
            changedisplay(resultados, 1, contransporte, conts);
        } else if (i === 2) {
            changedisplay(resultados, 2, contransporte, conts);
            await III(jsons, jstring, resultados);
        }
    });
}
