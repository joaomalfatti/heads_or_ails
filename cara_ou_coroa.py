import random

def cara_ou_coroa():
    resultado = random.randint(0, 1)
    if resultado == 0:
        return "cara"
    else:
        return "coroa"

escolha = ""
while escolha not in ["cara", "coroa"]:
    escolha = input("Escolha cara ou coroa: ")
    escolha = escolha.lower()

resultado = cara_ou_coroa()

if escolha == resultado:
    print("Você ganhou!")
else:
    print("Você perdeu!")
