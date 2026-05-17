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

        # 🔥 escalar SOLO por ancho
        ancho_objetivo = zona.SizeWidth

        if shape_referencia:

            ancho_objetivo = (
                shape_referencia.SizeWidth
            )

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
        shape.CenterX = zona.CenterX

        # 🔥 alineación vertical
        if align == "top":

            shape.TopY = zona.TopY

        elif align == "bottom":

            shape.BottomY = zona.BottomY

    def fit_logo_inteligente(
        self,
        shape,
        zone,
        alto_objetivo
    ):

        altura_original = (
            shape.SizeHeight
        )

        ancho_original = (
            shape.SizeWidth
        )

        proporcion = (
            ancho_original /
            altura_original
        )

        nuevo_alto = alto_objetivo

        nuevo_ancho = (
            nuevo_alto
            * proporcion
        )

        shape.SetSize(
            nuevo_ancho,
            nuevo_alto
        )

        shape.CenterX = zone.CenterX
        shape.CenterY = zone.CenterY