class Animal:
  def __init__(self, nome) -> None:
    self.nome = nome
  def emitir_som(self):
    pass

class mamifero(Animal):
  def amamentar(self):
    return f"{self.nome} está amamentando"

class ave(Animal):
  def voar(self):
    return f"{self.nome} está voando"
  
class Morcego(mamifero, ave):
  def emitir_som(self):
    return "Morcegos emitem sons ultrassônicos"
  
morcego = Morcego(nome="batman")

print("nome do morcego:", morcego.nome)
print("som do morcego:", morcego.emitir_som())

#acessando classes mamifero e ave

print("Morcego amamentando:",morcego.amamentar())
print("morcego voando:", morcego.voar())
