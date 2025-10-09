import reflex as rx
from ..model import Prodcut

class ConsultarState(rx.State):

    form_data: dict = {}
    actual_product: Prodcut = Prodcut()
    img_actual_product: list[str] = []

    @rx.var 
    def get_codi(self) -> str:
        return self.router.page.params.get("codi", "")

    @rx.event
    def get_produc(self):
        with rx.session() as session:
            actual_product = session.exec(
                Prodcut.select().where(
                    Prodcut.id == self.get_codi   
                )   
            ).first()
            if actual_product:
                self.actual_product = actual_product
                self.img_actual_product = actual_product.img_nom.split("#") #convertir str en llista

    
    @rx.event
    def handle_change_codi(self,value):
        self.actual_product.codi = value
    
    @rx.event
    def handle_change_nom(self,value):
        self.actual_product.nom = value

    @rx.event
    def handle_change_preu(self,value):
        self.actual_product.preu = value



    @rx.event
    def actualitzar_producte(self):
        """Handle the form submit."""
        with rx.session() as session:
            actual_product = session.exec(
                Prodcut.select().where(
                    Prodcut.id == self.get_codi
            ),
        ).one_or_none()
            actual_product.codi = self.actual_product.codi
            actual_product.nom = self.actual_product.nom
            actual_product.preu = self.actual_product.preu
            session.add(actual_product)
            session.commit()
        return rx.redirect("/mostrar")
        #print(self.form_data)


    @rx.event
    def eliminar_producte(self):
        """Handle the form submit."""
        with rx.session() as session:
            actual_product = session.exec(
                Prodcut.select().where(
                    Prodcut.id == self.get_codi
            ),
        ).one_or_none()
            session.delete(actual_product)
            session.commit()
        return rx.redirect("/mostrar")
        #print(self.form_data)
    
    # The images to show.
    img: list[str]

    @rx.event
    async def handle_upload(
        self, files: list[rx.UploadFile]
    ):
        """Handle the upload of file(s).

        Args:
            files: The uploaded files.
        """

        
        for file in files:
            upload_data = await file.read()
            outfile = rx.get_upload_dir() / file.name

            # Save the file.
            with outfile.open("wb") as file_object:
                file_object.write(upload_data)

            # Update the img var.
            self.img.append(file.name)

            with rx.session() as session:
                actual_product = session.exec(
                    Prodcut.select().where(
                        Prodcut.id == self.get_codi
              ),
                ).one_or_none()
                actual_product.img_nom += file.name + "#"
                session.add(actual_product)
                session.commit()

            
    img: list[str] = []

    @rx.event
    def eliminar_imagen(self, filename: str):
        if filename in self.img_actual_product:
            self.img_actual_product.remove(filename)
            with rx.session() as session:
                actual_product = session.exec(
                    Prodcut.select().where(
                        Prodcut.id == self.get_codi
                ),
            ).one_or_none()
            actual_product.img_nom = actual_product.img_nom.replace(f"{filename}#", "")
            session.add(actual_product)
            session.commit()
           