from services.pedido_utils import ( obtener_producto_por_talla)

def obtener_producto_pagina(page,pedido):

    nombre_pagina = (
        page.Name.upper()
    )

    talla = (
        nombre_pagina.split("_")[0]
    )

    return obtener_producto_por_talla(
        pedido,
        talla
    )