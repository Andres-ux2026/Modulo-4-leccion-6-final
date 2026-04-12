import os

def menu_principal():
    while True:
        limpiar_pantalla()
        print("==========================================")
        print("       SISTEMA DE ECOMMERCE ")
        print("==========================================")
        print("1. Ingresar como ADMINISTRADOR")
        print("2. Ingresar como CLIENTE")
        print("3. Salir")
        print("------------------------------------------")
        
        rol = input("Seleccione su rol: ")
    
        if rol == "1":
            menu_admin()
        elif rol == "2":
            menu_cliente()
        elif rol == "3":
            print("\n¡Gracias por usar la app! Saliendo...")
            break
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
        print("5- Vaciar carro:")
        print("0- Salir:")

        opcion= int(input("Ingrese una opcion: "))
        return opcion


def menu_admin():
    while True:
        limpiar_pantalla()
        print("==========================================")
        print("        PANEL DE ADMINISTRACIÓN")
        print("==========================================")
        print("1. Ver inventario completo")
        print("2. Agregar nuevo producto")
        print("3. Actualizar stock/precio")
        print("4. Eliminar producto")
        print("5. <-- Volver al Menú Principal")
        print("------------------------------------------")
        
        opcion = input("Seleccione una acción: ")
        
        if opcion == "5":
            break
        elif opcion in ["1", "2", "3", "4"]:
            print(f"\nHas seleccionado la opción {opcion}. (Aquí irá la lógica)")
            input("\nPresione Enter para continuar...")
        else:
            print("\nOpción no válida. Intente de nuevo.")
            input()

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')