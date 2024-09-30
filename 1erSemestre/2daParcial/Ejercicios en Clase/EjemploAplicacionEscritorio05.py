import pyttsx3
from guizero import App, Text, PushButton, TextBox

engine = pyttsx3.init()

def generar_cuadrado():
    resultado = str(int(num.value)**2)
    cadena = f"El cuadrado de {num.value} es : {resultado}"
    engine.say(cadena)
    engine.runAndWait()

app = App(title="Cuadrado de un número")

message = Text(app,text="Dame un número: ")
num = TextBox(app,width=20)

button = PushButton(app,text="Calcular", command=generar_cuadrado)

app.display()