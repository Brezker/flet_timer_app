import flet as ft

def main(page: ft.Page):
    page.title = "Flet Timer App"
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

    selected_hours = 0
    selected_minutes = 0
    selected_seconds = 0

    def update_display():
        timer_display.value = f"{selected_hours:02d}:{selected_minutes:02d}:{selected_seconds:02d}"
        page.update()

    def create_time_picker(max_value, on_select):
        return ft.ListView(
            width=80,
            height=150,
            spacing=0,
            auto_scroll=False,
            # scroll_bar_visible=False,
            controls=[
                ft.Container(
                    content=ft.Text("", size=24, text_align=ft.TextAlign.CENTER),
                    on_click=lambda _: on_select(0),
                    padding=10,
                    alignment=ft.alignment.center,
                )
            ] + [
                ft.Container(
                    content=ft.Text(f"{i:02d}", size=24, text_align=ft.TextAlign.CENTER),
                    on_click=lambda _, i=i: on_select(i),
                    padding=10,
                    alignment=ft.alignment.center,
                )
                for i in range(max_value)
            ],
        )

    def select_hours(value):
        nonlocal selected_hours
        selected_hours = value
        update_display()

    def select_minutes(value):
        nonlocal selected_minutes
        selected_minutes = value
        update_display()

    def select_seconds(value):
        nonlocal selected_seconds
        selected_seconds = value
        update_display()

    hours_picker = create_time_picker(24, select_hours)
    minutes_picker = create_time_picker(60, select_minutes)
    seconds_picker = create_time_picker(60, select_seconds)

    def add_timer(e):
        # Timer adding logic will be implemented here
        print(f"Adding timer: {selected_hours:02d}:{selected_minutes:02d}:{selected_seconds:02d}")

    def reset_timer(e):
        nonlocal selected_hours, selected_minutes, selected_seconds
        selected_hours = selected_minutes = selected_seconds = 0
        update_display()

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
                ft.Row(
                    [
                        ft.Column([
                            ft.Container(
                                content=ft.Text("Hours", text_align=ft.TextAlign.CENTER),
                                alignment=ft.alignment.center,
                                width=80
                            ),
                            hours_picker
                        ]),
                        ft.Column([
                            ft.Container(
                                content=ft.Text("Minutes", text_align=ft.TextAlign.CENTER),
                                alignment=ft.alignment.center,
                                width=80
                            ),
                            minutes_picker
                        ]),
                        ft.Column([
                            ft.Container(
                                content=ft.Text("Seconds", text_align=ft.TextAlign.CENTER),
                                alignment=ft.alignment.center,
                                width=80
                            ),
                            seconds_picker
                        ]),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
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
