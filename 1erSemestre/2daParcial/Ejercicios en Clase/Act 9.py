#Ejercicio 9: Obtenga la suma de 5 números capturados entre [5,10]

from guizero import App, Text, PushButton, TextBox, Window

i=0
suma = 0

def mostrar_error():
    ventana_error = Window(app, title="Error", width=500, height=120)
    mensaje_error = Text(ventana_error, text="El dato es erroneo, ingrese un número entre [5,10]")
    boton_ok = PushButton(ventana_error, text="OK", command=ventana_error.destroy)

def mostrar_siguiente_numero():
    global i, message, num, button_siguiente
    if i < 5:
        message = Text(app, text=f"Ingrese el número {i+1}: ")
        num = TextBox(app, width=20)
        i+=1
        button_siguiente = PushButton(app, text="Siguiente", command=calcular_suma)
    else:
        calcular_suma()

def calcular_suma():
    global button_siguiente, num, suma
    global i
    button_siguiente.destroy()
    if num.value == '' or int(num.value) < 5 or int(num.value) > 10:
        mostrar_error()
        i-=1
        message.destroy()
        num.destroy()
        mostrar_siguiente_numero()
    elif not num.value.isnumeric():
        mostrar_error()
        i-=1
        message.destroy()
        num.destroy()
        mostrar_siguiente_numero()
    else:
        num = int(num.value)
        suma += num
        if i < 5:
            mostrar_siguiente_numero()     
        else:
            generar_cuadrado()

def generar_cuadrado():
    app.info(title="Resultado", text=f"La suma de los números es : {suma}")

app = App(title="Suma de 5 números")

message = Text(app, text="Programa que genera la suma\n de 5 números capturados entre [5,10]")
mostrar_siguiente_numero()

app.display()