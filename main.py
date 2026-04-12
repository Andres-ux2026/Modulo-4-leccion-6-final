from menu.menu import menu_principal,limpiar_pantalla
""" from funciones.mostrar_catalogo import ver_productos, buscar_producto
from productos.catalogo import catalogo
from carrito.agregar_carrito import agrega_producto,calcular_total,mostrar_carrito,vaciar_carrito

 """
def main():
    carr_prod =[]

  
limpiar_pantalla()
opcion=menu_principal()
""" 
        if opcion ==1:
      
            limpiar_pantalla()
            ver_productos(catalogo)
            input("\nPresiona Enter para volver al menú...")

        elif opcion ==2:

            limpiar_pantalla()
            print("------Bienvenido a nuestro buscador de productos:------")
            msj=input("Ingrese Nombre o categoria del producto a buscar:")
            buscar_producto(catalogo,msj)
            input("\nPresiona Enter para volver al menú...")


        elif opcion ==3:
            limpiar_pantalla()
            print("Agregar productos al carrito:")
            op1= int(input("ingrese ID del producto a comprar:"))
            op2= int(input("Ingrese la cantidad:"))
            agrega_producto(catalogo,carr_prod,op1,op2)
            input("\nPresiona Enter para volver al menú...")

        elif opcion ==4:
            limpiar_pantalla()
            print("Ver carro de compras:")
            
            if not carr_prod:
                print("El carrito está vacío.")
            else:
                mostrar_carrito(carr_prod)
               
            print("Total a pagar $",calcular_total(carr_prod))
            

            input("\nPresiona Enter para volver al menú...")


        elif opcion ==5:
            limpiar_pantalla()
            print("------Vaciar el carro de compras------")
            if not carr_prod:
                print("El carrito está vacío.")
            else:    
             op3 = input("Escriba SI para vaciar carrito:")
             vaciar_carrito(carr_prod,op3)
            input("\nPresiona Enter para volver al menú...")


        elif opcion ==0:
           break
 """
main()    