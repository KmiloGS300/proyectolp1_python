#Librerias

import os
import time

#Listas

mensajes=[]
Historial=[]

# Alfabeto con caracteres

A=["\033[31m""  O  ","\033[31m"" O O ","\033[31m""O   O","\033[31m""OOOOO","\033[31m""O   O"]
B=["\033[32m""OOOO ","\033[32m""O   O","\033[32m""OOOO ","\033[32m""O   O","\033[32m""OOOO "]
C=["\033[33m"" OOO ","\033[33m""O   O","\033[33m""O    ","\033[33m""O   O","\033[33m"" OOO "]
D=["\033[36m""OOOO ","\033[36m""O   O","\033[36m""O   O","\033[36m""O   O","\033[36m""OOOO "]
E=["\033[35m""OOOOO","\033[35m""O    ","\033[35m""OOOO ","\033[35m""O    ","\033[35m""OOOOO"]
F=["\033[34m""OOOOO","\033[34m""O    ","\033[34m""OOOO ","\033[34m""O    ","\033[34m""O    "]
G=["\033[31m"" OOO ","\033[31m""O    ","\033[31m""O  OO","\033[31m""O   O","\033[31m"" OOO "]
H=["\033[32m""O   O","\033[32m""O   O","\033[32m""OOOOO","\033[32m""O   O","\033[32m""O   O"]
I=["\033[33m""OOOOO","\033[33m""  O  ","\033[33m""  O  ","\033[33m""  O  ","\033[33m""OOOOO"]
J=["\033[36m""OOOOO","\033[36m""   O ","\033[36m""   O ","\033[36m""O  O ","\033[36m""OOO  "]
K=["\033[35m""O   O","\033[35m""O  O ","\033[35m""OOO  ","\033[35m""O  O ","\033[35m""O   O"]
L=["\033[34m""O    ","\033[34m""O    ","\033[34m""O    ","\033[34m""O    ","\033[34m""OOOOO"]
M=["\033[31m""O   O","\033[31m""OO OO","\033[31m""O O O","\033[31m""O   O","\033[31m""O   O"]
N=["\033[32m""O   O","\033[32m""OO  O","\033[32m""O O O","\033[32m""O  OO","\033[32m""O   O"]
O=["\033[33m"" OOO ","\033[33m""O   O","\033[33m""O   O","\033[33m""O   O","\033[33m"" OOO "]
P=["\033[36m""OOOO ","\033[36m""O   O","\033[36m""OOOO ","\033[36m""O    ","\033[36m""O    "]
Q=["\033[35m"" OOO ","\033[35m""O   O","\033[35m""O O O","\033[35m""OOOOO","\033[35m""   O "]
R=["\033[34m""OOOO ","\033[34m""O   O","\033[34m""OOOO ","\033[34m""O  O ","\033[34m""O   O"]
S=["\033[31m"" OOO ","\033[31m""O    ","\033[31m"" OOO ","\033[31m""    O","\033[31m""OOOO "]
T=["\033[32m""OOOOO","\033[32m""  O  ","\033[32m""  O  ","\033[32m""  O  ","\033[32m""  O  "]
U=["\033[33m""O   O","\033[33m""O   O","\033[33m""O   O","\033[33m""O   O","\033[33m""OOOOO"]
V=["\033[36m""O   O","\033[36m""O   O","\033[36m""O   O","\033[36m"" O O ","\033[36m""  O  "]
W=["\033[35m""O   O","\033[35m""O   O","\033[35m""O O O","\033[35m""OO OO","\033[35m""O   O"]
X=["\033[34m""O   O","\033[34m"" O O ","\033[34m""  O  ","\033[34m"" O O ","\033[34m""O   O"]
Y=["\033[31m""O   O","\033[31m"" O O ","\033[31m""  O  ","\033[31m""  O  ","\033[31m""  O  "]
Z=["\033[32m""OOOOO","\033[32m""   O ","\033[32m""  O  ","\033[32m"" O   ","\033[32m""OOOOO"]


#Funciones 

#Ayuda a imprimir lo que ingreso el usuario en caracteres
def mostrar_banner(mensaje):
    mensaje = mensaje.upper()
    alfabeto = [A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z]
    Numeros={"0":["\033[37m""\033[1m"" 000 ","\033[37m""\033[1m""0   0","\033[37m""\033[1m""0   0","\033[37m""\033[1m""0   0","\033[37m""\033[1m"" 000 "],
             "1":["\033[37m""\033[1m""  1  ","\033[37m""\033[1m"" 11  ","\033[37m""\033[1m""  1  ","\033[37m""\033[1m""  1  ","\033[37m""\033[1m""11111"],
             "2":["\033[37m""\033[1m"" 222 ","\033[37m""\033[1m""2   2","\033[37m""\033[1m""   2 ","\033[37m""\033[1m""  2  ","\033[37m""\033[1m""22222"],
             "3":["\033[37m""\033[1m""3333 ","\033[37m""\033[1m""    3","\033[37m""\033[1m"" 333 ","\033[37m""\033[1m""    3","\033[37m""\033[1m""3333 "],
             "4":["\033[37m""\033[1m""4  4 ","\033[37m""\033[1m""4  4 ","\033[37m""\033[1m""44444","\033[37m""\033[1m""   4 ","\033[37m""\033[1m""   4 "],
             "5":["\033[37m""\033[1m""55555","\033[37m""\033[1m""5    ","\033[37m""\033[1m""5555 ","\033[37m""\033[1m""    5","\033[37m""\033[1m""5555 "],
             "6":["\033[37m""\033[1m"" 666 ","\033[37m""\033[1m""6    ","\033[37m""\033[1m""6666 ","\033[37m""\033[1m""6   6","\033[37m""\033[1m"" 666 "],
             "7":["\033[37m""\033[1m""77777","\033[37m""\033[1m""   7 ","\033[37m""\033[1m""  7  ","\033[37m""\033[1m"" 7   ","\033[37m""\033[1m""7    "],
             "8":["\033[37m""\033[1m"" 888 ","\033[37m""\033[1m""8   8","\033[37m""\033[1m"" 888 ","\033[37m""\033[1m""8   8","\033[37m""\033[1m"" 888 "],
             "9":["\033[37m""\033[1m"" 999 ","\033[37m""\033[1m""9   9","\033[37m""\033[1m"" 999 ","\033[37m""\033[1m""    9","\033[37m""\033[1m""9999 "]}
    arr = []
    for i in range(5):
  
        for letra in mensaje:
            if letra.isalpha(): #la funcion detecta si el valor que ingreso el usiario es una letra
                index = ord(letra) - ord('A')
                letra_banner = alfabeto[index]#se almacena en la variable letra banner, y ya imprime la letra correspondiente formada por caracteres 
                print(letra_banner[i], end=" ")
                arr.append(letra_banner[i])
            elif letra.isdigit():  # el programa detecta que el valor ingresado e sun numero entonces da la orden de que se imprima el numero correspondiente en el diccionario de numeros
                    numero_banner = Numeros[letra]
                    print(numero_banner[i], end=" ")# se almacena el numero con caracteres para proceder a imprimirlo
            else:
                print("      ", end=" ")#si lo ingresado es diferente a una letra o numero se imprime un espacio en blanco

        print()
        time.sleep(0)

 
#Muetra el historial de palabras
def mostrar_historial(mensajes):
    print("Este es el Historial de Palabras")
    print(" ")

    for i in range(len(mensajes)):

        print(f"- {mensajes[i]}") # se imprime todo lo que esta almacenado en la lista mensajes


primera_vez = True

#El usuario ingresa una palabra
def agregar_palabra(mensajes, Historial):
    global primera_vez
    
    print("\033[37m""\033[1m""Ingresa Alguna Palabra ")
    mensaje = input("\033[37m""\033[1m""= ")
    print(" ")
    mensajes.append(mensaje)
    Historial.append(mensaje)
    print("Convirtiendo mensaje...")
    print(" ")
    time.sleep(1)
    print("Mensaje convertido con exito")
    print(" ")
    mostrar_banner(mensaje)
    print(" ")

    #Movimiento del banner
    empuje = " " * 20#se le dice al programa que empiece a imprimir en la pocion 20
    for j in range(20):
        os.system("cls")
        empuje = " " * (20-j)# cuando ya empiece a imprimir se le va a restar una pocicion y sea borrada la anterior con el Os.system("cls")
        
        if primera_vez:
            print(empuje + mensaje)
            primera_vez = False

        else:
            mostrar_banner(empuje + mensaje)

        if j > 1:
            time.sleep(0.5) #cuando j sea mayor a uno se reducira la velocidad para poder ver el movimiento del banner

#Menú

while True:
    
    print(" ")
    print("\033[36m""\033[1m""OPCIONES")
    print(" ")

    print("\033[37m""\033[1m""1. Producto y Precio")
    print("\033[37m""\033[1m""2. ")
    print("\033[37m""\033[1m""3. Salir ")
    print(" ")

    print("\033[36m""\033[1m""Escoja una Opcion")
    opcion=input("\033[36m""\033[1m""=  ")
    os.system("cls")
    


    if opcion=="1":
        agregar_palabra(mensajes,Historial)

    elif opcion=="2":
        mostrar_historial(Historial)

    elif opcion=="3":
        os.system("cls")
        
        print("\033[36m""\033[1m""Saliste del Banner")
        
        break
        

    else:
        print("OPCION NO VALIDA!")