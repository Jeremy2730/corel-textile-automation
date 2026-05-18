class FitManager:

    def fit_shape_to_zone(
        self,
        shape,
        zone,
        padding=0.9
    ):

        shape_w = shape.SizeWidth
        shape_h = shape.SizeHeight

        # 🔥 protección
        if shape_w <= 0 or shape_h <= 0:
            return

        zone_w = zone.SizeWidth
        zone_h = zone.SizeHeight

        scale_x = zone_w / shape_w
        scale_y = zone_h / shape_h

        scale = min(
            scale_x,
            scale_y
        )

        scale *= padding

        new_w = shape_w * scale
        new_h = shape_h * scale

        shape.SetSize(
            new_w,
            new_h
        )

        shape.CenterX = zone.CenterX
        shape.CenterY = zone.CenterY


    def ajustar_overlay_inteligente(
        self,
        shape,
        zona,
        shape_referencia=None,
        align="top"
    ):

        shape_w = shape.SizeWidth
        shape_h = shape.SizeHeight

        if shape_w <= 0 or shape_h <= 0:
            return

        # 🔥 ancho objetivo
        ancho_objetivo = zona.SizeWidth

        if shape_referencia:

            ancho_objetivo = (
                shape_referencia.SizeWidth
            )

        # 🔥 escalar proporcional
        scale = (
            ancho_objetivo /
            shape_w
        )

        nuevo_w = (
            shape_w * scale
        )

        nuevo_h = (
            shape_h * scale
        )

        shape.SetSize(
            nuevo_w,
            nuevo_h
        )

        # 🔥 centrar horizontalmente
        if shape_referencia:

            shape.CenterX = (
                shape_referencia.CenterX
            )

        else:

            shape.CenterX = zona.CenterX

        # 🔥 alineación vertical
        if align == "top":

            shape.TopY = zona.TopY

        elif align == "bottom":

            shape.BottomY = zona.BottomY