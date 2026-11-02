#Hi, if u see this, pls go to see bast.yeremisb.com
cartera = 0.00
ingresoval = 0.00
gastoval = 0.00
ingresos = []
gastos = []
def ingreso_add(nombre,valor):
  ingresos.append((nombre, valor))
def gasto_add(nombre, valor):
  gastos.append((nombre, valor))

while 1: 
  print("======Bast-UltraMini======")
  print("Cartera: ", cartera)
  print("OPCIONES")
  print("1. Registrar ingresos")
  print("2. Registrar gasto")
  print("3. Lista gasto")
  print("4. Lista ingresos")
  print("5. Buscar gasto")
  print("6. Buscar ingreso")
  print("7. Salir")
  
  try:
    opcion = int(input("ingrese indice de opcion (numero):"))
    if opcion == 1:
      while 1:
        inn = input("Nombre del ingreso?").lower()
        try:
          inv = float(input("Valor del ingreso?"))
        except ValueError:
          print("monto invalido")
          continue
        else:
          break
      ingreso_add(inn,inv)
    if opcion == 2:
      while 1:
        gn = input("Nombre del gasto?").lower()
        try:
          gv = float(input("Valor del gasto?"))
        except ValueError:
          print("monto invalido")
          continue
        else:
          break
      gasto_add(gn,gv)
    if opcion == 3:
      print(gastos)
    if opcion == 4:
      print(ingresos)
    if opcion == 5:  
      buscado = input("Nombre del gasto a buscar?").lower()
      encontrado = False
      for nombre,valor in gastos:
        if buscado == nombre:
          print("Nombre: ", nombre)
          print("Valor: ", valor)
          encontrado = True
      if encontrado == False:
        print("No existe")
         
    if opcion == 6:  
      buscado = input("Nombre del ingreso a buscar?").lower()
      encontrado = False
      for nombre,valor in ingresos:
        if buscado == nombre:
          print("Nombre: ", nombre)
          print("Valor: ", valor)
          encontrado = True
      if encontrado == False:
        print("No existe")
    if opcion == 7:
      quit()
  except ValueError:
    print("Operacion invalida")
    continue

  ingresoval = 0
  for nombre,valor in ingresos:
    ingresoval += valor
  gastoval = 0
  for nombre,valor in gastos:
    gastoval += valor
  cartera = ingresoval - gastoval
  