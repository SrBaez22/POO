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