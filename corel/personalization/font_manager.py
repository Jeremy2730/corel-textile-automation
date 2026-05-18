import os


class FontManager:

    def __init__(self):

        self.fonts_path = (
            os.path.join(
                "assets",
                "fonts"
            )
        )

    def obtener_fuente_principal(self):

        archivos = os.listdir(
            self.fonts_path
        )

        fuentes = [

            f for f in archivos

            if f.lower().endswith(
                ".ttf"
            )
        ]

        if len(fuentes) == 0:

            raise Exception(
                "No hay fuentes TTF"
            )

        return fuentes[0]