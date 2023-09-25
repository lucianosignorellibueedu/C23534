let numero;
let esValido = false;

do {
    numero = prompt("Por favor, ingresa un número mayor que 10:");
    if (parseInt(numero) > 10) {
        esValido = true;
    }
} while (!esValido);

console.log("Número válido ingresado: " + numero);




let numeroSecreto = 7;
let intento;
let intentosRealizados = 0;

do {
    intento = parseInt(prompt("Adivina el número secreto (entre 1 y 10):"));
    intentosRealizados++;

    if (intento === numeroSecreto) {
        console.log("¡Felicitaciones! Adivinaste el número en " + intentosRealizados + " intentos.");
    } else {
        console.log("Intento incorrecto. Sigue intentando.");
    }
} while (intento !== numeroSecreto);





let opcion;

do {
    console.log("Menú de opciones:");
    console.log("1. Ver perfil");
    console.log("2. Editar perfil");
    console.log("3. Salir");

    opcion = parseInt(prompt("Elige una opción (1/2/3):"));

    switch (opcion) {
        case 1:
            console.log("Mostrando perfil...");
            break;
        case 2:
            console.log("Editando perfil...");
            break;
        case 3:
            console.log("Saliendo del programa.");
            break;
        default:
            console.log("Opción no válida. Intenta de nuevo.");
    }
} while (opcion !== 3);
