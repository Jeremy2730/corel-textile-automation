from corel.origen_manager import (
    buscar_shape_origen
)

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


class OverlayManager:

    def __init__(self):

        self.zone_manager = ZoneManager()

        self.fit_manager = FitManager()

    def insertar_overlay_powerclip(
        self,
        app,
        page,
        doc_base,
        asset_name,
        powerclip_destino
    ):

        zone_name = (
            f"zona_{asset_name}"
        )

        zona = self.zone_manager.get_zone(
            page,
            zone_name
        )

        if not zona:
            return

        shape_origen = buscar_shape_origen(
            doc_base,
            asset_name
        )

        if not shape_origen:

            log_warning(
                f"Asset no encontrado: "
                f"{asset_name}"
            )

            return

        shape_origen.Copy()

        page.Activate()

        app.ActiveLayer.Paste()

        copia = (
            app.ActiveSelection.Shapes[0]
        )

        if asset_name == "rayas_hombros":

            self.fit_manager.ajustar_overlay_inteligente(
                copia,
                zona,
                align="top"
            )

        else:

            self.fit_manager.ajustar_overlay_inteligente(
                copia,
                zona,
                align="bottom"
            )

        copia.AddToPowerClip(
            powerclip_destino
        )

        log_info(
            f"Overlay insertado: "
            f"{asset_name}"
        )