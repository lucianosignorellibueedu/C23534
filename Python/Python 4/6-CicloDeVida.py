# Variable global
variable_global = 10

def funcion_local():
    # Variable local
    variable_local = 5
    print("Variable local dentro de la función:", variable_local)

    # Acceder a la variable global desde la función
    print("Variable global dentro de la función:", variable_global)

# Llamada a la función
funcion_local()

# Intentar acceder a la variable local fuera de la función generará un error
# print("Intento de acceder a la variable local fuera de la función:", variable_local)

# Variable libre (no local)
def funcion_principal():
    # Variable libre (no local) utilizada dentro de una función anidada
    variable_libre = 20

    def funcion_anidada():
        # Acceder a la variable libre desde la función anidada
        print("Variable libre desde la función anidada:", variable_libre)

    # Llamada a la función anidada
    funcion_anidada()

# Llamada a la función principal
funcion_principal()

# Intentar acceder a la variable libre fuera de la función generará un error
# print("Intento de acceder a la variable libre fuera de la función:", variable_libre)



"""Cuándo Utilizar Cada Caso:

Utiliza variables globales cuando necesites compartir datos entre diferentes partes de tu programa.

Utiliza variables locales cuando solo necesites que una variable sea válida dentro de una función específica.

Utiliza variables libres (no locales) cuando quieras compartir datos entre funciones anidadas y la función principal. Esto puede ser útil para la implementación de funciones cerradas (closures)."""