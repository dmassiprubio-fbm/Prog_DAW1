import reflex as rx
from ..controlers.pricipal_state import PrincipalState
from ..controlers.Consultarstate import ConsultarState


color = "rgb(107,99,246)"


def form_add_product():
    return rx.vstack(
        rx.heading(ConsultarState.actual_product.nom),
        rx.form(
            rx.vstack(
                 rx.input(
                    value=ConsultarState.actual_product.id,
                    name="id_game",
                    style={"padding": "8px", "border": "1px solid #ccc", "border-radius": "5px", "margin-bottom": "15px", "font-size": "16px"}
                ),
                rx.input(
                    value=ConsultarState.actual_product.codi,
                    on_change=ConsultarState.handle_change_codi,
                    placeholder="Codi",
                    name="codi_game",
                    style={"padding": "8px", "border": "1px solid #ccc", "border-radius": "5px", "margin-bottom": "15px", "font-size": "16px"}
                ),
                rx.input(
                    value=ConsultarState.actual_product.nom,
                    on_change=ConsultarState.handle_change_nom,
                    placeholder="Nom",
                    name="nom_game",
                    style={"padding": "8px", "border": "1px solid #ccc", "border-radius": "5px", "margin-bottom": "15px", "font-size": "16px"}
                ),
                rx.input(
                    value=ConsultarState.actual_product.preu,
                    on_change=ConsultarState.handle_change_preu,
                    placeholder="Preu",
                    name="preu_game",
                    style={"padding": "8px", "border": "1px solid #ccc", "border-radius": "5px", "margin-bottom": "15px", "font-size": "16px"}
                ),
                #rx.button("Modificar", type="button", color_scheme = 'purple', on_click=ConsultarState.actualitzar_producte),
                rx.button(
                    "Modificar",
                    type="submit",
                    style={
                        "background-color": color,
                        "color": "white",
                        "padding": "12px 20px",
                        "border": "none",
                        "border-radius": "5px",
                        "cursor": "pointer",
                        "transition": "background-color 0.3s",
                        "font-size": "16px",
                        "font-weight": "bold",
                    },
                    on_click=ConsultarState.actualitzar_producte
                ),
                #rx.button("Eliminar", type="button", color_scheme = "red", on_click=ConsultarState.eliminar_producte),
                rx.button(
                    "Eliminar",
                    type="submit",
                    style={
                        "background-color": "red",
                        "color": "white",
                        "padding": "12px 20px",
                        "border": "none",
                        "border-radius": "5px",
                        "cursor": "pointer",
                        "transition": "background-color 0.3s",
                        "font-size": "16px",
                        "font-weight": "bold",
                    },
                    on_click=ConsultarState.eliminar_producte
                
            ),
            reset_on_submit=True,

        ),
        margin_top = "100px",
        ),
    ),

def consultarpg() -> rx.Component:
    return rx.container(
        form_add_product(),
        ConsultarImagen(),
        eliminarimagen(), 
        )

color = "rgb(107,99,246)"

def ConsultarImagen():
    """The main view."""
    return rx.vstack(
        rx.upload(
            rx.vstack(
                rx.button(
                    "Select File",
                    color=color,
                    bg="white",
                    border=f"1px solid {color}",
                ),
                rx.text(
                    "Afegeix aquí imatges per guardar records i èxits" 
                ),
            ),
            id="upload1",
            border=f"1px dotted {color}",
            padding="5em",
        ),
        rx.hstack(
            rx.foreach(
                rx.selected_files("upload1"), rx.text
            )
        ),
        rx.button(
            "Upload",
            on_click=ConsultarState.handle_upload(
                rx.upload_files(upload_id="upload1")
            ),
        ),
        rx.button(
            "Clear",
            on_click=rx.clear_selected_files("upload1"),
        ),
        rx.alert_dialog.root(
            rx.alert_dialog.trigger(
                rx.button("Alert"),
            ),
            rx.alert_dialog.content(
                rx.alert_dialog.title("Alerta"),
                rx.alert_dialog.description(
                    "Desprès d'afegir o eliminar una imatge espera que la pagina torni a carregar.",
                ),
                rx.flex(
                    rx.alert_dialog.cancel(
                        rx.button("Cancel"),
                    ),
                    spacing="3",
                ),
            ),
        ),
        
        rx.foreach(
            ConsultarState.img_actual_product,  # State.img should be a list of filenames
            #lambda product_img: rx.image(src=rx.get_upload_url(product_img))
            lambda product_img: rx.cond(product_img!="", rx.image(src=rx.get_upload_url(product_img)))
        ),
        padding="5em",
    )

def eliminarimagen():
    return rx.vstack(
        rx.foreach(
            ConsultarState.img_actual_product,
            lambda img: rx.hstack(
                
                rx.cond(img!="",rx.button("Eliminar", on_click=ConsultarState.eliminar_imagen(img))),
            ),
        ),
    )



