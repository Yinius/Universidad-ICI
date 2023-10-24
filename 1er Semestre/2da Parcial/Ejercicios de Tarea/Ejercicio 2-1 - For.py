# Ejercicio 2-1 - For - Obten el producto de 2 números enteros positivos mediante sumas sucesivas

res = 0

print("Programa que obtiene multiplicaciónes usando sumas")
n1: int = int(input("Ingrese un número 1: "))

while n1<=0:
    print("El  número ingresado es erroneo")
    n1 = int(input("Ingrese un número 1: "))

n2: int = int(input("Ingrese un número 2: "))

while n2<=0:
    print("El  número ingresado es erroneo")
    n2 = int(input("Ingrese el número 2: "))

for i in range(n2):
   res += n1
print(f"El producto total es: {res}")
