print("======PYTHON EXPERIMENTS======")
print("1. Bast-Ultra-Lite")
print("2. Calc ")
print("3. Product CLI")
print("4. MiniRoooms")
print("6. Salir/exit")
print("WARNING: ALL PROJECTS ARE IN SPANISH")
while 1: 
  try:
    slc = int(input("Select from the option index: "))
  except ValueError:
    print("Invalid")
    continue
  if slc == 1:
    import bast_ultralite