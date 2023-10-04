// const a = ['3','10','1','31','5']
// a.sort()
// console.log(a) //['1','10','3','31','5']

// const arreglo = [4,45,5,59,1,2]
// arreglo.sort()
// console.log(arreglo) //[1,2,4,45,5,59]





// const frutas = ['manzana', 'banana', 'naranja', 'uva'];

// // Elimina 'naranja' desde la posición 2 y agrega 'pera' y 'cereza'
// const eliminados = frutas.splice(2, 1, 'pera', 'cereza');

// console.log(frutas); // Resultado: ['manzana', 'banana', 'pera', 'cereza', 'uva']
// console.log(eliminados); // Resultado: ['naranja']


// const frutas = ['manzana', 'banana', 'naranja', 'uva'];
// // [1,3)  >= <
// // Crea una copia de las frutas desde la posición 1 hasta 3 (no incluye 3)
// const copiaFrutas = frutas.slice(1, 3);

// console.log(copiaFrutas); // Resultado: ['banana', 'naranja']


// const numeros = [1, 2, 10, 3, 4, 5];

// numeros.reverse();
// console.log(numeros); // Resultado: [5, 4, 3, 2, 1]


// const frutas = ['manzana', 'banana', 'naranja', 'uva'];

// frutas.sort();
// console.log(frutas); // Resultado: ['banana', 'manzana', 'naranja', 'uva']


// const numeros = [10, 5, 8, 2, 1];
// // sort(func)
// numeros.sort((a, b) => a - b); // Orden numérico ascendente
// console.log(numeros); // Resultado: [1, 2, 5, 8, 10]



// const numeros = [1, 2, 3, 4, 5];

// numeros.forEach(function(numero) {
//     console.log(numero * 2);
// });

    

// const edades = [20, 25, 18, 32, 27];

// const todosMayoresDeEdad = edades.every(function(edad) {
//     return edad >= 18;
// });

//  console.log(todosMayoresDeEdad); // Resultado: true


// const edades = [10, 15, 17, 12, 18];

// const algunosMayoresDeEdad = edades.some(function(edad) {
//     return edad >= 18;
// });

// console.log(algunosMayoresDeEdad); // Resultado: true



// const numeros = [1, 2, 3, 4, 5];

// const duplicados = numeros.map(function(numero) {
//     return numero * 2;
// });

// console.log(duplicados); // Resultado: [2, 4, 6, 8, 10]



// const edades = [20, 15, 18, 32, 27];

// const mayoresDeEdad = edades.filter(function(edad) {
//     return edad >= 18;
// });

// console.log(mayoresDeEdad); // Resultado: [20, 18, 32, 27]
