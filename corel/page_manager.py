def obtener_nombres_paginas(doc):

    paginas = []

    try:

        for page in doc.Pages:

            paginas.append(
                page.Name.strip().upper()
            )

    except Exception as e:

        print(
            f"❌ Error obteniendo páginas: {e}"
        )

    return paginas

def obtener_paginas_originales(doc):

    paginas = []

    for i in range(1, doc.Pages.Count + 1):

        paginas.append(
            doc.Pages.Item(i)
        )

    return paginas


def crear_nueva_pagina(doc):

    doc.AddPages(1)

    return doc.Pages.Item(
        doc.Pages.Count
    )


def mover_pagina(
    pagina,
    posicion
):

    pagina.MoveTo(posicion)