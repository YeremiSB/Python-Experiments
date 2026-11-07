import tkinter
from tkinter import filedialog
from tkinter import Tk
from tkinter import ttk

ventana = Tk()
ventana.title("MicroBlog")

ventana.geometry("900x600")
barra_menu = tkinter.Menu(ventana)

txt = tkinter.Text(ventana, width = 90, height = 10)

def abrir():
	file_a = filedialog.askopenfilename(title = "Abrir Archivo", filetypes = [("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")])
	print(file_a)

def guardar():
	file_b = filedialog.asksaveasfilename(title = "Abrir Archivo", filetypes = [("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")])
	content = txt.get("1.0", "end-1c") 
	print(content)

txt.pack(fill = "both", expand = True)
s = ttk.Scrollbar()
s.pack()
menu_archivo = tkinter.Menu(barra_menu, tearoff = 0)
menu_archivo.add_command(label = "Abrir Archivo",  command=abrir)
menu_archivo.add_command(label = "Guardar Archivo",  command=guardar)
barra_menu.add_cascade(label ="Archivo", menu = menu_archivo)


ventana.config(menu = barra_menu)
ventana.mainloop()
