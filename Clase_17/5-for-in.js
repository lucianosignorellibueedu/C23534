const persona = {
    nombre: 'Juan',
    edad: 30,
    ciudad: 'México'
};

for (let propiedad in persona) {
    console.log(propiedad + ': ' + persona[propiedad]);
}
