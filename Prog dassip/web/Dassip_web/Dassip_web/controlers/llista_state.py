import reflex as rx
from ..model import Prodcut

class LlistaState(rx.State):
    product: list[Prodcut]


    @rx.event
    def get_product(self):
        with rx.session() as session:
            self.product = session.exec(
                Prodcut.select()        
            ).all()


