class FitManager:

    def fit_shape_to_zone(
        self,
        shape,
        zone,
        padding=0.9
    ):

        shape_w = shape.SizeWidth
        shape_h = shape.SizeHeight

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
        align="top"
    ):

        shape.SetSize(
            zona.SizeWidth,
            zona.SizeHeight
        )

        shape.CenterX = zona.CenterX
        shape.CenterY = zona.CenterY

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