// const persona = {
//     nombre: 'Juan',
//     edad: 30,
//     dni: 12312321,
//     saludar: function(){
//         console.log('Hola, Soy', this.nombre + 'y tengo ' + this.edad)
//     }
// };

// persona.saludar();
// console.log(persona.nombre);

class Persona{
    constructor(nombre,edad){
        this.nombre = nombre;
        this.edad = edad;
    }

    saludar(){
        console.log('Hola, Soy', this.nombre + 'y tengo ' + this.edad)
    }
}


let persona1 = new Persona('Luciano', 34);

let persona2 = new Persona('Juana', 24);

persona1.saludar();
persona2.saludar();
