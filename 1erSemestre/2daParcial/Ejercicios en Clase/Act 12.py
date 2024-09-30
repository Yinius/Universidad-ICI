# Ejercicio 12: Genere la siguiente secuencia 01010101

from guizero import App, Text, TextBox, PushButton


app = App("Generador de secuencia de 0 y 1")
texto = Text(app, text="")  
def secuencia():
    caracteres = "01"
    while True:
        texto.value += caracteres
        app.update()
secuencia()

app.display()
