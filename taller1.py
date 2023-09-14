from tkinter import *
from tkinter import messagebox

def sumar():
    num1 = int(txtnum1.get())
    num2 = int(txtnum2.get())

    suma = num1+num2

    return total.set(suma)


ventana = Tk()
ventana.title("Formulario Principal") # titulo del formulario
ventana.geometry("500x500") # dimensiones
ventana.resizable(False,False)#bloqueo tamaño de la ventana
ventana.config(bg="#808080")#colr del fondo

#manejo de controles
lbltit = Label(ventana, text="SUMA", bg="#808080", fg="black")#crea el mensage que se va a mostrar en la etiqueta y con su color de letra y fondo
lbltit.pack(padx=5, pady=3, ipadx=5, ipady=5, fill=X)#se empaqueta para darle el tamaño y posicionarse en la ventana

#Etiqueta Num 1
lblnum1 = Label(ventana, text="Numero 1", bg="#808080", fg="black")#crea el mensage que se va a mostrar en la etiqueta y con su color de letra y fondo
lblnum1.pack(padx=5, pady=3, ipadx=5, ipady=5, fill=X)#se empaqueta para darle el tamaño y posicionarse en la ventana
txtnum1 = Entry(ventana, bg="#4F4F4F", fg="white")#se crea el cuadro de texto, y con sus colores de fondo y el color de la letra que se ingrese
txtnum1.pack(padx=70, pady=3, ipadx=70, ipady=5, fill=X)#se empaqueta para darle el tamaño y posicionarlo en la ventana

#Etiqueta Num 2
lblnum2 = Label(ventana, text="Numero 2", bg="#808080", fg="black")#crea el mensage que se va a mostrar en la etiqueta y con su color de letra y fondo
lblnum2.pack(padx=5, pady=3, ipadx=5, ipady=5, fill=X)#se empaqueta para darle el tamaño y posicionarse en la ventana
txtnum2 = Entry(ventana, bg="#4F4F4F", fg="white")#se crea el cuadro de texto, y con sus colores de fondo y el color de la letra que se ingrese
txtnum2.pack(padx=70, pady=3, ipadx=70, ipady=5, fill=X)#se empaqueta para darle el tamaño y posicionarlo en la ventana

#Boton
btnsumar = Button(ventana, text="Sumar", bg="#228B22", fg="black", command=sumar)#se crea el cuadro de texto, y con sus colores de fondo y el color de la letra que se ingrese
btnsumar.pack(padx=150, pady=3, ipadx=150, ipady=5, fill=X)#se empaqueta para darle el tamaño y posicionarlo en la ventana

#Etiqueta Resultado
lblresult=Label(ventana, text="Resultado de la Suma", bg="#808080", fg="black")#crea el mensage que se va a mostrar en la etiqueta y con su color de letra y fondo
lblresult.pack(padx=5, pady=3, ipadx=5, ipady=5, fill=X)#se empaqueta para darle el tamaño y posicionarse en la ventana

total = StringVar()

txtresult = Entry(ventana, bg="#808080", fg="black", state="disabled", textvariable=total)#se crea el cuadro de texto, y con sus colores de fondo y el color de la letra que se ingrese
txtresult.pack(padx=160, pady=3, ipadx=160, ipady=5, fill=X)#se empaqueta para darle el tamaño y posicionarlo en la ventana

ventana.mainloop()