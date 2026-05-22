class TextFitManager:

    def fit_text_to_zone(
        self,
        text_shape,
        zone,
        target_height,
        max_width_ratio=0.95,
        base_stretch_x=135
    ):

        text_w = text_shape.SizeWidth
        text_h = text_shape.SizeHeight

        if text_w <= 0 or text_h <= 0:
            return

        # --------------------------------
        # 1. ESCALAR POR ALTURA
        # --------------------------------

        scale = target_height / text_h

        text_shape.Stretch(
            scale,
            scale
        )

        # --------------------------------
        # 2. VALIDAR ANCHO
        # --------------------------------

        text_shape.Stretch(
            base_stretch_x / 100,
            1
        )

        max_w = (
            zone.SizeWidth * max_width_ratio
        )

        current_w = text_shape.SizeWidth

        # --------------------------------
        # 3. COMPRIMIR SOLO HORIZONTAL
        # --------------------------------

        if current_w > max_w:

            compression = (
                max_w / current_w
            )

            text_shape.Stretch(
                compression,
                1
            )

        # --------------------------------
        # 4. CENTRAR
        # --------------------------------

        text_shape.CenterX = zone.CenterX
        text_shape.CenterY = zone.CenterY