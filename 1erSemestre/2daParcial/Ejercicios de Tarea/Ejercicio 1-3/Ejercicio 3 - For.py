# Ejercicio 3 - Estructura For

sum = 1

n: int = int(input("Ingrese un número: "))

while n<=0:
    print("El  número ingresado es erroneo")
    n = int(input("Ingrese un número: "))

for i in range(n):
   i+=1
   sum = (sum*i)*2
print(f"El producto total es: {sum}")