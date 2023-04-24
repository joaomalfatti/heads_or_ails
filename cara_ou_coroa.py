import random

def cara_ou_coroa():
    # Gera um número aleatório entre 0 e 1
    resultado = random.randint(0, 1)
    
    # Se o resultado for 0, é cara, caso contrário é coroa
    if resultado == 0:
        return "cara"
    else:
        return "coroa"
    
# Pede ao jogador para escolher cara ou coroa
escolha = input("Escolha cara ou coroa: ")

# Joga a moeda e obtém o resultado
resultado = cara_ou_coroa()

# Verifica se a escolha do jogador corresponde ao resultado da moeda
if escolha == resultado:
    print("Você ganhou!")
else:
    print("Você perdeu!")
