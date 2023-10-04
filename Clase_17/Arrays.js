//Definir un array vacio;
let array = [];
//Array de numeros
let arrayNumberos= [1,2,3,4,5];
let arrayLetras = ['Hola','Jorge','Chau','Chevrolet']

let arrayFutbol = ['Boca','River','Independiente','Gimansia'];
const persona ={
    nombre: 'Juan',
    apellido: 'Martinez'
}
let arrayObjetos = [1,'Cosas','Otra cosa',4,10,25,persona, true];

console.log(arrayFutbol[3]);
console.log(arrayObjetos[3]);
console.log(arrayObjetos[6]);
console.log(arrayObjetos[7]);
console.log(arrayObjetos[8]);

console.log(arrayObjetos.length);
console.log(arrayObjetos.length-1);
let ult = arrayObjetos.length-1;
console.log(arrayObjetos[ult]);
console.log(arrayObjetos[arrayObjetos.length-1]);


for(let i=0; i < arrayObjetos.length;i++){
    console.log(`${i}: ${arrayObjetos[i]}`);
    if(arrayObjetos[i] === 1)
    {
        console.log('Es el numero 1')
    }
}

arrayObjetos.forEach(item => {
    console.log('Con ForEach',item);
    if(item === 1)
    {
        console.log('Es el numero 1')
    }
    if(item.apellido != undefined)
        console.log(item.apellido);
    if(item.nombre != undefined)
        console.log(item.nombre);
});


