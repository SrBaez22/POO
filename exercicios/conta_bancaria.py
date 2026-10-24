class ContaBancaria:
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"voce adocionou {valor} na sua conta")
        else:
            print("valor invalido")
    def sacar(self, valor):
        if valor <= 0:
            print("erro ao sacar")
        elif valor > self.saldo:
            print("valor insuficiente")
        else:
            self.saldo -= valor
            return valor

    def consultar_saldo(self):
        print(f"Titular: {self.titular}")
        return self.saldo
        

        
pessoa1 = ContaBancaria('sergio')
pessoa1.depositar(500)
pessoa1.sacar(200)
pessoa1.consultar_saldo()