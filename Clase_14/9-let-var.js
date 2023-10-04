// if (true) {
//     var variableVar = "Variable declarada con var";
//     let variableLet = "Variable declarada con let";
// }

// console.log(variableVar); // Imprime "Variable declarada con var"
// console.log(variableLet); // Generará un error, variableLet no está definida



// // Ejemplo con var
// var numeroVar = 10;
// if (true) {
//     var numeroVar = 20;
// }
// console.log(numeroVar); // Imprime 20



// Ejemplo con let
// let numeroLet = 10;
// if (true) {
//     let numeroLet = 20;
// }
// console.log(numeroLet); // Imprime 10

// let total = 10

// function sumarIva(n){
//     //chequear que recibimos un numero
//     // chequear que no es una cadena de caracteres
//     n += 21;
//     return n;
// }
// total = sumarIva(total);

// conIva = sumarIva(10);

// pasarpepe = sumarIva("15");



var n = 10;
function sumaDos(n){
    n +=2;
    console.log(n);
    return n
}
sumaDos(n);
// n = sumaDos(n);
console.log(n)
