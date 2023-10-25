# Ejercicio 1 - Estructura For

sum = 0
i = 0

n: int = int(input("Ingrese un número: "))

while n<=0:
    print("El  número ingresado es erroneo")
    n = int(input("Ingrese un número: "))

for i in range(n):
   sum += (i+1)*2
print(f"La suma total es: {sum}")
