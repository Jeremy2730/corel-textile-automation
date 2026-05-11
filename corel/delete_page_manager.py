def eliminar_paginas(
    paginas
):

    for page in paginas:

        print(
            f"🗑️ Eliminando talla: "
            f"{page.Name}"
        )

        page.Delete()