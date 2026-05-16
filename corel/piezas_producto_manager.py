from config.productos import PRODUCTOS


def obtener_piezas_producto(
    producto
):

    config_producto = (
        PRODUCTOS[producto]
    )

    piezas_permitidas = (
        config_producto["piezas"]
    )

    piezas = []

    from config.piezas import PIEZAS

    for origen, destino in PIEZAS.items():

        if destino not in piezas_permitidas:
            continue

        piezas.append(
            (origen, destino)
        )

    return piezas