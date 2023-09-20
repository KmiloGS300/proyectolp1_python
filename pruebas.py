# Importación de módulos necesarios
from tkinter import * 
from tkinter import ttk
import pandas as pd
from pandastable import Table, TableModel
from tkinter import messagebox

# Listas globales para almacenar información de vehículos
Matricula = []
Propietario = []
telefono = []
TipoVehiculo = []

# Inicialización de contadores para tipos de vehículos y recaudo total
espacios_coches = 5
espacios_motocicletas = 10
total_recaudo = 0

# Función para calcular el cobro según el tipo de vehículo
def calcular_cobro(tipo_vehiculo):#Esta función calcula el cobro según el tipo de vehículo ingresado. 
    tarifas = {"Coche": 2500, "Motocicleta": 1500}
    return tarifas.get(tipo_vehiculo, 0)#Si el tipo de vehículo no se encuentra en el diccionario, devuelve 0

# Función para calcular el recaudo total
def calcular_recaudo():#Esta función calcula el recaudo total sumando los cobros de todos los vehículos ingresados en la lista Matricula y actualiza la variable global 
    global Matricula, TipoVehiculo, total_recaudo
    total_recaudo = 0
    for i in range(len(Matricula)):
        tipo_vehiculo = TipoVehiculo[i]
        cobro = calcular_cobro(tipo_vehiculo)
        total_recaudo += cobro #muestra el total a cobrar en recaudo

# Función para agregar un vehículo
def agregar_vehiculo():#Esta función se llama cuando se presiona el botón "Ingresar vehículo". 
    global Matricula, Propietario, telefono, TipoVehiculo, espacios_coches, espacios_motocicletas
    matricula = txtMatricula.get().upper()
    tipo_vehiculo = comboTipo.get()
    if (tipo_vehiculo == "Coche" and espacios_coches > 0) or (tipo_vehiculo == "Motocicleta" and espacios_motocicletas > 0):
        Matricula.append(matricula)#agregar matricula
        Propietario.append(txtPropietario.get())#agrega propietario
        telefono.append(txtTelefono.get())#agrega telefono
        TipoVehiculo.append(tipo_vehiculo)#agrega el tipo de vehiculo

        if tipo_vehiculo == "Coche":
            espacios_coches -= 1#muetsra si es vehiculo carro
        else:
            espacios_motocicletas -= 1#muestra si es vehiculo motocicleta

        messagebox.showinfo("Ingresado", f"Se ha ingresado correctamente el {tipo_vehiculo.lower()}.")
    else:
        messagebox.showinfo("No hay espacio", f"No hay suficientes espacios disponibles para {tipo_vehiculo.lower()}")

    limpiar()

# Función para sacar un vehículo
def sacar_vehiculo():
    global Matricula, Propietario, telefono, TipoVehiculo, espacios_coches, espacios_motocicletas, total_recaudo
    matricula_a_sacar = txtMatricula.get().upper()
    if matricula_a_sacar in Matricula:
        indice = Matricula.index(matricula_a_sacar)
        tipo_vehiculo = TipoVehiculo[indice]#Esta función se llama cuando se presiona el botón "Sacar Vehículo". Primero, obtiene la matrícula ingresada en el campo de entrada. Luego, verifica si la matrícula se encuentra en la lista

        del Matricula[indice]#Si se encuentra, elimina los detalles del vehículo de las listas correspondientes, actualiza el contador de espacios disponibles y calcula el cobro utilizando la función 
        del Propietario[indice]
        del telefono[indice]
        del TipoVehiculo[indice]

        if tipo_vehiculo == "Coche":
            espacios_coches += 1
        else:
            espacios_motocicletas += 1

        cobro = calcular_cobro(tipo_vehiculo)
        total_recaudo += cobro#Luego, muestra un mensaje con el resultado de la operación. Si la matrícula no se encuentra, muestra un mensaje indicando que no se encontró la matrícula. Finalmente, llama a la función
        messagebox.showinfo("Sacado", f"Se ha sacado con éxito el vehículo. Cobro: {cobro} Pesos")
    else:
        messagebox.showinfo("Matrícula no encontrada", "La matrícula no fue encontrada en la lista de vehículos")

    limpiar()#para borrar los campos de entrada.

# Función para limpiar los campos de entrada
def limpiar():#Esta función se utiliza para borrar los campos de entrada y restablecer el campo de selección de tipo de vehículo a su estado inicial.
    comboTipo.set("")
    txtMatricula.delete(0, END)#borra matricula
    txtPropietario.delete(0, END)#borra propietario
    txtTelefono.delete(0, END)#borra telefono

# Función para mostrar los datos de los vehículos en la tabla
def mostrar_datos():#Esta función se llama cuando se presiona el botón "Mostrar Info". Borra los datos existentes en la tabla y muestra los datos de los vehículos almacenados en las listas Matricula, Propietario, telefono, TipoVehiculo en la tabla.
    tabla.delete(*tabla.get_children())
    global Matricula, Propietario, telefono, TipoVehiculo
    for i in range(len(Matricula)):
        tabla.insert('', END, text=Matricula[i], values=(Propietario[i], telefono[i], TipoVehiculo[i]))

# Función para guardar los datos en un archivo CSV
def guardar_datos():#Esta función guarda los datos de los vehículos en un archivo CSV llamado "registros_vehiculos.csv" utilizando la biblioteca Pandas.
    global Matricula, Propietario, telefono, TipoVehiculo
    data = {'Matricula': Matricula, 'Propietario': Propietario, 'Telefono': telefono, 'TipoVehiculo': TipoVehiculo}
    df = pd.DataFrame(data)#se verifica informacion guardada 
    df.to_csv('registros_vehiculos.csv', index=False)
    messagebox.showinfo("Guardado", "Los registros de vehículos han sido guardados correctamente en registros_vehiculos.csv")#muetsra recuadro indicando la informacion q fue guardada

# Función para cargar los datos desde un archivo CSV (si existe)
def cargar_datos():
    global Matricula, Propietario, telefono, TipoVehiculo
    try:
        df = pd.read_csv('registros_vehiculos.csv')#archivo CVS para almacenar los datos
        Matricula = df['Matricula'].tolist()#listado de matriculas de vehiculos
        Propietario = df['Propietario'].tolist()#listado de nombres de propietarios del vehiculo
        telefono = df['Telefono'].tolist()#listado de telefonos de propietarios del vehiculo
        TipoVehiculo = df['TipoVehiculo'].tolist()#listado de tipo de vehiculo
        messagebox.showinfo("Cargado", "Los registros de vehículos han sido cargados desde registros_vehiculos.csv")
    except FileNotFoundError:#utilizada para cuando el vehiculo no aparezca en la direccion especifica
        messagebox.showinfo("Archivo no encontrado", "El archivo 'registros_vehiculos.csv' no existe.")#indica cuando no se encuentra el vehiculo indique no existe ubicacion especifica

# Funciones para las opciones del menú
def disponibilidad():#funcion q muestra la disponibilidad de espacios en el parqueadero
    global espacios_coches, espacios_motocicletas
    mensaje = f"Disponibilidad de espacios:\n\n\nCoches: {espacios_coches}/5\n\nMotocicletas: {espacios_motocicletas}/10"#determina cuantos espacios hay libres para cada tipo de vehiculo
    messagebox.showinfo("Disponibilidad", mensaje)#nos mueestra el recuadro informando la cantidad de espacios que se enuentran desponibles

def recaudo():#nos hace el calculo del recaudo que se debe cobrar
    calcular_recaudo()
    messagebox.showinfo("Recaudo Total", f"El recaudo total es de {total_recaudo} Pesos")#mostrara recuadro con el valor del recaudo

def salir():
    exit = messagebox.askokcancel("Salir", "¿Realmente desea salir de la Aplicación?")#nos mostrara recuadro verificando si el usuario en realidad desea salir
    if exit:
        # Guardar los datos antes de salir
        guardar_datos()#guarda los datos en cvs
        ventana.destroy()#cerrar ventana principal y se finaliza ejecucion del programa

# Configuración de la interfaz del programa
ventana = Tk()#ventana principal
ventana.title('Parqueadero')#establece el titulo en la ventana principal
ventana.geometry('700x400')#indica el tamaña de la ventada del programa
ventana.resizable(1, 1)#habilita la capacidad de redimencionar de ancho y alto

# Función para ajustar los tamaños de los elementos cuando se redimensiona la ventana
def on_resize(event):#funcion de redimencionar la ventana principal
    ventana.grid_columnconfigure(0, weight=1)#permite que la fila 0 se expanda verticalmente cuando se redimensiona la ventana.
    ventana.grid_columnconfigure(1, weight=1)#permite que la fila 0 se expanda verticalmente cuando se redimensiona la ventana.
    ventana.grid_rowconfigure(0, weight=1)#permite que la fila 0 se expanda verticalmente cuando se redimensiona la ventana.
    frame1.grid(row=0, column=0, sticky='nsew')
    frame2.grid(row=0, column=1, sticky='nsew')

ventana.bind("<Configure>", on_resize)

frame1 = Frame(ventana, bg='gray15')#permite que el frame se expanda en todas las direcciones
frame1.grid(row=0, column=0, sticky='nsew')#permite que el frame se expanda en las direcciones norte, sur, este y oeste para llenar el espacio disponible.

frame2 = Frame(ventana, bg='gray15')#que se utilizará para contener elementos de la interfaz en la parte derecha de la ventana principal.
frame2.grid(row=0, column=1, sticky='nsew')#permite que el frame se expanda en todas las direcciones.

# Definición de etiquetas y campos de entrada
lblMatricula = Label(frame1, text='Matricula', width=10)#Una etiqueta con el texto "Matricula". Se utiliza para mostrar una descripción de un campo de entrada.
lblMatricula.grid(row=0, column=0, padx=10, pady=20)#muestra tamaño y posicion del boton
txtMatricula = Entry(frame1, width=20, font=('Arial', 12))#permite que el usuario ingrese la informacion 
txtMatricula.grid(row=0, column=1)

lblPropietario = Label(frame1, text='Propietario', width=10)#Una etiqueta con el texto "Propietario". Similar a la etiqueta anterior, se utiliza para describir otro campo de entrada.
lblPropietario.grid(row=1, column=0, padx=10, pady=20)#muestra tamaño y posicion del boton
txtPropietario = Entry(frame1, width=20, font=('Arial', 12))#permite que el usuario ingrese la informacion 
txtPropietario.grid(row=1, column=1)

lblTelefono = Label(frame1, text='Telefono', width=10)#Una etiqueta con el texto "Telefono". Al igual que las etiquetas anteriores, describe un campo de entrada.
lblTelefono.grid(row=2, column=0, padx=10, pady=20)#muestra tamaño y posicion del boton
txtTelefono = Entry(frame1, width=20, font=('Arial', 12))#permite que el usuario ingrese la informacion 
txtTelefono.grid(row=2, column=1)

lblTipo = Label(frame1, text='Tipo', width=10)#Una etiqueta con el texto "Tipo". Descripción del campo de selección de tipo de vehículo.
lblTipo.grid(row=3, column=0, padx=10, pady=20)#muestra tamaño y posicion del boton
comboTipo = ttk.Combobox(frame1, values=["Coche", "Motocicleta"], width=17, font=('Arial', 12))#permite al usuario elegir entre las opciones "Coche" y "Motocicleta" como el tipo de vehículo.
comboTipo.grid(row=3, column=1)#Está configurado para que se coloque en la cuadrícula de la fila 3 y columna 1 del contenedor

# Botones para agregar y sacar vehículos
btnAgregar = Button(frame1, width=20, font=('Arial', 12, 'bold'), text='Ingresar vehiculo', 
                  bg='orange', bd=5, command=agregar_vehiculo)#que permite al usuario ingresar un vehículo. 
btnAgregar.grid(row=5, columnspan=2, padx=10, pady=20)#se ejecuta cuando se haga clic en el boton ingresar vehiculo

btnSacar = Button(frame1, width=20, font=('Arial', 12, 'bold'), text='Sacar Vehiculo', 
                  bg='red', bd=5, command=sacar_vehiculo)# permite al usuario sacar un vehículo.
btnSacar.grid(row=6, columnspan=2, padx=10, pady=20)#se ejecuta cuando se haga clic en el boton sacar vehiculo

# Etiqueta y tabla para mostrar los datos de los vehículos ingresados
lblArchivo = Label(frame2, text='Vehiculos Ingresados', width=25, bg='gray16',
                 font=('Arial', 12, 'bold'), fg='white')#que muestra el texto "Vehículos Ingresados".
lblArchivo.grid(row=0, column=0, padx=10, pady=10)#se utiliza para mostrar los datos de los vehículos ingresados.

tabla = ttk.Treeview(frame2, columns=('Propietario', 'Telefono', 'TipoVehiculo'))#configura que va a tener la tabla
tabla.grid(row=1, column=0)#Esta línea de código configura la ubicación de la tabla

# Configuración de las columnas de la tabla
tabla.column('#0', width=80)#Establece el ancho de la columna con el identificador #0 (columna de la matrícula) en 80 unidades.
tabla.column('Propietario', width=80, anchor='center')#Establece el ancho de la columna "Propietario" en 80 unidades y ajusta el texto al centro de la celda.
tabla.column('Telefono', width=80, anchor='center')#Establece el ancho de la columna "Telefono" en 80 unidades y ajusta el texto al centro de la celda.
tabla.column('TipoVehiculo', width=80, anchor='center')#Establece el ancho de la columna "TipoVehiculo" en 80 unidades y ajusta el texto al centro de la celda.

# Encabezados de las columnas de la tabla
tabla.heading('#0', text='Matricula', anchor='center')#Configura el encabezado de la columna con el identificador #0 con el texto "Matrícula" y ajusta el texto al centro.
tabla.heading('Propietario', text='Propietario', anchor='center')#Configura el encabezado de la columna "Propietario" con el texto "Propietario" y ajusta el texto al centro.
tabla.heading('Telefono', text='Telefono', anchor='center')#Configura el encabezado de la columna "Telefono" con el texto "Telefono" y ajusta el texto al centro.
tabla.heading('TipoVehiculo', text='Tipo', anchor='center')#Configura el encabezado de la columna "TipoVehiculo" con el texto "Tipo" y ajusta el texto al centro.

# Botón para mostrar los datos en la tabla
btnGuardar = Button(frame2, width=20, font=('Arial', 12, 'bold'), text='Mostrar Info', bg='green2', bd=5, command=mostrar_datos)
btnGuardar.grid(row=2, column=0, padx=10, pady=10)#muestra tamaño y color del boton 

# Barra de menú
barraMenu = Menu(ventana)#Se crea un objeto de menú (Menu) que se asocia con la ventana principal
ventana.config(menu=barraMenu, bg="#A9A9A9", width=400, height=400)#dimenciones del objeto menu

# Opciones del menú
parqueaderoMenu = Menu(barraMenu, tearoff=False)
parqueaderoMenu.add_command(label="Disponibilidad", command=disponibilidad)#definicion de variable
parqueaderoMenu.add_command(label="Recaudo", command=recaudo)#definicion de variable
parqueaderoMenu.add_separator()#definicion de variable
parqueaderoMenu.add_command(label="Guardar Datos", command=guardar_datos)#definicion de variable
parqueaderoMenu.add_command(label="Cargar Datos", command=cargar_datos)#definicion de variable
parqueaderoMenu.add_separator()#definicion de variable
parqueaderoMenu.add_command(label="Salir", command=salir)#definicion de variable

barraMenu.add_cascade(label="Menu de Admin", menu=parqueaderoMenu)

# Iniciar la aplicación
ventana.mainloop()#Inicia la aplicación y la mantiene en un bucle infinito para que responda a las interacciones del usuario. La aplicación seguirá ejecutándose hasta que el usuario la cierre.