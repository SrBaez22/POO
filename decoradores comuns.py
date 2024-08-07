#@classmethod
#@staticmethod

class MinhaClasse:
  valor = 10 #atributo de classe
  def __init__(self, nome) -> None:
    self.nome = nome #Atributo de instancia
  
  #requer uma instancia para ser chamado
  def metodo_instancia(self):
    return f"metodo de instancia chamado para {self.valor}"
  
  @classmethod
  def metodo_classe(cls):
    return f"metodo da classe chamado para valor={cls.valor}"
  
  @staticmethod
  def metodo_estatico():
    return "método estático chamado"



obj = MinhaClasse(nome="Classe exemplo")
print(obj.metodo_instancia())
print(MinhaClasse.valor)
print(MinhaClasse.metodo_classe())
print(MinhaClasse.metodo_estatico())

class Carro:
  def __init__(self, marca, modelo, ano) -> None:
    self.marca = marca
    self.modelo = modelo
    self.ano = ano

  @classmethod
  def criar_carro(cls, configuracao):
    marca, modelo, ano = configuracao.split(",")
    return cls(marca, modelo, int(ano))

configuracao1 = "Toyota,Corolla,2022"
carro1 = Carro.criar_carro(configuracao1)
print(f"marca: {carro1.marca}\nmodelo: {carro1.modelo}\nano: {carro1.ano}")

class Matematica:
  @staticmethod
  def somar(a, b):
    return a + b
print(Matematica.somar(a=8, b=4))

  