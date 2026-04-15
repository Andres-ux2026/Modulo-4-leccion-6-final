
class Producto:
    def __init__(self,id,nombre,categoria,precio,stock):
        self.id = id
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.stock = stock


    def __str__(self):
        return f" id: {self.id} -Nombre: {self.nombre} - Categoria: {self.categoria} - Precio:{self.precio}- Stock:{self.stock}"
    
