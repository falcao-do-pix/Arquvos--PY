def calcular_media(notas):
    return sum(notas) / len(notas)

def main():
    # Abre o arquivo notas.txt para leitura
    with open('notas.txt', 'r') as arquivo:
        linhas = arquivo.readlines()

    # Processa cada linha do arquivo
    for linha in linhas:
        # Divide a linha em nome e notas (separadas por vírgula)
        partes = linha.strip().split(',')
        nome = partes[0]
        notas = [float(nota) for nota in partes[1:]]

        # Calcula a média das notas
        media = calcular_media(notas)

        # Imprime o nome e a média
        print(f'O estudante {nome} teve média {media:.2f}')

if __name__ == "__main__":
    main()
