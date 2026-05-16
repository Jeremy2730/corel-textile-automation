def ajustar_textura_powerclip(
    contenido_pc,
    shape_destino
):

    try:

        ancho_molde = (
            shape_destino.SizeWidth
        )

        alto_molde = (
            shape_destino.SizeHeight
        )

        ancho_textura = (
            contenido_pc.SizeWidth
        )

        alto_textura = (
            contenido_pc.SizeHeight
        )

        scale_x = (
            ancho_molde / ancho_textura
        )

        scale_y = (
            alto_molde / alto_textura
        )

        escala = max(
            scale_x,
            scale_y
        )

        if escala < 1:

            contenido_pc.SetSize(
                ancho_textura * escala,
                alto_textura * escala
            )

        contenido_pc.CenterX = (
            shape_destino.CenterX
        )

        contenido_pc.CenterY = (
            shape_destino.CenterY
        )

    except Exception as e:

        print(
            f"⚠️ Error ajustando textura: {e}"
        )