inventario = {
    "P001": {
        "nombre": "Teclado",
        "precio": 85.50,
        "stock": 10
    },
    "P002": {
        "nombre": "Mouse",
        "precio": 45.00,
        "stock": 20
    }
}
def registrar_producto(inventario, codigo, nombre, precio, stock):
  try:
    precio = float(precio)
    stock = int(stock)
    if codigo in inventario:
      print("producto existente")
      return False
    elif precio <= 0:
      print("Precio invalido")
      return False
    elif stock < 0:
      print("Stock invalido")
      return False
    else:
      inventario[codigo] = {
          "nombre": nombre,
          "precio": precio,
          "stock" : stock 
      }
      print("Se ha añadido el siguiente producto")
      consultar_producto(inventario, codigo)
      return True
  except (ValueError,TypeError):
    print("Error, no se pudo completar la operacion")
    return False
def actualizar_stock(inventario, codigo, cantidad):
    try:
      cantidad = int(cantidad)
      if codigo in inventario:
        if cantidad >= 0:
          inventario[codigo]["stock"] = cantidad
          return True
        else:
          print("invalido, intente de nuevo")
          return False
      else:
        print("codigo inexistente")
        return False
    except (ValueError,TypeError):
      print("Error, intentelo de nuevo")
      return False
def consultar_producto(inventario, codigo):
    if codigo in inventario:
      print("Nombre:", inventario[codigo]["nombre"])
      print("Precio:", inventario[codigo]["precio"])
      print("Stock:", inventario[codigo]["stock"])
      return inventario[codigo]
    else:
      print("codigo inexistente")
      return None
def calcular_valor_total(inventario):
    total = 0
    for producto in inventario.values():
      total += producto["precio"] * producto["stock"]
    return total