marcas_autos = {
    "Toyota": "Japonesa",
    "Ford": "Estadounidense",
    "Volkswagen": "Alemán",
    "Hyundai": "Surcoreana",
    "Honda": "Japonesa"
}

print(marcas_autos["Toyota"])

# Agregar y modificar valores en un diccionario

marcas_autos = {
    "Toyota": "Japonesa",
    "Ford": "Estadounidense"
}

# Agregamos una nueva marca
marcas_autos["Chevrolet"] = "Estadounidense"

# Modificamos una marca existente
marcas_autos["Ford"] = "Norteamericana"

print(marcas_autos)

# Eliminar una entrada de un diccionario

marcas_autos = {
    "Toyota": "Japonesa",
    "Ford": "Estadounidense",
    "Volkswagen": "Alemán"
}

# Eliminamos la entrada "Ford"
del marcas_autos["Ford"]

print(marcas_autos)


