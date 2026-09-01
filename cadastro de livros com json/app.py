import json
import os

ARQUIVO = "livros.json"

# Lista para armazenar os empréstimos
emprestimos = []


# Carrega os livros do arquivo JSON
def carregar_livros():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    return []


# Salva os livros no arquivo JSON
def salvar_livros(livros):
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(livros, arquivo, indent=4, ensure_ascii=False)


# Cadastrar livro
def cadastrar_livro(livros):
    if len(livros) >= 5:
        print("\nLimite de 5 livros atingido!")
        return

    titulo = input("Título: ")
    autor = input("Autor: ")

    livro = {
        "titulo": titulo,
        "autor": autor
    }

    livros.append(livro)
    salvar_livros(livros)

    print("\nLivro cadastrado com sucesso!")


# Exibir livros
def exibir_livros(livros):
    if len(livros) == 0:
        print("\nNenhum livro cadastrado.")
        return

    print("\nLivros cadastrados:")
    for i, livro in enumerate(livros, start=1):
        print(f"{i} - {livro['titulo']} ({livro['autor']})")


# Realizar empréstimo
def emprestar_livro(livros):
    if len(livros) == 0:
        print("\nNão há livros cadastrados.")
        return

    exibir_livros(livros)

    try:
        opcao = int(input("\nDigite o número do livro: "))

        if 1 <= opcao <= len(livros):
            livro = livros[opcao - 1]
            emprestimos.append(livro)
            print(f"\nO livro '{livro['titulo']}' foi emprestado.")
        else:
            print("\nLivro inválido.")

    except ValueError:
        print("\nDigite um número válido.")


# Mostrar livros emprestados
def mostrar_emprestados():
    if len(emprestimos) == 0:
        print("\nNenhum livro emprestado.")
        return

    print("\nLivros emprestados:")
    for livro in emprestimos:
        print(f"- {livro['titulo']}")


# Programa principal
def main():
    livros = carregar_livros()

    while True:
        print("\n===== BIBLIOTECA =====")
        print("1 - Cadastrar livro")
        print("2 - Exibir livros")
        print("3 - Realizar empréstimo")
        print("4 - Mostrar livros emprestados")
        print("5 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            cadastrar_livro(livros)

        elif opcao == "2":
            exibir_livros(livros)

        elif opcao == "3":
            emprestar_livro(livros)

        elif opcao == "4":
            mostrar_emprestados()

        elif opcao == "5":
            print("\nEncerrando...")
            break

        else:
            print("\nOpção inválida.")


main()