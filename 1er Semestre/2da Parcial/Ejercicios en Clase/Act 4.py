#Ejercicio 4: Programa que calcule el cuadrado de un número positivo leido desde un teclado

from guizero import App, Text, PushButton, TextBox, Window

def mostrar_error():
    ventana_error = Window(app, title="Error", width=500, height=120)
    mensaje_error = Text(ventana_error, text="El dato debe ser positivo")
    boton_ok = PushButton(ventana_error, text="OK", command=ventana_error.destroy)

def aceptar_n():
    global nint
    if (n.value == ''):
        mostrar_error()
    elif not n.value.isnumeric():
        mostrar_error()
    else:
        nint = int(n.value)
        button_acepatar.destroy()
        calcular_promedio()

def calcular_promedio():
    global num
    if n.value == '':
        mostrar_error()
    elif not n.value.isnumeric():
        mostrar_error()
    else:
        num = int(n.value)
        generar_cuadrado()

def generar_cuadrado():
    resultado = str(num ** 2)
    app.info(title="Resultado", text=f"El cuadrado de {nint} es: {resultado}")

app = App(title="Cuadrado de un número")

message = Text(app, text="Programa que obtiene el cuadrado de un número")
message = Text(app, text="Ingrese el número a calcular: ")
n = TextBox(app, width=20)
button_acepatar = PushButton(app, text="Aceptar", command=aceptar_n)

app.display()