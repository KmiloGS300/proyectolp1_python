from tkinter import * 
from tkinter import ttk
import pandas as pd
#pip install pandastable, python3 -m pip install pandastable
from pandastable import Table, TableModel

#listas globales
nombre,apellido,edad,correo,telefono=[],[],[],[],[]

def agregar_datos():
    global nombre,apellido,edad,correo,telefono
    nombre.append(txtNombre.get())
    apellido.append(txtApellido.get())
    edad.append(txtEdad.get())
    correo.append(txtCorreo.get())
    telefono.append(txtTelefono.get())
    limpiar()

def limpiar():
    txtNombre.delete(0,END)
    txtApellido.delete(0,END)
    txtEdad.delete(0,END)
    txtCorreo.delete(0,END)
    txtTelefono.delete(0,END)

def mostrar_datos():
    tabla.delete(*tabla.get_children())
    global nombre,apellido,edad,correo,telefono  
    for i in range(len(nombre)):
        tabla.insert('',END,text=nombre[i], values=(apellido[i],edad[i],correo[i],telefono[i]))
    
ventana= Tk()
ventana.title('Guardar datos en excel')
ventana.geometry('800x600')
ventana.resizable(1,1)

frame1= Frame(ventana,bg='gray15')
frame1.grid(row=0,column=0,sticky='nsew')

frame2= Frame(ventana,bg='gray16')
frame2.grid(row=0,column=1,sticky='nsew')

lblNombre= Label(frame1, text='Nombre', width=10)
lblNombre.grid(row=0,column=0,padx=10, pady=20)
txtNombre=Entry(frame1, width=20, font=('Arial',12))
txtNombre.grid(row=0,column=1)

lblApellido= Label(frame1, text='Apellido', width=10)
lblApellido.grid(row=1,column=0,padx=10, pady=20)
txtApellido=Entry(frame1, width=20, font=('Arial',12))
txtApellido.grid(row=1,column=1)

lblEdad= Label(frame1, text='Edad', width=10)
lblEdad.grid(row=2,column=0,padx=10, pady=20)
txtEdad=Entry(frame1, width=20, font=('Arial',12))
txtEdad.grid(row=2,column=1)

lblCorreo= Label(frame1, text='Correo', width=10)
lblCorreo.grid(row=3,column=0,padx=10, pady=20)
txtCorreo=Entry(frame1, width=20, font=('Arial',12))
txtCorreo.grid(row=3,column=1)

lblTelefono= Label(frame1, text='Telefono', width=10)
lblTelefono.grid(row=4,column=0,padx=10, pady=20)
txtTelefono=Entry(frame1, width=20, font=('Arial',12))
txtTelefono.grid(row=4,column=1)

btnAgregar=Button(frame1,width=20,font=('Arial',12,'bold'),text='Agregar', 
                  bg='orange',bd=5,command=agregar_datos)
btnAgregar.grid(row=5,columnspan=2,padx=10,pady=20)

#Elementos del Frame2
lblArchivo=Label(frame2,text='Contenido',width=25,bg='gray16',
                 font=('Arial',12,'bold'),fg='white')
lblArchivo.grid(row=0,column=0,padx=10,pady=10)

tabla = ttk.Treeview(frame2,columns=( 'Apellidos','Edad','Correo','Telefono'))
tabla.grid(row=1,column=0)

tabla.column('#0',width=80)
tabla.column('Apellidos',width=80,anchor='center')
tabla.column('Edad',width=80,anchor='center')
tabla.column('Correo',width=80,anchor='center')
tabla.column('Telefono',width=80,anchor='center')

tabla.heading('#0', text='Nombres', anchor='center')
tabla.heading('Apellidos', text='Apellidos', anchor='center')
tabla.heading('Edad', text='Edad', anchor='center')
tabla.heading('Correo', text='Correo', anchor='center')
tabla.heading('Telefono', text='Telefono', anchor='center')

btnGuardar=Button(frame2,width=20,font=('Arial',12,'bold'),text='Mostrar',bg='green2',bd=5,command=mostrar_datos)
btnGuardar.grid(row=2,column=0,padx=10,pady=10)



ventana.mainloop()
