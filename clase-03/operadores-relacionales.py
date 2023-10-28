a = 10
b = 15

# Igualdad (==)
if a == b:
  print("a y b son iguales")

# Desigualdad (!=)
if a != b:
  print("a y b son diferentes")

# Mayor que >, Menor que <
if a < b:
  print("a es menor que b")

if a > b:
  print("a es mayor que b")

# Mayor o igual que >=, Menor o igual que <=
if a <= b:
  print("a es menor o igual que b")

if a >= b:
  print("a es mayor o igual que b")


# Ejercicio 01: Pedir un numero al usuario y hacer una condición que verifique si el número es impar o par, y mostrar sus respectivos mensajes según la condición

numero_usuario = int(input("Ingresa un número: "))

if numero_usuario % 2 == 0:
  print(str(numero_usuario), "es par")
else:
  print(str(numero_usuario), "es impar")


# Ejercicio 02: Pedir dos edades de personas, y luego compararlas y mostrar mensajes de quien es mayor que quien según su edad. OPCIONAL: Pueden usar diccionarios para agregar datos adicionales como nombre, edad, etc

primer_nombre = input("Ingresa el primer nombre: ")
primera_edad = int(input("Ingresa la primera edad: "))
segundo_nombre = input("Ingresa el segundo nombre: ")
segunda_edad = int(input("Ingresa la segunda edad: "))

personas = {
  primer_nombre: primera_edad,
  segundo_nombre: segunda_edad
}


if personas[primer_nombre] == personas[segundo_nombre]:
  print("Ambos tienen la misma edad")
elif personas[primer_nombre] > personas[segundo_nombre]:
  print("La edad de", primer_nombre, "es mayor")
else:
  print("La edad de", segundo_nombre, "es mayor")


# Ejercicio 03: Pedir dos palabras al usuario, luego comprarlas entre ellas para ver que palabra es más grande
primera_palabra = input("Ingresa la primera palabra: ")
segunda_palabra = input("Ingresa la segunda palabra: ")

if len(primera_palabra) < len(segunda_palabra):
  print("La segunda palabra", segunda_palabra, "es más larga.")
else:
  print("La primera palabra", primera_palabra, "es más larga.")