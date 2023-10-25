nombre = input("¿Cuál es tu nombre? ")
edad = int(input("¿Cuál es tu edad? "))
telefono = input("¿Cuál es tu teléfono? ")
tienes_mascota = input("¿Tienes mascota? ")

if tienes_mascota.lower() == ("si" or "sí"):
    tienes_mascota = True
else:
    tienes_mascota = False

nombre_de_mascota = None

if tienes_mascota:
    nombre_de_mascota = input("¿Cuál es el nombre de tu mascota? ")

sistema_operativo = input("¿Que sistema operativo usas? ")
marca_de_laptop = input("¿Cuál es la marca de tu laptop? ")
ciudad_donde_vives = input("¿Ciudad donde vives? ")

print(nombre, edad, telefono, tienes_mascota, nombre_de_mascota, sistema_operativo, marca_de_laptop, ciudad_donde_vives)
