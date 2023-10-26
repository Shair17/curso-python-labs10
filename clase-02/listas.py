# listas

# Crear una lista
mi_lista = [1, 2, 3, 'cuatro', 5.0]

# Acceder a elementos de la lista
primer_elemento = mi_lista[0]  # Acceder al primer elemento (índice 0)
ultimo_elemento = mi_lista[-1]  # Acceder al último elemento
rango = mi_lista[1:4]  # Obtener un rango de elementos (índices 1 a 3)

# Modificar o mutar elementos de la lista
mi_lista[2] = 'tres'  # Modificar el tercer elemento

# Agregar elementos a la lista
mi_lista.append(6)  # Agregar un elemento al final

mi_lista.insert(1, 'nuevo')  # Insertar un elemento en un índice específico

# Eliminar elementos de la lista
mi_lista.remove(2)  # Eliminar el elemento con valor 2

elemento_eliminado = mi_lista.pop(3)  # Eliminar el elemento en el índice 3

# Obtener la longitud de la lista
longitud = len(mi_lista)

# Iterar a través de la lista
for elemento in mi_lista:
    print(elemento)


# Crear una lista de números, luego definir una lista pero vacía, y esta lista vacía llenarla con los números pares de la primera lista

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros_pares = []

for numero in numeros:
    if numero % 2 == 0:
        numeros_pares.append(numero)


print("numeros pares:", numeros_pares)