# Ejercicio 15: Programa del menu de una calculadora funcional que pueda sumar, restar, multiplicar y dividir
# al seleccionar el tipo de operación dar 2 números

from guizero import App, Text, TextBox, PushButton, Window

def mostrar_error():
    ventana_error = Window(app, title="Error", width=500, height=120)
    Text(ventana_error, text="Datos incorrecto")
    PushButton(ventana_error, text="OK", command=ventana_error.destroy)

def suma(a,b):
    global resultado
    resultado = a+b
    app.info(title="Resultado", text=f"El resultado es : {resultado}")

def resta(a,b):
    global resultado
    resultado = a-b
    app.info(title="Resultado", text=f"El resultado es : {resultado}")

def multiplicacion(a,b):
    global resultado
    resultado = a*b
    app.info(title="Resultado", text=f"El resultado es : {resultado}")

def division(a,b):
    global resultado
    resultado = a/b
    app.info(title="Resultado", text=f"El resultado es : {resultado}")

def menu():
    global nint
    nint = int(n.value)

    if nint < 1 or nint > 5:
        mostrar_error()
    else:
        match nint:
            case 1:
                a = TextBox(app, width=20)
                b = TextBox(app, width=20)
                PushButton(app, text="Calcular", command=lambda: suma(int(a.value),int(b.value)))
            case 2:
                a = TextBox(app, width=20)
                b = TextBox(app, width=20)
                PushButton(app, text="Calcular", command=lambda: resta(int(a.value),int(b.value)))
            case 3:
                a = TextBox(app, width=20)
                b = TextBox(app, width=20)
                PushButton(app, text="Calcular", command=lambda: multiplicacion(int(a.value),int(b.value)))
            case 4:
                a = TextBox(app, width=20)
                b = TextBox(app, width=20)
                PushButton(app, text="Calcular", command=lambda: division(int(a.value),int(b.value)))
            case 5:
                app.destroy()
    
            
app = App(title="Calculadora")

Text(app, text="1. Suma")
Text(app, text="2. Resta")
Text(app, text="3. Multiplicación")
Text(app, text="4. División")
Text(app, text="5. Salir")
message = Text(app, text="Ingrese una opcion:")
n = TextBox(app, width=20)
button = PushButton(app, text="Elegir", command=menu)

app.display()