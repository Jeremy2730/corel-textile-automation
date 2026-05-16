from corel.texture_manager import (
    ajustar_textura_powerclip
)


def copiar_a_powerclip(
    app,
    page,
    interno,
    shape_destino
):

    try:

        interno.Copy()

        page.Activate()

        app.ActiveLayer.Paste()

        pegado = app.ActiveSelection.Shapes[0]

        pegado.AddToPowerClip(
            shape_destino
        )

        ajustar_textura_powerclip(
            pegado,
            shape_destino
        )

        return True

    except Exception as e:

        print(
            f"❌ Error copiando a PowerClip: {e}"
        )

        return False