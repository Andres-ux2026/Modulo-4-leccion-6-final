
class Producto:
    def __init__(self,id,nombre,categoria,precio,stock):
        self.id = id
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.stock = stock


    def __str__(self):
        return f"el id del producto es : {self.id} - {self.nombre} - {self.categoria} - {self.precio}- {self.stock}"
    
