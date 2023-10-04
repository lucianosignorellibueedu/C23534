saludar();

//Sin parametros y no devuelve valores
function saludar() {
    console.log("¡Hola, mundo!");
}

saludar();

//Sin parametros y no devuelve valores
function validarSaldo(){
    let saldo = parseInt(prompt('Ingrese el saldo'));
    if( saldo > 0){
        console.log('Tiene un saldo de', saldo)
    }
    else{
        console.log('No tiene saldo');
    }
}

// validarSaldo();

//recibe un parametro y no devuelve valores
function validarSaldoConParametro(saldo){
    debugger;
    if( saldo > 0){
        console.log('Tiene un saldo de', saldo)
    }
    else{
        console.log('No tiene saldo');
    }
}
// let saldo = parseInt(prompt('Ingrese el saldo'));
// validarSaldoConParametro(saldo);


//No pasa parametros y devuelve un valor
function obtenerFecha() {
    let fecha = new Date();
    return fecha.toDateString();
}

let fechaActual = obtenerFecha();
console.log("La fecha actual es: " + fechaActual);


//Pasamos parametros,pero no devuelve valor
function imprimirMensaje(nombre, edad) {
    console.log("Hola, " + nombre + ". Tienes " + edad + " años.");
}

imprimirMensaje("Juan", 30);


//Pasamos parametros y devuelve un valor
function calcularAreaRectangulo(ancho, alto) {
    let area = ancho * alto;
    return area;
}

let area = calcularAreaRectangulo(5, 10);
console.log("El área del rectángulo es: " + area + " metros cuadrados.");
