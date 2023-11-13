# Ejemplo de función que devuelve varios valores
def dividir_y_obtener_resto(dividendo, divisor):
    """
    Esta función toma dos números, los divide y devuelve el cociente y el resto.

    Parámetros:
        - dividendo (int): El número que se dividirá.
        - divisor (int): El número por el cual se dividirá.

    Devolución:
        - tuple: Una tupla que contiene el cociente y el resto.
    """
    cociente = dividendo // divisor
    resto = dividendo % divisor
    return cociente, resto

# Uso de la función que devuelve varios valores
resultado = dividir_y_obtener_resto(10, 3)
print("Cociente:", resultado[0])
print("Resto:", resultado[1])

