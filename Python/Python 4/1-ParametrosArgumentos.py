# Ejemplo de función con parámetros
def saludar(nombre, saludo="Hola"):
    """
    Esta función saluda a la persona con el nombre proporcionado.
    
    Parámetros:
        - nombre (str): El nombre de la persona.
        - saludo (str): El saludo que se utilizará. Por defecto, es "Hola".
    """
    mensaje = f"{saludo}, {nombre}!"
    return mensaje

# Ejemplo de llamada a la función con argumentos
resultado = saludar('Lio')

print(resultado)



"""Parámetros Obligatorios: Utiliza parámetros obligatorios cuando la información es esencial para que la función realice su tarea y no tiene un valor predeterminado adecuado."""

def calcular_area(base, altura):
    return base * altura

# Uso de parámetros obligatorios
area = calcular_area(5, 10)


"""Parámetros Opcionales: Utiliza parámetros opcionales cuando la información es secundaria o puede tener un valor predeterminado razonable."""

def saludar(nombre, saludo="Hola"):
    return f"{saludo}, {nombre}!"

# Uso de parámetro opcional
mensaje = saludar("Carlos")
