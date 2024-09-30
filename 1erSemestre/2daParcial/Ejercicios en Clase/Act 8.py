#Ejercicio 8:Programa que dado el año de nacimineto indique cuantos años va a cumplir una persona el siguiente año

from guizero import App, Text, PushButton, TextBox, Window

anio_a = 0
edad = 0

def mostrar_error():
    ventana_error = Window(app, title="Error", width=500, height=120)
    mensaje_error = Text(ventana_error, text="El dato debe ser mayor a 1")
    boton_ok = PushButton(ventana_error, text="OK", command=ventana_error.destroy)

def aceptar_n():
    global nint
    if (a_n.value == '' or a_n.value == "0" or a_n.value=="1"):
        mostrar_error()
    elif not a_n.value.isnumeric():
        mostrar_error()
    else:
        nint = int(a_n.value)
        generar_edad()

def generar_edad():
    button_acepatar.destroy()
    global a_a
    message = Text(app, text="Ingrese el año actual ")
    a_a = TextBox(app, width=20)
    button_generar = PushButton(app, text="Aceptar", command=generar_resta)

def generar_resta():
    global edad
    if (a_a.value == '' or a_a.value == "0" or a_a.value=="1"):
        mostrar_error()
    elif not a_a.value.isnumeric():
        mostrar_error()
    else:
        a_aint = int(a_a.value)
        edad = (a_aint-nint)+1
        resultado = str(edad)
        app.info(title="Resultado", text=f"La edad de la persona el siguiente año será: {resultado}")

app = App(title="Calcular edad")

message = Text(app, text="Programa que obtiene la edad")
message = Text(app, text="Ingrese el año de nacimiento: ")
a_n = TextBox(app, width=20)
button_acepatar = PushButton(app, text="Aceptar", command=aceptar_n)


app.display()