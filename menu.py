from tkinter import *
from tkinter import messagebox
from collections import namedtuple

lista = []

def CrearResponsables():
    #crear tupla
    Responsable = namedtuple("Encargado", "documento nombres apellidos celular correo")
    global lista
    doc = docV.get()
    existe = validaDoc(doc)
    if not existe:

        doc = docV.get()
        nom = nomV.get()
        ape = apeV.get()
        cel = celV.get()
        cor = corV.get()

    resp = Responsable(doc, nom, ape, cel, cor)
    lista.append(resp)
    messagebox.showinfo("Mensaje", "El responsable fue creado con exito...")
    Limpiar()

def validaDoc(doc):
    ex = False
    for i in lista:
        if i.documento == doc:
                ex = True
                messagebox.showinfo("Revisar", " El responsable fue creado con exito")
    return ex

def BuscarResp():
    doc = docV.get()
    Encargado = namedtuple("Responsable", "documento nombres apellidos celular correo")
    for i in lista:
         if i.documento == doc:
                docV.set(i.documento)
                nomV.set(i.nombres)
                apeV.set(i.apellidos)
                celV.set(i.celular)
                corV.set(i.correo)

def modifResp():
    doc = docV.get
    responsable = namedtuple("Modificar", "documento nombres apellidos celular correo")
    
        

def salir():
    exit = messagebox.askokcancel("Salir", " Realmente Desea a Salir de la Aplicacion?")
    if(exit):
        ventana.destroy()

def Limpiar():
            docV.set("")
            nomV.set("")
            apeV.set("")
            celV.set("")
            corV.set("")

def Licencia():
    lic = '''
        Version:1.0
        Fecha: 06/09/2023
        Distribucion: Beta
        Contacto: Ing Sistemas S III LP I 
'''
    messagebox. showinfo("info", lic)

def frmresponsable():
    #Crear una ventana secundaria
    ventana_responsable = Toplevel()
    ventana_responsable.title("CRUD de responsable")
    ventana_responsable.config(bg = "#FFE4C4", width = 600, height = 400)

    #Crear Controles para la Captura de la Informacion
    lblDocumentos = Label(ventana_responsable, text = "Documento")
    lblDocumentos.grid(row = 0, column = 0, sticky = "e", padx = 10, pady = 10)
    txtDocumento = Entry(ventana_responsable, textvariable = docV)
    txtDocumento.grid(row = 0, column = 1, sticky = "e", padx = 10, pady = 10) 

    lblDocumentos = Label(ventana_responsable, text = "Nombre")
    lblDocumentos.grid(row = 1, column = 0, sticky = "e", padx = 10, pady = 10)
    txtDocumento = Entry(ventana_responsable, textvariable = nomV)
    txtDocumento.grid(row = 1, column = 1, sticky = "e", padx = 10, pady = 10)

    lblDocumentos = Label(ventana_responsable, text = "Apellido")
    lblDocumentos.grid(row = 2, column = 0, sticky = "e", padx = 10, pady = 10)
    txtDocumento = Entry(ventana_responsable, textvariable = apeV)
    txtDocumento.grid(row = 2, column = 1, sticky = "e", padx = 10, pady = 10)

    lblDocumentos = Label(ventana_responsable, text = "Celular")
    lblDocumentos.grid(row = 3, column = 0, sticky = "e", padx = 10, pady = 10)
    txtDocumento = Entry(ventana_responsable, textvariable = celV)
    txtDocumento.grid(row = 3, column = 1, sticky = "e", padx = 10, pady = 10)

    lblDocumentos = Label(ventana_responsable, text = "Correo")
    lblDocumentos.grid(row = 4, column = 0, sticky = "e", padx = 10, pady = 10)
    txtDocumento = Entry(ventana_responsable, textvariable = corV)
    txtDocumento.grid(row = 4, column = 1, sticky = "e", padx = 10, pady = 10)

    frame1 = Frame(ventana_responsable, bg = "blue")
    frame1.grid(row = 5, column = 0, columnspan = 2)
    
    btnCrear = Button(frame1, text = "Crear", command = CrearResponsables)
    btnCrear.grid(row = 5, column = 0, sticky = "e", padx = 5, pady = 5)
    
    btnBuscar = Button(frame1, text = "Buscar", command = BuscarResp)
    btnBuscar.grid(row = 5, column = 1, sticky = "e", padx = 5, pady = 5)

    btnModificar = Button(frame1, text = "Modificar")
    btnModificar.grid(row = 5, column = 2, sticky = "e", padx = 5, pady = 5)
    
    btnEliminar = Button(frame1, text = "Eliminar")
    btnEliminar.grid(row = 5, column = 3, sticky = "e", padx = 5, pady = 5)



    #Enfocar Ventana Secundaria
    ventana_responsable.focus()
    ventana_responsable.grab_set()


ventana = Tk()
ventana.title("Formulario Principal")

#Barra Menu
barraMenu = Menu(ventana)
ventana.config(menu = barraMenu, bg= "#A9A9A9", width = 400, height = 400)

#Variables Vinculadas
docV = StringVar()
nomV = StringVar()
apeV = StringVar()
celV = StringVar()
corV = StringVar()

#Opciones Menu
responsableMenu = Menu (barraMenu, tearoff = False)#Elimina la Opcion de los Guiones
responsableMenu.add_command(label = "Gestionar Responsable", command = frmresponsable)
responsableMenu.add_command(label = "Reportes")
responsableMenu.add_separator()#Crea una Linea de Separacion
responsableMenu.add_command(label = "Salir", command = salir)

salonMenu = Menu(barraMenu, tearoff = False)
salonMenu.add_command(label = "Gestionar Salon")
salonMenu.add_command(label = "Reportes")

ayudaMenu = Menu(barraMenu, tearoff = False)
ayudaMenu.add_command(label = "Acerca de...")
ayudaMenu.add_command(label = "Licencia", command = Licencia)

#Adicionar Opciones Para Mostrar
barraMenu.add_cascade(label = "Responsables", menu = responsableMenu)
barraMenu.add_cascade(label = "Salones", menu = salonMenu)
barraMenu.add_cascade(label = "Ayuda", menu = ayudaMenu)


ventana.mainloop()