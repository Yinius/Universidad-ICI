from guizero import App, Text, PushButton, TextBox

def change_message():
    message.value = "Arriba Isrrael"

app = App(title="Hola ICI")

message = Text(app,text="Dame tu nombre")
name = TextBox(app,width=20)

button = PushButton(app,text="Click Here", command=change_message)



app.display()