# 2. Escribir una función que calcule el mínimo común múltiplo entre dos números

def calcular_mcm(a, b):
    mcd = calcular_mcd(a, b)
    return (a * b) // mcd

def calcular_mcd(a, b):
    while b:
        a, b = b, a % b
    return a

numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))

mcm = calcular_mcm(numero1, numero2)
print(f"El mínimo común múltiplo entre {numero1} y {numero2} es {mcm}")
