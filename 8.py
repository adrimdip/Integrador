""" 8. Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase 
CuantaJoven que deriva de la clase creada en el punto 7. Cuando se crea esta nueva clase, 
además del titular y la cantidad se debe guardar una bonificación que estará expresada en 
tanto por ciento. Crear los siguientes métodos para la clase:
 Un constructor.
 Los setters y getters para el nuevo atributo.
 En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, por lo 
tanto hay que crear un método es_titular_valido() que devuelve verdadero si el titular es 
mayor de edad pero menor de 25 años y falso en caso contrario.
 Además, la retirada de dinero sólo se podrá hacer si el titular es válido.
 El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la 
cuenta
 """
class Persona:
    def __init__(self, nombre=None, edad=None, dni=None):
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = dni

    def set_nombre(self, nombre):
        if isinstance(nombre, str) and len(nombre) > 0:
            self.__nombre = nombre
        else:
            print("Error: Nombre inválido")

    def get_nombre(self):
        return self.__nombre

    def set_edad(self, edad):
        if isinstance(edad, int) and edad >= 0:
            self.__edad = edad
        else:
            print("Error: Edad inválida")

    def get_edad(self):
        return self.__edad

    def set_dni(self, dni):
        if isinstance(dni, str) and len(dni) == 9:
            self.__dni = dni
        else:
            print("Error: DNI inválido")

    def get_dni(self):
        return self.__dni


class Cuenta:
    def __init__(self, titular=None, cantidad=0.0):
        self.__titular = titular
        self.__cantidad = cantidad

    def set_titular(self, titular):
        if isinstance(titular, Persona):
            self.__titular = titular
        else:
            print("Error: Titular inválido")

    def get_titular(self):
        return self.__titular

    def get_cantidad(self):
        return self.__cantidad

    def mostrar(self):
        print("Titular:", self.__titular.get_nombre() if self.__titular else "N/A")
        print("Cantidad:", self.__cantidad)

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.__cantidad += cantidad

    def retirar(self, cantidad):
        if cantidad > 0:
            self.__cantidad -= cantidad


class CuentaJoven(Cuenta):
    def __init__(self, titular=None, cantidad=0.0, bonificacion=0.0):
        super().__init__(titular, cantidad)
        self.__bonificacion = bonificacion

    def set_bonificacion(self, bonificacion):
        if bonificacion >= 0:
            self.__bonificacion = bonificacion
        else:
            print("Error: Bonificación inválida")

    def get_bonificacion(self):
        return self.__bonificacion

    def es_titular_valido(self):
        if self.get_titular() and self.get_titular().get_edad():
            return 18 <= self.get_titular().get_edad() < 25
        return False

    def retirar(self, cantidad):
        if self.es_titular_valido():
            super().retirar(cantidad)
        else:
            print("Error: No se puede retirar dinero debido a que el titular no es válido.")

    def mostrar(self):
        super().mostrar()
        print("Tipo de cuenta: Cuenta Joven")
        print("Bonificación:", self.__bonificacion, "%")



persona_joven = Persona("Ana", 20, "987654321")
cuenta_joven = CuentaJoven(persona_joven, 500.0, 5.0)
cuenta_joven.mostrar()

cuenta_joven.retirar(100)  # Intenta retirar dinero con un titular válido
cuenta_joven.retirar(200)  # Intenta retirar dinero con un titular no válido

cuenta_joven.mostrar()

