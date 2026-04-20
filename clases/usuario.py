import os
from clases.producto import Producto 
from clases.catalogo import Catalogo
from clases.carrito import Carrito



def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')



class Usuario:
    def __init__(self,rut,nombre,apellido,tipo_usuario):
        self.rut = rut
        self.nombre = nombre
        self.apellido = apellido
        self.tipo_usuario = tipo_usuario

    def menu(self):
        pass    


class Admin(Usuario):
    def __init__(self, rut, nombre, apellido, tipo_usuario):
        super().__init__(rut, nombre, apellido, tipo_usuario)

    def menu_admin(self,mi_productos):
     while True:
        limpiar_pantalla()
        print("==========================================")
        print("        PANEL DE ADMINISTRACIÓN")
        print("==========================================")
        print("1- Ver Catalogo")
        print("2- Agregar nuevo producto")
        print("3- Actualizar productos")
        print("4- Eliminar producto")
        print("5- <-- Volver al Menú Principal")
        print("------------------------------------------")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            limpiar_pantalla()
            print("=========================================================================")
            print("                                 CATALOGO")
            print("=========================================================================")
            mi_productos.abrir_catalogo()
            mi_productos.listar_catalogo()
            print("=========================================================================")
            input("Presione Enter para volver al menú...") 

        elif opcion =="2":
            limpiar_pantalla()
            print("==========================================")
            print("         AGREGAR NUEVO PRODUCTO")
            print("==========================================")
            try:
                cod_prod = input("Ingrese ID del producto:")
                if mi_productos.buscar_por_id(cod_prod):
                     print(f"ERROR: El ID '{cod_prod}' ya existe en el catálogo.")
                     input("Presione Enter para intentar con otro ID...")
                     continue
                nom_prod = input("Ingrese Nombre del producto:")
                cat_prod = input("Ingrese categoria:")
                pre_prod = int(input("Ingrese precio:"))
                stock_prod = int(input("Ingrese Stock del producto:"))
                print("==========================================")
                confirmacion = input("Presione Y para guardar el producto:").upper() 
                if confirmacion == "Y":
                  producto= Producto(cod_prod,nom_prod,cat_prod,pre_prod,stock_prod)
                  mi_productos.agregar_producto(producto)
                  mi_productos.guardar_catalogo()
                  print("Producto Guardado")
                else:
                 print("Producto no guardado")

                input("Presione Enter para volver al menu...")
            except ValueError:
                print("ERROR: El precio y el stock deben ser números enteros.")
            except Exception as e:
                 print(f"Ocurrió un error inesperado: {e}")


        elif opcion =="3":
            limpiar_pantalla()
            print("=========================================================================")
            print("                            ACTUALIZAR PRODUCTOS")
            print("=========================================================================")
            mi_productos.abrir_catalogo()
            if len(mi_productos.producto) == 0: 
                print("El catálogo está vacío.")
                input("Presione Enter para volver al menú...")
                continue # Regresa al menú principal
            mi_productos.listar_catalogo()
            print("=========================================================================")
            try:
                opcion_mod = input("Escriba ID del producto a modificar:")
                producto_encontrado = mi_productos.buscar_por_id(opcion_mod)
                if not producto_encontrado:
                    print(f"ERROR: El ID '{opcion_mod}' no existe en el catálogo.")
                    input("Presione Enter para volver al menú...")
                    continue
                   
                nom_prod = input("Ingrese Nombre del producto:")
                cat_prod = input("Ingrese categoria:")
                pre_prod = int(input("Ingrese precio:"))
                stock_prod = int(input("Ingrese Stock del producto:"))
                print("==========================================")
                opcion2 = input("Presione Y para guardar el producto:") 
                if opcion2 == "Y":
                  modificar = mi_productos.actualizar_producto(opcion_mod,nom_prod,cat_prod,pre_prod,stock_prod)
                  if modificar:
                     print("Producto actualizado y guardado correctamente.")
                  else:
                    print(" Error: No se encontró un producto con ese ID.")
                else:
                 print("Producto no guardado")
                 input("Presione Enter para volver al menú...") 
            except ValueError:
                print("ERROR: El precio y el stock deben ser números enteros.")
                input("Presione Enter para volver al menú...")
            except Exception as e:
                 print(f"Ocurrió un error inesperado: {e}")
                 input("Presione Enter para volver al menú...")



        elif opcion =="4":
            limpiar_pantalla()
            print("=========================================================================")
            print("                             ELIMINAR PRODUCTO")
            print("=========================================================================")
            mi_productos.abrir_catalogo()
            if len(mi_productos.producto) == 0: 
                print("El catálogo está vacío.")
                input("Presione Enter para volver al menú...")
                continue
            mi_productos.listar_catalogo()
            print("=========================================================================")
            opcion_eli = input("Escriba ID del producto a eliminar:")
            producto_encontrado = mi_productos.buscar_por_id(opcion_eli)
            if not producto_encontrado:
                    print(f"ERROR: El ID '{opcion_eli}' no existe en el catálogo.")
                    input("Presione Enter para volver al menú...")
                    continue
            else:
                mi_productos.eliminar_producto(opcion_eli)
                input("\nPresione Enter para volver al menú...")
              

        elif opcion =="5":
            limpiar_pantalla()
            break
        else:
            print("\nOpción no válida. Intente de nuevo.")
            input()

    


class Cliente(Usuario):
    def __init__(self, rut, nombre, apellido, tipo_usuario):
        super().__init__(rut, nombre, apellido, tipo_usuario)
        self.carrito = Carrito()


    def menu_cliente(self,mi_productos):
       mi_productos.abrir_catalogo()
       while True:
            limpiar_pantalla()
            print("==========================================")
            print("        PANEL DE CLIENTE")
            print("==========================================")
            print("1- Ver catalogos de productos:")
            print("2- Buscar productos:")
            print("3- Agregar productos al carro:")
            print("4- Ver carro:")
            print("5- confirmar compra:")
            print("6- <-- Volver al Menú Principal")

            opcion= input("Ingrese una opcion: ")
            if opcion == "1":
                limpiar_pantalla()
                print("================================================================================")
                print("                                    CATALOGO")
                print("================================================================================")
                mi_productos.listar_catalogo()
                print("================================================================================")
                input("Presione Enter para volver al menu...")
            elif opcion =="2":
                limpiar_pantalla()
                print("=====================================================================================================")
                print("                                          BUSCAR PRODUCTOS")
                print("=====================================================================================================")
                msj=input("Ingrese Nombre o categoria del producto a buscar o presione enter para cargar todos los productos:")
                print("=====================================================================================================")
                mi_productos.buscar_producto(msj)
                print("=====================================================================================================")
                input("\nPresione Enter para vover al menu ...")

            elif opcion =="3":
                limpiar_pantalla()
                print("=====================================================================================================")
                print("                                     AGREGAR PRODUCTOS AL CARRO")
                print("=====================================================================================================")
                msj=input("Ingrese Nombre o categoria del producto a buscar o presione enter para cargar todos los productos:")
                print("=====================================================================================================")
                mi_productos.buscar_producto(msj)
                print("=====================================================================================================")
                op_1 = input("Ingresa ID del producto a agregar:")
                op_2 = input("Ingrese la cantidad del producto:")
                print("=====================================================================================================")
                buscar= mi_productos.buscar_por_id(op_1)
                if buscar:
                    self.carrito.agregar_carrito(buscar,op_2)
                    input("Presione Enter para vover al menu ...")
                else:
                    print("Error: ID de producto no encontrado.")
                    input("Presione Enter para vover al menu ...")
            elif opcion =="4": 
                limpiar_pantalla()
                print("=============================================")
                print("               TU CARRO DE COMPRAS")
                print("=============================================")
                self.carrito.ver_carrito()  
                print("=============================================")   
                input("Presione Enter para vover al menu ...")
            elif opcion=="5":
                limpiar_pantalla()
                
                print("==============================================")
                print("               CONFIRMA TU COMPRA")
                print("==============================================")
                self.carrito.ver_carrito()
                print("==============================================")
                op_compra= input("Para confirmar su compra presione Y:").upper() 
                if op_compra== "Y":
                    self.carrito.confirmar_compra(mi_productos)   
                    input("Presione Enter para vover al menu ...")
                else:
                    print("opcion incorrecta compra no realizada")   
            elif opcion == "6":
                limpiar_pantalla()
                if len(self.carrito.items) == 0:
                     break
                op_salir = input("Hay productos en el carro de compras.Si sale se cancelara la compra. 'Si desea salir presione' 'Y':").upper()
                if op_salir == "Y":
                        input("Productos eliminados del carro de compras...")
                        self.carrito.devolver_stock_()
                        break
                else:
                     print("opcion invalida...")
                     input("Presione Enter para continuar con su compra...")




