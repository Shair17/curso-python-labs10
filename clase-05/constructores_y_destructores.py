class MiClase:
  def __init__(self):
    print("Se ha creado un objeto")

  def __del__(self):
    print("Se ha destruido un objeto")

objeto1 = MiClase()
objeto2 = MiClase()

# El segundo objeto se destruye automáticamente al finalizar el programa
