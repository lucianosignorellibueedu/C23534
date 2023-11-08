# Definir un conjunto con marcas de autos
marcas_autos = {"Toyota", "Ford", "Honda", "Toyota", "Nissan"}

# También puedes crear un conjunto a partir de una lista
ciudades_argentinas = set(["Buenos Aires", "Córdoba", "Rosario", "Mendoza"])



# Iterar a través de los elementos del conjunto de ciudades argentinas
for ciudad in ciudades_argentinas:
    print(ciudad)


# Agregar una ciudad al conjunto de ciudades argentinas
ciudades_argentinas.add("Salta")


# Eliminar una ciudad del conjunto de ciudades argentinas
ciudades_argentinas.remove("Buenos Aires")

# Crear un segundo conjunto de ciudades
otras_ciudades = {"Mar del Plata", "La Plata", "Córdoba"}

# Unión de conjuntos
union_ciudades = ciudades_argentinas.union(otras_ciudades)

# Intersección de conjuntos
interseccion_ciudades = ciudades_argentinas.intersection(otras_ciudades)

# Diferencia de conjuntos
diferencia_ciudades = ciudades_argentinas.difference(otras_ciudades)
