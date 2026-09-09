import sqlite3

banco = sqlite3.connect("filmes.db")

cursor = banco.cursor()

cursor.execute("""
  CREATE TABLE IF NOT EXISTS filmes(
    id INT PRIMARY KEY,
    nome VARCHAR(50),
    genero VARCHAR(50),
    classificacao INT
    );
""")

while True:
  print("\n---Menu---")
  print("1 - Cadastrar filme")
  print("2 - Listar filmes")
  print("3 - Alterar filme")
  print("4 - Excluir filme")
  print("5 - Sair")

  opcao = int(input("Digite uma opção: "))

  if opcao == 1:
    id = int(input("Digite o id: "))
    nome = input("Digite o nome do filme: ")
    genero = input("Digite o gênero do filme: ")
    classificacao = int(input("Digite a classificação indicatória do filme: "))

    cursor.execute(""" 
      INSERT INTO filmes(id, nome, genero, classificacao)
      VALUES(?, ?, ?, ?)
    """, (id,nome, genero, classificacao))

    banco.commit()
    print("Filme cadastrado com sucesso!")

  elif opcao == 2:
    cursor.execute("""
      SELECT * FROM filmes
    """)
    filmes = cursor.fetchall()
    print("\n---FILMES CADASTRADOS---")
    for filme in filmes:
      print(filme)

    banco.commit()
    print("Filmes selecionados com sucesso!")

  elif opcao == 3:
    id_alterar = int(input("Digite o ID do filme que deseja alterar: "))
    novo_nome = input("Digite o novo nome do filme: ")
    novo_genero = input("Digite o novo gênero do filme: ")
    
    cursor.execute("""
    UPDATE filmes
    SET nome = ?, genero = ?
    WHERE id = ?
    """, (novo_nome, novo_genero, id_alterar))

    banco.commit()
    print("Filme alterado com sucesso!")

  elif opcao == 4:
    id_excluir = int(input("Digite o ID  do filme que deseja excluir: "))

    cursor.execute("""
    DELETE FROM filmes
    WHERE id = ?
    """, (id_excluir,))

    banco.commit()
    print("Filme excluído com sucesso!")

  elif opcao == 5:
    print("Programa encerrado.")
    break
  else:
    print("Opção inválida!")

banco.close()