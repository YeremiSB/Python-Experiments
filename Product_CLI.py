import inventario as inv

while 1:
  print("======PRODUCT MANAGER======")
  print("1. Registrar producto")
  print("2. Actualizar stock")
  print("3. Consultar producto")
  print("4. Mostrar inventario")
  print("5. Calcular valor total")
  print("6. Salir")
  try:
    s = int(input("Selecciona el indice de una opción: "))
  except ValueError:
    print("Opcion no valida")
    continue
    
  if s == 1:
    a = input("Codigo del producto?: ")
    b = input("Nombre del producto?: ")
    c = input("Costo del producto?: ")
    d = input("Stock del producto?: ")
    inv.registrar_producto(inv.inventario,a,b,c,d)
  elif s == 2:
    a = input("Codigo del producto?: ")
    b = input("Stock del producto?: ")
    inv.actualizar_stock(inv.inventario,a,b)
  elif s == 3:
    a = input("Codigo del producto?: ")
    inv.consultar_producto(inv.inventario, a)
  elif s == 4:
    print("------------------")
    for codigo in inv.inventario:
      inv.consultar_producto(inv.inventario,codigo)
      print("------------------")
  elif s == 5:
    print("el total seria: ", inv.calcular_valor_total(inv.inventario))
  elif s == 6:
    print("Gracias por usar!")
    quit()
  else:
    print("Elija una opcion valida")