# Definir una tupla con nombres de personas
personas = ("Jose", "Maria", "Pato")

# También puedes definir una tupla sin paréntesis
numeros_primos = 2, 3, 5, 7


# Acceder al primer elemento de la tupla personas
primer_nombre = personas[0]
print(primer_nombre)  # Salida: "Jose"


# Iterar a través de los elementos de la tupla numeros_primos
for numero in numeros_primos:
    print(numero)


# Desempaquetar una tupla en variables individuales
nombre1, nombre2, nombre3 = personas
print(nombre1)  # Salida: "Jose"
print(nombre2)  # Salida: "Maria"
print(nombre3)  # Salida: "Pato"



# Concatenar dos tuplas
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)
tupla_concatenada = tupla1 + tupla2
print(tupla_concatenada)  # Salida: (1, 2, 3, 4, 5, 6)
