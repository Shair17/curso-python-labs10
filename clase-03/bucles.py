# for
lista_frutas = ["🍎", "🍏", "🍓", "🍍", "🥥", "🍉", "🍇", "🍒", "🍑", "🍊", "🍋", "🍌"]

for fruta in lista_frutas:
  print(fruta)


indice = 0

while indice < (len(lista_frutas) - 1):
  indice +=1
  print(lista_frutas[indice])

# while
contador = 0
# 0
# 1
# 2
# 3
# ...
# 9

while contador < 100:
  contador += 1
  print(contador)
  if contador == 50:
    break

