# Método keys()
# El método keys() se utiliza para acceder a todas las claves de un diccionario.
marcas_autos = {
    "Toyota": "Japonesa",
    "Ford": "Estadounidense",
    "Volkswagen": "Alemán"
}

claves = marcas_autos.keys()

print("Claves del diccionario:")
for clave in claves:
    print(clave)


# Método items()
# El método items() se utiliza para acceder a pares clave-valor en un diccionario.

marcas_autos = {
    "Toyota": "Japonesa",
    "Ford": "Estadounidense",
    "Volkswagen": "Alemán"
}

items = marcas_autos.items()

print("Pares clave-valor del diccionario:")
for clave, valor in items:
    print(clave, "-", valor)
