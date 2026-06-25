classe Pessoa:
  def __init__ (self, nome: str, altura: float):
    self.nome = nome
    self.altura = float(altura)
  def __str__(self):
    return f"Nome: {self.nome} | Altura: {self.altura}"
  def __gt__(self, other):
    retorne self.altura > other.altura
  def __lt__(self, other):
    retornar self.altura <outro.altura
    
lst = []
D = int(input("Quantas pessoas estão cadastradas?"))
para i em range(D):
  nome = input("Qual o nome da pessoa?")
  h = float("Qual a altura da pessoa?")
  p = Pessoa(nome, h)
  lista.append(p)
imprimir('MAIOR:', max(lst))
imprimir('MENOR:', min(lst))
para pessoa em sorted(lst):
  imprimir(pessoa)

