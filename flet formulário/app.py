import flet as ft

def main(page: ft.Page):
    page.title = "Cadastro"
    page.bgcolor = ft.Colors.WHITE
    page.padding = 20
    page.scroll = ft.ScrollMode.AUTO

    titulo = ft.Text(
        "Cadastrar Aluno",
        size=36,
        weight=ft.FontWeight.BOLD
    )

    subtitulo = ft.Text(
        "Preencha os campos abaixo.",
        size=18,
        color=ft.Colors.GREY_500
    )

    perfil = ft.Container(
        content=ft.Icon(
            ft.Icons.PERSON,
            size=70,
            color=ft.Colors.GREY_400
        ),
        width=140,
        height=140,
        border=ft.Border.all(
            2,
            ft.Colors.GREY_300
        ),
        border_radius=70,
        alignment=ft.Alignment.CENTER
    )

    nome = ft.TextField(
        label="Nome completo",
        hint_text="Digite seu nome",
        filled=True,
        fill_color=ft.Colors.GREY_200,
        border=ft.InputBorder.NONE,
        border_radius=12
    )

    cpf = ft.TextField(
        label="CPF",
        hint_text="999.999.999-99",
        filled=True,
        fill_color=ft.Colors.GREY_200,
        border=ft.InputBorder.NONE,
        border_radius=12
    )

    whatsapp = ft.TextField(
        label="WhatsApp",
        hint_text="(99) 99999-9999",
        filled=True,
        fill_color=ft.Colors.GREY_200,
        border=ft.InputBorder.NONE,
        border_radius=12
    )

    termos = ft.Checkbox(
        label="Li e aceito os termos de uso",
        value=False
    )

    botao = ft.Button(
        content="Confirmar",
        height=60,
        color=ft.Colors.WHITE,
        bgcolor=ft.Colors.BLUE_700,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(
                radius=30
            )
        )
    )

    formulario = ft.Column(
        controls=[
            titulo,
            subtitulo,
            ft.Container(height=15),
            perfil,
            ft.Container(height=15),
            nome,
            cpf,
            whatsapp,
            termos,
            botao
        ],
        spacing=12,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    area_formulario = ft.Container(
        content=formulario,
        padding=10
    )

    def ajustar_tamanho(e):
        largura = e.width
        if largura < 600:
            area_formulario.width = largura - 40
        else:
            area_formulario.width = 500
        nome.width = area_formulario.width
        cpf.width = area_formulario.width
        whatsapp.width = area_formulario.width
        botao.width = area_formulario.width
        page.update()
    page.on_resize = ajustar_tamanho

    page.add(
        ft.Row(
            controls=[
                area_formulario
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

ft.run(main)