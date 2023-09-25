function ejemploScopeLocal() {
    let variableLocal = "Soy local";

    console.log(variableLocal); // Se puede acceder dentro de la función
}

ejemploScopeLocal();
console.log(variableLocal); // Generará un error, la variable no está definida aquí



let variableGlobal = "Soy global";

function ejemploScopeGlobal() {
    console.log(variableGlobal); // Se puede acceder dentro de la función
}

ejemploScopeGlobal();
console.log(variableGlobal); // Se puede acceder fuera de la función







let variableGlobal = "Soy global";

function ejemploScopeGlobal() {
    console.log(variableGlobal); // Se puede acceder dentro de la función
}

ejemploScopeGlobal();
console.log(variableGlobal); // Se puede acceder fuera de la función


function crearCalculadora() {
    let resultado = 0; // Variable local dentro de la función

    return {
        sumar: function (valor) {
            resultado += valor;
        },
        restar: function (valor) {
            resultado -= valor;
        },
        obtenerResultado: function () {
            return resultado;
        }
    };
}

const calculadora = crearCalculadora();
calculadora.sumar(5);
calculadora.restar(3);
console.log(calculadora.obtenerResultado()); // Devuelve 2
console.log(resultado); // Generará un error, la variable 'resultado' no está definida aquí
