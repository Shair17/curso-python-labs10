# Definición de una clase
class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    def describir_coche(self):
        return f"Este coche es un {self.marca} {self.modelo}"

# Creación de objetos a partir de la clase Coche
coche1 = Coche("Toyota", "Corolla")
coche2 = Coche("Ford", "Mustang")

# Uso de métodos de los objetos
print(coche1.describir_coche())  # Output: Este coche es un Toyota Corolla
print(coche2.describir_coche())  # Output: Este coche es un Ford Mustang
