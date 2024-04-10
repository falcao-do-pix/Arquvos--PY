# Escreve os números no arquivo "decrescente.txt"
with open('decrescente.txt', 'w') as arquivo:
    for i in range(100, 0, -1):
        arquivo.write(str(i))
        arquivo.write('\n')

print("Arquivo 'decrescente.txt' criado com sucesso!")
