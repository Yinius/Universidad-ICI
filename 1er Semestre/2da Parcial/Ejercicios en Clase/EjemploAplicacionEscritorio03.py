from guizero import App, Text, PushButton, TextBox

def generar_cuadrado():
    mostar_cuadrado.value = str(int(num.value)**2)

app = App(title="Cuadrado de un número")

message = Text(app,text="Dame un número: ")
num = TextBox(app,width=20)

button = PushButton(app,text="Calcular", command=generar_cuadrado)

mostar_cuadrado = Text(app,text="")

app.display()