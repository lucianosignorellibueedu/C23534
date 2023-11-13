# Ejemplo de función con paso por valor
def duplicar_numero(numero):
    """
    Esta función duplica un número.

    Parámetros:
        - numero (int): El número a duplicar.
    """
    numero *= 2
    print("Dentro de la función:", numero)
    return numero
# Ejemplo de función con paso por referencia (apariencia)
def modificar_lista(lista):
    """
    Esta función agrega un elemento a una lista.

    Parámetros:
        - lista (list): La lista a modificar.
    """
    lista.append(4)
    print("Dentro de la función:", lista)

# Uso de la función con paso por valor
mi_numero = 3
mi_numero = duplicar_numero(mi_numero)
print("Fuera de la función:", mi_numero)

# Uso de la función con paso por referencia (apariencia)
mi_lista = [1, 2, 3]
modificar_lista(mi_lista)
print("Fuera de la función:", mi_lista)





"""Cuándo Utilizar Cada Caso:

Paso por Valor (Inmutables): Utiliza este enfoque cuando desees que el valor original de una variable no se modifique por la función."""
numero = 10
duplicar_numero(numero)
# Valor original no se modifica


"""Paso por Referencia Aparente (Mutables): Utiliza este enfoque cuando desees modificar el contenido de objetos mutables, como listas, y esos cambios se reflejen fuera de la función."""
mi_lista = [1, 2, 3]
modificar_lista(mi_lista)
# Cambios se reflejan fuera de la función


"""
Son mutables los siguientes tipos:

Listas
Bytearray
Memoryview
Diccionarios
Sets

Y clases definidas por el usuario
Y son inmutables:

Booleanos
Complejos
Enteros
Float
Frozenset
Cadenas
Tuplas
Range
Bytes"""