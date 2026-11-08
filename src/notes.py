import tkinter
from tkinter import filedialog
from tkinter import messagebox
from tkinter import Tk
from tkinter import ttk

class App:
	def __init__(self):
		self.ventana = Tk()
		self.ventana.title("MicroBlog")

		self.ventana.geometry("900x600")
		self.vent_frame = ttk.Frame(self.ventana, padding = 1)
		self.barra_menu = tkinter.Menu(self.ventana)
		self.txt = tkinter.Text(self.vent_frame, width = 90, height = 10)
		self.txt.grid(row = 0, column=0, sticky = "nwse")
		self.vent_frame.columnconfigure(0 ,weight=1)
		self.vent_frame.rowconfigure(0, weight = 1)
		self.s = ttk.Scrollbar(self.vent_frame)
		self.s.grid(row = 0, column = 1 , sticky = "ns")
		self.txt.config(yscrollcommand = self.s.set)
		self.s.config(command = self.txt.yview)
		self.vent_frame.pack(fill = "both", expand = True)

		self.menu_archivo = tkinter.Menu(self.barra_menu, tearoff = 0)
		self.menu_archivo.add_command(label = "Abrir Archivo",  command=self.abrir)
		self.menu_archivo.add_command(label = "Guardar Archivo",  command=self.guardar)
		self.barra_menu.add_cascade(label ="Archivo", menu = self.menu_archivo)
		self.ventana.config(menu = self.barra_menu)

	def abrir(self):
			file_sel = filedialog.askopenfilename(title = "Abrir Archivo", filetypes = [("Archivos de texto", "*.txt"),("Python Files", ("*.py", "*.pyw")), ("Todos los archivos", "*.*")])
			if file_sel == "":
				messagebox.showinfo(message= "No se seleciono un archivo, cancelando", icon = "error")
			else:
				with open(file_sel, "r", encoding = "utf-8") as file_a:
					file = file_a.read()
					self.txt.delete("1.0", "end")
					self.txt.insert("1.0", file)
	def guardar(self):
			file_sel = filedialog.asksaveasfilename(title = "Guardar Archivo", filetypes = [("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")])
			if file_sel == "":
				messagebox.showinfo(message= "No se seleciono un archivo, cancelando", icon = "error")
			else:
				with open(file_sel, "w", encoding = "utf-8") as file_g:
					file_g.write(self.txt.get("1.0", "end-1c"))

	def correr(self):
			self.ventana.mainloop()
#ventana = Tk()
#ventana.title("MicroBlog")

#ventana.geometry("900x600")
#vent_frame = ttk.Frame(ventana, padding = 1)
#barra_menu = tkinter.Menu(ventana)
#txt = tkinter.Text(vent_frame, width = 90, height = 10)
#txt.grid(row = 0, column=0, sticky = "nwse")
#vent_frame.columnconfigure(0 ,weight=1)
#vent_frame.rowconfigure(0, weight = 1)
#s = ttk.Scrollbar(vent_frame)
#s.grid(row = 0, column = 1 , sticky = "ns")
#txt.config(yscrollcommand = s.set)
#s.config(command = txt.yview)
#vent_frame.pack(fill = "both", expand = True)

#def abrir():
#	file_sel = filedialog.askopenfilename(title = "Abrir Archivo", filetypes = [("Archivos de texto", "*.txt"),("Python Files", ("*.py", "*.pyw")), ("Todos los archivos", "*.*")])
#	if file_sel == "":
#		messagebox.showinfo(message= "No se seleciono un archivo, cancelando", icon = "error")
#	else:
#		with open(file_sel, "r", encoding = "utf-8") as file_a:
#			file = file_a.read()
#			txt.delete("1.0", "end")
#			txt.insert("1.0", file)

#def guardar():
#	file_sel = filedialog.asksaveasfilename(title = "Abrir Archivo", filetypes = [("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")])
#	if file_sel == "":
#		messagebox.showinfo(message= "No se seleciono un archivo, cancelando", icon = "error")
#	else:
#		with open(file_sel, "w", encoding = "utf-8") as file_g:
#			file_g.write(txt.get("1.0", "end-1c"))


#menu_archivo = tkinter.Menu(barra_menu, tearoff = 0)
#menu_archivo.add_command(label = "Abrir Archivo",  command=abrir)
#menu_archivo.add_command(label = "Guardar Archivo",  command=guardar)
#barra_menu.add_cascade(label ="Archivo", menu = menu_archivo)


#ventana.config(menu = barra_menu)
#ventana.mainloop()
notes = App()

notes.correr()