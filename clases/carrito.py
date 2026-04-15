
from clases.producto import Producto

class Carrito():
   def __init__(self):
      self.items = {}

   def __str__(self):
      return f"{self.items}"   

   def agregar_carrito(self,producto,cantidad):
      if producto in self.items:
         self.items["producto"]+= cantidad
      else:
         self.items["producto"]= cantidad
            
   def calcular_total(self):
        pass
   def vaciar_carrito(self):
     pass   
