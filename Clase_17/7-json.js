const persona = {
    "nombre": "Juan",
    "edad": 30,
    "casado": false,
    "dirección": {
      "calle": "123 Main St",
      "ciudad": "Ciudad Ejemplo"
    },
    "amigos": ["María", "Carlos"]
  };
  

  // Convertir un objeto JavaScript a una cadena JSON
const personaJSON = JSON.stringify(persona);

// Convertir una cadena JSON de vuelta a un objeto JavaScript
const personaDeNuevo = JSON.parse(personaJSON);


console.log(persona.nombre); // Resultado: "Juan"
console.log(persona["edad"]); // Resultado: 30


const frutasJSON = '["manzana", "plátano", "naranja"]';
const frutas = JSON.parse(frutasJSON);

console.log(frutas[0]); // Resultado: "manzana"
