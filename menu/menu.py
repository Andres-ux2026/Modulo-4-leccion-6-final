import os
from clases.producto import Producto 
from clases.catalogo import Catalogo

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

mi_productos = Catalogo()
def menu_principal():
    while True:
        
        print("==========================================")
        print("       SISTEMA DE ECOMMERCE ")
        print("==========================================")
        print("1. Ingresar como ADMINISTRADOR")
        print("2. Ingresar como CLIENTE")
        print("3. Salir")
        print("------------------------------------------")
        
        rol = input("Seleccione su rol: ")
    
        if rol == "1":
            limpiar_pantalla()
            menu_admin()
        elif rol == "2":
            limpiar_pantalla()
            menu_cliente()
        elif rol == "3":
            return False
        else:
            print("\nOpción no válida. Intente de nuevo.")
            input()

def menu_cliente():
    while True:
        print("==========================================")
        print("        PANEL DE CLIENTE")
        print("==========================================")
        print("1- Ver catalogos de productos:")
        print("2- Buscar productos:")
        print("3- Agregar productos al carro:")
        print("4- Ver carro:")
        print("5- confirmar compra:")
        print("6- <-- Volver al Menú Principal")

        opcion= int(input("Ingrese una opcion: "))
        if opcion == "1":
            mi_productos.listar_catalogo()
            input("\nPresione Enter para continuar...")
        elif opcion == "6":
            break


def menu_admin():
    while True:
        
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
            print("==========================================")
            print("                CATALOGO")
            print("==========================================")
            mi_productos.abrir_catalogo()
            mi_productos.listar_catalogo()
            input("\nPresione Enter para volver al menú...") 

        elif opcion =="2":
            limpiar_pantalla()
            print("==========================================")
            print("         AGREGAR NUEVO PRODUCTO")
            print("==========================================")
            cod_prod = input("Ingrese ID del producto:")
            nom_prod = input("Ingrese Nombre del producto:")
            cat_prod = input("Ingrese categoria:")
            pre_prod = input("Ingrese precio:")
            stock_prod = input("Ingrese Stock del producto:")
            print("==========================================")
            opcion = input("\nPresione Y para guardar el producto:") 
            if opcion == "Y":
                producto= Producto(cod_prod,nom_prod,cat_prod,pre_prod,stock_prod)
                mi_productos.agregar_producto(producto)
                mi_productos.guardar_catalogo()
            else:
                print("Producto no guardado")

        elif opcion =="3":
            limpiar_pantalla()
            print("==========================================")
            print("          ACTUALIZAR PRODUCTOS")
            print("==========================================")
            mi_productos.abrir_catalogo()
            mi_productos.listar_catalogo()
            opcion = input("Escriba ID del producto a modificar:")
            cod_prod = input("Ingrese ID del producto:")
            nom_prod = input("Ingrese Nombre del producto:")
            cat_prod = input("Ingrese categoria:")
            pre_prod = input("Ingrese precio:")
            stock_prod = input("Ingrese Stock del producto:")
            print("==========================================")
            opcion = input("\nPresione Y para guardar el producto:") 
            if opcion == "Y":
                mi_productos.actualizar_producto(cod_prod,nom_prod,cat_prod,pre_prod,stock_prod)
            else:
                print("Producto no guardado")

        elif opcion =="4":
            limpiar_pantalla()
            print("==========================================")
            print("           ELIMINAR PRODUCTO")
            print("==========================================")
            mi_productos.abrir_catalogo()
            mi_productos.listar_catalogo()
            opcion = input("Escriba ID del producto a eliminar:")
            mi_productos.eliminar_producto(opcion)

            input("\nPresione Enter para volver al menú...")

        elif opcion =="5":
            limpiar_pantalla()
            break
        else:
            print("\nOpción no válida. Intente de nuevo.")
            input()

