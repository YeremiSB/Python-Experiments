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

lista = [5, 5, 5, 5]
objetivo = 10
def num_plus(lista, objetivo):
  vistos = set()
  posibles = []
  for i in lista:
    complemento = objetivo - i
    if complemento not in vistos:
      vistos.add(i)
    else:
     posibles.append([i, complemento])
  return posibles
print(num_plus(lista, objetivo))

texto = "aabbcddex"
def busc_letn(texto):
  frec = {}
  letra_u = []
  for letra in texto:
    if letra not in frec:
     frec[letra] = 1
    elif letra in frec:
      frec[letra] += 1
  for letra in texto:
    if frec[letra] == 1:
      letra_u.append(letra)
  return letra_u
l = busc_letn(texto)
print(l)
def busc_letn2(texto):
  letra_u = []
  for letra in texto:
    a = texto.count(letra)
    if a > 1:
      continue
    else:
      letra_u.append(letra)
  return letra_u
print(busc_letn2(texto))