from corel.powerclip_manager import (
    limpiar_powerclip
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
    destino_nombre
):

    print(
        f"🎯 {origen_nombre} "
        f"→ {destino_nombre}"
    )

    limpiar_powerclip(
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