#Exemplo de herança
print("\nExemplo de herança")

class Animal:
  def __init__(self, nome) -> None:
    self.nome = nome
  def andar(self):
    print(f"o animal{self.nome} andou")
    pass
  def emitir_som(self):
    pass

class Cachorro(Animal):
  def emitir_som(self):
    return "au au"
  
class gato(Animal):
  def emitir_som(self):
    return "miau miau"
  
dog = Cachorro(nome="Rex")
cat = gato(nome = "negro")

print("\nExemplo de polimorfismo")
animais = [dog, cat]
for animal in animais:
  print(f"{animal.nome} faz {animal.emitir_som()}")

print("Exemplo de encapsulamento:")
class conta_bancária:
  def __init__(self, saldo) -> None:
    self.__saldo = saldo #Atributo privado
  def depositar(self, valor):
    if valor > 0:
      self.__saldo += valor
  def sacar_valor(self, valor):
    if valor > 0 and valor <= self.__saldo:
      self.__saldo -= valor
  def consultar_saldo(self):
    return self.__saldo

conta = conta_bancária(saldo=1000)
print(F"Saldo da conta é de {conta.consultar_saldo()}")
conta.depositar(valor=500)
print(F"Saldo da conta é de {conta.consultar_saldo()}")
conta.depositar(valor=500)
print(F"Saldo da conta é de {conta.consultar_saldo()}")
conta.sacar_valor(valor=1000)
print(F"Saldo da conta é de {conta.consultar_saldo()}")

#Abstração
print("exemplo de abstração")
from abc import ABC, abstractmethod
class Veículo(ABC):
  @abstractmethod
  def ligar(self):
    pass

  @abstractmethod
  def desligar(self):
    pass

class carro(Veículo):
  def __init__(self) -> None:
    super().__init__()
  def ligar(self):
    return "O carro ligou usando a chave"
  def desligar(self):
    return "Carro desligado usando a chave"

carro_amarelo = carro()
print(carro_amarelo.ligar())
print(carro_amarelo.desligar())