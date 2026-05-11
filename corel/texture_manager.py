def ajustar_textura_powerclip(
    contenido_pc,
    shape_destino
):

    try:

        # 📏 medidas molde
        ancho_molde = shape_destino.SizeWidth
        alto_molde = shape_destino.SizeHeight

        # 📏 medidas textura
        ancho_textura = contenido_pc.SizeWidth
        alto_textura = contenido_pc.SizeHeight

        # 🔥 escala proporcional
        escala_x = ancho_molde / ancho_textura
        escala_y = alto_molde / alto_textura

        escala = max(escala_x, escala_y)

        # 🔥 solo reducir
        if escala < 1:

            nuevo_ancho = ancho_textura * escala
            nuevo_alto = alto_textura * escala

            contenido_pc.SetSize(
                nuevo_ancho,
                nuevo_alto
            )

        # 🔥 centrar
        contenido_pc.CenterX = shape_destino.CenterX
        contenido_pc.CenterY = shape_destino.CenterY

    except Exception as e:

        print(
            f"⚠️ Error ajustando PowerClip: {e}"
        )


def ajustar_ultimo_powerclip(shape_destino):

    powerclip_shapes = shape_destino.PowerClip.Shapes

    if powerclip_shapes.Count == 0:
        return

    contenido_pc = powerclip_shapes.Item(
        powerclip_shapes.Count
    )

    ajustar_textura_powerclip(
        contenido_pc,
        shape_destino
    )