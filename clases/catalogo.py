
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

    def eliminar_producto():
        pass



