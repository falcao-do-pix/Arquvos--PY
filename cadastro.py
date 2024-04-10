def cadastrar_aluno():
    # Solicita informações do aluno
    nome = input("Digite o nome do aluno: ")
    email = input("Digite o email do aluno: ")
    curso = input("Digite o curso do aluno: ")

    # Cria uma string com os dados do aluno
    aluno_info = f"Nome: {nome}\nEmail: {email}\nCurso: {curso}\n"

    # Salva os dados do aluno em um arquivo
    with open('alunos.txt', 'a') as arquivo:
        arquivo.write(aluno_info)
        arquivo.write("-" * 20 + "\n")  # Separador entre registros

    print("Aluno cadastrado com sucesso!")

def main():
    while True:
        # Menu de opções
        print("\n--- Menu ---")
        print("1. Cadastrar aluno")
        print("2. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_aluno()
        elif opcao == '2':
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
