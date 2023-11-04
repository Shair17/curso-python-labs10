class Animal:
  def __init__(self, nombre, habitad):
    self.nombre = nombre
    self.habitad = habitad

  def presentarse(self):
    return f"Hola, me llamo {self.nombre} y mi habitad es {self.habitad}"


class Perro(Animal):
  def saludo(self):
    return "Guau"

class Gato(Animal):
  def saludo(self):
    return "Miau"

class Correcaminos(Animal):
  def saludo(self):
    return "MecMec"

perro = Perro("Bobby", "casa")
gato = Gato("Pelusa", "casa")
correcaminos = Correcaminos("Max", "desierto")

print(perro.nombre)
print(gato.nombre)
print(correcaminos.nombre)
print(perro.saludo())
print(gato.saludo())
print(correcaminos.saludo())
print(perro.presentarse())
print(gato.presentarse())
print(correcaminos.presentarse())


# Crear un objeto base de vehiculo, luego crear varios tipos de vehiculos heredando de la clase vehiculo, crear al menos 5 tipos de vehiculos, cada clase u objeto con sus propiedades y métodos correspondientes