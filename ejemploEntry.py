from tkinter import *

raiz=Tk()

marco=Frame(raiz,width=1200,height=700)
marco.pack()

minombre=StringVar()

cuadronombre=Entry(marco,textvariable=minombre)    
cuadronombre.grid(row=0,column=1, padx=10,pady=10)
cuadronombre.config(fg="red",justify="right")

cuadropass=Entry(marco)
cuadropass.grid(row=3,column=1, padx=10,pady=10)
cuadropass.config(show="*")

cuadroape=Entry(marco)    
cuadroape.grid(row=1,column=1, padx=10,pady=10)

cuadrodir=Entry(marco)    
cuadrodir.grid(row=2,column=1, padx=10,pady=10)

textocomentario=Text(marco, width=16,height=5)
textocomentario.grid(row=4,column=1,padx=10,pady=10)

scrolv=Scrollbar(marco,command=textocomentario.yview)
scrolv.grid(row=4,column=2,sticky="nsew")

textocomentario.config(yscrollcommand=scrolv.set)

nombre=Label(marco,text="Nombre:")
nombre.grid(row=0,column=0, padx=10,pady=10)

ape=Label(marco,text="Apellido:")
ape.grid(row=1,column=0,padx=10,pady=10)

dire=Label(marco,text="Direccion:")
dire.grid(row=2,column=0,padx=10,pady=10)

passlabel=Label(marco,text="Password:")
passlabel.grid(row=3,column=0,sticky="e",padx=10,pady=10)


comenLabel=Label(marco,text="Comentarios:")
comenLabel.grid(row=4,column=0,sticky="e",padx=10,pady=10)

def codigoBoton():
    minombre.set("Luis")

botonEnvio=Button(raiz,text="Enviar",command=codigoBoton)
botonEnvio.pack()

raiz.mainloop()