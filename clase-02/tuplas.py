# tuplas

# Crear una tupla
mi_tupla = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# Acceder a elementos de la tupla (similar a las listas)
primer_elemento = mi_tupla[0]
ultimo_elemento = mi_tupla[-1]

rango = mi_tupla[1:4]

print("rango", rango)

# Las tuplas son inmutables, por lo que no puedes modificar sus elementos
# Por lo tanto, no puedes agregar, eliminar ni cambiar elementos en una tupla

# Obtener la longitud de la tupla
longitud = len(mi_tupla)

# Iterar a través de la tupla
for elemento in mi_tupla:
    print(elemento)


# 1. Crear una tupla de números, luego calcular la suma y el producto de la tupla
numeros_tupla = (1, 2, 3, 4, 5)

suma = 0
producto = 1

for numero in numeros_tupla:
    suma = suma + numero
    producto = producto * numero

print("suma total:", suma)
print("producto", producto)

# 2. Crear una tupla de números, luego encontrar el máximo y el minimo valor en cada tupla, hacer el ejercicio con y sin búcles
mi_tupla_2 = (100, 10, 20, 500, 540, 33)

# sin bucles
maximo = max(mi_tupla_2)
minimo = min(mi_tupla_2)

print("sin bucles")
print("Valor maximo", maximo)
print("Valor minimo", minimo)

print("con bucles")

maximo_b = mi_tupla_2[0]
minimo_b = mi_tupla_2[0]

for numero in mi_tupla_2:
    if numero > maximo_b:
        maximo_b = numero
    
    if numero < minimo_b:
        minimo_b = numero


print("maximo bucle:", maximo_b)
print("minimo bucle:", minimo_b)