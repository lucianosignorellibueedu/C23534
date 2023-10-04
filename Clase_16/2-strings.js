let cadena = "    Esto ES UN objeto string";
//           012345  
let cadena2 = new String("Objeto String");

//length = Longitud de la cadena de caracteres.
console.log('Longitud de la cadena: ', cadena.length);

console.log('',cadena.charAt(2));
console.log('',cadena.charAt(6)); 

let concatenar = cadena + cadena2;

let concatenar2 = cadena2.concat(cadena2, cadena);
console.log(concatenar);
console.log(cadena2);
console.log(concatenar2);
 console.log('IndexOF',cadena.indexOf('to'));
console.log('LastIndexOF',cadena.lastIndexOf('to'));
console.log('LowerCase',cadena.toLocaleLowerCase());
console.log('Upper',cadena.toUpperCase());
console.log('Con TRIM',cadena.trim());
console.log('Replace',cadena.replace('to','nuevo'));
console.log('Substring',cadena.substring(3,8));
console.log('',cadena.substring(5,9));


let edad = 32
let nombre = 'Luciano'
let apellido = 'Signorelli'
// `... ${nombre_variable} ...`
console.log(`Mi nombre es ${nombre}, mi apellido ${apellido} y tengo ${edad} años`)
console.log('Mi nombre es', nombre + ' mi apellido es', apellido);



function suma(a,b){return a+b}
var a=2;
var b=5;
console.log(a + " + " + b + " es " + suma(a,b)) // 12 + 21 es 33
console.log(`${a} + ${b} es ${suma(a,b)}`) ;


console.log(Math.round(3.49));