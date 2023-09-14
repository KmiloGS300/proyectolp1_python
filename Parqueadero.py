from tkinter import * 
from tkinter import ttk
import pandas as pd
#pip install pandastable, python3 -m pip install pandastable
from pandastable import Table, TableModel
from tkinter import messagebox

#listas globales
Matricula = []
Propietario = []
telefono = []

def agregar_vehiculo():
    global Matricula, Propietario, telefono
    Matricula.append(txtMatricula.get().upper())
    Propietario.append(txtPropietario.get())
    telefono.append(txtTelefono.get())
    messagebox.showinfo
    limpiar()

def sacar_vehiculo():
    global Matricula, Propietario, telefono

    # Obtén la matrícula del vehículo que se va a sacar
    matricula_a_sacar = txtMatricula.get()

    # Encuentra el índice del vehículo con esa matrícula
    indice = None
    for i, matricula in enumerate(Matricula):
        if matricula == matricula_a_sacar:
            indice = i
            break

    # Si se encontró la matrícula, elimina el vehículo
    if indice is not None:
        del Matricula[indice]
        del Propietario[indice]
        del telefono[indice]

    # Limpiar los campos de entrada
    limpiar()

def limpiar():
    txtMatricula.delete(0,END)
    txtPropietario.delete(0,END)
    txtTelefono.delete(0,END)

def mostrar_datos():
    tabla.delete(*tabla.get_children())
    global Matricula,Propietario,telefono  
    for i in range(len(Matricula)):
        tabla.insert('',END,text=Matricula[i], values=(Propietario[i],telefono[i]))
    
ventana= Tk()
ventana.title('Parqueadero')
ventana.geometry('550x350')
ventana.resizable(1,1)

frame1= Frame(ventana,bg='gray15')
frame1.grid(row=0,column=0,sticky='nsew')

frame2= Frame(ventana,bg='gray16')
frame2.grid(row=0,column=1,sticky='nsew')

lblMatricula= Label(frame1, text='Matricula', width=10)
lblMatricula.grid(row=0,column=0,padx=10, pady=20)
txtMatricula=Entry(frame1, width=20, font=('Arial',12))
txtMatricula.grid(row=0,column=1)

lblPropietario= Label(frame1, text='Propietario', width=10)
lblPropietario.grid(row=1,column=0,padx=10, pady=20)
txtPropietario=Entry(frame1, width=20, font=('Arial',12))
txtPropietario.grid(row=1,column=1)

lblTelefono= Label(frame1, text='Telefono', width=10)
lblTelefono.grid(row=2,column=0,padx=10, pady=20)
txtTelefono=Entry(frame1, width=20, font=('Arial',12))
txtTelefono.grid(row=2,column=1)

btnAgregar=Button(frame1,width=20,font=('Arial',12,'bold'),text='Agregar', 
                  bg='orange',bd=5,command=agregar_vehiculo)
btnAgregar.grid(row=5,columnspan=2,padx=10,pady=20)

btnSacar = Button(frame1, width=20, font=('Arial', 12, 'bold'), text='Sacar Vehiculo', 
                  bg='red', bd=5, command=sacar_vehiculo)
btnSacar.grid(row=6, columnspan=2, padx=10, pady=20)

#Elementos del Frame2
lblArchivo=Label(frame2,text='Contenido',width=25,bg='gray16',
                 font=('Arial',12,'bold'),fg='white')
lblArchivo.grid(row=0,column=0,padx=10,pady=10)

tabla = ttk.Treeview(frame2,columns=('Propietario', 'Telefono'))
tabla.grid(row=1,column=0)

tabla.column('#0',width=80)
tabla.column('Propietario',width=80,anchor='center')
tabla.column('Telefono',width=80,anchor='center')

tabla.heading('#0', text='Matricula', anchor='center')
tabla.heading('Propietario', text='Propietario', anchor='center')
tabla.heading('Telefono', text='Telefono', anchor='center')

btnGuardar=Button(frame2,width=20,font=('Arial',12,'bold'),text='Mostrar',bg='green2',bd=5,command=mostrar_datos)
btnGuardar.grid(row=2,column=0,padx=10,pady=10)



ventana.mainloop()
