import streamlit as st #alias aka
import pandas as pd

#1. Función de saludo simple: 
def saludo(nombre="Streamlit"):
    return f"¡Hola, {nombre}!"

#2. Suma de dos números
def sumar(a,b):
    return a+b

#3. Área de un triángulo
def calcular_area_triangulo(base, altura):
    return 1/2*base*altura

#4. Calculadora de descuento
def calcular_precio_final(precio, descuento=10, impuesto=16):
    precio_final = precio - precio*descuento/100 + precio*impuesto/100
    return precio_final

#5. Suma de una lista de números
def sumar_lista(lista):
    suma = 0
    for numero in lista:
        suma += numero
    return suma

#6. Funciones con valores predeterminados
def producto(nombre_producto, cantidad=1, precio_unidad=10):
    return nombre_producto,cantidad*precio_unidad

#7. Números pares e impares
def numeros_pares_e_impares(lista):
    pares = []
    impares = []
    for numero in lista:
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)
    return pares, impares

#8. Multiplicación con *args
def multiplicar_todos(*args):
    resultado = 1
    for numero in args:
        resultado *= numero
    return resultado

#9. Información de una persona con **kwargs
def informacion_personal(**kwargs):
    info = ""
    for clave, valor in kwargs.items():
        info += f"{clave}: {valor}\n\n"
    return info.strip()
        

#10. Calculadora flexible
def calculadora_flexible(a, b, operacion="suma"):
    if operacion == "suma":
        return a + b
    elif operacion == "resta":
        return a - b
    elif operacion == "multiplicacion":
        return a * b
    elif operacion == "division":
        if b != 0:
            return a / b
        else:
            return "Error: división por cero"

menu_funciones = ["Saludo", "Suma", "Área de un triángulo", "Calculadora de descuento", "Suma de una lista de números", "Producto", "Números pares e impares", "Multiplicación con *args", "Información personal", "Calculadora flexible"]

st.sidebar.title("Menú de funciones")
opcion = st.sidebar.radio("Selecciona una función", menu_funciones)

if opcion == "Saludo":
    st.title("Función de saludo")
    nombre = st.text_input("Ingresa tu nombre")
    if st.button("Saludar"):
        st.write(saludo(nombre))
    if nombre == "":
        st.write("Ingresa tu nombre")
    if st.button("Saludar sin nombre"):
        st.write(saludo())

elif opcion == "Suma":
    st.title("Suma de dos números")
    num1 = st.number_input("Ingresa el primer número", value=0)
    num2 = st.number_input("Ingresa el segundo número", value=0)
    if st.button("Sumar"):
        st.write(f"La suma de {num1} y {num2} es {sumar(num1, num2)}")

elif opcion == "Área de un triángulo":
    st.title("Área de un triángulo")
    base = st.number_input("Ingresa la base", value=0)
    altura = st.number_input("Ingresa la altura", value=0)
    if st.button("Calcular área"):
        st.write(f"El área del triángulo es {calcular_area_triangulo(base, altura)}")

elif opcion == "Calculadora de descuento":
    st.title("Calculadora de descuento")
    precio = st.number_input("Ingresa el precio", value=0)
    descuento = st.number_input("Ingresa el descuento (%)", value=10)
    impuesto = st.number_input("Ingresa el impuesto (%)", value=16)
    if st.button("Calcular precio final"):
        st.write(f"El precio final es {calcular_precio_final(precio, descuento, impuesto)}")

elif opcion == "Suma de una lista de números":
    st.title("Suma de una lista de números")
    lista = st.text_input("Ingresa una lista de números separados por comas")
    if st.button("Sumar"):
        lista = [int(numero) for numero in lista.split(",")]
        st.write(f"La suma de los números es {sumar_lista(lista)}")

elif opcion == "Producto":
    st.title("Producto")
    nombre_producto = st.text_input("Ingresa el nombre del producto")
    cantidad = st.number_input("Ingresa la cantidad", value=1)
    precio_unidad = st.number_input("Ingresa el precio unitario", value=10)
    if st.button("Calcular precio total"):
        st.write(f"El precio total del producto es {producto(nombre_producto, cantidad, precio_unidad)}")

elif opcion == "Números pares e impares":
    st.title("Números pares e impares")
    lista = st.text_input("Ingresa una lista de números separados por comas")
    if st.button("Clasificar"):
        lista = [int(numero) for numero in lista.split(",")]
        pares, impares = numeros_pares_e_impares(lista)
        st.write(f"Números pares: {pares}")
        st.write(f"Números impares: {impares}")

elif opcion == "Multiplicación con *args":
    st.title("Multiplicación con *args")
    numeros = st.text_input("Ingresa una lista de números separados por comas")

    if st.button("Multiplicar"):
        numeros = [int(numero) for numero in numeros.split(",")]
        st.write(f"El resultado de la multiplicación es {multiplicar_todos(*numeros)}")

elif opcion == "Información personal":
    st.title("Información personal")
    nombre = st.text_input("Ingresa tu nombre")
    edad = st.number_input("Ingresa tu edad", value=0)
    ciudad = st.text_input("Ingresa tu ciudad")

    if st.button("Mostrar información"):
        st.write(informacion_personal(nombre=nombre, edad=edad, ciudad=ciudad))

elif opcion == "Calculadora flexible":
    st.title("Calculadora flexible")
    num1 = st.number_input("Ingresa el primer número", value=0)
    num2 = st.number_input("Ingresa el segundo número", value=0)
    operacion = st.selectbox("Selecciona la operación", ["suma", "resta", "multiplicacion", "division"])
    if st.button("Calcular"):
        st.write(f"El resultado de la operación es {calculadora_flexible(num1, num2, operacion)}")

else:
    st.write("Selecciona una función del menú")






