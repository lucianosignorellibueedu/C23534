let contador = 1;

while (contador <= 5) {
    console.log(contador);
    contador++;
}



let numero;
let esValido = false;

while (!esValido) {
    numero = prompt("Por favor, ingresa un número mayor que 10:");
    if (parseInt(numero) > 10) {
        esValido = true;
    }
}

console.log("Número válido ingresado: " + numero);
