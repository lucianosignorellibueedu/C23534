index(elemento): Devuelve el índice de la primera ocurrencia del elemento especificado en la lista.


colores = ["rojo", "verde", "azul"]
índice_azul = colores.index("azul")
# índice_azul es 2

count(elemento): Devuelve el número de veces que un elemento aparece en la lista.


numeros = [1, 2, 3, 2, 4, 2, 5]
veces_dos = numeros.count(2)
# veces_dos es 3
sort(): Ordena la lista en orden ascendente.


numeros = [4, 2, 1, 3]
numeros.sort()
# numeros ahora es [1, 2, 3, 4]
reverse(): Invierte el orden de los elementos en la lista.


numeros = [1, 2, 3, 4]
numeros.reverse()
# numeros ahora es [4, 3, 2, 1]
# copy(): Crea una copia superficial de la lista.


frutas = ["manzana", "pera", "naranja"]
copia_frutas = frutas.copy()
# copia_frutas es una copia de frutas
# clear(): Elimina todos los elementos de la lista.


numeros = [1, 2, 3, 4, 5]
numeros.clear()
# numeros ahora es []