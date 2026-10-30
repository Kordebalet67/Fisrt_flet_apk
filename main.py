import flet as ft
import flet_webview as fwv

def main(page: ft.Page):
    # Базовая настройка страницы
    page.title = "GitFut App"
    page.theme_mode = ft.ThemeMode.DARK
    # Темно-синяя палитра в стиле GitFut
    page.bgcolor = "#0B132B"
    page.padding = 40
    page.window_min_width = 450
    page.window_min_height = 700

    # Поля ввода
    username = ft.TextField(
        label="GitHub Username",
        hint_text="например, torvalds",
        border_color="#3A506B",
        bgcolor="#1C2541",
        color="#FFFFFF",
        label_style=ft.TextStyle(color="#5BC0BE"),
        hint_style=ft.TextStyle(color="#6C757D"),
    )
    
    country = ft.TextField(
        label="Country Code",
        hint_text="например, RU, US, DE",
        border_color="#3A506B",
        bgcolor="#1C2541",
        color="#FFFFFF",
        label_style=ft.TextStyle(color="#5BC0BE"),
        hint_style=ft.TextStyle(color="#6C757D"),
    )

    def go_to_webview(e):
        # Простая валидация
        if not username.value:
            username.error_text = "Введите username!"
            username.update()
            return
        
        user = username.value.strip()
        cnt = country.value.strip().lower() if country.value else "US"
        
        # Очищаем страницу от формы настроек
        page.controls.clear()
        
        # Верхняя панель с кнопкой "Назад"
        top_bar = ft.Row(
            [
                ft.IconButton(
                    icon=ft.Icons.ARROW_BACK,
                    icon_color="#5BC0BE",
                    tooltip="Назад к настройкам",
                    on_click=lambda _: show_settings()
                ),
                ft.Text(f"gitfut.com/{user}", size=16, color="#FFFFFF", weight=ft.FontWeight.BOLD),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        )
        
        # Формируем целевой URL
        url = f"https://gitfut.com/{user}?country={cnt}"
        
        # Компонент WebView для отображения сайта
        web_view = fwv.WebView(
            url=url,
            expand=True,
        )
        
        # Добавляем новый экран
        page.add(
            ft.SafeArea(
                content=ft.Column(
                    [
                        top_bar,
                        ft.Container(
                            content=web_view,
                            expand=True,
                            border_radius=12,
                            # ИСПРАВЛЕНИЕ: ft.border.all заменен на ft.BorderSide
                            border=ft.BorderSide(1, "#3A506B"),
                            margin=ft.Margin(top=10),
                        )
                    ],
                    expand=True
                ),
                expand=True
            )
        )
        page.update()

    def show_settings():
        page.controls.clear()
        page.add(
            ft.SafeArea(
                content=ft.Column(
                    [
                        ft.Container(
                            content=ft.Column([
                                ft.Text("GITFUT", size=42, weight=ft.FontWeight.BOLD, color="#5BC0BE", style=ft.TextStyle(letter_spacing=2)),
                                ft.Text("SCOUT", size=24, weight=ft.FontWeight.W_300, color="#FFFFFF", style=ft.TextStyle(letter_spacing=4)),
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                            margin=ft.Margin(bottom=30)
                        ),
                        ft.Text(
                            "Преврати свой GitHub в карточку игрока",
                            size=14,
                            color="#A0AAB5",
                            text_align=ft.TextAlign.CENTER,
                        ),
                        ft.Divider(height=40, color=ft.Colors.TRANSPARENT),
                        username,
                        ft.Divider(height=10, color=ft.Colors.TRANSPARENT),
                        country,
                        ft.Divider(height=30, color=ft.Colors.TRANSPARENT),
                        ft.Button(
                            "SCOUT (Создать карточку)",
                            icon=ft.Icons.STAR,
                            width=300,
                            height=55,
                            style=ft.ButtonStyle(
                                color="#0B132B",
                                bgcolor="#5BC0BE",
                                shape=ft.RoundedRectangleBorder(radius=12),
                            ),
                            on_click=go_to_webview,
                        )
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    alignment=ft.MainAxisAlignment.CENTER,
                    expand=True,
                ),
                expand=True
            )
        )
        page.update()

    # Запускаем первый экран при старте
    show_settings()

if __name__ == "__main__":
    ft.run(main)