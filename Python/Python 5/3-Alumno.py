class Alumno:
    # Atributo de clase para contar el número de alumnos
    nro_alumnos = 0

    def __init__(self, nombre, nota):
        # Atributos de instancia
        self.nombre = nombre
        self.nota = nota

        # Incrementar el contador de alumnos al instanciar un nuevo objeto
        Alumno.nro_alumnos += 1

    def mostrar_estado(self):
        # Método para mostrar el estado del alumno
        if self.nota <= 4:
            return "Estado: Regular"
        elif 4 < self.nota < 9:
            return "Estado: Bueno"
        else:
            return "Estado: Excelente"

    def imprimir_informacion(self):
        # Método para imprimir información sobre el alumno
        print(f"Nombre: {self.nombre}")
        print(f"Nota: {self.nota}")
        print(self.mostrar_estado())

    def __del__(self):
        # Método destructor que se llama al eliminar el objeto
        print(f"El alumno {self.nombre} ha sido eliminado.")

# Programa principal
if __name__ == "__main__":
    # Instanciar dos objetos de la clase Alumno
    alumno1 = Alumno("Juan", 7)
    alumno2 = Alumno("Maria", 10)

    # Imprimir información sobre los alumnos
    alumno1.imprimir_informacion()
    print("----------")
    alumno2.imprimir_informacion()

    # Mostrar el número total de alumnos
    print(f"\nNúmero total de alumnos: {Alumno.nro_alumnos}")

# Al salir del programa, se eliminarán automáticamente los objetos y se llamará al método __del__
