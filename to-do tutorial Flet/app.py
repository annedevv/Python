from dataclasses import field
from typing import Callable

import flet as ft


PRETO = "#121212"
CARD = "#1E1E1E"
ROSA = "#FF4FA3"
BRANCO = "#FFFFFF"


@ft.control
class Task(ft.Column):
    task_name: str = ""
    on_status_change: Callable[[], None] = field(default=lambda: None)
    on_delete: Callable[["Task"], None] = field(default=lambda task: None)

    def init(self):
        self.completed = False

        self.display_task = ft.Checkbox(
            value=False,
            label=self.task_name,
            label_style=ft.TextStyle(color=BRANCO),
            active_color=ROSA,
            on_change=self.status_changed,
        )

        self.edit_name = ft.TextField(
            expand=1,
            border_radius=20,
            filled=True,
            bgcolor=PRETO,
            color=BRANCO,
            border_color=ROSA,
        )

        self.display_view = ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                self.display_task,
                ft.Row(
                    spacing=0,
                    controls=[
                        ft.IconButton(
                            icon=ft.Icons.CREATE_OUTLINED,
                            icon_color=ROSA,
                            tooltip="Editar tarefa",
                            on_click=self.edit_clicked,
                        ),
                        ft.IconButton(
                            icon=ft.Icons.DELETE_OUTLINE,
                            icon_color=ROSA,
                            tooltip="Excluir tarefa",
                            on_click=self.delete_clicked,
                        ),
                    ],
                ),
            ],
        )

        self.edit_view = ft.Row(
            visible=False,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                self.edit_name,
                ft.IconButton(
                    icon=ft.Icons.DONE_OUTLINE_OUTLINED,
                    icon_color=ROSA,
                    tooltip="Salvar tarefa",
                    on_click=self.save_clicked,
                ),
            ],
        )

        self.controls = [
            ft.Container(
                content=ft.Column(
                    controls=[
                        self.display_view,
                        self.edit_view,
                    ]
                ),
                bgcolor=CARD,
                border_radius=15,
                padding=15,
            )
        ]

    def edit_clicked(self, e):
        self.edit_name.value = self.display_task.label
        self.display_view.visible = False
        self.edit_view.visible = True
        self.update()

    def save_clicked(self, e):
        self.display_task.label = self.edit_name.value
        self.display_view.visible = True
        self.edit_view.visible = False
        self.update()

    def status_changed(self, e):
        self.completed = self.display_task.value
        self.on_status_change()

    def delete_clicked(self, e):
        self.on_delete(self)


@ft.control
class TodoApp(ft.Column):
    def init(self):
        self.new_task = ft.TextField(
            hint_text="O que você precisa fazer?",
            expand=True,
            border_radius=25,
            filled=True,
            bgcolor=CARD,
            color=BRANCO,
            border_color=ROSA,
        )

        self.tasks = ft.Column(spacing=10)

        self.filter = ft.TabBar(
    scrollable=False,
    label_color="#C2185B",      # rosa escuro
    unselected_label_color="#C2185B",
    tabs=[
        ft.Tab(label="Todos"),
        ft.Tab(label="Ativos"),
        ft.Tab(label="Completos"),
    ],
)

        self.filter_tabs = ft.Tabs(
    length=3,
    selected_index=0,
    on_change=lambda e: self.update(),
    content=self.filter,
        )

        self.width = 700

        self.controls = [
            ft.Text(
                "Minha Lista de Tarefas",
                size=28,
                weight=ft.FontWeight.BOLD,
                color=ROSA,
            ),
            ft.Row(
                controls=[
                    self.new_task,
                    ft.FloatingActionButton(
                        icon=ft.Icons.ADD,
                        bgcolor=ROSA,
                        foreground_color=BRANCO,
                        on_click=self.add_clicked,
                    ),
                ],
            ),
            ft.Column(
                spacing=25,
                controls=[
                    self.filter_tabs,
                    self.tasks,
                ],
            ),
        ]

    def add_clicked(self, e):
        if not self.new_task.value.strip():
            return

        task = Task(
            task_name=self.new_task.value,
            on_status_change=self.task_status_change,
            on_delete=self.task_delete,
        )

        self.tasks.controls.append(task)
        self.new_task.value = ""
        self.update()

    def task_status_change(self):
        self.update()

    def task_delete(self, task):
        self.tasks.controls.remove(task)
        self.update()

    def before_update(self):
        status = self.filter.tabs[self.filter_tabs.selected_index].label

        for task in self.tasks.controls:
            task.visible = (
                status == "Todos"
                or (status == "Ativos" and not task.completed)
                or (status == "Completos" and task.completed)
            )

    def tabs_changed(self, e):
        self.update()


def main(page: ft.Page):
    page.title = "Aplicativo de Tarefas"

    page.bgcolor = PRETO
    page.theme_mode = ft.ThemeMode.DARK

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 30

    app = TodoApp()

    page.add(app)


ft.run(main)