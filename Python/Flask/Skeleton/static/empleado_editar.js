console.log(location.search); // Lee los argumentos pasados a este formulario
var id = location.search.substr(4);
console.log(id);

const { createApp } = Vue;

createApp({
    data() {
        return {
            id: 0,
            nombre: "",
            apellido: "",
            dni: "",
            num_empleado: "",
            correo: "",
            cargo: "",
            fecha_nacimiento: "",
            url: 'http://localhost:5000/empleados/' + id,
        };
    },
    methods: {
        fetchData(url) {
            fetch(url)
                .then(response => response.json())
                .then(data => {
                    console.log(data);
                    this.id = data.id;
                    this.nombre = data.nombre;
                    this.apellido = data.apellido;
                    this.dni = data.dni;
                    this.num_empleado = data.num_empleado;
                    this.correo = data.correo;
                    this.cargo = data.cargo;
                    this.fecha_nacimiento = data.fecha_nacimiento;
                })
                .catch(err => {
                    console.error(err);
                    this.error = true;
                });
        },
        modificar() {
            let empleado = {
                nombre: this.nombre,
                apellido: this.apellido,
                dni: this.dni,
                num_empleado: this.num_empleado,
                correo: this.correo,
                cargo: this.cargo,
                fecha_nacimiento: this.fecha_nacimiento,
            };
            var options = {
                body: JSON.stringify(empleado),
                method: 'PUT',
                headers: { 'Content-Type': 'application/json' },
                redirect: 'follow'
            };
            fetch(this.url, options)
                .then(function () {
                    alert("Registro modificado");
                    window.location.href = "./index.html";
                })
                .catch(err => {
                    console.error(err);
                    alert("Error al Modificar");
                });
        }
    },
    created() {
        this.fetchData(this.url);
    },
}).mount('#app');