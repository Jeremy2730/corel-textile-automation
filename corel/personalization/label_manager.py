from utils.logger import (
    log_warning,
    log_info
)


class LabelManager:

    def insertar_label_powerclip(
        self,
        page,
        powerclip_destino,
        color=None
    ):

        labels_encontrados = []

        # ====================================
        # 🔥 buscar todos los labels
        # ====================================

        for shape in page.Shapes:

            try:

                nombre = (
                    shape.Name
                    .strip()
                    .lower()
                )

                if nombre == "label talla":

                    labels_encontrados.append(
                        shape
                    )

            except:
                continue

        if not labels_encontrados:

            log_warning(
                "Label talla no encontrado"
            )

            return

        # ====================================
        # 🔥 detectar label dentro de pieza
        # ====================================

        label_correcto = None

        for label in labels_encontrados:

            try:

                dentro_x = (

                    label.CenterX >=
                    powerclip_destino.LeftX

                    and

                    label.CenterX <=
                    powerclip_destino.RightX
                )

                dentro_y = (

                    label.CenterY >=
                    powerclip_destino.BottomY

                    and

                    label.CenterY <=
                    powerclip_destino.TopY
                )

                if dentro_x and dentro_y:

                    label_correcto = label
                    break

            except:
                continue

        if not label_correcto:

            log_warning(
                f"No hay label dentro de "
                f"{powerclip_destino.Name}"
            )

            return

        # ====================================
        # 🔥 cambiar color
        # ====================================

        if color:

            try:

                (
                    label_correcto
                    .Fill
                    .UniformColor
                    .CMYKAssign(*color)
                )

            except:
                pass

        # ====================================
        # 🔥 NO mover posición
        # ====================================

        label_correcto.AddToPowerClip(
            powerclip_destino
        )

        log_info(
            f"Label insertado en "
            f"{powerclip_destino.Name}"
        )