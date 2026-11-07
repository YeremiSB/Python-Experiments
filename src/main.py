print("======PYTHON EXPERIMENTS======")
print("1. ChatYipit (New!)")
print("2. Bast-Ultra-Lite")
print("3. Calc ")
print("4. Product CLI")
print("5. MiniRooms")
print("6. Salir/exit")
print("WARNING: ALL PROJECTS ARE IN SPANISH")
while 1: 
  try:
    slc = int(input("Select from the option index: "))
  except ValueError:
    print("Invalid")
    continue
  if slc == 1:
    print("Loading...")
    import ChatYipiti
  if slc == 2:
    import bast_ultralite
  elif slc == 3:
    import Calc
  elif slc == 4:
    import Product_CLI
  elif slc == 5:
    import MiniRooms
  elif slc == 6:
    print("Hasta la vista, baby")
    quit()
  else:
    print("Invalid")