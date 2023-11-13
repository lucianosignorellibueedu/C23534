from functools import reduce

# Lista de números
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Uso de función lambda con map para elevar al cuadrado cada elemento
cuadrados = list(map(lambda x: x**2, numeros))
print("Cuadrados:", cuadrados)

# Uso de función lambda con filter para obtener los números pares
pares = list(filter(lambda x: x % 2 == 0, numeros))
print("Números pares:", pares)

# Uso de función lambda con reduce para obtener la suma de todos los elementos
suma_total = reduce(lambda x, y: x + y, numeros)
print("Suma total:", suma_total)


"""
Cuándo Utilizar Cada Caso:

Utiliza map() cuando necesites aplicar una operación a cada elemento de una lista y obtener una nueva lista con los resultados.

Utiliza filter() cuando necesites filtrar elementos de una lista según una condición específica.

Utiliza reduce() cuando necesites reducir una lista a un solo valor acumulando los resultados de la función aplicada de manera secuencial.
"""

