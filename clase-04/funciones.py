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

def es_primo(numero: int) -> bool:
  if numero <= 1:
    return False

  for i in range(2, int((numero) ** 0.5) + 1):
    if numero % i == 0:
      return False

  return True


numero_para_evaluar_si_es_primo = 17
resultado_es_primo = es_primo(numero_para_evaluar_si_es_primo)
if (resultado_es_primo):
  print("El número " + str(numero_para_evaluar_si_es_primo) + " es primo")
else:
  print("El número " + str(numero_para_evaluar_si_es_primo) + " no es primo")


def factorial(numero: int) -> float:
  if numero == 0 or numero == 1:
    return 1
  
  return numero * factorial(numero - 1)


factorial_numero = 5
resultado_factorial = factorial(factorial_numero)

print(f"El factorial de {factorial_numero} es {resultado_factorial}")


def es_palindromo(cadena: str) -> bool:
  cadena = cadena.lower().replace(" ", "")

  return cadena == cadena[::-1]

cadena = "Anita lava la tina"
cadena_es_palindroma = es_palindromo(cadena)

if (cadena_es_palindroma):
  print(f"la cadena {cadena} es palindroma")
else:
  print(f"la cadena {cadena} no es palindroma")

def mostrar_saludo():
  print(__name__)
  print("Hola desde funciones.py")