# Método len() - devuelve la longitud de una cadena
def obtener_longitud(cadena):
    """
    Esta función toma una cadena de caracteres como entrada y devuelve su longitud.
    """
    return len(cadena)

cadena = "Hola, Mundo!"
print(f"Longitud de la cadena '{cadena}': {obtener_longitud(cadena)}")

# Método upper() - convierte una cadena en mayúsculas
def convertir_a_mayusculas(cadena):
    """
    Esta función toma una cadena de caracteres como entrada y la convierte en mayúsculas.
    """
    return cadena.upper()

cadena = "Hola, Mundo!"
print(f"Mayúsculas: {convertir_a_mayusculas(cadena)}")

# Método lower() - convierte una cadena en minúsculas
def convertir_a_minusculas(cadena):
    """
    Esta función toma una cadena de caracteres como entrada y la convierte en minúsculas.
    """
    return cadena.lower()

cadena = "Hola, Mundo!"
print(f"Minúsculas: {convertir_a_minusculas(cadena)}")

# Método strip() - elimina espacios en blanco al principio y al final de una cadena
def eliminar_espacios(cadena):
    """
    Esta función toma una cadena de caracteres como entrada y elimina los espacios en blanco al principio y al final.
    """
    return cadena.strip()

cadena = "  Hola, Mundo!  "
print(f"Eliminación de espacios en blanco: '{eliminar_espacios(cadena)}'")

# Método split() - divide una cadena en una lista de subcadenas utilizando un delimitador
def dividir_cadena(cadena, delimitador):
    """
    Esta función toma una cadena de caracteres y un delimitador como entrada, y divide la cadena en una lista de subcadenas.
    """
    return cadena.split(delimitador)

cadena = "Hola, Mundo!"
delimitador = ","
print(f"División de la cadena: {dividir_cadena(cadena, delimitador)}")

# Método join() - une una lista de cadenas en una sola cadena utilizando un separador
def unir_cadenas(lista, separador):
    """
    Esta función toma una lista de cadenas y un separador como entrada, y une las cadenas en una sola cadena.
    """
    return separador.join(lista)

lista = ["Hola", "Mundo"]
separador = " "
print(f"Unión de cadenas: {unir_cadenas(lista, separador)}")

# Método replace() - reemplaza una subcadena por otra en una cadena
def reemplazar_subcadena(cadena, antigua, nueva):
    """
    Esta función toma una cadena de caracteres, una subcadena antigua y una nueva como entrada, y reemplaza la subcadena antigua por la nueva en la cadena.
    """
    return cadena.replace(antigua, nueva)

cadena = "Hola, Mundo!"
antigua = "Hola"
nueva = "Saludos"
print(f"Reemplazo de subcadena: {reemplazar_subcadena(cadena, antigua, nueva)}")
