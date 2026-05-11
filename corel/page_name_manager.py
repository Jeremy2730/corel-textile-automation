def obtener_nombres_paginas(
    pages
):

    nombres = []

    for page in pages:

        nombres.append(
            page.Name.strip().upper()
        )

    return nombres