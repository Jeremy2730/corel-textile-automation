def pieza_permitida_producto(
    producto,
    nombre_pieza,
    productos_config
):

    piezas = productos_config.get(
        producto,
        []
    )

    return nombre_pieza in piezas