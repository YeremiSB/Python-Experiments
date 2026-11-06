class CuentaBancaria:
  def __init__(self, titular):
    self.__titular = titular
    self.__saldo = 0.0
  @property
  def titular(self):
    return self.__titular
  @titular.setter
  def titular(self, nuevo_titular):
    if nuevo_titular.strip():
      self.__titular = nuevo_titular
    else:
      print("Nombre invalido, intente de nuevo")   
  def depositar(self, cantidad):
    try:
      cantidad = float(cantidad)
      if cantidad < 0:
        print("Saldo Invalido, intente de nuevo")
      else:
        self.__saldo += cantidad
        print("Saldo depositado exitosamente, saldo actual: ", self.__saldo)
    except ValueError:
      print("Saldo Invalido, intente de nuevo")
  def retirar(self, cantidad):
    try:
      cantidad = float(cantidad)
      if cantidad > self.__saldo or cantidad <= 0:
        print("Falta saldo para esta operacion")
      else:
        self.__saldo -= cantidad
    except ValueError:
     print("Saldo Invalido, intente de nuevo")
  @property
  def saldo(self):
      return self.__saldo
class CuentaAhorros(CuentaBancaria):
  def __init__(self, titular):
    super().__init__(titular)
  def tasa_interes(self):
    interes = self.saldo * 0.02
    return interes
  def aplicar_interes(self):
    self.depositar(self.tasa_interes())