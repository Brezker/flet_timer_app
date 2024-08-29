import flet as ft
import time

def main(page: ft.Page):
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"

    def go_back(e):
        import main
        page.clean()
        main.main(page)

    page.appbar = ft.AppBar(
        leading=ft.IconButton(ft.icons.ARROW_BACK, on_click=go_back),
    )

    timer_display = ft.Text(
        value="01:00",
        size=60,
        weight=ft.FontWeight.BOLD,
        color=ft.colors.BLUE_500,
    )

    remaining_time = 60  # 1 minute in seconds
    timer_active = False

    def update_timer():
        nonlocal remaining_time, timer_active
        if remaining_time > 0 and timer_active:
            remaining_time -= 1
            minutes, seconds = divmod(remaining_time, 60)
            timer_display.value = f"{minutes:02d}:{seconds:02d}"
            page.update()
            page.client.set_timeout(1, update_timer)
        elif remaining_time == 0:
            timer_active = False
            start_pause_button.text = "Start"
            page.update()

    def toggle_timer(e):
        nonlocal timer_active
        if not timer_active:
            timer_active = True
            start_pause_button.text = "Pause"
            update_timer()
        else:
            timer_active = False
            start_pause_button.text = "Resume"
        page.update()

    def reset_timer(e):
        nonlocal remaining_time, timer_active
        remaining_time = 60
        timer_active = False
        timer_display.value = "01:00"
        start_pause_button.text = "Start"
        page.update()

    start_pause_button = ft.ElevatedButton("Start", on_click=toggle_timer)
    reset_button = ft.ElevatedButton("Reset", on_click=reset_timer)

    timer_controls = ft.Row(
        [start_pause_button, reset_button],
        alignment=ft.MainAxisAlignment.CENTER,
    )

    timer_container = ft.Container(
        content=ft.Column(
            [
                timer_display,
                timer_controls,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        width=300,
        height=300,
        border=ft.border.all(2, ft.colors.BLUE_500),
        border_radius=10,
        padding=20,
    )

    page.add(timer_container)

    page.update()

if __name__ == "__main__":
    ft.app(target=main)

