import flet as ft
import random


def main(page: ft.Page):
    page.title = "🧿 Orion AI Assistant"
    page.window.width = 600
    page.window.height = 600
    page.window.resizable = False

    page.theme_mode = ft.ThemeMode.DARK

    t = ft.Text(value = "Hello, I am your AI Assistant.", color = "green", font_family = "Arial")
    page.controls.append(t)
    page.update()

ft.run(main)