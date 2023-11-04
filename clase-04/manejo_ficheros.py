# r -> read -> leer

archivo_modo_lectura = open("lectura.txt", "r", encoding="utf-8")
archivo_modo_lectura_contenido = archivo_modo_lectura.read()

print(archivo_modo_lectura_contenido)

archivo_modo_lectura.close()



# w -> write -> escribir

# archivo_modo_escritura = open("escritura.txt", "w", encoding="utf-8")
# archivo_modo_escritura.write("hola!, esta es la primera línea\n")
# archivo_modo_escritura.write("adios!, esta es la segunda línea\n")
# archivo_modo_escritura.close()

archivo = open("escritura.txt", "r", encoding="utf-8")
contenido = archivo.read()
lista = contenido.split("\n")
print(lista)

# Crear un archivo notas de unidades, como este ejemplo:
# 12, 14, 18
# 19, 10, 20
# 13, 15, 10
# ...
# luego de leer el archivo de notas, agruparlos en una lista, luego sacar el promedio de cada 3 notas y determinar si la persona que saco esa nota aprobó o no.

# Crear un archivo de numeros, luego leer el archivo y hacer la sumatoria con esos números

# Escribir dentro de un archivo números aleatorios, separados por comas, como este ejemplo:
# 5, 4, 3
# 9, 8, 7
# ...