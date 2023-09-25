// Ejemplo de operador lógico &&
let edad = 25;
let tieneLicencia = true;

if (edad >= 18 && tieneLicencia) {
    console.log("Puede conducir legalmente.");
} else {
    console.log("No puede conducir.");
}

// Ejemplo de operador lógico ||
let dia = "lunes";

if (dia === "sábado" || dia === "domingo") {
    console.log("Es un fin de semana.");
} else {
    console.log("Es un día laborable.");
}


// Ejemplo de operador lógico !
let estaLloviendo = false;

if (!estaLloviendo) {
    console.log("Puedes salir a jugar al aire libre.");
} else {
    console.log("Debes quedarte en casa debido a la lluvia.");
}
