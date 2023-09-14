from tkinter import *
from tkinter import messagebox

def sumar():
    num1 = int(txtnum1.get())
    num2 = int(txtnum2.get())
    suma = num1 + num2
    total.set(suma)

def restar():
    num1 = int(txtnum1.get())
    num2 = int(txtnum2.get())
    resta = num1 - num2
    total.set(resta)

def multiplicar():
    num1 = int(txtnum1.get())
    num2 = int(txtnum2.get())
    producto = num1 * num2
    total.set(producto)

def dividir():
    num1 = int(txtnum1.get())
    num2 = int(txtnum2.get())
    if num2 != 0:
        division = num1 / num2
        total.set(division)
    else:
        messagebox.showerror("No se puede dividir entre 0")

def clear():
    

ventana = Tk()
ventana.title("Calculadora Básica")
ventana.geometry("320x300")
ventana.resizable(False, False)
ventana.config(bg="#808080")

# Etiqueta y cuadro de texto para Numero 1
lblnum1 = Label(ventana, text="Numero 1", bg="#808080", fg="black")
lblnum1.grid(row=1, column=0, padx=10, pady=10)
txtnum1 = Entry(ventana, bg="#4F4F4F", fg="white")
txtnum1.grid(row=1, column=1, padx=10, pady=10)

# Etiqueta y cuadro de texto para Numero 2
lblnum2 = Label(ventana, text="Numero 2", bg="#808080", fg="black")
lblnum2.grid(row=2, column=0, padx=10, pady=10)
txtnum2 = Entry(ventana, bg="#4F4F4F", fg="white")
txtnum2.grid(row=2, column=1, padx=10, pady=10)

# Botones para operaciones
btnsumar = Button(ventana, text="Suma  +", width= 15, height= 2, bg="#00FA9A", fg="#0a0a0a", command=sumar)
btnsumar.grid(row=3, column=0, padx=10, pady=10)

btnrestar = Button(ventana, text="Resta  -", width= 15, height= 2, bg="#00FA9A", fg="#0a0a0a", command=restar)
btnrestar.grid(row=3, column=1, padx=10, pady=10)

btnmultiplicar = Button(ventana, text="Multiplicacion  *", width= 15, height= 2, bg="#00FA9A", fg="#0a0a0a", command=multiplicar)
btnmultiplicar.grid(row=4, column=0, padx=10, pady=10)

btndividir = Button(ventana, text="Division  /", width= 15, height= 2, bg="#00FA9A", fg="#0a0a0a", command=dividir)
btndividir.grid(row=4, column=1, padx=10, pady=10)

# Botón Clear
btnclear = Button(ventana, text="CLEAR / BORRAR", bg="#DC143C", fg="white", command=clear)
btnclear.grid(row=5, column=1, padx=10, pady=10)

total = StringVar()

# Etiqueta y cuadro de texto para el resultado
lblresult=Label(ventana, text="Resultado de la Operacion", bg="#808080", fg="black")
txtresult = Entry(ventana, bg="#808080", fg="black", state="disabled", textvariable=total)

lblresult.grid(row=6, column=0, padx=10, pady=10)
txtresult.grid(row=6, column=1, padx=10, pady=10)

ventana.mainloop()






