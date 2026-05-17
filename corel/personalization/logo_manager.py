from corel.origen_manager import (buscar_shape_origen)
from corel.personalization.zone_manager import (ZoneManager)
from corel.personalization.fit_manager import (FitManager)
from utils.logger import (log_warning,log_info)
from config.logo_rules import (LOGO_RULES)


class LogoManager:

    def __init__(self):

        self.zone_manager = ZoneManager()

        self.fit_manager = FitManager()

    def insertar_logo_powerclip(
        self,
        app,
        page,
        doc_base,
        asset_name,
        zone_name,
        powerclip_destino
    ):

        zona = self.zone_manager.get_zone(
            page,
            zone_name
        )

        if not zona:

            log_warning(
                f"Zona no encontrada: {zone_name}"
            )

            return

        shape_origen = buscar_shape_origen(
            doc_base,
            asset_name
        )

        if not shape_origen:

            log_warning(
                f"Logo no encontrado: {asset_name}"
            )

            return

        # ✅ copiar
        shape_origen.Copy()

        page.Activate()

        # ✅ pegar
        app.ActiveLayer.Paste()

        copia = (
            app.ActiveSelection.Shapes[0]
        )

        # ✅ ajustar tamaño
        rules = LOGO_RULES.get(
            asset_name,
            {}
        )

        padding = rules.get(
            "padding",
            0.85
        )

        self.fit_manager.fit_shape_to_zone(
            copia,
            zona,
            padding
        )

        # ✅ meter al powerclip
        copia.AddToPowerClip(
            powerclip_destino
        )

        log_info(
            f"Logo insertado: {asset_name}"
        )