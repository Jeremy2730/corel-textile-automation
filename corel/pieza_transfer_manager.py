from corel.powerclip_manager import (
    limpiar_placeholders
)

from corel.texture_transfer_manager import (
    transferir_texturas
)


def transferir_pieza(
    app,
    page,
    shape_origen,
    shape_destino,
    origen_nombre,
    destino_nombre,
    limpiar=True
):

    print(
        f"🎯 {origen_nombre} "
        f"→ {destino_nombre}"
    )

    if limpiar:

        limpiar_placeholders(
            shape_destino
        )

    contenido = (
        shape_origen
        .PowerClip
        .Shapes
    )

    transferir_texturas(
        app,
        page,
        contenido,
        shape_destino
    )