# Operador Lógico *AND*

# tienes que ser mayor de edad (+18) y además tener un presupuesto mayor de 50
edad = 18
presupuesto = 100

condicion_and = edad >= 18 and presupuesto > 50

print("cumple con los requisitos para ingresar", condicion_and)


# Operador Lógico *OR*
numero_aleatorio = 25

condicion_or = numero_aleatorio < 20 or numero_aleatorio < 30

print("el número es menor que 20 o menor que 30", condicion_or)

esta_soleado = False
condicion_not = not esta_soleado
print("está soleado?", condicion_not)

# Ejercicios de operadores lógicos:

# AND
# Solicitar datos al usuario como su edad, nacionalidad y si trabaja o no. Luego hacer un rango para mostrar un mensaje en consola. Este mensaje se mostrará siempre y cuando la persona sea mayor de edad y sea menor que 65, además que tiene que ser peruano.
edad_usuario = int(input("¿Cuál es tu edad?"))
nacionalidad_usuario = input("¿Cuál es tu país?")
trabajas_usuario = input("¿Trabajas actualmente?") # Si si Sí

if edad_usuario >= 18 and edad_usuario < 65 and (nacionalidad_usuario.lower() == 'perú' or nacionalidad_usuario.lower() == "peru") and (trabajas_usuario.lower() == 'si' or trabajas_usuario.lower() == 'sí'):
  print("felicidades, cumples con los requisitos!")
else:
  print("oh no, no cumples con los requisitos!")



# OR
# Solicitar al usuario una oración que incluya nombres de paises, y si la oración incluye perú o méxico entonces el usuario gana! caso contrario mostrar mensaje de ¡perdiste!
oracion_usuario = input("Escribe la oración que incluya nombres de paises: ")

if 'peru' in oracion_usuario.lower() or 'mexico' in oracion_usuario.lower() or 'perú' in oracion_usuario.lower() or 'méxico' in oracion_usuario.lower():
  print("Ganaste!")
else:
  print("Perdiste!")


# NOT
# Solicitar al usuario una contraseña, recuerda que una contraseña segura es considerada mayor a 10 dígitos y además que la contraseña no tiene que ser contraseña. Si la condición se cumplió pues mostrar un mensaje de felicidades, caso contrario recomendarle cambiar su contraseña
password_usuario = input("Ingresa la contraseña: ")

if len(password_usuario) > 10 and (not password_usuario == 'contraseña' or not password_usuario == 'password'):
  print("tu contraseña es considerada segura!")
else:
  print("tu contraseña es insegura!!")