classe Personagem:
  def __init__ (self, nome:str, vida:int):
    self.nome = nome
    self.vida = vida
  def Tomar_dano(self, valor:int):
    self.vida == valor
classe Mago(Personagem):
    def __init__(self, nome: str, vida: int, mana: float):
        super().__init__(nome, vida)
        self.mana = float(mana)
    def __str__(self):
      return f"Mago: {self.nome} | Vida: {self.vida} ​​| Mana: {self.mana}"
    def __add__(self, valor: float):
      auto.mana += valor
      retornar self.mana
    def __sub__(self, valor: float):
      self.mana -= valor
      se self.mana < 0:
        self.mana = 0.0
      retornar self.mana
    def __mul__(self, fator:float):
      self.mana *= fator
      retornar self.mana
      
    def __truediv__(self, valor:float):
      se valor == 0:
        print("Erro: Não é possível dividir a mana por zero!")
        retornar self.mana
      outro:
        self.mana = self.mana / valor
        retornar self.mana
classe Barbaro(Personagem):
  def __init__(self, nome: str, vida: int, stamina: float, furia: bool):
    super().__init__(nome, vida)
    auto.resistência = resistência
    self.furia = fúria
  def __str__(self):
    return f"Bárbaro: {self.nome} | {self.vida} ​​| stamina: {self.stamina} | furia: {self.furia}"
  def __add__(self, valor):
      self.furia = self.furia + valor
      retornar self.furia
  def __sub__(self, valor: float):
    auto.resistência = auto.resistência - valor
    Se self.stamina == 0 e self.furia == falso:
      self.furia == verdadeiro
      resistência própria = 5
      print("O guerreiro entrou na FÚRIA! Stamina subiu para 5.0")
    retornar auto.stamina
  def __mul__(self, fator: float):
    self.furia = self.furia * fator
    retornar self.furia
  def __truediv__(self, valor):
    self.furia = self.furia / valor
    se valor == 0:
      print("Erro: Não dá para dividir por zero!")
    retornar self.furia

print("=== CRIAR PERSONAGEM ===")
nome_usuario = input("Qual o nome do personagem? ")
vida_usuario = int(input("Quanta vida ele vai ter? "))
tipo_classe = input("Escolha a classe (Mago ou Bárbaro): ")
if tipo_classe == "mago" ou tipo_classe == "Mago":
  mana_usuario = float(input("Quanta mana inicial? "))
    jogador = Mago(nome_usuario, vida_usuario, mana_usuario)
outro:
    furia_usuario = float(input("Quanta fúria inicial? "))
    jogador = Bárbaro(nome_usuario, vida_usuario, furia_usuario)

print("Personagem criado!")
enquanto jogador.vida > 0:
    imprimir(jogador)
    
    print("O que você quer fazer?")
    print("1 - Tomar poção simples")
    print("2 - Tomar poção especial")
    print("3 - Usar ataque básico")
    print("4 - Usar ataque especial")
    print("5 - Sair do jogo")
    opcao = input("Escolha o número da opção: ")
    se opcao == "1":
        jogador + 5
        print("Você tomou uma poção simples! (+5)")
    elif opcao == "2":
        jogador * 1,5
        print("Você tomou uma poção especial! (*1.5)")
    elif opcao == "3":
        jogador - 2
        print("Você usou o ataque básico! (-2)")
    elif opcao == "4":
        jogador / 2
        print("Você usou o ataque especial! (/2)")
    elif opcao == "5":
        print("Você saiu do jogo.")
        quebrar
    outro:
        print("Opção inválida!")
    dano_do_monstro = random.randint(1, 10)
    jogador.tomar_dano(dano_do_monstro)
      rint("Um monstro te arrancou e jogou " + str(dano_do_monstro) + " de vida!")
se jogador.vida <= 0:
    print("\nSua vida acabou... Fim de jogo!")





