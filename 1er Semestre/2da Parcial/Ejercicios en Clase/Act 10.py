#Ejercicio 10: Calcular el salario de una persona con las siguientes percepciones: sueldo base, 
# 5% de canasta basica, 3% prima de antiguedad. Y deducciónes: si el salario base excede $10,000 el ISR es de 30%, 
# y menos de eso el 20%. 
# Indique cuanto es el total de la nómina a pagar y cuantos son los impuestos que el jege debe pagar al SAT.

from guizero import App, Text, PushButton, TextBox, Window

def calcular():
    global salarioint
    salarioint = float(salario.value)
    canasta = salarioint * 0.05
    antiguedad = salarioint * 0.03
    total = salarioint + canasta + antiguedad
    if salarioint > 10000:
        isr = 0.30 * salarioint
    else:
        isr = 0.20 * salarioint
    app.info(title="Resultado", text=f"La nomina a pagar es : {total}\nEl ISR a pagar es: {isr}")

app = App(title="Salario")

message = Text(app, text="Programa que obtiene el salario de una persona")
message = Text(app, text="Ingrese el sueldo base: ")
salario = TextBox(app, width=20)
btnCalcular = PushButton(app, text="Calcular", command=calcular)

app.display()