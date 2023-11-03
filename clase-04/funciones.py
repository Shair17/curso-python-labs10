def mostrar_mensaje(nombres: str, apellidos: str, edad: int):
  nombres = nombres.title()
  apellidos = apellidos.title()
  print("Hola, soy " + nombres + " " + apellidos + ", tengo " + str(edad) + " años.")


def sumar_numeros(numero1: int, numero2: int) -> int:
  suma = numero1 + numero2

  return suma


mostrar_mensaje("juan carlos", "gil malca", 25)
print(sumar_numeros(5, 6))



def es_par(numero: int) -> bool:
  if numero % 2 == 0:
    print("el número", numero, "es par")
    return True
  else:
    print("el número", numero, "no es par")
    return False

es_par(3)

def primera_letra_en_mayuscula(palabras: str) -> str:
  palabras = palabras.split()
  palabras_primera_letra_mayuscula = ' '.join(palabra[0].upper() + palabra[1:] for palabra in palabras)
  return palabras_primera_letra_mayuscula


print(primera_letra_en_mayuscula("hola y bienvenidos a la clase de python en labs10"))

# recuerda agregar el tipado necesario
# Crear una función para determinar si un número es primo
# Crear una función para obtener el factorial de un número
# Crear una función para determinar si una cadena de texto es palíndromo