// Sintaxis básica de una función flecha:
let nombreFuncion = (parametro1, parametro2) => {
    // Código de la función
    return resultado;
};

//Forma tradicional
function sumar(a,b){
    return a + b;
}
//Con arrow 
const sumar = (a, b) => a + b;

const resultado = sumar(5, 3);
console.log(resultado); // Resultado: 8



const saludar = () => {
    console.log("¡Hola, mundo!");
};

saludar(); // Esto imprimirá "¡Hola, mundo!" en la consola



const obtenerFecha = () => {
    let fecha = new Date();
    return fecha.toDateString();
};

const fechaActual = obtenerFecha();
console.log("La fecha actual es: " + fechaActual);


const imprimirMensaje = (nombre, edad) => {
    console.log(`Hola Soy, ${nombre}. Tienes ${edad} años.`);
    console.log('Hola Soy'+ nombre + '.' + ' Tiene' + ' ' + edad + 'años.')
};

imprimirMensaje("Juan", 30); // Esto imprimirá "Hola, Juan. Tienes 30 años." en la consola



const calcularAreaRectangulo = (ancho, alto) => ancho * alto;

const area = calcularAreaRectangulo(5, 10);
console.log(`El área del rectángulo es: ${area} metros cuadrados.`);
