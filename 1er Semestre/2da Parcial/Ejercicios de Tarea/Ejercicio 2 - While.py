# Ejercicio 2 - Estructura While

sum = 1
i=0

n: int = int(input("Ingrese un número: "))

while n<=0:
    print("El  número ingresado es erroneo")
    n = int(input("Ingrese un número: "))

while i<n:
   i+=1
   sum = sum*i
print(f"El producto total es: {sum}")
