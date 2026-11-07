from tkinter import Tk
from tkinter import ttk

ventana = Tk()
ventana.title("Hola mundo")

ventana.geometry("900x600")
texto = ttk.Label(ventana, text="Hola Mundo", font=("arial", 40))
texto.pack()
ventana.mainloop()
