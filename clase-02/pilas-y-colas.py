from collections import deque

# PILAS

# Crear una pila
mi_pila = []

# Apilar elementos
mi_pila.append(1)
mi_pila.append(2)
mi_pila.append(3)

print("mi_pila", mi_pila)

# Desapilar elementos
elemento_desapilado = mi_pila.pop()  # Desapilará el 3

# Ver el elemento en la cima sin desapilar
elemento_en_la_cima = mi_pila[-1]  # Devolverá 2

print("elemento_desapilado", elemento_desapilado)
print("elemento_en_la_cima", elemento_en_la_cima)

# COLAS

# Crear una cola
mi_cola = deque()

# Encolar elementos
mi_cola.append(1)
mi_cola.append(2)
mi_cola.append(3)

print("mi_cola", mi_cola)

# Desencolar elementos
elemento_desencolado = mi_cola.popleft()  # Desencolará el 1

print("elemento_desencolado", elemento_desencolado)

print("mi_cola", mi_cola)