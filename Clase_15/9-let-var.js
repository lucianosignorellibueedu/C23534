if (true) {
    var variableVar = "Variable declarada con var";
    let variableLet = "Variable declarada con let";
}

console.log(variableVar); // Imprime "Variable declarada con var"
console.log(variableLet); // Generará un error, variableLet no está definida



// Ejemplo con var
var numeroVar = 10;
if (true) {
    var numeroVar = 20;
}
console.log(numeroVar); // Imprime 20



// Ejemplo con let
let numeroLet = 10;
if (true) {
    let numeroLet = 20;
}
console.log(numeroLet); // Imprime 10
