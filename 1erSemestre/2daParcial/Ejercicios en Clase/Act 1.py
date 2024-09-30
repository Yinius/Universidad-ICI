from guizero import App, Text, PushButton, TextBox, Window

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
        message = Text(app, text=f"Ingrese el número {i}: ")
        num = TextBox(app, width=20)
        i+=1
        button_siguiente = PushButton(app, text="Siguiente", command=calcular_promedio)
    else:
        calcular_promedio()

def calcular_promedio():
    #Desaparece el boton de siguiente
    global button_siguiente
    button_siguiente.destroy()

    global i, num, sum, c
    if num.value == '':
        mostrar_error()
    elif not num.value.isnumeric():
        mostrar_error()
    else:
        num = int(num.value)
        sum += num
        c += 1
        if i <= nint:
            mostrar_siguiente_numero()
        else:
            generar_promedio()

def generar_promedio():
    resultado = str(sum / c)
    app.info(title="Resultado", text=resultado)

i = 1
sum = 0
c = 0
nint = 0

app = App(title="Promedio de n números")

message = Text(app, text="Programa que obtiene el promedio de ciertos números ingresados")
message = Text(app, text="Ingrese el número de números a ingresar: ")
n = TextBox(app, width=20)
button_acepatar = PushButton(app, text="Aceptar", command=aceptar_n)

app.display()