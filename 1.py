# 1. Escribir una función que calcule el máximo común divisor entre dos números.

def calcular_mcd(a, b):
    while b:
        a, b = b, a % b
    return a

numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))

mcd = calcular_mcd(numero1, numero2)
print(f"El máximo común divisor entre {numero1} y {numero2} es {mcd}")