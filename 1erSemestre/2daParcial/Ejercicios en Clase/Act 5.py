#Ejercicio 5: Imrpimir los números pares entre 0 y 20 consecutivos y obtener la suma de todos los cuadrados de estos

from guizero import App, Text, PushButton, TextBox, Window

suma = 0

def generar_num():
    global num, suma
    num = 0
    while num <= 20:
        if num % 2 == 0:
            message = Text(app, text=f"{num}")
            suma += num * num
        num += 1
    generar_cuadrado()

def generar_cuadrado():
    resultado = str(suma)
    app.info(title="Resultado", text=f"La suma del cuadrado de los\n números es: {resultado}")

app = App(title="Cuadrado de un número")

message = Text(app, text="Programa que obtiene la suma del cuadrado\n de los números pares entre 0 y 20")
message = Text(app, text="\n")
generar_num()

app.display()