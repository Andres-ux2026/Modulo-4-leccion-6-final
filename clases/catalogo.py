
class Catalogo:
    def __init__(self):
        self.producto = []

        
    def agregar_producto(self,producto):
        self.producto.append(producto)



    def listar_catalogo(self):
        if not self.producto:
         print("No hay productos registrados en el sistema.")
        else:
         for p in self.producto:
            print(p) 

    def buscar_por_id(self,id):
          for p in self.producto:
             if p.id == id:
                return p  

    def eliminar_producto(self,id):
       p = self.buscar_por_id(id)
       self.producto.remove(p)
        
    def guardar_catalogo(self,nombre_archivo="catalogo.txt"):
       try:
          with open(nombre_archivo,"w") as f:
             for p in self.producto:
                f.write(f"{p.id},{p.nombre},{p.categoria},{p.precio},{p.stock}\n")
       except Exception  as error:
          print(f"error en el archivo: {error}")
           

             
          


