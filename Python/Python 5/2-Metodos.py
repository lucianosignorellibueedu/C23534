class JugadorArgentina:
    # Atributo de clase
    pais = "Argentina"

    # Método constructor
    def __init__(self, nombre, edad, fecha_nacimiento, dni):
        # Atributos de instancia
        self.nombre = nombre
        self.edad = edad
        self.fecha_nacimiento = fecha_nacimiento
        self.dni = dni

    # Método especial para representación de cadena
    def __str__(self):
        return f"{self.nombre}, {self.edad} años, DNI: {self.dni}"

    # Método destructor (no siempre es necesario)
    def __del__(self):
        print(f"Objeto {self.nombre} eliminado")

# Crear instancias de la clase JugadorArgentina
messi = JugadorArgentina("Lionel Messi", 34, "24/06/1987", "12345678")
aguero = JugadorArgentina("Sergio Agüero", 33, "02/06/1988", "87654321")

# Acceder a atributos
print(messi.nombre)
print(aguero.edad)

# Acceder al atributo de clase
print(f"Pais de origen: {messi.pais}")

# Llamar al método __str__
print(str(messi))

# Eliminar una instancia (esto también llamará al método __del__)
del aguero
