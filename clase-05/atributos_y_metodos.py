class Persona:
  def __init__(self, nombre: str, edad: int, comidas_favoritas: list[str], funkos: list[str], perifericos: dict[str, str], musica: list[str]):
    self.nombre = nombre
    self.edad = edad
    self.comidas_favoritas = comidas_favoritas
    self.funkos = funkos
    self.perifericos = perifericos
    self.musica = musica

  def mostrar_musica(self):
    for indice, musica in enumerate(self.musica):
      print(f"Mi canción favorita número {indice + 1} es {musica.upper()}")

  def mostrar_perifericos(self):
    for periferico, periferico_detalles in self.perifericos.items():
      print(f"El periferico {periferico} es {periferico_detalles}")

  def mostrar_funkos(self):
    for indice, funko in enumerate(self.funkos):
      print(f"El funco número {indice + 1} es {funko}")

  def mostrar_comidas_favoritas(self):
    for comida_favorita in self.comidas_favoritas:
      print(comida_favorita)
    
  def presentarse(self):
    print(f"Hola, soy {self.nombre} y tengo {self.edad} años")



nombre = input("Dime tu nombre: ")
edad = int(input("Dime tu edad: "))
comidas_favoritas = []
funkos = []
perifericos = {
  "mouse": "",
  "teclado": "",
  "audifonos": "",
  "microfono": ""
}
musica = []

comidas_favoritas_cantidad = int(input("Dime cuantas comidas favoritas tienes: "))

for indice in range(comidas_favoritas_cantidad):
  comida_favorita = input(f"Dime tu comida favorita {indice + 1}: ")
  comidas_favoritas.append(comida_favorita)

funkos_cantidad = int(input("Dime cuantos funkos tienes: "))

for indice in range(funkos_cantidad):
  funko = input(f"Dame el nombre de tu funko {indice + 1}: ")
  funkos.append(funko)

for periferico, _ in perifericos.items():
  nuevo_valor = input(f"Dame los detalles para el perifico {periferico}: ")
  perifericos[periferico] = nuevo_valor

musica_cantidad = int(input("Dime cuantas canciones favoritas tienes: "))

for indice in range(musica_cantidad):
  musica_favorita = input(f"Dime tu música favorita {indice + 1}: ")
  musica.append(musica_favorita)


juan = Persona(nombre, 30, comidas_favoritas, funkos, perifericos, musica)
juan.presentarse()
juan.mostrar_comidas_favoritas()
juan.mostrar_funkos()
juan.mostrar_perifericos()
juan.mostrar_musica()