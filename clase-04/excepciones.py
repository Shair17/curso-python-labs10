def division_segura(dividendo: int, divisor: int):
  try:
    resultado = dividendo / divisor
    print(f"El resultado es {resultado}")
  except ZeroDivisionError:
    print("error: división por cero no permitida")


division_segura(10, 2)
division_segura(8, 0)

# hacer una función que pida un número entero al usuario con input, y si ingresa el dato equivocado mostrarle una excepción

def leer():
  try:
    return int(input("Ingresa un numero entero: "))
  except ValueError:
    print("Error: el valor introducido no es un número entero")

numero_a_leer = leer()
print(numero_a_leer)