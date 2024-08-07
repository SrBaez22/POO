import random
#Personagem: classe mãe
#Héroi: controlado pelo usuário
#inimigo: adversário do usuário
class Personagem:
  def __init__(self, nome, vida, nivel):
    self.__nome = nome
    self.__vida = vida
    self.__nivel = nivel

  def get_nome(self):
    return self.__nome
  
  def get_vida(self):
    return  self.__vida

  def get_nivel(self):
    return self.__nivel
  
  def exibir_detalhes(self):
    return f"nome: {self.get_nome()}\nVida: {self.get_vida()}\nNível: {self.get_nivel()}"

  def receber_ataque(self, dano):
    self.__vida -= dano
    if self.__vida < 0:
      self.__vida = 0

  def atacar(self, alvo):
    dano = random.randint(self.get_nivel() * 2, self.get_nivel() * 4) #Baseado no nível
    alvo.receber_ataque(dano)
    print(f"{self.get_nome()} atacou {alvo.get_nome()} e causou {dano} de dano!")

class Heroi(Personagem):
  def __init__(self, nome, vida, nivel, habilidade):
    super().__init__(nome, vida, nivel)
    self.__habilidade = habilidade

  def get_habilidade(self):
    return self.__habilidade
  
  def exibir_detalhes(self):
    return f"{super().exibir_detalhes()}\nHabilidade: {self.__habilidade}\n"
  
  def ataque_especial(self, alvo):
    dano = random.randint(self.get_nivel() * 5, self.get_nivel() * 8)
    alvo.receber_ataque(dano)
    print(f"{self.get_nome()} executou o ataque especial {self.get_habilidade()} em {alvo.get_nome()} e causou {dano} de dano!")


class Inimigo(Personagem):
  def __init__(self, nome, vida, nivel, tipo):
    super().__init__(nome, vida, nivel)
    self.__tipo = tipo

  def get_tipo(self):
    return self.__tipo
  
  def exibir_detalhes(self):
    return f"{super().exibir_detalhes()}\nTipo: {self.__tipo}"
  
class Jogo:
  """Classe orquestradora do jogo"""
  def __init__(self):
    self.heroi = Heroi(nome="Herói", vida=100, nivel=5, habilidade="Super Força")
    self.inimigo = Inimigo(nome="morcego", vida=100, nivel=5, tipo="voador")  
  
  def iniciar_batalha(self):
    """Fazer gestão da batalha em turnos"""
    print("Iniciando batalha")
    while self.heroi.get_vida() > 0 and self.inimigo.get_vida() > 0:
      print("\nDetalhe dos personagens")
      print(self.heroi.exibir_detalhes())
      print(self.inimigo.exibir_detalhes())

      input("Pressione enter para atacar...")
      escolha = input("Escolha (1 - Ataque normal, 2 - Ataque especial): ")
      if escolha == "1":
        self.heroi.atacar(self.inimigo)

      elif escolha == "2":
        self.heroi.ataque_especial(self.inimigo)
      
      else:
        print("Escolha inválida. Escolha novamente")
      
      if self.inimigo.get_vida() > 0:
        self.inimigo.atacar(self.heroi)
        
    if self.heroi.get_vida() > 0:
      print("Parabéns, você venceu!")
    else:
      print("Você foi derrotado.")

#Instância do jogo em iniciar batalha
jogo = Jogo()
jogo.iniciar_batalha()
  
