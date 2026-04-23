
from clases.catalogo import Catalogo
from clases.usuario import Admin, Cliente,limpiar_pantalla


class Tienda:
        def __init__(self):
            self.catalogo = Catalogo()
            self.catalogo.abrir_catalogo()
            self.admin_actual = Admin("16551814-4","Andres","Moraga","admin")
            self.cliente_actual = Cliente("16551814-4","Andres","Moraga","cliente")

   

        def iniciar(self):

         while True:
            limpiar_pantalla()    
            print("==========================================")
            print("       SISTEMA DE ECOMMERCE ")
            print("==========================================")
            print("1. Ingresar como ADMINISTRADOR")
            print("2. Ingresar como CLIENTE")
            print("3. Salir")
            print("------------------------------------------")
            try:
                 opcion = input("Seleccione el rol:")
            except EOFError:
                print("Error de lectura cerrando programa")
                break
            if opcion == "1":
                
                self.admin_actual.menu_admin(self.catalogo)

            elif opcion =="2":
                
                self.cliente_actual.menu_cliente(self.catalogo)
            else: 
                break


if __name__ == "__main__":
    try: 
        tienda = Tienda()
        tienda.iniciar()
    except KeyboardInterrupt:
        print("Saliendo del sistema...")
    except Exception as e:
        print(f"Error inesperado: {e}")    