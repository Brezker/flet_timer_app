import flet as ft
import timer_details

def main(page: ft.Page):
    page.title = "Timers"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"

    timers_list = [
        ft.Text("Timer 1"),
        ft.Text("Timer 2"),
        ft.Text("Timer 3"),
    ]

    def close_dlg(e):
        dlg_modal.open = False
        page.update()

    def add_timer(e):
        if not timer_name_field.value:
            timer_name_field.error_text = "Please enter a timer name"
            page.update()
        else:
            timer_name = timer_name_field.value
            timer_name_field.value = ""
            timer_name_field.error_text = None
            close_dlg(e)  # Cierra el modal
            
            # Cambia el contenido de la página
            page.clean()
            timer_details.main(page, timer_name)
            page.update()

    timer_name_field = ft.TextField(label="Timer Name", width=300)

    dlg_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text("Add New Timer"),
        content=ft.Column([
            timer_name_field,
        ], tight=True),
        actions=[
            ft.Row(
                [
                    ft.TextButton("Cancel", on_click=close_dlg),
                    ft.ElevatedButton("Submit", on_click=add_timer),
                ],
                alignment=ft.MainAxisAlignment.END,
            ),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    def open_dlg_modal(e):
        page.dialog = dlg_modal
        dlg_modal.open = True
        page.update()

    def open_drawer(e):
        page.drawer = drawer
        drawer.open = True
        page.update()

    page.appbar = ft.AppBar(
        title=ft.Text("Timers"),
        leading=ft.IconButton(ft.icons.MENU, on_click=open_drawer),
    )

    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.icons.ADD, on_click=open_dlg_modal
    )

    drawer = ft.NavigationDrawer(
        controls=[
            ft.NavigationDrawerDestination(
                icon=ft.icons.ADD_TO_HOME_SCREEN_SHARP, label="Item 1"
            ),
            ft.NavigationDrawerDestination(icon=ft.icons.ADD_COMMENT, label="Item 2"),
        ],
    )

    timers_listview = ft.ListView(controls=timers_list, expand=1, spacing=10, padding=20)
    
    page.add(timers_listview)

    page.update()

ft.app(target=main)

