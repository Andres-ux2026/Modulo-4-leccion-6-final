# Modulo-4-ejercicio-final
Ejercicio Práctico - Desarrollo Portafolio Módulo 4

🛒 Sistema de E-commerce (Consola)
Este es un sistema de gestión de ventas desarrollado en Python en Programación Orientada a Objetos (POO). Permite administrar un inventario de productos y realizar simulaciones de compra mediante una interfaz de línea de comandos.

📝 Descripción
El programa gestiona de forma persistente un catálogo de productos a través de archivos de texto. Cuenta con dos perfiles de usuario que interactúan con el sistema de manera distinta: el Administrador, encargado del inventario, y el Cliente, encargado del proceso de compra.

Características principales:
Persistencia de datos: Los productos se guardan en catalogo.txt y las ventas en ordenes.txt.

Gestión de Stock: El sistema descuenta productos automáticamente al agregarlos al carro y permite devolverlos si la compra no se concreta.

Validaciones: Control de errores para entradas no numéricas y stock insuficiente.

🚀 Cómo usar el programa
1. Inicio
Ejecuta el archivo principal. Se desplegará un menú para elegir tu rol:

Opción 1: Administrador.

Opción 2: Cliente.

Opción 3: Salir del sistema.

2. Panel de Administración
Si ingresas como Administrador, puedes:

Ver Catálogo: Listado completo de productos actuales.

Agregar: Crear productos nuevos (ID, nombre, categoría, precio y stock).

Actualizar: Modificar los datos de un producto existente buscando por su ID.

Eliminar: Quitar productos del inventario permanentemente.

3. Panel de Cliente
Si ingresas como Cliente, puedes:

Buscar: Filtrar productos por nombre o categoría.

Añadir al carro: Ingresa el ID y la cantidad deseada. El sistema validará si hay stock disponible.

Ver carro: Revisa el subtotal por producto y el total general de tu compra.

Confirmar compra: Al presionar Y, se genera una orden de compra detallada en el archivo ordenes.txt y se limpia el carrito.

📂 Estructura de Archivos
catalogo.txt: Base de datos de los productos.

ordenes.txt: Registro histórico de todas las compras realizadas (tickets).

clases/: Carpeta que contiene los módulos de lógica (producto.py, catalogo.py, usuario.py, carrito.py).

🛠️ Requisitos
Python 3.x instalado.

Ejecutar el programa desde una terminal para visualizar correctamente la limpieza de pantalla.