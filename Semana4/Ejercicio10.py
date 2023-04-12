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

carro_1 = Carro("Negro", 50)

print("El color de mi primer carro es: {}".format(carro_1.color))

carro_2 = Carro("Rojo", 80)
carro_2.marchas = 30000

print("El numero de marchas de mi segundo carro es: {}".format(carro_2.marchas))