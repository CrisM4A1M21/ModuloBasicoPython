"""Creacion del objeto"""
class Carro:
    ruedas = 4

    def __init__(self, color, aceleracion):
        self.color = color
        self.aceleracion = aceleracion
        self.velocidad = 0

    def acelerar(self):
        self.velocidad = self.velocidad + self.aceleracion

    def frena(self):
        velocidad = self.velocidad - self.aceleracion
        if velocidad < 0:
            velocidad = 0
        self.velocidad = velocidad


"""Instanciacion del objeto"""

carro_1 = Carro("Azul", 50)
print("El color del primer carro es {}".format(carro_1.color))
print("La aceleracion del primer carro es {}".format(carro_1.aceleracion))

carro_2 = Carro("Rojo", 70)
print("El color del segundo carro es {}".format(carro_2.color))
print("La aceleracion del segundo carro es {}".format(carro_2.aceleracion))
