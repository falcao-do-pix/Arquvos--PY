# Escreve os números no arquivo "crescente.txt"
with open('crescente.txt', 'w') as arquivo:
    for i in range(1, 101):
        arquivo.write(str(i))
        # Adiciona um ';' se não for o último número
        if i != 100:
            arquivo.write(';')

print("Arquivo 'crescente.txt' criado com sucesso!")
