console.log("Desde al archivo APP2.JS")
// Sumar 2 + 2
console.log(2+2)


// Variables

//Variable con alcance global 
// var nombre = "Luciano"

// Variable con alcance de bloque
let nombreCompleto = "Luciano Signorelli"

//Constantes que no se pueden modificar
const IVA = 21;


// console.log("Tu nombre es: ",nombre);
console.log('Tu nombre completo: ',nombreCompleto);
console.log('El Valor del IVA es: ',IVA);

// nombre = 23;
// console.log("Tu nombre es: ",nombre);

nombreCompleto = true;
console.log('Tu nombre completo: ',nombreCompleto);


console.log('El Valor del IVA es: ',IVA);

let nombre = "Luciano";
let apellido = "Signorelli2";
let edad = 26;
let edadString = "29";
nombreCompleto = nombre + ' ' + apellido;
// console.log("nombre y apellido: ", nombre + ' ' + apellido);
console.log(nombreCompleto);

console.log(edad + edadString);



// var s = "Hola, me llamo Juan"; // s, de string
// var n = 28; // n, de número
// var b = true; // b, de booleano
// var u; // u, de undefined
// console.log(typeof s);
// console.log(typeof n);
// console.log(typeof b);
// console.log(typeof u);
// console.log(edad + parseInt(edadString));
// console.log(parseInt(apellido));

// console.log(2 * 3);
// console.log(++edad);




// let nombreTeclado = prompt("Ingrese su nombre", "");
// let edadTeclado = prompt('Ingrese su edad', "");
//  document.write( "Hola " + nombreTeclado);
//  document.write('Su edad es' + edadTeclado);



//  Operadores
let a = 2;
let b = 2;
let c = "2";

console.log('Con == a==b',a == b)
console.log('Con == a==c',a == c)

//Comparamos el tipo de dato y el valor
// Tipo de datos es string y number. Valor = 2
console.log('Con === a===c',a === c)

console.log('Con === a===b',a === b)


console.log(a++);
console.log(++b);
