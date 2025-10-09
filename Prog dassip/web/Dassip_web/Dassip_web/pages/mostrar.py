import reflex as rx
from ..controlers.pricipal_state import PrincipalState
from ..controlers import LlistaState
from..model import Prodcut

def show_product(product: Prodcut):
    """Show a person in a table row."""
    return rx.table.row(
        rx.table.cell(rx.link(product.codi, href=f"consultar/{product.id}")),
        rx.table.cell(product.nom),
        rx.table.cell(product.preu),
        rx.table.cell(product.img_nom),
    )

def foreach_table_example():
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("Codi"),
                rx.table.column_header_cell("Nom"),
                rx.table.column_header_cell("Preu"),
                rx.table.column_header_cell("IMG"),
            ),
        ),
        rx.table.body(
            rx.foreach(LlistaState.product, show_product),
        ),
        width="100%",
    )

def page2() -> rx.Component:
    return rx.container(
        rx.text("Benvingut a la pagina per consultar la teva colecció de jocs"),
        foreach_table_example(),
    )
