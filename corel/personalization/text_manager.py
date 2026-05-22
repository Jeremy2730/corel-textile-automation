from corel.personalization.zone_manager import (
    ZoneManager
)

from corel.personalization.text_fit_manager import (
    TextFitManager
)

from utils.logger import (
    log_warning,
    log_info
)
from config.fonts import (
    FONT_PRINCIPAL
)


class TextManager:

    def __init__(self):

        self.zone_manager = ZoneManager()

        self.text_fit_manager = TextFitManager()

    def insertar_texto_powerclip(
        self,
        app,
        page,
        texto,
        zone_name,
        powerclip_destino,
        font_name=FONT_PRINCIPAL,
        color_rgb=(248,236,45),
        target_height=32,
        max_width_ratio=0.95
    ):

        zona = self.zone_manager.get_zone(
            page,
            zone_name
        )

        if not zona:

            log_warning(
                f"Zona no encontrada: "
                f"{zone_name}"
            )

            return None

        try:

            page.Activate()

            # 🔥 crear texto artístico
            texto_shape = (
                app.ActiveLayer.CreateArtisticText(
                    zona.CenterX,
                    zona.CenterY,
                    str(texto)
                )
            )


            texto_shape.Name = (
                f"texto_{zone_name}"
            )

            if zone_name == "zona_nombre":

                texto_shape.Name = "TEXT_NOMBRE"

            else:

                texto_shape.Name = (
                    f"texto_{zone_name}"
                )


            # 🔥 fuente
            texto_shape.Text.Story.Font = (
                font_name
            )

            # 🔥 color RGB
            r, g, b = color_rgb

            texto_shape.Fill.UniformColor.RGBAssign(
                r,
                g,
                b
            )

            # 🔥 quitar outline
            texto_shape.Outline.SetNoOutline()

            # 🔥 ajustar geometría
            self.text_fit_manager.fit_text_to_zone(
                texto_shape,
                zona,
                target_height,
                max_width_ratio
            )

            # 🔥 meter al powerclip
            texto_shape.AddToPowerClip(
                powerclip_destino
            )

            log_info(
                f"Texto insertado: "
                f"{texto}"
            )

            return texto_shape

        except Exception as e:

            log_warning(
                f"Error insertando texto: "
                f"{e}"
            )

            return None