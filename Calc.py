#My """first""" calculator
def suma(a, b):
  op_suma = a + b
  return op_suma
def resta(a, b):
  op_resta = a - b
  return op_resta
def multi(a, b):
  op_mult = a * b
  return op_mult
def division(a, b):
  if b == 0:
      print("Por favor, amablemente cierre este programa, no soportamos a los que intentan dividir entre cero")
      return "INVALIDO"
  else:
    op_div = a / b
    return op_div
    

while 1: 
  print("=====CALCULADORA V.0.1====")
  print("Operaciones Disponibles")
  print("* Suma")
  print("* Resta")
  print("* Multiplicacion")
  print("* Division")
  print("Nota: Indique salir en cualquiera de los campos para salir")
  nro1 = input("Primer numero?").lower()
  if nro1 == "salir":
    quit()
  nro2 = input("Segundo numero?").lower()
  if nro2 == "salir":
    quit()
  try:
    nro1 = float(nro1)
    nro2 = float(nro2)
  except ValueError:
    print("Nro. no valido")
    continue
      
  operacion = input("Operacion?").lower()
  if operacion == "suma":
    resultado = suma(nro1, nro2)
  elif operacion == "resta":
    resultado = resta(nro1, nro2)
  elif operacion == "multiplicacion" or operacion == "multiplicación":
    resultado = multi(nro1, nro2)
  elif operacion == "division":
    resultado = division(nro1, nro2)
  else:
     print("no valido")
     continue
      
  print("respuesta: ",resultado)