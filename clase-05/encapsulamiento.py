class Coche:
  def __init__(self, marca, modelo):
    self.__secreto = "secreto"
    self.__marca = marca  # __ indica que es privado
    self.__modelo = modelo

  def obtener_secreto(self):
    return self.__secreto[::-1]

  def get_marca(self):
    return self.__marca

  def set_marca(self, nueva_marca):
    self.__marca = nueva_marca

# Uso de encapsulamiento
coche = Coche("Toyota", "Corolla")
print(coche.get_marca())  # Output: Toyota

# Intento de acceder directamente al atributo privado (no debería funcionar)
# print(coche.__marca)  # Esto dará un error

# Modificación a través de un método
coche.set_marca("Ford")
print(coche.get_marca())  # Output: Ford

print(coche.obtener_secreto())

# Crear una instancia de un producto el cual tiene ingredientes publicos e ingredientes secretos, luego mostrar esos ingredientes secretos pero de manera encriptada