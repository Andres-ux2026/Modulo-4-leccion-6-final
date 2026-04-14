class Usuario:
    def __init__(self,rut,nombre,apellido,tipo_usuario):
        self.rut = rut
        self.nombre = nombre
        self.nombre = apellido
        self.tipo_usuario = tipo_usuario


class Admin(Usuario):
    def __init__(self, rut, nombre, apellido, tipo_usuario):
        super().__init__(rut, nombre, apellido, tipo_usuario)

    


class Cliente(Usuario):
    def __init__(self, rut, nombre, apellido, tipo_usuario):
        super().__init__(rut, nombre, apellido, tipo_usuario)

    




