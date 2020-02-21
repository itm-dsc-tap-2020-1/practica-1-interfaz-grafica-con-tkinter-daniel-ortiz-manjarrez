import tkinter as tk
from tkinter import ttk
from tkinter import Menu
from tkinter import messagebox as mBox
from tkinter import scrolledtext

# Funciones para ventanas emergentes
def funcion_box1(x):
    mBox.showinfo('Tus Datos son: ',x)

def funcion_box2():
    mBox.showinfo('Error','Espacios incompletos')

# Funciones de validacion para la captura de datos pestañas 1 y 2
def funcion_validarp1():
    for i in Lista:
        if not i: 
            return False
    return True

def funcion_validarp2():
    if sctext.get(1.0, tk.END) == "\n":
        return False
    return True

# Funcion Captura Pestaña 2
def funcion_capture2():
    Lista2.clear()
    if funcion_validarp2() == False:
        funcion_box2()
        return
    texto = "Pasatiempos: "
    if Check.get() == 1: Lista2.append("Leer")
    if Check2.get() == 1: Lista2.append("Peliculas")
    if Check3.get() == 1: Lista2.append("Redes sociales")
    
    for i in Lista2:
        texto+=i+", "
    texto+="\n"+"Estado: "
    if Opcion.get() == 1: texto+="Soltero"
    if Opcion.get() == 2: texto+="Casado"
    if Opcion.get() == 3: texto+="Viudo"
    texto+="\n"+"Objetivo de la vida: "+"\n"+sctext.get(1.0, tk.END)
    funcion_box1(texto)

# Funcion Captura Pestaña 1
def funcion_capture():
    Lista.clear()
    Lista.append(nombre.get())
    Lista.append(apellidoPaterno.get())
    Lista.append(apellidoMaterno.get())
    Lista.append(direccion.get())
    Lista.append(colonia.get())
    Lista.append(ciudad.get())
    Lista.append(municipio.get())
    if funcion_validarp1() == False:
        funcion_box2()
        return
    x =  ""
    y = 0
    for i in Lista:
        if(y == 0):
            x+="Nombre: "+i+"\n"
        if(y == 1):
            x+="Apellido Paterno: "+i+"\n"
        if(y == 2):
            x+="Apellido Materno: "+i+"\n"
        if(y == 3):
            x+="Direccion: "+i+"\n"
        if(y == 4):
            x+="Colonia: "+i+"\n"
        if(y == 5):
            x+="Ciudad: "+i+"\n"
        if(y == 6):
            x+="Municipio: "+i
        y+=1
    funcion_box1(x)
    
# Funcion captura del menu imprimir
def funcion_capture3():
    Lista.clear()
    Lista.append(nombre.get())
    Lista.append(apellidoPaterno.get())
    Lista.append(apellidoMaterno.get())
    Lista.append(direccion.get())
    Lista.append(colonia.get())
    Lista.append(ciudad.get())
    Lista.append(municipio.get())
    if funcion_validarp1() == False:
        funcion_box2()
        return
    x =  ""
    y = 0
    for i in Lista:
        if(y == 0):
            x+="Nombre: "+i+"\n"
        if(y == 1):
            x+="Apellido Paterno: "+i+"\n"
        if(y == 2):
            x+="Apellido Materno: "+i+"\n"
        if(y == 3):
            x+="Direccion: "+i+"\n"
        if(y == 4):
            x+="Colonia: "+i+"\n"
        if(y == 5):
            x+="Ciudad: "+i+"\n"
        if(y == 6):
            x+="Municipio: "+i
        y+=1
    Lista2.clear()
    if funcion_validarp2() == False:
        funcion_box2()
        return
    x += "\n"+"Pasatiempos: "
    if Check.get() == 1: Lista2.append("Leer")
    if Check2.get() == 1: Lista2.append("Peliculas")
    if Check3.get() == 1: Lista2.append("Redes sociales")
    
    for i in Lista2:
        x+=i+", "
    x+="\n"+"Estado: "
    if Opcion.get() == 1: x+="Soltero"
    if Opcion.get() == 2: x+="Casado"
    if Opcion.get() == 3: x+="Viudo"
    x+="\n"+"Objetivo de la vida: "+"\n"+sctext.get(1.0, tk.END)
    funcion_box1(x)

ColumnaPestaña1=0
FilaPestaña1=0

ColumnaPestaña2=0
FilaPestaña2=0

def Next():
    global ColumnaPestaña1
    global FilaPestaña1
    ColumnaPestaña1 = 0
    FilaPestaña1 += 1

def Next2():
    global ColumnaPestaña2
    global FilaPestaña2
    ColumnaPestaña2 = 0
    FilaPestaña2 += 1

    
def funcion_salir():
    ventana.quit()
    ventana.destroy()
    exit()

# Estructura general de la ventana

ventana = tk.Tk()
ventana.title("Sistema Escolar")

barra_menu = Menu(ventana)
ventana.config(menu = barra_menu)

opciones_menu = Menu(barra_menu)
opciones_menu.add_command(label = "Imprimir", command = funcion_capture3)
opciones_menu.add_separator()
opciones_menu.add_command(label = "Salir", command = funcion_salir)
barra_menu.add_cascade(label = "Sistema", menu = opciones_menu)

menu_ayuda = Menu(barra_menu, tearoff = 0)
menu_ayuda.add_command(label = "Acerca de")
barra_menu.add_cascade(label = "Ayuda", menu = menu_ayuda)

tabControl = ttk.Notebook(ventana)
tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text = 'Datos Personales')
tabControl.pack(expand = 1, fill = "both")

tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text = 'Datos Extras')

#Lista de Apoyo

Lista = []
Lista2 = []

# Atributos de Pestaña 1

labelNombre = ttk.Label(tab1, text = "Nombre: ")
labelNombre.grid(column = ColumnaPestaña1, row = FilaPestaña1)

nombre = tk.StringVar()
ColumnaPestaña1+=1

nombreCapturado = ttk.Entry(tab1, width = 20, textvariable = nombre)
nombreCapturado.grid(column = ColumnaPestaña1, row = FilaPestaña1, columnspan = 8)
Next()

labelApellidoPaterno = ttk.Label(tab1, text = "Apellido Paterno: ")
labelApellidoPaterno.grid(column = ColumnaPestaña1, row = FilaPestaña1)

apellidoPaterno = tk.StringVar()
ColumnaPestaña1+=1

apellidoPaternoCapturado = ttk.Entry(tab1, width = 20, textvariable = apellidoPaterno)
apellidoPaternoCapturado.grid(column = ColumnaPestaña1, row = FilaPestaña1, columnspan = 8)
Next()

labelApellidoMaterno = ttk.Label(tab1, text = "Apellido Materno: ")
labelApellidoMaterno.grid(column = ColumnaPestaña1, row = FilaPestaña1)

apellidoMaterno = tk.StringVar()
ColumnaPestaña1+=1

apellidoMAternoCapturado = ttk.Entry(tab1, width = 20, textvariable = apellidoMaterno)
apellidoMAternoCapturado.grid(column = ColumnaPestaña1, row = FilaPestaña1, columnspan = 8)
Next()

labelDireccion = ttk.Label(tab1, text = "Direccion: ")
labelDireccion.grid(column = ColumnaPestaña1, row = FilaPestaña1)

direccion = tk.StringVar()
ColumnaPestaña1+=1

direccionSeleccionada = ttk.Combobox(tab1, textvariable = direccion, state="readonly")
direccionSeleccionada['values'] = ("Hospital de Charo", "Hospital de Huetamo", "Hospital de Jiquilpan")
direccionSeleccionada.grid(column = ColumnaPestaña1, row = FilaPestaña1)
direccionSeleccionada.current(0)
Next()

labelColonia = ttk.Label(tab1, text = "Colonia: ")
labelColonia.grid(column = ColumnaPestaña1, row = FilaPestaña1)
ColumnaPestaña1+=1

colonia = tk.StringVar()
coloniaSeleccionada = ttk.Combobox(tab1, textvariable = colonia, state="readonly")
coloniaSeleccionada['values'] = ("Don Vasco", "Huetamo", "Viveros")
coloniaSeleccionada.grid(column = ColumnaPestaña1, row = FilaPestaña1)
coloniaSeleccionada.current(0)
Next()

labelCiudad = ttk.Label(tab1, text = "Ciudad: ")
labelCiudad.grid(column = ColumnaPestaña1, row = FilaPestaña1)
ColumnaPestaña1+=1

ciudad = tk.StringVar()
ciudadSeleccionada = ttk.Combobox(tab1, textvariable = ciudad, state="readonly")
ciudadSeleccionada['values'] = ("Morelia", "Tres Marias", "Jesus del Monte")
ciudadSeleccionada.grid(column = ColumnaPestaña1, row = FilaPestaña1)
ciudadSeleccionada.current(0)
Next()

labelMunicipio = ttk.Label(tab1, text = "Municipio: ")
labelMunicipio.grid(column = ColumnaPestaña1, row = FilaPestaña1)
ColumnaPestaña1+=1

municipio = tk.StringVar()
municipioSeleccionado = ttk.Combobox(tab1, textvariable = municipio, state="readonly")
municipioSeleccionado['values'] = ("Morelia", "Tarimbaro", "Zamora")
municipioSeleccionado.grid(column = ColumnaPestaña1, row = FilaPestaña1)
municipioSeleccionado.current(0)
Next()
ColumnaPestaña1 = 3

# Atributos Pestaña 2

labelPasatiempos = ttk.Label(tab2, text = "Pasatiempos")
labelPasatiempos.grid(column = ColumnaPestaña2, row = FilaPestaña2, columnspan =10)
Next2()

Check = tk.IntVar()
Casilla1 = tk.Checkbutton(tab2, text = "Leer", variable = Check)
Casilla1.deselect()
Casilla1.grid(column = ColumnaPestaña2, row = FilaPestaña2, sticky = tk.W)
ColumnaPestaña2 += 1

Check2 = tk.IntVar()
Casilla2 = tk.Checkbutton(tab2, text = "Peliculas", variable = Check2)
Casilla2.deselect()
Casilla2.grid(column = ColumnaPestaña2, row = FilaPestaña2, sticky = tk.W)
ColumnaPestaña2 += 1

Check3 = tk.IntVar()
Casilla3 = tk.Checkbutton(tab2, text = "Reder sociales", variable = Check3)
Casilla3.deselect()
Casilla3.grid(column = ColumnaPestaña2, row = FilaPestaña2, sticky = tk.E)
Next2()

labelEstado = ttk.Label(tab2, text = "Estado")
labelEstado.grid(column = ColumnaPestaña2, row = FilaPestaña2, columnspan = 12)
Next2()

Opcion = tk.IntVar()
Radio1 = tk.Radiobutton(tab2, text = "Soltero", variable = Opcion, value = 1)
Radio1.grid(column = ColumnaPestaña2, row = FilaPestaña2, sticky = tk.W)
ColumnaPestaña2 += 1
Radio1.select()

Radio2 = tk.Radiobutton(tab2, text = "Casado", variable = Opcion, value = 2)
Radio2.grid(column = ColumnaPestaña2, row = FilaPestaña2, sticky = tk.W)
ColumnaPestaña2 += 1

Radio3 = tk.Radiobutton(tab2, text = "Viudo", variable = Opcion, value = 3)
Radio3.grid(column = ColumnaPestaña2, row = FilaPestaña2, sticky = tk.E)
Next2()

labelObjetivo = ttk.Label(tab2, text = "Objetivo de la vida")
labelObjetivo.grid(column = ColumnaPestaña2, row = FilaPestaña2, columnspan = 12)
Next2()

sctext = scrolledtext.ScrolledText(tab2, width = 30, height = 5, wrap = tk.WORD)
sctext.grid(column = ColumnaPestaña2, row = FilaPestaña2)
Next2()
ColumnaPestaña2 = 3

# Botones para las pestañas 1 y 2

BotonPestaña1 = ttk.Button(tab1, text = "Imprimir datos personales", command = funcion_capture)
BotonPestaña1.grid(column = ColumnaPestaña1, row = FilaPestaña2)

BotonPestaña2 = ttk.Button(tab2, text="Boton Imprimir Datos", command = funcion_capture2)
BotonPestaña2.grid(column = ColumnaPestaña2, row = FilaPestaña2)



ventana.mainloop()