class Auto:
    #Constructor
    def __init__(self, color, modelo):
        self.color = color #Atributo
        self.modelo = modelo #Atributo

    def arrancar(self):
        print("El Auto ha arrancado.")

# Crear un objeto de la clase Auto
mi_auto = Auto(color="rojo", modelo="sedán")

# Acceder a atributos
print("Color:", mi_auto.color)
print("Modelo:", mi_auto.modelo)

# Llamar a un método
mi_auto.arrancar()

auto2 = Auto('Azul','Deportivo')
print("Color:", auto2.color)
print("Modelo:", auto2.modelo)
auto2.arrancar()