# Definición de una clase
class Carro:
  def __init__(self, marca, modelo, cantidad_llantas, maxima_velocidad):
    self.marca = marca
    self.modelo = modelo
    self.cantidad_llantas = cantidad_llantas
    self.maxima_velocidad = maxima_velocidad

  def describir_coche(self) -> str:
    return f"Este carro es un {self.marca} {self.modelo}"

  def obtener_maxima_velocidad(self) -> str:
    return f"Este carro tiene una máxima velocidad de {self.maxima_velocidad}km/h"

# Creación de objetos a partir de la clase Coche
carro1 = Carro("Toyota", "Corolla", 4, 300)
carro2 = Carro("Ford", "Mustang", 4, 400)

# Uso de métodos de los objetos
print(carro1.describir_coche())  # Output: Este coche es un Toyota Corolla
print(carro2.describir_coche())  # Output: Este coche es un Ford Mustang

print(carro1.obtener_maxima_velocidad())
print(carro2.obtener_maxima_velocidad())

# Crear un cajero automático con POO, en el cajero se puede establecer la cantidad de dinero que hay disponible, se puede retirar y depositar dinero. Además debería de poder mostrar la cantidad de dinero disponible.

class Cajero:
  def __init__(self, saldo):
    self.saldo = saldo

  def depositar(self, cantidad_deposito):
    self.saldo += cantidad_deposito
    print(f"Se ha depositado {cantidad_deposito}")

  def retirar(self, cantidad_retiro):
    if self.saldo >= cantidad_retiro:
      self.saldo -= cantidad_retiro
      print(f"Se ha retirado {cantidad_retiro}")
    else:
      print(f"Dinero insuficiente")

  def mostrar_saldo(self):
    print(f"Saldo actual: {self.saldo}")

cajero_1 = Cajero(1000)
cajero_1.mostrar_saldo()
cajero_1.depositar(500)
cajero_1.retirar(1500)
cajero_1.mostrar_saldo()

# Crear un objeto de una persona y en base a eso crear distintas instancias con datos o acciones según tu criterio