import reflex as rx
from ..model import Prodcut

class AfegriState(rx.State):

    form_data: dict = {}

    @rx.event
    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data
        with rx.session() as session:
            session.add(
                Prodcut(
                    codi = form_data["codi_game"],
                    nom=form_data["nom_game"],
                    preu=form_data["preu_game"],
                    img_nom=""
                ),
            ),
            session.commit()
        return rx.redirect("/mostrar")

    # # The images to show.
    # img: list[str] = []

    # @rx.event
    # async def handle_upload(
    #     self, files: list[rx.UploadFile]
    # ):
    #     """Handle the upload of file(s).

    #     Args:
    #         files: The uploaded files.
    #     """
    #     for file in files:
    #         upload_data = await file.read()
    #         outfile = rx.get_upload_dir() / file.filename

    #         # Save the file.
    #         with outfile.open("wb") as file_object:
    #             file_object.write(upload_data)

    #         # Update the img var.
    #         self.img.append(file.filename)
    
    # img: list[str] = []

    # @rx.event
    # def eliminar_imagen(self, filename: str):
    #     if filename in self.img:
    #         self.img.remove(filename)