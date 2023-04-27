import random

# Perguntar ao usuário quantos números devem ser sorteados
num_sorteados = int(input("Quantos números deseja sortear? "))

# Perguntar ao usuário os limites do intervalo de sorteio
limite_inf = int(input("Qual o valor mínimo do intervalo? "))
limite_sup = int(input("Qual o valor máximo do intervalo? "))

# Sortear os números aleatórios
sorteados = []
for i in range(num_sorteados):
    sorteados.append(random.randint(limite_inf, limite_sup))

# Exibir os números sorteados
print(f"Os {num_sorteados} números sorteados entre {limite_inf} e {limite_sup} foram:")
for i in sorteados:
    print(i)

# Perguntar ao usuário se deseja salvar os números sorteados em um arquivo
salvar_arquivo = input("Deseja salvar os números sorteados em um arquivo? (s/n) ").lower()
if salvar_arquivo == "s":
    nome_arquivo = input("Digite o nome do arquivo: ")
    with open(nome_arquivo, "w") as arquivo:
        for i in sorteados:
            arquivo.write(str(i) + "\n")
    print("Números sorteados salvos com sucesso!")
elif salvar_arquivo == "n":
    print("Os números sorteados não foram salvos em um arquivo.")
else:
    print("Opção inválida. Os números sorteados não foram salvos em um arquivo.")
