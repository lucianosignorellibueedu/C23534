// // Crear un objeto JSON
// const persona = {
//     "nombre": "Juan",
//     "edad": 30,
//     "casado": false
//   };
  
//   // Convertir el objeto JSON en una cadena JSON
//   const personaJSON = JSON.stringify(persona);
  
//   // Almacenar la cadena JSON en sessionStorage bajo una clave específica
//   sessionStorage.setItem("usuario", personaJSON);
  
//   // Recuperar la cadena JSON de sessionStorage
//   const usuarioJSON = sessionStorage.getItem("usuario");
  
//   // Convertir la cadena JSON de vuelta a un objeto JavaScript
//   const usuario = JSON.parse(usuarioJSON);
  
//   // Acceder a los datos en el objeto recuperado
//   console.log(usuario.nombre); // Resultado: "Juan"
//   console.log(usuario.edad);   // Resultado: 30
//   console.log(usuario.casado); // Resultado: false
  