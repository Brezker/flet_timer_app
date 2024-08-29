import flet as ft

def main(page: ft.Page, timer_name: str):
    # page.title = f"Timer: {timer_name}"
    # page.title = f"{timer_name} Timer"
    page.title = f"{timer_name}"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    # page.update()

    def go_back(e):
        import main
        page.clean()
        main.main(page)

    page.appbar = ft.AppBar(
        title=ft.Text(f"Timer: {timer_name}"),
        leading=ft.IconButton(ft.icons.ARROW_BACK, on_click=go_back),
    )

    timer_list = [
        ft.Text("Timer 1"),
        ft.Text("Timer 2"),
        ft.Text("Timer 3"),
        ft.Text("Timer 4"),
    ]

    timer_listview = ft.ListView(controls=timer_list, expand=1, spacing=10, padding=20)
    
    page.add(timer_listview)

    page.update()

if __name__ == "__main__":
    ft.app(target=main)
