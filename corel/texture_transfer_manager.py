from corel.transfer_manager import copiar_a_powerclip
from config.constants import (TEXTURA_PREFIX)

def transferir_texturas(
    app,
    page,
    contenido,
    shape_destino
):

    for interno in contenido:

        nombre_textura = interno.Name.lower()

        if not nombre_textura.startswith(
            TEXTURA_PREFIX
        ):
            continue

        exito = copiar_a_powerclip(
            app,
            page,
            interno,
            shape_destino
        )

        if not exito:
            print(
                f"⚠️ No se pudo transferir "
                f"{interno.Name}"
            )