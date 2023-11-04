class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def presentarse(self):
        return f"Hola, soy {self.nombre} y tengo {self.edad} años"

juan = Persona("Juan", 30)
print(juan.presentarse())  # Output: Hola, soy Juan y tengo 30 años
