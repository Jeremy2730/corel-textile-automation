def obtener_producto_por_talla(
    pedido,
    talla
):

    talla = talla.upper()

    for item in pedido:

        if item["talla"].upper() == talla:

            return item["producto"]

    return None


def obtener_cantidad_por_talla(
    pedido,
    talla
):

    talla = talla.upper()

    for item in pedido:

        if item["talla"].upper() == talla:

            return item["cantidad"]

    return 1

def obtener_tallas_pedido(
    pedido
):

    tallas = []

    for item in pedido:

        tallas.append(
            item["talla"].upper()
        )

    return tallas