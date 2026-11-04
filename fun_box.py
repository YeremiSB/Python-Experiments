def HelloWolrd(printe):
  if printe == "print":
    print("Hello World")

A = [10, 5, 20, 8, 15]

def segundo_mayor(lista):
  mayor = None
  segundo = None
  for i in lista:
    if mayor is None:
      mayor = i
    elif i > mayor:
      segundo = mayor
      mayor = i
    elif i != mayor and (segundo is None or i > segundo):
      segundo = i
  return segundo

lista = [1, 2, 4, 6, 8, 9]
objetivo = 10

# Resultado: (2, 8)