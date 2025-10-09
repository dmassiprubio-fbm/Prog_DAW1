import reflex as rx
from ..controlers.pricipal_state import PrincipalState

# def center_container()-> rx.Component:
#     return rx.container(
#         rx.color_mode.button(position="top-right"),
#         rx.vstack(
#             rx.heading("Bnvinguts " + PrincipalState.text, size="9"),
#             rx.heading("A la clase de Guillem", size="5"),
#             rx.link("A la pàgina primera", href="/primera"),
#             rx.input(
#                 default_value=PrincipalState.text,
#                 on_change=PrincipalState.update_text, # se actualiza al instante
#             ),
#             # rx.input(
#             #     default_value=MyState.text,
#             #     on_blur=MyState.update_text,  #s'actualitza quan surts de l'init
#             # ),  
#             rx.hstack(
#                 rx.button("click me + 1",size="4",color="darkblue",border_radius = "50px", on_click=lambda :PrincipalState.increment(1)),
#                 rx.button("click me + 5",size="4",color="darkblue",border_radius = "50px", on_click=lambda :PrincipalState.increment(5)),
#                 rx.text(PrincipalState.count, color=PrincipalState.color, font_size = "40px"),
#                 rx.button("restart",size="4", color="red", border_radius = "50px", on_click=PrincipalState.strat_increment),
#                 align = "center"
        
#             ),
#             rx.hstack(
#                 rx.cond(
#                     PrincipalState.color == "red",
#                     rx.text("color vermell", color = PrincipalState.color),
#                     rx.text("color verd", color = PrincipalState.color),
#                 ),
#                 align = "center"
#             ),
#             # rx.box(
#             #     rx.foreach(MyState.alumnes, _render_alume) #llista d'alumnes
#             # ),
#             spacing="4",
#             justify="center",
#             align = "center",   
#             min_height="85vh",
#         ),
#         rx.logo(),
#     )


def center_container()-> rx.Component:
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.image(
                src="/game.webp",
                width="10000px",
                height="top-center",
                ),
            rx.heading("BENVINGUT A LA TEVA COL·LECCIÓ DE VIDEOJOCS", size="9"),
            rx.accordion.root(
                rx.accordion.item(
                    header="Afegrir",
                    content="Aquí podràs afegir la informació bàsica dels teus jocs",
                ),
                rx.accordion.item(
                    header="Mostrar col·lecció",
                    content="Aquí podràs veure tota la informació dels jocs en un llistat",
                ),
                rx.accordion.item(
                    header="Modificar/consultar",
                    content="Fent click damunt el codi podràs modificar la informació i afegir imatges",
                ),
                collapsible=True,
                width="300px",
                type="multiple",
            ),
            # rx.box(
            #     rx.text("Aquí podràs emmagatzemar la informació sobre els teu videojocs i pujar imatges per guardar, rècords, memòries, i objectius dels teus jocs.", size="5"),
            #     padding="1em",
            #     borde_width="2px",
            # ),
        rx.heading("Dassip.", size="5"),
        text_align="center",
        spacing="4",
        justify="center",
        align = "center",   
        min_height="85vh",
        ),
        
        rx.logo(),
    )

       

def _render_alume(alumne:str) -> rx.Component:
    return rx.text(alumne, color= "purple")