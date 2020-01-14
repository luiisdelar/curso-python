from tkinter import *

raiz=Tk()

marco=Frame(raiz,width=500,height=500)
marco.pack()

img=PhotoImage(file="img.png")

label=Label(raiz,image=img).place(x=50,y=50)
#label=Label(marco,text="Hablenme claro", fg="orange", font=("Comic Sans MS",18)).place(x=100,y=100)

raiz.mainloop()