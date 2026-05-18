from corel.personalization.zone_manager import (
    ZoneManager
)

from corel.personalization.fit_manager import (
    FitManager
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

        self.fit_manager = FitManager()

    def insertar_texto_powerclip(
        self,
        app,
        page,
        texto,
        zone_name,
        powerclip_destino,
        font_name=FONT_PRINCIPAL,
        color_rgb=(248, 236, 45),
        padding=0.9
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
            self.fit_manager.fit_shape_to_zone(
                texto_shape,
                zona,
                padding
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