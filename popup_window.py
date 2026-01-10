import flet as ft
import random

def main(page: ft.Page):
    page.title = "Orion AI Assistant"
    page.window.width = 400
    page.window.height = 300
    page.window.resizable = False

    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.DARK
