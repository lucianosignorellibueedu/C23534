# Ejemplo de función que utiliza otra función
def cuadrado(numero):
    """Esta función calcula el cuadrado de un número."""
    return numero ** 2

def suma_cuadrados(a, b):
    """
    Esta función toma dos números, calcula sus cuadrados utilizando la función 'cuadrado'
    y devuelve la suma de los cuadrados.

    Parámetros:
        - a (int): Primer número.
        - b (int): Segundo número.

    Devolución:
        - int: Suma de los cuadrados de 'a' y 'b'.
    """
    cuadrado_a = cuadrado(a)
    cuadrado_b = cuadrado(b)
    suma_total = cuadrado_a + cuadrado_b
    return suma_total

# Uso de la función que utiliza otra función
resultado = suma_cuadrados(3, 4)
print("Suma de los cuadrados:", resultado)
