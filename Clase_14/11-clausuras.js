function creaContador() {
    let contador = 0;

    function incrementaContador() {
        contador++;
        console.log(contador);
    }

    return incrementaContador;
}

const miContador = creaContador();
miContador(); // Imprime 1
miContador(); // Imprime 2




function creaMensajeSaludo(saludo) {
    return function(nombre) {
        console.log(saludo + " " + nombre);
    };
}

const saludarEnIngles = creaMensajeSaludo("Hello");
const saludarEnEspanol = creaMensajeSaludo("Hola");

saludarEnIngles("John"); // Imprime "Hello John"
saludarEnEspanol("Maria"); // Imprime "Hola Maria"
