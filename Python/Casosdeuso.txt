La elección entre listas, conjuntos, tuplas y diccionarios en Python depende de las necesidades específicas de tu programa.

Listas:
Cuando necesitas almacenar una colección de elementos en un orden específico y es posible que necesites modificar la lista.
Ejemplo: Una lista de tareas pendientes que puede crecer o reducirse a medida que se completan tareas.

tareas_pendientes = ["Comprar víveres", "Lavar el auto", "Hacer ejercicio"]

Conjuntos:
Cuando necesitas almacenar elementos únicos y no te importa el orden.
Para eliminar duplicados de una lista.
Ejemplo: Almacenas nombres de usuarios únicos en una aplicación.

nombres_usuarios = {"usuario1", "usuario2", "usuario3"}

Tuplas:
Cuando necesitas una colección inmutable de elementos.
Para garantizar que los datos no cambien.
Ejemplo: Coordenadas (latitud, longitud) de ubicaciones fijas.
coordenadas = (40.7128, -74.0060)

Diccionarios:
Cuando necesitas asociar claves con valores (como un conjunto de pares clave-valor).
Para buscar valores rápidamente por su clave.
Ejemplo: Un diccionario de contactos donde las claves son nombres y los valores son números de teléfono.

contactos = {"Juan": "123-456-7890", "Ana": "987-654-3210", "Pedro": "555-555-5555"}
