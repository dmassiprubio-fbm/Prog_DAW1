import reflex as rx

class Prodcut(rx.Model, table=True):
    codi: str
    nom: str
    preu: str
    img_nom: str


