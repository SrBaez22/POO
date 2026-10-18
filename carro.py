class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.velocidade = 0

    def acelerar(self, valor):

        try:
            self.velocidade += valor
            print(f"seu carro é um {self.marca} {self.modelo}")
            return f"voce esta a {self.velocidade}k/h"
        except e:
            print(f"{e}")
    def frear(self, valor):
        self.velocidade -= valor
        return f"seu carro diminuiu {self.velocidade}k/h"


    def exibir_status(self):
        if self.velocidade < 0:
            print("a velocidade nao pode ser negativa")
            return "Error"
        return f"a sua velocidade está: {self.velocidade} km/h"


carro1 = Carro("volkswagen", "gol")
print(carro1.acelerar(400))
print(carro1.frear(300))
print(carro1.exibir_status())