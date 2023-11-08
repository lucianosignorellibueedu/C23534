# Ejemplo de estructura secuencial
nombre = "Juan"
apellido = "Pérez"
edad = 30

print("Nombre completo:", nombre, apellido)
print("Edad:", edad)


# Ejemplo de estructura condicional
edad = 18

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")


# Ejemplo de estructura iterativa
n = 5
i = 0

while i < n:
    print("Iteración", i + 1)
    i += 1


# Ejemplo 1: Recorriendo una lista:

 
 
frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print(fruta)
# Este bucle for recorre la lista de frutas e imprime cada una de ellas.

# Ejemplo 2: Recorriendo un rango: 
 
for i in range(5):
    print(i)
# Este bucle for itera sobre un rango de números del 0 al 4 e imprime cada número.

# Ejemplo 3: Recorriendo una cadena de texto:

 
 
mensaje = "Hola, Python"
for letra in mensaje:
    print(letra)
# Este bucle for recorre cada carácter en la cadena de texto "mensaje" e imprime cada carácter.

# Ejemplo 4: Bucle for anidado:

 
 
for i in range(3):
    for j in range(3):
        print(f"({i}, {j})")
# Este ejemplo muestra cómo se pueden utilizar bucles for anidados para iterar a través de combinaciones de valores.

# Ejemplo 5: Usando enumerate para obtener índices y valores:

 
 
frutas = ["manzana", "banana", "cereza"]
for indice, fruta in enumerate(frutas):
    print(f"Índice {indice}: {fruta}")

# El uso de la función enumerate permite obtener tanto el índice como el valor de los elementos en la lista.
# Estos son algunos ejemplos de cómo se pueden usar bucles for en Python. Los bucles for son una herramienta poderosa para iterar sobre secuencias de datos y realizar tareas repetitivas.


# La declaración break se utiliza en estructuras repetitivas (como bucles for o while) en Python para salir prematuramente del bucle en función de una condición dada. Cuando se ejecuta la declaración break, el flujo del programa se interrumpe y sale del bucle, sin continuar con las iteraciones posteriores.

frutas = ["manzana", "banana", "cereza", "sandía", "kiwi"]

for fruta in frutas:
    print(fruta)
    if fruta == "cereza":
        break

print("¡Encontramos una cereza y salimos del bucle!")
