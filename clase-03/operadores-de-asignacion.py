# Asignación (=)
x = 5

# Suma y Asignación (+=)
x += 3

# Resta y Asignación (-=)
x -= 2

# Multiplicación y Asignación (*=)
x *= 3

# División y Asignación (/=)
x /= 8

print(x)

# Solicitar un numero inicial y un numero para incrementar, es decir, si el usuario ingresa 0 y en numero para incrementar ingresa 5, entonces hacer la operación con el operador de asignación de suma
numero_inicial = int(input("Ingresa el número inicial: "))
numero_incremental = int(input("Ingresa el número incremental: "))

numero_inicial += numero_incremental

print("El resultado es", numero_inicial)

# Solicitar precio de un producto, luego solicitar el porcentaje de descuento, y luego mostrar el precio del producto y el precio con descuento al final
precio_producto = int(input("Ingresa el precio del producto: "))
porcentaje_descuento = int(input("Ingresa el porcentaje de descuento (0 - 100)"))

precio_producto *= (1 - (porcentaje_descuento / 100))

print("El precio final del producto es", precio_producto)

# Pedir x (tiene que ser dinamico) textos al usuario, e ir concatenando cada texto para al final ser mostrado
cantidad_textos = int(input("Ingresa la cantidad de textos que debo preguntar: "))
valor = ""

for posicion in range(cantidad_textos):
  texto = input("Ingresa el texto número " + str(posicion + 1) + ": ")
  valor += "\n"
  valor += texto

print(valor)