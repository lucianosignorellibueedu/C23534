// function saludar(nombre) {
//     console.log("Hola, " + nombre + "!");
// }

// function procesarSaludo(nombre, callback) {
//     console.log("Procesando saludo...");
//     callback(nombre);
// }

// procesarSaludo("Juan", saludar); // Llama a la función 'saludar' como callback


function realizarOperacion(a, b, operacionCallback) {
    debugger;
    const resultado = operacionCallback(a, b);
    console.log("El resultado es: " + resultado);
}

function suma(x, y) {
    return x + y;
}

function resta(x, y) {
    return x - y;
}

realizarOperacion(5, 3, suma); // Resultado: 8
realizarOperacion(10, 4, resta); // Resultado: 6



// function ejecutarDespuesDeSegundos(segundos, callback) {
//     setTimeout(callback, segundos * 1000);
// }

// function saludar() {
//     console.log("¡Hola después de 3 segundos!");
// }

// ejecutarDespuesDeSegundos(3, saludar);




// const boton = document.getElementById("miBoton");

// function handleClick() {
//     alert("¡Hiciste clic en el botón!");
// }

// boton.addEventListener("click", handleClick);

