from guizero import App, Text, PushButton, TextBox

def generar_cuadrado():
    resultado = str(int(num.value)**2)
    app.info(title="Resultado",text=resultado)

app = App(title="Cuadrado de un número")

message = Text(app,text="Dame un número: ")
num = TextBox(app,width=20)

button = PushButton(app,text="Calcular", command=generar_cuadrado)

app.display()