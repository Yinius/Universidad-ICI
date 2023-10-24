# Ejercicio 11: Genere una secuencia que va 010101 con el número de digitos que el ususaio quiere que tenga

from guizero import App, Text, TextBox, PushButton

cero = False

def generar():
    global nint
    nint = int(n.value)
    if nint>0:
        cero=True
        for i in range(nint):
            if cero==True:
                caracter="0"
                secuencia.value=secuencia.value+caracter
                cero=False
            else:
                caracter="1"
                cero=True
                secuencia.value=secuencia.value+caracter
    

app = App(title="Secuencia")

message = Text(app, text="Programa que genera una secuencia")
message = Text(app, text="Ingrese los digitos totales que tendrá\n la secuencia: ")
n = TextBox(app, width=20)
btnGenerar = PushButton(app, text="Generar", command=generar)

secuencia = Text(app, text="")

app.display()
