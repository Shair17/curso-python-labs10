# Polimorfismo
# Poli -> varios
# morfismo -> formas

class Animal:
  def hacer_sonido(self):
    pass

class Perro(Animal):
  def hacer_sonido(self):
    return "Guau"

class Gato(Animal):
  def hacer_sonido(self):
    return "Miau"

# Función polimórfica
def hacer_sonar(animal: Animal):
  return animal.hacer_sonido()

# Crear instancias de diferentes clases
perro = Perro()
gato = Gato()

# Llamar al método hacer_sonar con diferentes instancias
print(hacer_sonar(perro))  # Output: Guau
print(hacer_sonar(gato))   # Output: Miau
