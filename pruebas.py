from tkinter import * 
from tkinter import ttk
from tkinter import messagebox

#listas globales
Matricula = []
Propietario = []
telefono = []
TipoVehiculo = []

#Se inicializan los contadores para cada tipo de vehiculo
espacios_coches = 10
espacios_motocicletas = 30

#funciones de el programa
def agregar_vehiculo():
    global Matricula, Propietario, telefono, TipoVehiculo, espacios_coches, espacios_motocicletas
    tipo_vehiculo = comboTipo.get()
    if (tipo_vehiculo == "Coche" and espacios_coches > 0) or (tipo_vehiculo == "Motocicleta" and espacios_motocicletas > 0):
        Matricula.append(txtMatricula.get().upper())
        Propietario.append(txtPropietario.get())
        telefono.append(txtTelefono.get())
        TipoVehiculo.append(tipo_vehiculo)

        if tipo_vehiculo == "Coche":
            espacios_coches -= 1
        else:
            espacios_motocicletas -= 1

        messagebox.showinfo("Ingresado", f"Se ha ingresado correctamente el {tipo_vehiculo.lower()}...")
    else:
        messagebox.showinfo("No hay espacio", f"No hay suficientes espacios disponibles para {tipo_vehiculo.lower()}")

def sacar_vehiculo():
    global Matricula, Propietario, telefono, TipoVehiculo, espacios_coches, espacios_motocicletas
    matricula_a_sacar = txtMatricula.get()
    indice = None
    for i, matricula in enumerate(Matricula):
        if matricula == matricula_a_sacar:
            indice = i
            break
    if indice is not None:
        del Matricula[indice]
        del Propietario[indice]
        del telefono[indice]
        tipo_vehiculo = TipoVehiculo[indice]
        del TipoVehiculo[indice]

        if tipo_vehiculo == "Coche":
            espacios_coches += 1
        else:
            espacios_motocicletas += 1

    messagebox.showinfo("Sacado", "Se ha sacado con éxito el vehículo...")
    limpiar()

def limpiar():
    comboTipo.set("")
    txtMatricula.delete(0,END)
    txtPropietario.delete(0,END)
    txtTelefono.delete(0,END)

def mostrar_datos():
    tabla.delete(*tabla.get_children())
    global Matricula, Propietario, telefono, TipoVehiculo
    for i in range(len(Matricula)):
        tabla.insert('', END, text=Matricula[i], values=(Propietario[i], telefono[i], TipoVehiculo[i]))


#Funciones de las opciones del menú
def disponibilidad():
    global espacios_coches, espacios_motocicletas
    mensaje = f"Disponibilidad de espacios:\n\n\nCoches: {espacios_coches}/10\n\nMotocicletas: {espacios_motocicletas}/30"
    messagebox.showinfo("Disponibilidad", mensaje)

def salir():
    exit = messagebox.askokcancel("Salir", " Realmente Desea a Salir de la Aplicacion?")
    if(exit):
        ventana.destroy()

#configuracion de la interfaz del programa
ventana= Tk()
ventana.title('Parqueadero')
ventana.geometry('600x400')
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

lblTipo = Label(frame1, text='Tipo', width=10)
lblTipo.grid(row=3, column=0, padx=10, pady=20)
comboTipo = ttk.Combobox(frame1, values=["Coche", "Motocicleta"], width=17, font=('Arial',12))
comboTipo.grid(row=3, column=1)

btnAgregar=Button(frame1,width=20,font=('Arial',12,'bold'),text='Ingresar vehiculo', 
                  bg='orange',bd=5,command=agregar_vehiculo)
btnAgregar.grid(row=5,columnspan=2,padx=10,pady=20)

btnSacar = Button(frame1, width=20, font=('Arial', 12, 'bold'), text='Sacar Vehiculo', 
                  bg='red', bd=5, command=sacar_vehiculo)
btnSacar.grid(row=6, columnspan=2, padx=10, pady=20)

lblArchivo=Label(frame2,text='Vehiculos Ingresados',width=25,bg='gray16',
                 font=('Arial',12,'bold'),fg='white')
lblArchivo.grid(row=0,column=0,padx=10,pady=10)

tabla = ttk.Treeview(frame2, columns=('Propietario', 'Telefono', 'TipoVehiculo'))
tabla.grid(row=1, column=0)

tabla.column('#0', width=80)
tabla.column('Propietario', width=80, anchor='center')
tabla.column('Telefono', width=80, anchor='center')
tabla.column('TipoVehiculo', width=80, anchor='center')

tabla.heading('#0', text='Matricula', anchor='center')
tabla.heading('Propietario', text='Propietario', anchor='center')
tabla.heading('Telefono', text='Telefono', anchor='center')
tabla.heading('TipoVehiculo', text='Tipo', anchor='center')

btnGuardar=Button(frame2,width=20,font=('Arial',12,'bold'),text='Mostrar Info',bg='green2',bd=5,command=mostrar_datos)
btnGuardar.grid(row=2,column=0,padx=10,pady=10)

#Barra Menu
barraMenu = Menu(ventana)
ventana.config(menu = barraMenu, bg= "#A9A9A9", width = 400, height = 400)

#Opciones Menu
parqueaderoMenu = Menu(barraMenu, tearoff=False)
parqueaderoMenu.add_command(label="Disponibilidad", command=disponibilidad)
parqueaderoMenu.add_command(label="Recaudo", command="recaudo")
parqueaderoMenu.add_separator()
parqueaderoMenu.add_command(label="Salir", command=salir)

barraMenu.add_cascade(label = "Menu de Admin", menu = parqueaderoMenu)

ventana.mainloop()