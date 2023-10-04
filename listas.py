import os

Nombre_producto = ["Doritos", "Margarita - Limon", "margarita - Pollo", "Trocipollos"]
Precio_producto = [2000,2500,2500,1000]


def Mostrar_productos(Nombre_producto, Precio_producto):
    print(Nombre_producto)
    print("_____________________________________________________________________________________________________________________________________________________________________________")
    print(Precio_producto)


def Adicionar_producto(Nombre_producto, Precio_producto):
    producto = input("Nombre del producto = ")
    precio = input("Precio del producto = ")
    Nombre_producto.append(producto)
    Precio_producto.append(precio)
    print("se agrego el producto")


def Adicionar_varios():
    while True:
        nombre = input("Ingrese el nombre del producto (o presione Enter para terminar): ")
        if not nombre:
            break
        try:
            precio = float(input("Ingrese el precio del producto: "))
        except ValueError:
            print("¡Error! Por favor, ingrese un número válido.")
            continue

        Nombre_producto.append(nombre)
        Precio_producto.append(precio)

    print("Lista de productos:")
    for i in range(len(Nombre_producto)):
        print(f"Nombre: {Nombre_producto[i]}, Precio: {Precio_producto[i]}")


def Eliminar_producto(Nombre_producto, Precio_producto):
    print(Nombre_producto)
    print("_____________________________________________________________________________________________________________________________________________________________________________")
    print(Precio_producto)
    print (" ")
    
    producto = input("Que producto quiere eliminar? = ")
    pos_producto = Nombre_producto.index(producto)
    print(pos_producto)

    Nombre_producto.remove(producto)
    print(Nombre_producto)

    Precio_producto.pop(pos_producto)
    print(Precio_producto)


def Adicionar_producto_posicion(nombre_producto, precio_producto, posicion, nombre_nuevo, precio_nuevo):
        nombre_producto.insert(posicion, nombre_nuevo)
        precio_producto.insert(posicion, precio_nuevo)
        print(f"Producto '{nombre_nuevo}' con precio {precio_nuevo} agregado en la posición {posicion}.")



while True:
    
    print(" ")
    print("\033[36m""\033[1m""OPCIONES")
    print(" ")

    print("\033[37m""\033[1m""1. Mostrar Productos con Precios")
    print("\033[37m""\033[1m""2. Adicionar un producto")
    print("\033[37m""\033[1m""3. Adicionar Varios Productos")
    print("\033[37m""\033[1m""4. Eliminar un Producto")
    print("\033[37m""\033[1m""5. ")
    print(" ")

    print("\033[36m""\033[1m""Escoja una Opcion")
    opcion=input("\033[36m""\033[1m""=  ")
    os.system("cls")
    

    if opcion=="1":
        Mostrar_productos(Nombre_producto, Precio_producto)

    elif opcion=="2":
        Adicionar_producto(Nombre_producto, Precio_producto)

    elif opcion=="3":
        Adicionar_varios(Nombre_producto, Precio_producto)

    elif opcion=="4":
        Eliminar_producto(Nombre_producto, Precio_producto)

    elif opcion=="5":
        Adicionar_producto(Nombre_producto, Precio_producto)

        
        print("\033[36m""\033[1m""Saliste del Banner")
        
        break
        

    else:
        print("OPCION NO VALIDA!")