import flet as ft
import time

def main(page: ft.Page):
    page.title = "Add Timer"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Theme Mods
    page.theme = ft.Theme(
        scrollbar_theme=ft.ScrollbarTheme(
            thickness=0,
        )
    )

    timer_display = ft.Text(
        value="00:00:00",
        size=60,
        weight=ft.FontWeight.BOLD,
        color=ft.colors.BLUE_500,
    )

    def handle_timer_picker_change(e):
        val = int(e.data)
        timer_display.value = time.strftime("%H:%M:%S", time.gmtime(val))
        page.update()

    timer_picker = ft.CupertinoTimerPicker(
        value=0,
        second_interval=1,
        minute_interval=1,
        mode=ft.CupertinoTimerPickerMode.HOUR_MINUTE_SECONDS,
        on_change=handle_timer_picker_change,
        height=216,
    )

    def reset_values():
        # Not working
        # timer_picker.value = 0
        # timer_picker.second_interval = 1
        # timer_picker.minute_interval = 1
        # timer_picker.mode = ft.CupertinoTimerPickerMode.HOUR_MINUTE_SECONDS
        # timer_picker.on_change = handle_timer_picker_change
        timer_display.value = "00:00:00"
        page.update()

    def add_timer(e):
        # Timer adding logic will be implemented here
        print(f"Adding timer: {timer_display.value}")
        # Reset values after adding
        reset_values()

    def reset_timer(e):
        reset_values()

    add_button = ft.ElevatedButton(
        text="Add",
        on_click=add_timer,
        style=ft.ButtonStyle(color=ft.colors.WHITE, bgcolor=ft.colors.GREEN_500)
    )
    reset_button = ft.ElevatedButton(
        text="Reset",
        on_click=reset_timer,
        style=ft.ButtonStyle(color=ft.colors.WHITE, bgcolor=ft.colors.RED_500)
    )

    page.add(
        ft.Column(
            [
                timer_display,
                timer_picker,
                ft.Row(
                    [add_button, reset_button],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
        )
    )

ft.app(target=main)
