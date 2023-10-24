# Ejercicio 4 - Estructura While

sum = 0
i = 0

n: int = int(input("Ingrese un número: "))

while n<=0:
    print("El  número ingresado es erroneo")
    n = int(input("Ingrese un número: "))

while i<n:
   sum += (i+1)**3
   i+=1
print(f"La suma total es: {sum}")
