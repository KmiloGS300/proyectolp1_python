import os

#Listas Principales
Nombre_producto = ["Doritos", "Lays", "Trocipollos", "Choclitos"]
Precio_producto = [2000,2500,1400,1000]

#Para cuando desea aregar mas d e1 producto
Nuevos_productos = []
Nuevos_precios = []

#Listas para la copia del inventarii
copia_productos = []
copia_precios = []


def Comprar_producto(Nombre_producto, Precio_producto):
    print(Nombre_producto)
    print("_____________________________________________________________________________________________________________________________________________________________________________")
    print(Precio_producto)
    print(" ")
    
    productos_seleccionados = []  # Lista para almacenar los precios de los productos seleccionados
    
    while True:
        print(" ")
        producto = input("\033[37m""Qué producto quiere Comprar? "+"\033[31m"+"\n(ingrese 1 para finalizar la compra) = ")
        
        if producto == '1':
            break
        
        if producto in Nombre_producto:
            pos_producto = Nombre_producto.index(producto)
            precio = Precio_producto[pos_producto]
            print(" ")
            print(f"El precio del producto {producto} es: ${precio}")
            
            productos_seleccionados.append(precio)  # Agregar el precio del producto seleccionado
            
            Nombre_producto.pop(pos_producto)
            Precio_producto.pop(pos_producto)
        else:
            print("Producto no encontrado")
    
    print(" ")
    total_pagar = sum(productos_seleccionados)
    print(f"Total a pagar: {total_pagar}")


def Adicionar_producto(Nombre_producto, Precio_producto):
    producto = input("Nombre del producto = ")
    precio = input("Precio del producto = ")
    Nombre_producto.append(producto)
    Precio_producto.append(precio)
    print("se agrego el producto")


def Adicionar_varios(Nombre_producto, Precio_producto):
    while True:
        producto_nuevo = input("\033[37m""Ingrese un producto para agregar a la vitrina "+"\033[31m"+"\n(Ingrese 1 para salir) = ")
        if producto_nuevo == "1":
            break
        else:
            precio_nuevo = input(f"Ingrese el precio para {producto_nuevo}: ")
            Nuevos_productos.append(producto_nuevo)
            Nuevos_precios.append(precio_nuevo)
    
    print(" ")
    opcion = input(f"Ingrese 1 si desea añadir todos estos productos: {Nuevos_productos} = ")
    
    if opcion == "1":
        Nombre_producto.extend(Nuevos_productos)
        Precio_producto.extend(Nuevos_precios)

    print(Nombre_producto)
    print(Precio_producto)


def Mostrar_productos(Nombre_producto, Precio_producto):
    print(Nombre_producto)
    print("_____________________________________________________________________________________________________________________________________________________________________________")
    print(Precio_producto)


def Adicionar_producto_posicion(Nombre_producto, Precio_producto, posicion, nombre_nuevo, precio_nuevo):
        Nombre_producto.insert(posicion, nombre_nuevo)
        Precio_producto.insert(posicion, precio_nuevo)
        print(f"Producto '{nombre_nuevo}' con precio {precio_nuevo} agregado en la posición {posicion}.")


def Invertir_vitrina(Nombre_producto, Precio_producto):
    print(Precio_producto)
    print(Nombre_producto)

    Precio_producto.reverse()
    Nombre_producto.reverse()
    print("_____________________________________________________________________________________________________________________________________________________________________________")
    print(Precio_producto)
    print(Nombre_producto)


def Copia_productos(Nombre_producto, Precio_producto):
    copia_productos = Nombre_producto.copy()
    print(copia_productos)

    copia_precios = Precio_producto.copy()
    print(copia_precios)


def Ordenar_productos(Nombre_producto, Precio_producto, copia_productos, copia_precios):  
    copia_productos.sort()
    print(Nombre_producto)

    copia_precios.sort()
    print(Precio_producto)


def Eliminar_copia(Nombre_producto, Precio_producto, copia_productos, copia_precios):
    copia_productos.clear()
    print(copia_productos)
    print(Nombre_producto)
    copia_precios.clear()
    print(copia_precios)
    print(Precio_producto)

    print("Se elimino toda la copia del inventario")


def Stock_productos(Nombre_producto):
    print(Nombre_producto)

    producto = input("Ingrese el producto el cual desa consultar el stock = ")
    print(" ")
    frecuencia=Nombre_producto.count(producto)
    print(frecuencia)


#Menu de opciones para la tienda
while True:
    
    print(" ")
    print("\033[36m""\033[1m""OPCIONES TIENDITA DE BARRIO")
    print(" ")

    print("\033[31m""\033[1m""1. COMPRAR UN PRODUCTO")
    print("\033[37m""\033[1m""2. Adicionar un producto")
    print("\033[37m""\033[1m""3. Adicionar Varios Productos")
    print("\033[37m""\033[1m""4. Mostrar Productos con Precios")
    print("\033[37m""\033[1m""5. Invertir Vitrina")
    print("\033[37m""\033[1m""6. Hacer Una Copia Del Inventario")
    print("\033[37m""\033[1m""7. Ordenar Productos")
    print("\033[37m""\033[1m""8. Eliminar Copia Del Inventario")
    print("\033[37m""\033[1m""9. Stock de Productos")
    print("\033[37m""\033[1m""10. Salir")
    print(" ")

    print("\033[36m""\033[1m""Escoja una Opcion")
    opcion=input("\033[36m""\033[1m""=  ")
    
    

    if opcion=="1":
        Comprar_producto(Nombre_producto, Precio_producto)

    elif opcion=="2":
        Adicionar_producto(Nombre_producto, Precio_producto)

    elif opcion=="3":
        Adicionar_varios(Nombre_producto, Precio_producto)

    elif opcion=="4":
        Mostrar_productos(Nombre_producto, Precio_producto)

    elif opcion=="5":
        Invertir_vitrina(Nombre_producto, Precio_producto)

    elif opcion=="6":
        Copia_productos(Nombre_producto, Precio_producto)

    elif opcion=="7":
        Ordenar_productos(copia_productos, copia_precios)

    elif opcion=="8":
        Eliminar_copia(Nombre_producto, Precio_producto, copia_productos, copia_precios)

    elif opcion=="9":
        Stock_productos(Nombre_producto)

    elif opcion=="10":
        os.system("cls")

        print("\033[36m""\033[1m""Saliste del Banner")
        
        break
        

    else:
        print("OPCION NO VALIDA!")