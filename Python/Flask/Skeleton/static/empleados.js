const { createApp } = Vue;

createApp({
    data() {
        return {
            empleados: [],
            url: 'http://127.0.0.1:5000/empleados',
            error: false,
            cargando: true,
            id: 0,
            nombre: '',
            apellido: '',
            dni: '',
            correo: '',
            cargo: '',
            fecha_nacimiento: '',
            num_empleado: '',
        };
    },
    methods: {
        fetchData(url) {
            fetch(url)
                .then(response => response.json())
                .then(data => {
                    this.empleados = data;
                    this.cargando = false;
                })
                .catch(err => {
                    console.error(err);
                    this.error = true;
                });
        },
        eliminar(empleado) {
            const url = this.url + '/' + empleado;
            var options = {
                method: 'DELETE',
            };
            fetch(url, options)
                .then(response => response.json())
                .then(response => {
                    location.reload();
                })
        },
        grabar(){
            let empleado = {
                nombre: this.nombre,
                apellido : this.apellido,
                dni: this.dni,
                num_empleado : this.num_empleado,
                correo: this.correo,
                cargo: this.cargo,
                fecha_nacimiento: this.fecha_nacimiento,
            };
            var options = {
                method: 'POST',
                body: JSON.stringify(empleado),
                headers: { 'Content-Type': 'application/json' },
                redirect: 'follow'
            };
            fetch(this.url, options)
            .then(function () {
                alert('Se registro el empleado');
                window.location.href = './index.html';
            })
            .catch(err => {
                console.error(err);
            });
        }
    },
    
    created() {
        this.fetchData(this.url)
    }


}).mount('#app');