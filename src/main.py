print("======PYTHON EXPERIMENTS======")
print("1. Bast-Ultra-Lite")
print("2. Calc ")
print("3. Product CLI")
print("4. MiniRooms")
print("5. Salir/exit")
print("WARNING: ALL PROJECTS ARE IN SPANISH")
while 1: 
  try:
    slc = int(input("Select from the option index: "))
  except ValueError:
    print("Invalid")
    continue
  if slc == 1:
    import bast_ultralite
  elif slc == 2:
    import Calc
  elif slc == 3:
    import Product_CLI
  elif slc == 4:
    import MiniRooms
  elif slc == 5:
    print("Hasta la vista, baby")
    quit()
  else:
    print("Invalid")