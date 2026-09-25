import flet as ft
import mysql.connector

def main(page: ft.Page):
    page.title = "Acompanhamento de Processos Operacionais"

    titulo = ft.Text(
        "Acompanhamento de Processos Operacionais",
        size=25
    )
    campo_titulo = ft.TextField(label="Tarefa")

    campo_descricao = ft.TextField(
      label="Descrição",
      multiline=True
    )

    def cadastrar(e):
      cursor = conexao.cursor()

      cursor.execute(
        "INSERT INTO tarefas (titulo, descricao) VALUES (%s, %s)",
        (campo_titulo.value, campo_descricao.value)
    )
    conexao.commit()

    campo_titulo.value = ""
    campo_descricao.value = ""

    page.update()

    botao_cadastrar = ft.ElevatedButton(
      "Cadastrar",
      on_click=cadastrar
    )

    page.add(
        titulo,
        campo_titulo,
        campo_descricao,
        botao_cadastrar
  )

ft.app(target=main)

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="karol202418@",
    database="processos_operacionais"
)

print("Conexão realizada com sucesso!")