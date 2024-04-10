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

        # Calcula a nota mínima e máxima
        nota_minima = min(notas)
        nota_maxima = max(notas)

        # Imprime o nome, nota mínima e nota máxima
        print(f'O estudante {nome} teve nota mínima {nota_minima} e nota máxima {nota_maxima}')

if __name__ == "__main__":
    main()
