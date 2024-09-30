#jercicio 3: Se desea saber la cantidad de alumnos que pasaron una materia. Son 25 y la calificación aprobatoria es 7

from guizero import App, Text, PushButton, TextBox, Window

suma = 0
i = 1

def mostrar_error():
    ventana_error = Window(app, title="Error", width=500, height=120)
    mensaje_error = Text(ventana_error, text="El dato debe ser mayor a 1")
    boton_ok = PushButton(ventana_error, text="OK", command=ventana_error.destroy)

def mostrar_siguiente_numero():
    global i, message, num, button_siguiente
    if i <= 25:
        message = Text(app, text=f"Ingrese la calificación de la persona {i}: ")
        num = TextBox(app, width=20)
        i+=1
        button_siguiente = PushButton(app, text="Siguiente", command=calcular_promedio)
    else:
        calcular_promedio()

def calcular_promedio():
    global button_siguiente, message, num
    global i, suma
    num.destroy()
    button_siguiente.destroy()
    message.destroy()
    if num.value == '':
        mostrar_error()
        i-=1
        mostrar_siguiente_numero()
    elif not num.value.isnumeric():
        mostrar_error()
        i-=1
        mostrar_siguiente_numero()
    else:
        num = int(num.value)
        if num >= 7:
            suma += 1
        if i <= 25:
            mostrar_siguiente_numero()
        else:
            generar_promedio()
        
        
        
    
    

def generar_promedio():
    resultado = str(suma)
    app.info(title="Resultado", text=f"Los alumnos aprobados fueron: {resultado}")

app = App(title="Promedio de alumnos aprobados")

message = Text(app, text="Programa que obtiene el promedio de alumnos aprobados")
mostrar_siguiente_numero()

app.display()