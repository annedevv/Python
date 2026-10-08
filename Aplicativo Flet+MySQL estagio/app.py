import os
import shutil

import flet as ft
import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="karol202418@",
    database="processos_operacionais"
)

PASTA_FOTOS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fotos")
os.makedirs(PASTA_FOTOS, exist_ok=True)


def main(page: ft.Page):
    page.title = "Acompanhamento de Processos Operacionais"
    page.scroll = ft.ScrollMode.AUTO

    titulo = ft.Text("Acompanhamento de Processos Operacionais", size=25)
    campo_titulo = ft.TextField(label="Tarefa")
    campo_descricao = ft.TextField(label="Descrição", multiline=True)
    lista_tarefas = ft.Column()

    seletor_foto = ft.FilePicker()
    page.services.append(seletor_foto)

    def concluir(e, id_tarefa):
        cursor = conexao.cursor()
        cursor.execute(
            "UPDATE tarefas SET concluida = %s WHERE id = %s",
            (e.control.value, id_tarefa)
        )
        conexao.commit()
        cursor.close()
        listar_tarefas()

    def salvar_observacao(e, id_tarefa):
        cursor = conexao.cursor()
        cursor.execute(
            "UPDATE tarefas SET observacao = %s WHERE id = %s",
            (e.control.value, id_tarefa)
        )
        conexao.commit()
        cursor.close()

    async def anexar(id_tarefa):
        arquivos = await seletor_foto.pick_files(
            allow_multiple=False,
            file_type=ft.FilePickerFileType.IMAGE
        )
        if not arquivos:
            return

        origem = arquivos[0].path
        extensao = os.path.splitext(origem)[1]
        nome_arquivo = f"tarefa_{id_tarefa}{extensao}"
        shutil.copy(origem, os.path.join(PASTA_FOTOS, nome_arquivo))

        cursor = conexao.cursor()
        cursor.execute(
            "UPDATE tarefas SET foto_caminho = %s WHERE id = %s",
            (nome_arquivo, id_tarefa)
        )
        conexao.commit()
        cursor.close()

        listar_tarefas()

    def listar_tarefas():
        lista_tarefas.controls.clear()

        cursor = conexao.cursor()
        cursor.execute(
            "SELECT id, titulo, descricao, concluida, observacao, foto_caminho "
            "FROM tarefas"
        )
        tarefas = cursor.fetchall()
        cursor.close()

        for id_t, titulo_t, descricao_t, concluida_t, obs_t, foto_t in tarefas:
            controles = [
                ft.ListTile(
                    leading=ft.Checkbox(
                        value=bool(concluida_t),
                        on_change=lambda e, id_t=id_t: concluir(e, id_t),
                    ),
                    title=ft.Text(titulo_t),
                    subtitle=ft.Text(descricao_t),
                ),
                ft.TextField(
                    label="Observação",
                    value=obs_t or "",
                    multiline=True,
                    on_blur=lambda e, id_t=id_t: salvar_observacao(e, id_t),
                ),
                ft.ElevatedButton(
                    "Anexar foto",
                    on_click=lambda e, id_t=id_t: page.run_task(anexar, id_t),
                ),
            ]

            if foto_t:
                controles.append(
                    ft.Image(src=os.path.join(PASTA_FOTOS, foto_t), width=200)
                )

            lista_tarefas.controls.append(
                ft.Card(
                    content=ft.Container(
                        padding=10,
                        content=ft.Column(controles),
                    )
                )
            )

        page.update()

    def cadastrar(e):
        cursor = conexao.cursor()
        cursor.execute(
            "INSERT INTO tarefas (titulo, descricao) VALUES (%s, %s)",
            (campo_titulo.value, campo_descricao.value)
        )
        conexao.commit()
        cursor.close()

        campo_titulo.value = ""
        campo_descricao.value = ""

        listar_tarefas()

    botao_cadastrar = ft.ElevatedButton("Cadastrar", on_click=cadastrar)

    page.add(
        titulo,
        campo_titulo,
        campo_descricao,
        botao_cadastrar,
        lista_tarefas,
    )

    listar_tarefas()


ft.run(main)