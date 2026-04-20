
from datetime import datetime
class Carrito():
   def __init__(self):
      self.items = {}

   def __str__(self):
      return f"{self.items}"   

   def agregar_carrito(self,producto,cantidad):
       
       try:
        cantidad = int(cantidad)
        stock_actual = int(producto.stock)
        if cantidad <= 0:
            print("Error: La cantidad debe ser mayor a 0.")
            return False
        if cantidad > stock_actual:
            print(f"No se puede agregar: Stock insuficiente.")
            print(f"Solicitado: {cantidad} | Disponible: {stock_actual}")
            return False
        if producto in self.items:
            self.items[producto] += cantidad
        else:
            self.items[producto] = cantidad
    
        producto.stock = stock_actual - cantidad
        
        print(f"{producto.nombre} agregado al carrito.")
        print(f"Stock restante actualizado: {producto.stock}")
        return True

       except ValueError:
        print("ERROR: La cantidad debe ser un número entero.")
        return False

      

   def ver_carrito(self):

      if not self.items:
            print("El carrito está vacío.")
            return
      total=0
      for p,c  in self.items.items():
         subtotal = (p.precio) * (c)
         total += subtotal  
         print(f"Producto:{p.nombre}- cantidad:{c}-subtotal:{subtotal}")   
      print(f"total de la compra:{total}")    
            

   def vaciar_carrito(self):
     self.items.clear()  

   def confirmar_compra(self,catalogo):
        if not self.items:
            print(" El carrito está vacío.")
            return False

        try:
            total = 0
            ahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open("ordenes.txt", "a") as archivo:
                archivo.write(f"--- ORDEN DE COMPRA: {ahora}")
                
                for p, c in self.items.items():
                   
                    precio = (p.precio)
                    cantidad = (c)
                    subtotal = precio * cantidad
                    total += subtotal
                    
                    linea = f"Producto: {p.nombre} | Cantidad: {c} | Subtotal: ${subtotal}\n"
                    archivo.write(linea)
                
                archivo.write(f"TOTAL PAGADO: ${total}\n")
                archivo.write("-" * 40 + "\n\n")
                catalogo.guardar_catalogo()  

            print(f"Compra confirmada por ${total}. Registro guardado en ordenes.txt.")
            self.vaciar_carrito()
            return True

        except Exception as e:
            print(f"Error al procesar la compra: {e}")
            return False


   def devolver_stock_(self):
      if not self.items:
        return

      for producto, cantidad in self.items.items():
        producto.stock = int(producto.stock) + cantidad
      self.items.clear() 
     
