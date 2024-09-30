
# Proyecto Streamlit: Funciones Variadas

### Autor: Elian Yin Sánchez Ung  
**Fecha**: 29/09/2024  
**Institución**: Universidad de Colima, 3°B

Este código implementa una aplicación interactiva en **Streamlit**, la cual contiene varias funciones de utilidad, desde operaciones matemáticas simples hasta el manejo de listas y entrada de datos. Cada función está integrada en un menú de la barra lateral para que el usuario seleccione y realice diversas operaciones.

## Dependencias
El código requiere las siguientes bibliotecas para su ejecución:
- **Streamlit** (`st`): Para crear la interfaz gráfica de la aplicación web interactiva.
- **Pandas** (`pd`): Aunque importada, no se utiliza en este script, pero se puede usar para manejar estructuras de datos complejas como DataFrames.

```python
import streamlit as st
import pandas as pd
```

## Funciones Definidas

### 1. `saludo(nombre="Streamlit")`
Función que retorna un saludo personalizado o un saludo genérico si no se proporciona nombre.
```python
def saludo(nombre="Streamlit"):
    return f"¡Hola, {nombre}!"
```

### 2. `sumar(a, b)`
Suma dos números y devuelve el resultado.
```python
def sumar(a, b):
    return a + b
```

### 3. `calcular_area_triangulo(base, altura)`
Calcula el área de un triángulo usando la fórmula:
\[ 	ext{Área} = rac{1}{2} 	imes 	ext{base} 	imes 	ext{altura} \]
```python
def calcular_area_triangulo(base, altura):
    return 1/2 * base * altura
```

### 4. `calcular_precio_final(precio, descuento=10, impuesto=16)`
Calcula el precio final después de aplicar un descuento e impuesto.
- **precio**: Precio base del producto.
- **descuento**: Porcentaje de descuento (predeterminado 10%).
- **impuesto**: Porcentaje de impuesto (predeterminado 16%).
```python
def calcular_precio_final(precio, descuento=10, impuesto=16):
    precio_final = precio - precio * descuento / 100 + precio * impuesto / 100
    return precio_final
```

### 5. `sumar_lista(lista)`
Suma todos los elementos de una lista de números.
```python
def sumar_lista(lista):
    suma = 0
    for numero in lista:
        suma += numero
    return suma
```

### 6. `producto(nombre_producto, cantidad=1, precio_unidad=10)`
Calcula el costo total de un producto dado su cantidad y precio por unidad.
```python
def producto(nombre_producto, cantidad=1, precio_unidad=10):
    return nombre_producto, cantidad * precio_unidad
```

### 7. `numeros_pares_e_impares(lista)`
Clasifica una lista de números en pares e impares.
```python
def numeros_pares_e_impares(lista):
    pares = []
    impares = []
    for numero in lista:
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)
    return pares, impares
```

### 8. `multiplicar_todos(*args)`
Multiplica una lista arbitraria de números utilizando `*args`.
```python
def multiplicar_todos(*args):
    resultado = 1
    for numero in args:
        resultado *= numero
    return resultado
```

### 9. `informacion_personal(**kwargs)`
Genera una cadena de texto con información personal basada en argumentos clave-valor.
```python
def informacion_personal(**kwargs):
    info = ""
    for clave, valor in kwargs.items():
        info += f"{clave}: {valor}\n\n"
    return info.strip()
```

### 10. `calculadora_flexible(a, b, operacion="suma")`
Realiza una operación matemática (suma, resta, multiplicación o división) según el parámetro especificado.
```python
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
```

## Interfaz de Usuario

El menú de la aplicación está disponible en la barra lateral de **Streamlit**. Los usuarios pueden seleccionar una función y realizar las operaciones interactivas correspondientes.

- **Menú de Funciones**: Se ofrece un listado con 10 opciones, cada una de las cuales activa una funcionalidad específica.
  
### Ejemplo: Selección de Funciones
La interfaz permite ingresar valores numéricos, seleccionar operaciones, y mostrar los resultados de forma dinámica. Cada función está ligada a un bloque de código condicional que se activa según la opción seleccionada por el usuario.

```python
opcion = st.sidebar.radio("Selecciona una función", menu_funciones)

if opcion == "Saludo":
    # Implementación del saludo interactivo...
```

## Comentarios Finales

Este script es un ejemplo básico de cómo combinar **Streamlit** con funciones de Python para crear aplicaciones web interactivas con capacidades variadas.
