from tkinter import *
from tkinter import messagebox
import sqlite3

#-------------funciones-----------------------

def conexionBBDD():

    miConexion=sqlite3.connect("Usuarios")
    miCursor=miConexion.cursor()

    try:
        miCursor.execute('''
            CREATE TABLE DATOSUSUARIOS(
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                NOMBRE_USUARIO VARCHAR(50),
                PASSWORD VARCHAR(50),
                APELLIDO VARCHARD(50),
                DIRECCION VARCHAR(50),
                COMENTARIOS VARCHAR(150)
            )
        ''')
        messagebox.showinfo("BBDD","BBDD creada con exito")
    except:
        messagebox.showwarning("¡Advertencia!","La BBDD ya existe")

def salirApp():
    valor=messagebox.askquestion("Salir","¿Quieres salir de la aplicación?")
    if valor=="yes":
        root.destroy()

def limpiarCampos():
    miId.set("")
    miNombre.set("")
    miApellido.set("")
    miDireccion.set("")
    miPass.set("")
    textoComentario.delete(1.0,END)

def crear():
    miConexion=sqlite3.connect("Usuarios")
    miCursor=miConexion.cursor()
    miCursor.execute("INSERT INTO DATOSUSUARIOS VALUES(NULL,'"+miNombre.get()+
    "','"+miPass.get()+
    "','"+miApellido.get()+
    "','"+miDireccion.get()+
    "','"+textoComentario.get("1.0",END)+"')")
    miConexion.commit()
    messagebox.showinfo("BBDD","Registro creado con exito")

def leer():
    miConexion=sqlite3.connect("Usuarios")
    miCursor=miConexion.cursor()
    miCursor.execute("SELECT * FROM DATOSUSUARIOS WHERE ID="+miId.get())
    elUsuario=miCursor.fetchall()

    if elUsuario==[]:
        messagebox.showinfo("Busqueda","No hay ningun registro con el id "+miId.get())

    for usuario in elUsuario:
        miId.set(usuario[0])
        miNombre.set(usuario[1])
        miPass.set(usuario[2])
        miApellido.set(usuario[3])
        miDireccion.set(usuario[4])
        textoComentario.insert("1.0",usuario[5])
    miConexion.commit()

def actualizar():
    miConexion=sqlite3.connect("Usuarios")
    miCursor=miConexion.cursor()
    miCursor.execute("UPDATE DATOSUSUARIOS SET NOMBRE_USUARIO='"+miNombre.get()+
        "',PASSWORD='"+miPass.get()+
        "',APELLIDO='"+miApellido.get()+
        "',DIRECCION='"+miDireccion.get()+
        "',COMENTARIOS='"+textoComentario.get("1.0",END)+
        "' WHERE ID="+miId.get())
    miConexion.commit()
    messagebox.showinfo("BBDD","Registro actualizado con exito")

def eliminar():
    miConexion=sqlite3.connect("Usuarios")
    miCursor=miConexion.cursor()
    miCursor.execute("DELETE FROM DATOSUSUARIOS WHERE ID="+miId.get())
    miConexion.commit()
    messagebox.showinfo("BBDD","Registro borrado con exito")
    

root=Tk()

barraMenu=Menu(root)
root.config(menu=barraMenu,width=600,height=400)

bbddMenu=Menu(barraMenu, tearoff=0)
bbddMenu.add_command(label="Conectar",command=conexionBBDD)
bbddMenu.add_command(label="Salir",command=salirApp)

borrarMenu=Menu(barraMenu, tearoff=0)
borrarMenu.add_command(label="Borrar campos",command=limpiarCampos)

crudMenu=Menu(barraMenu, tearoff=0)
crudMenu.add_command(label="Crear",command=crear)
crudMenu.add_command(label="Leer",command=leer)
crudMenu.add_command(label="Actualizar",command=actualizar)
crudMenu.add_command(label="Borrar",command=eliminar)

ayudaMenu=Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label="Licencia")
ayudaMenu.add_command(label="Acerca de...")

barraMenu.add_cascade(label="BBDD",menu=bbddMenu)
barraMenu.add_cascade(label="Borrar",menu=borrarMenu)
barraMenu.add_cascade(label="CRUD",menu=crudMenu)
barraMenu.add_cascade(label="Ayuda",menu=ayudaMenu)

#--------------comienzo de campos------------------------

miFrame=Frame(root)
miFrame.pack()

miId=StringVar()
miNombre=StringVar()
miApellido=StringVar()
miPass=StringVar()
miDireccion=StringVar()

cuadroID=Entry(miFrame,textvariable=miId)
cuadroID.grid(row=0,column=1,padx=10,pady=10)

cuadroNombre=Entry(miFrame,textvariable=miNombre)
cuadroNombre.grid(row=1,column=1,padx=10,pady=10)
cuadroNombre.config(fg="red",justify="right")

cuadroPass=Entry(miFrame,textvariable=miPass)
cuadroPass.grid(row=2,column=1,padx=10,pady=10)
cuadroPass.config(show="*")

cuadroApellido=Entry(miFrame,textvariable=miApellido)
cuadroApellido.grid(row=3,column=1,padx=10,pady=10)

cuadroDireccion=Entry(miFrame,textvariable=miDireccion)
cuadroDireccion.grid(row=4,column=1,padx=10,pady=10)

textoComentario=Text(miFrame,width=16,height=5)
textoComentario.grid(row=5,column=1,padx=10,pady=10)
scrolVert=Scrollbar(miFrame,command=textoComentario.yview)
scrolVert.grid(row=5,column=2,sticky="nsew")
textoComentario.config(yscrollcommand=scrolVert.set)

#---------------comienzo de labels----------------

idLabel=Label(miFrame,text="Id:")
idLabel.grid(row=0,column=0,sticky="e",padx=10,pady=10)

nombreLabel=Label(miFrame,text="Nombre:")
nombreLabel.grid(row=1,column=0,sticky="e",padx=10,pady=10)

passLabel=Label(miFrame,text="Password:")
passLabel.grid(row=2,column=0,sticky="e",padx=10,pady=10)

apellidoLabel=Label(miFrame,text="Apellido:")
apellidoLabel.grid(row=3,column=0,sticky="e",padx=10,pady=10)

direccionLabel=Label(miFrame,text="Direccion:")
direccionLabel.grid(row=4,column=0,sticky="e",padx=10,pady=10)

comentariosLabel=Label(miFrame,text="Comentarios:")
comentariosLabel.grid(row=5,column=0,sticky="e",padx=10,pady=10)

#---------------botones inferiores-------------------------

miFrame2=Frame(root)
miFrame2.pack()

botonCrear=Button(miFrame2,text="Crear",command=crear)
botonCrear.grid(row=1,column=0,sticky="e",padx=10,pady=10)

botonLeer=Button(miFrame2,text="Leer",command=leer)
botonLeer.grid(row=1,column=1,sticky="e",padx=10,pady=10)

botonActualizar=Button(miFrame2,text="Actualizar",command=actualizar)
botonActualizar.grid(row=1,column=2,sticky="e",padx=10,pady=10)

botonBorrar=Button(miFrame2,text="Borrar",command=eliminar)
botonBorrar.grid(row=1,column=3,sticky="e",padx=10,pady=10)

root.mainloop()