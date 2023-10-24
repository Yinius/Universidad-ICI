#Ejercicio 2: Obtener la edad promedio de n personas preguntando su número de nacimiento y asumiendo que el año actual es 2023

from guizero import App, Text, PushButton, TextBox, Window

anio_a = 2023
suma = 0
i = 1

def mostrar_error():
    ventana_error = Window(app, title="Error", width=500, height=120)
    mensaje_error = Text(ventana_error, text="El dato debe ser mayor a 1")
    boton_ok = PushButton(ventana_error, text="OK", command=ventana_error.destroy)

def aceptar_n():
    global nint
    if (n.value == '' or n.value == "0" or n.value=="1"):
        mostrar_error()
    elif not n.value.isnumeric():
        mostrar_error()
    else:
        nint = int(n.value)
        button_acepatar.destroy()
        mostrar_siguiente_numero()

def mostrar_siguiente_numero():
    global i, message, num, button_siguiente
    if i <= nint:
        message = Text(app, text=f"Ingrese el año de nacimiento de la persona {i}: ")
        num = TextBox(app, width=20)
        i+=1
        button_siguiente = PushButton(app, text="Siguiente", command=calcular_promedio)
    else:
        calcular_promedio()

def calcular_promedio():
    global button_siguiente
    button_siguiente.destroy()

    global i, num, suma
    if num.value == '':
        mostrar_error()
    elif not num.value.isnumeric():
        mostrar_error()
    else:
        num = int(num.value)
        edad = anio_a - num
        suma += edad
        if i <= nint:
            mostrar_siguiente_numero()
        else:
            generar_promedio()

def generar_promedio():
    resultado = str(suma / nint)
    app.info(title="Resultado", text=f"La edad promedio de las {nint} personas es: {resultado}")

app = App(title="Promedio de n edades")

message = Text(app, text="Programa que obtiene el promedio de edades de ciertas personas")
message = Text(app, text="Ingrese el número de personas a ingresar: ")
n = TextBox(app, width=20)
button_acepatar = PushButton(app, text="Aceptar", command=aceptar_n)

app.display()

