from tkinter import *

raiz=Tk()

raiz.title("Titulo de esta ventana")

# redimension de ventana (width: bool, height: bool)
raiz.resizable(True,True)

#icon
#raiz.iconbitmap("/icon.ico")

raiz.geometry("500x500")

raiz.config(bg="orange")
raiz.mainloop()