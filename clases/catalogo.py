from clases.producto import Producto
import os
class Catalogo:
    def __init__(self):
        self.producto = []

        
    def agregar_producto(self,producto):
        self.producto.append(producto)



    def listar_catalogo(self):
        if not self.producto:
         print("El catalogo esta vacio.")
        else:
         for p in self.producto:
            print(p) 

    def buscar_por_id(self,id):
          for p in self.producto:
             if p.id == id:
                return p  

    def eliminar_producto(self,id):
       producto_encontrado = None
       for p in self.producto:
            if p.id == id:
               producto_encontrado = p
               break
    
       if producto_encontrado:
        self.producto.remove(producto_encontrado)
        self.guardar_catalogo()
        print("Producto eliminado")
        return True
       return False
        
    def guardar_catalogo(self,nombre_archivo="catalogo.txt"):
       try:
          with open(nombre_archivo,"w") as f:
             for p in self.producto:
                f.write(f"{p.id},{p.nombre},{p.categoria},{p.precio},{p.stock}\n")
       except Exception  as error:
          print(f"error en el archivo: {error}")


    def abrir_catalogo(self,nombre_archivo="catalogo.txt"):
       
       try:
        if os.path.exists(nombre_archivo): 
            with open(nombre_archivo, "r") as f:
                self.producto = []
                for linea in f:
                    datos = linea.strip().split(",")
                    if len(datos) == 5:
                        id_p, nombre, cat, precio, stock = datos
                        nuevo_p = Producto(id_p, nombre, cat, precio, stock)
                        self.producto.append(nuevo_p)
           
        else:
            print("No se encontró un archivo previo, iniciando catálogo vacío.")
       except Exception as error:
               print(f"Error al cargar el archivo: {error}")
       
    def actualizar_producto(self,id,nuevo_nombre,nueva_cat,nuevo_precio,nuevo_stock):
      if not self.producto:
        print("El catalogo esta vacio:")
      else: 
          for p in self.producto:
           if p.id == id:
             p.nombre = nuevo_nombre
             p.categoria = nueva_cat
             p.precio = nuevo_precio
             p.stock = nuevo_stock
             self.guardar_catalogo()
             return True
      print("El id no coincide")
      return False
      
    def buscar_producto(self,msj:str):
        encontrar= False
    
        for i in self.producto:
             if msj.lower() in i.nombre.lower() or msj.lower() in i.categoria.lower():
                print(f"ID: {i.id} - Nombre: {i.nombre} - Precio: ${i.precio} - Categoria: {i.categoria} - Stock: {i.stock}")
                encontrar = True
        if not encontrar: 
         print("productos no encontrado por favor revise nuestro catalogo:")        
           

             
          


