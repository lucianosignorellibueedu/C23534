# Definición de una función lambda
suma = lambda x, y: x + y

# Uso de la función lambda
resultado = suma(3, 5)
print("Resultado de la función lambda:", resultado)

# Otra función lambda para elevar al cuadrado
cuadrado = lambda x: x**2

# Uso de la segunda función lambda
numero = 4
print(f"El cuadrado de {numero} es:", cuadrado(numero))

# Lista de números
numeros = [1, 2, 3, 4, 5]

# Uso de función lambda con la función map para duplicar cada elemento de la lista
duplicados = list(map(lambda x: x * 2, numeros))
print("Lista duplicada:", duplicados)


"""
Cuándo Utilizar Cada Caso:

Utiliza funciones lambda cuando necesites una función rápida y simple para una tarea específica, especialmente en situaciones donde no necesitas una función con nombre.

Son útiles en funciones como map, filter y reduce, donde necesitas proporcionar una función de forma concisa.
"""