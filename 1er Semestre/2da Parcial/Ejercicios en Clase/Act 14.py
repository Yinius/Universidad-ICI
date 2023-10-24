# Ejercicio 14: La tienda "brankos" debe vender productos a n alumnos, ofrecen: tortas, tacos, hot dogs, y pizzas. 
# Imprime los productos vendidos en total

from guizero import App, Text, TextBox, PushButton, Window

def mostrar_error():
    ventana_error = Window(app, title="Error", width=500, height=120)
    mensaje_error = Text(ventana_error, text="Llene correctamente los campos")
    boton_ok = PushButton(ventana_error, text="OK", command=ventana_error.destroy)

def calcular_venta():
    if tor.value == '' or taco.value == '' or hot.value == '' or pizza.value == '':
        mostrar_error()
    elif not tor.value.isnumeric() or not taco.value.isnumeric() or not hot.value.isnumeric() or not pizza.value.isnumeric():
        mostrar_error()
    else:
        torint = int(tor.value)
        tacoint = int(taco.value) 
        hotint = int(hot.value) 
        pizzaint = int(pizza.value)  
        total_ventas = torint + tacoint + hotint + pizzaint 
        app.info("Productos Vendidos", f"Tortas: {torint}\nTacos: {tacoint}\nHot Dogs: {hotint}\nPizzas: {pizzaint}\n\nTotal de Productos Vendidos: {total_ventas}")


app = App(title="Ventas Brankos")  

Text(app, text="Tortas:") 
tor = TextBox(app, width=30) 
Text(app, text="Tacos:")  
taco = TextBox(app, width=30) 
Text(app, text="Hot Dogs:")  
hot = TextBox(app, width=30) 
Text(app, text="Pizzas:")  
pizza = TextBox(app, width=30)  
button = PushButton(app, text="Calcular", command=calcular_venta)  
app.display()
