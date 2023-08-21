""" 5. Sabiendo que ValueError es la excepción que se lanza cuando no podemos convertir una 
cadena de texto en su valor numérico, escriba una función get_int() que lea un valor entero 
del usuario y lo devuelva, iterando mientras el valor no sea correcto. Intente resolver el 
ejercicio tanto de manera iterativa como recursiva
 """
#Iterativa
def get_int():
    while True:
        try:
            user_input = input("Ingrese un valor entero: ")
            value = int(user_input)
            return value
        except ValueError:
            print("Error: No es un valor entero válido. Intente nuevamente.")

resultado = get_int()
print("El valor entero ingresado es:", resultado)


#Recursiva
def get_int_recursive():
    try:
        user_input = input("Ingrese un valor entero: ")
        value = int(user_input)
        return value
    except ValueError:
        print("Error: No es un valor entero válido. Intente nuevamente.")
        return get_int_recursive()


resultado = get_int_recursive()
print("El valor entero ingresado es:", resultado)
