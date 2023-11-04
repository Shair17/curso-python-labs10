class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        pass

class Perro(Animal):
    def hacer_sonido(self):
        return "Guau"

class Gato(Animal):
    def hacer_sonido(self):
        return "Miau"

perro = Perro("Bobby")
gato = Gato("Pelusa")

print(perro.nombre)  # Output: Bobby
print(gato.nombre)   # Output: Pelusa
print(perro.hacer_sonido())  # Output: Guau
print(gato.hacer_sonido())   # Output: Miau
