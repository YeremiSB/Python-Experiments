#Soy capitan clark y estos son mis backrooms
items = []
room =0
while 1:
  print("======MINIROOMS======")
  print("MENU")
  print("* Jugar")
  print("* Salir")
  menu_op=input("Seleciona una opcion").lower()
  if menu_op == "jugar":
    break
  elif menu_op == "salir":
    quit()
while 1:
  if room == 0:
    print("Despiertas en una habitacion con tapizado amarillo y aspecto de oficina")
    print("tienes 2 pasillos a la izquierda y la derecha")
    print("* Izquierda")
    print("* Derecha")
    seleccion = input("A donde iras?").lower()
    if seleccion == "izquierda":
      room = 1
    if seleccion == "derecha":
      room = 2
  if room == 1:
    buscado = "llave"
    encontrado = False
    for item in items:
      if buscado == item:
        print("Llegas al final del pasillo, solo hay... soledad?")
        print("* llorar")
        print("* irse")
        seleccion = input().lower()
        if seleccion == "llorar":
          print("Se ha mojado el suelo con tus lagrimas")
        elif seleccion == "irse":
          room = 0
        encontrado = True
    if encontrado == False:
      print("Llegas al final del pasillo, solo hay una llave y soledad")
      print("* recoger llave")
      print("* irse")
      seleccion = input().lower()
      if "llave" in seleccion:
        print("llave recogida!")
        items.append("llave")
        room = 0
      elif seleccion == "irse":
        room = 0
  if room == 2:
    print("llegas al final donde hay una puerta cerrada y otra bifurcacion a la izquierda")
    buscado = "llave"
    encontrado = False
    for item in items:
      if buscado == item:
        print("que bueno que tienes una llave")
        print("* abrir puerta")
        print("* ir a la izquierda")
        print("* regresar")
        seleccion = input().lower()
        if seleccion == "abrir puerta":
          room = 4
        elif seleccion == "regresar":
            room = 0
        elif "izquierda" in seleccion:
          room = 3
      encontrado = True
    if encontrado == False:
      print("* ir a la izquierda")
      print("* regresar")
      seleccion = input().lower()
      if seleccion == "regresar":
          room = 0
      elif "izquierda" in seleccion:
          room = 3
  if room == 3:
    print("Llegas al final del pasillo, solo hay... soledad?")
    print("* llorar")
    print("* irse")
    seleccion = input()
    if seleccion == "llorar":
        print("Se ha mojado el suelo con tus lagrimas")
    elif seleccion == "irse":
        room = 2
  if room == 4: 
    print("tienes 3 pasillos de frente, a la izquierda y la derecha")
    print("* Izquierda")
    print("* De frente")
    print("* Derecha")
    seleccion = input().lower()
    if seleccion == "de frente":
      room = 5
    if seleccion == "izquierda":
      room = 6
    if seleccion == "derecha":
      room = 7
  if room == 5:
    buscado = "moneda" 
    encontrado = False
    for item in items:
      if buscado == item:
        print("Llegaste al final del pasillo, encuentras soledad")
        room = 4
        encontrado = True
    buscado = "llave2" 
    encontrado = False
    for item in items:
      if buscado == item:
        print("Llegaste al final del pasillo, encuentras soledad")
        room = 4
        encontrado = True
    if encontrado == False:
      print("Llegaste al final del pasillo, encuentras una moneda y una llave")
      print("* Coger llave")
      print("* Coger moneda")
      seleccion = input().lower()
      if "llave" in seleccion:
        print("llave recogida!")
        items.append("llave2")
        room = 4
      if "moneda" in seleccion:
        print("moneda recogida!")
        items.append("moneda")
        room = 4
    
      