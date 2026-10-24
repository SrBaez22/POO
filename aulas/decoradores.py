from typing import Any


def meu_decorador(func):
  def wrapper():
    print("Antes da minha função ser chamamda")
    func()
    print("Depois da minha função ser chamamda")
  return wrapper

@meu_decorador
def mimha_funcao():
  print("minha função foi chamada")

mimha_funcao()

class MeuDecoradorDeClasse():
  def __init__(self, func) -> None:
    self.func = func

  def __call__(self) -> Any:
    print("antes da função ser chamada (decorador de classe)")
    self.func()
    print("depois da função ser chamada(decorador de classe)")
    pass
@MeuDecoradorDeClasse
def segunda_funcao():
  print("segunda função foi chamada")

segunda_funcao()
    