"""7. Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una 
persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es 
opcional. Crear los siguientes métodos para la clase:
 Un constructor, donde los datos pueden estar vacíos.
 Los setters y getters para cada uno de los atributos. El atributo no se puede modificar 
directamente, sólo ingresando o retirando dinero.
 mostrar(): Muestra los datos de la cuenta.
 ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es 
negativa, no se hará nada.
 retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números 
rojos. """

class Cuenta:
    def __init__(self, titular, cantidad=0.0):
        self.titular = titular
        self.__cantidad = cantidad  # Atributo privado


    def get_titular(self):
        return self.titular
    
    def get_cantidad(self):
        return self.__cantidad
    
    def set_cantidad(self, cantidad):
        if cantidad >= 0:
            self.__cantidad = cantidad

    def mostrar(self):
        print(f"Titular: {self.titular}")
        print(f"Cantidad: {self.__cantidad}")
    
    def ingresar(self, cantidad):
        if cantidad > 0:
            self.__cantidad += cantidad
    
    def retirar(self, cantidad):
        if cantidad > 0:
            self.__cantidad -= cantidad


cuenta1 = Cuenta("Juan Pérez")
cuenta1.mostrar()

cuenta1.ingresar(1000)
cuenta1.retirar(200)
cuenta1.mostrar()

cuenta1.set_cantidad(1500)
cuenta1.mostrar()

titular = cuenta1.get_titular()
print("Titular:", titular)

cantidad = cuenta1.get_cantidad()
print("Cantidad:", cantidad)

