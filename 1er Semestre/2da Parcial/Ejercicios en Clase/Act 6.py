#Ejercicio 6: Obtenga la suma de todos los cuadrados de n números capturados del teclado

from guizero import App, Text, PushButton, TextBox, Window

suma = 0
i = 1

def mostrar_error():
    ventana_error = Window(app, title="Error", width=500, height=120)
    mensaje_error = Text(ventana_error, text="El dato debe ser mayor a 1")
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
        mostrar_siguiente_numero()

def mostrar_siguiente_numero():
    global i, message, num, button_siguiente
    if i <= nint:
        message = Text(app, text=f"Ingrese el número {i}: ")
        num = TextBox(app, width=20)
        i+=1
        button_siguiente = PushButton(app, text="Siguiente", command=calcular_suma)
    else:
        calcular_suma()

def calcular_suma():
    global button_siguiente, num
    global i, suma
    button_siguiente.destroy()
    if num.value == '':
        mostrar_error()
        i-=1
        mostrar_siguiente_numero()
    elif not num.value.isnumeric():
        mostrar_error()
        i-=1
        mostrar_siguiente_numero()
    else:
        num = int(num.value)
        if num % 2 == 0:
             suma += num * num
        if i <= nint:
            mostrar_siguiente_numero()     
        else:
            generar_cuadrado()

def generar_cuadrado():
    resultado = str(suma)
    app.info(title="Resultado", text=f"La suma del cuadrado de los {nint}\n números es: {resultado}")

app = App(title="Cuadrado de n números")

message = Text(app, text="Programa que genera la suma\n de todos los cuadrados de ciertos números")
message = Text(app, text="Ingrese los números a ingresar: ")
n = TextBox(app, width=20)
button_acepatar = PushButton(app, text="Aceptar", command=aceptar_n)

app.display()