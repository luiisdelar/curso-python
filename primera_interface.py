from tkinter import *

raiz=Tk()

raiz.title("Titulo de esta ventana")

# redimension de ventana (width: bool, height: bool)
raiz.resizable(True,True)

#icon
#raiz.iconbitmap("/icon.ico")

#raiz.geometry("500x500")

raiz.config(bg="orange")

marco=Frame()

marco.pack(fill="both",expand="true")

marco.config(bd=10)
marco.config(relief="groove")
marco.config(bg="gray")
marco.config(cursor="pirate")
marco.config(width="500",height="500")

raiz.mainloop()