# Cree una clase de Python llamada Usuario que use el método init y cree un nombre de usuario y una contraseña. 
# Crea un objeto usando la clase.

class Usuario:
    def __init__(self, usuario, password):
        self.usuario = usuario
        self.password = password

    def mostrar_datos(self):
        print(f"Tu usuario es {self.usuario}")

usuario1 = Usuario("Patricia", "1234")

usuario1.mostrar_datos()
