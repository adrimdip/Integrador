""" 4.Escribir una función que reciba una cadena de caracteres y devuelva un diccionario con cada 
palabra que contiene y la cantidad de veces que aparece (frecuencia). Escribir otra función 
que reciba el diccionario generado con la función anterior y devuelva una tupla con la 
palabra más repetida y su frecuencia
 """
def contar_palabras(cadena):
    palabras = cadena.split()
    frecuencia = {}

    for palabra in palabras:
        palabra = palabra.lower()
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1

    return frecuencia

def palabra_mas_repetida(diccionario):
    palabra_max = max(diccionario, key=diccionario.get)
    frecuencia_max = diccionario[palabra_max]
    return palabra_max, frecuencia_max

cadena = "hola hola hola mundo mundo ejemplo ejemplo ejemplo ejemplo"
resultado = contar_palabras(cadena)

print("Frecuencia de palabras:")
for palabra, cantidad in resultado.items():
    print(f"'{palabra}': {cantidad}")

palabra, frecuencia = palabra_mas_repetida(resultado)
print(f"Palabra más repetida: '{palabra}' con una frecuencia de {frecuencia}")

