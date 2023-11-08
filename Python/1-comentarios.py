# Comentario en línea: Estas son notas que explican una línea de código.
# Python ignora todo después del símbolo "#" en una línea.

def suma(a, b):

    """
    Esta es una función que toma dos números como argumentos y devuelve su suma.
    :param a: El primer número.
    :param b: El segundo número.
    :return: La suma de a y b.
    """
    resultado = a + b
    return resultado

   


# Comentario en bloque: Estos comentarios se utilizan para explicar secciones de código.
# Puedes escribirlos entre tres comillas dobles (""" ... """) o entre tres comillas simples (''' ... ''').

"""
Este es un comentario en bloque.
Puede abarcar varias líneas y se usa para explicar funciones o secciones de código.
"""

# Llamamos a la función suma y mostramos el resultado.
numero1 = 5
numero2 = 3
resultado_suma = suma(numero1, numero2)
print("El resultado de la suma es:", resultado_suma)
