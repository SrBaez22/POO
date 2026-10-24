class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.velocidade = 0
        print(f"seu carro é um {self.marca} {self.modelo}")



    def acelerar(self, valor):
        if not isinstance(valor, (int, float)) or isinstance(valor, bool):
           return "valor invalido"
        if valor <= 0:
            return "velocidade nao pode ser negativa"
        self.valor_acelerar = valor
        self.velocidade += valor
        print(f"voce esta a {self.velocidade}k/h")
        return self.velocidade



    def frear(self, valor):
        if not isinstance(valor, (int, float)) or isinstance(valor, bool):
            return "valor invalido"
        if valor <= 0:
            return "nao pode freiar negativo"          
        if self.velocidade == 0:
            print("Carro já parado")
            return 
        if valor > self.velocidade:
            print("erro ao freiar")
            return
        self.velocidade -= valor
        print(f"seu carro diminuiu {valor}k/h")
        return valor


    def exibir_status(self):
        print(f"a sua velocidade está: {self.velocidade} km/h")
        return self.velocidade


carro_1 = Carro("Volkswagen", "Gol")
carro_2 = Carro("chevrolet", "Onix")
carro_1.acelerar(100)
carro_1.frear(80)
carro_2.acelerar(30)