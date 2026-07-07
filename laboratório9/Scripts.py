#questão 01

primeiro_nome = input("Digite seu primeiro nome: ").strip()
sobrenome = input("Digite seu sobrenome: ").strip()
print(f"Bem-vinda, {primeiro_nome} {sobrenome}!")

#questão 02

frase = input("Digite a frase: ")
contador = 0
for caractere in frase:
    if caractere == " ":
        contador = contador + 1
print("Espaços em branco:", contador)

#questão 03

nome = input("Digite seu nome: ")
escada = ""
for letra in nome:
    escada = escada + letra
    print(escada)cs

#questão 04 

if len(num) == 9:
    if num[0] == "9":  
        print(f"Número Completo: {num[:5]}-{num[5:]}")
    else:
        print("Número Incorreto!")
elif len(num) == 8:
    print(f"Número Completo: 9{num[:4]}-{num[4:]}")
else:
    print("Número Errado!")

#questão 5

quantidade = 0
for i, letra in enumerate(txt):
    if letra in "AEIOUaeiou":
        ind.append(i)
        qnt += 1
print(f"Índices: {", ".join(ind)}")
print("Total:",quantidade)
    
