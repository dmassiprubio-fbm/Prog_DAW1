import reflex as rx
from ..controlers.pricipal_state import PrincipalState
from ..controlers.afegir_state import AfegriState

color = "rgb(107,99,246)"


def form_add_product():
    return rx.vstack(
        rx.form(
            rx.vstack(
                rx.heading("Afegir Producte", style={"color": color, "text-align": "center", "margin-bottom": "20px"}),
                rx.input(
                    placeholder="Codi",
                    name="codi_game",
                    name2="codi_product",
                    style={"padding": "8px", "border": "1px solid #ccc", "border-radius": "5px", "margin-bottom": "15px", "font-size": "16px"}
                ),
                rx.input(
                    placeholder="Nom",
                    name="nom_game",
                    name2="nom_product",
                    style={"padding": "8px", "border": "1px solid #ccc", "border-radius": "5px", "margin-bottom": "15px", "font-size": "16px"}
                ),
                rx.input(
                    placeholder="Preu",
                    name="preu_game",
                    name2="preu_product",
                    style={"padding": "8px", "border": "1px solid #ccc", "border-radius": "5px", "margin-bottom": "15px", "font-size": "16px"}
                ),
                rx.button(
                    "Afegir",
                    type="submit",
                    style={
                        "background-color": 'color',
                        "background-color": "color",
                        "color": "white",
                        "padding": "12px 20px",
                        "border": "none",
                        "border-radius": "5px",
                        "cursor": "pointer",
                        "transition": "background-color 0.3s",
                        "font-size": "16px",
                        "font-weight": "bold"
                    },
                    _hover={"background-color": "darkcyan"}
                ),
            ),
            on_submit=AfegriState.handle_submit,
            reset_on_submit=True,
            style={"background-color": "#f9f9f9", "padding": "30px", "border-radius": "10px", "box-shadow": "0 4px 20px rgba(0,0,0,0.1)", "max-width": "400px", "margin": "auto"}
            #style={"background-color": "#f9f9f9", "padding": "30px", "border-radius": "10px", "box-shadow": "0 4px 20px rgba(0,0,0,0.1)", "max-width": "400px", "margin": "auto"}

        ),
        width="90vw",
        height="90vh",
        justify_content="center",
        align_items="center",
        align_content=""

    )

    

def page1() -> rx.Component:
     return rx.container(
         rx.text("Aquí pots afegir els teus videojocs a la colecciò.", height="top-center", size = "6",justify="center", align = "center", ),
         form_add_product(), 
         )


# def AfegirImagen():
#     """The main view."""
#     return rx.vstack(
#         rx.upload(
#             rx.vstack(
#                 rx.button(
#                     "Select File",
#                     color=color,
#                     bg="white",
#                     border=f"1px solid {color}",
#                 ),
#                 rx.text(
#                     "Drag and drop files here or click to select files"
#                 ),
#             ),
#             id="upload1",
#             border=f"1px dotted {color}",
#             padding="5em",
#         ),
#         rx.hstack(
#             rx.foreach(
#                 rx.selected_files("upload1"), rx.text
#             )
#         ),
#         rx.button(
#             "Upload",
#             on_click=AfegriState.handle_upload(
#                 rx.upload_files(upload_id="upload1")
#             ),
#         ),
#         rx.button(
#             "Clear",
#             on_click=rx.clear_selected_files("upload1"),
#         ),
#         # rx.foreach(
#         #     AfegriState.img,
#         #     lambda img: rx.image(
#         #         src=rx.get_upload_url(img)
#         #     ),
#         # ),
#         padding="5em",
#     )


# def eliminarimagen():
#     return rx.vstack(
#         rx.foreach(
#             AfegriState.img,
#             lambda img: rx.hstack(
#                 rx.image(src=rx.get_upload_url(img)),
#                 rx.button("Eliminar", on_click=AfegriState.eliminar_imagen(img)),
#             ),
#         ),
#     )