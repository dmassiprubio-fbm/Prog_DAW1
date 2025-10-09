"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from rxconfig import config
from Dassip_web.pages import center_container
from Dassip_web.components import sidebar_bottom_profile
from Dassip_web.pages import page1, page2, consultarpg
from .controlers import LlistaState 
from .controlers import ConsultarState




def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.hstack(
        sidebar_bottom_profile(),
        center_container(),
    )
    
def prova() -> rx.Component:
    return rx.container(
        rx.heading("pagina de prova"),
        rx.link("pagina principal", href = "/"),
        rx.hstack(
            rx.text("HOLA CHAT", size = "9")
        )
    )

def afegeix() -> rx.Component:
    return rx.hstack(
            sidebar_bottom_profile(),
            page1(),
        rx.heading("Dassip."),
        ),
    

def mostrar() -> rx.Component:
    return rx.hstack(
            sidebar_bottom_profile(),
            page2(),
        rx.heading("Dassip."),   
    ),


def consultar() -> rx.Component:
    return rx.hstack(
            sidebar_bottom_profile(),
            consultarpg(),
        rx.heading("Dassip."),
        ),

app = rx.App(
        theme=rx.theme(
        appearance="light",
        has_background=True,
        radius="large",
        accent_color="purple",
        gray_color="gray"
    ))
app.add_page(index)
app.add_page(prova, route="primera")
app.add_page(afegeix, route="afegeix")
app.add_page(mostrar, route="mostrar", on_load=LlistaState.get_product)
app.add_page(consultar, route = "consultar/[codi]", on_load=ConsultarState.get_produc)