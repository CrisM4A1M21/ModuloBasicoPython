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


class CarroVolador(Carro):
    ruedas = 6

    def __init__(self, color, aceleracion, estado_volando = False):
        super().__init__(color, aceleracion)
        self.estadoVolando = estado_volando

    def vuela(self):
        self.estadoVolando = True

    def aterrizar(self):
        self.estadoVolando = False


carro_1 = Carro("Rojo", 70)
carro_V = CarroVolador("Blanco", 100)

print("Color carro_V: {}".format(carro_V.color))
print("Estado inicial de mi carro volador es: {}".format(carro_V.estadoVolando))


carro_V.acelerar()
print("Carro volador velocidad: {}".format(carro_V.velocidad))
