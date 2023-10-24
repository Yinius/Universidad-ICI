# Ejercicio 13: Usa una estructura switch para elegir entre los dias de la semana

from guizero import App, Text, TextBox, PushButton, Window

def mostrar_error():
    ventana_error = Window(app, title="Error", width=500, height=120)
    mensaje_error = Text(ventana_error, text="El dato es erroneo")
    boton_ok = PushButton(ventana_error, text="OK", command=ventana_error.destroy)

def elegir_dia():
        global dia
        nint = int(n.value)
        if nint < 1 or nint > 7:
            mostrar_error()
        else:
            match nint:
                case 1:
                    dia = "Lunes"
                case 2:
                    dia = "Martes"
                case 3:
                    dia = "Miércoles"
                case 4:
                    dia = "Jueves"
                case 5:
                    dia = "Viernes"
                case 6:
                    dia = "Sábado"
                case 7:
                    dia = "Domingo"
            dia_elegido()           

def dia_elegido():
    app.info(title="Resultado", text=f"El día es : {dia}")
            
app = App(title="Días de la semana")

message = Text(app, text="Ingrese un día del 1 al 7:")
n = TextBox(app, width=20)
button = PushButton(app, text="Elegir", command=elegir_dia)

app.display()
