def duplicar_shapes_pagina(
    app,
    pagina_origen,
    pagina_destino
):

    pagina_origen.Activate()

    sr = pagina_origen.Shapes.All()

    sr.CreateSelection()

    app.ActiveSelection.Duplicate()

    duplicados = app.ActiveSelectionRange

    pagina_destino.Activate()

    for shape in duplicados:

        shape.MoveToLayer(
            pagina_destino.ActiveLayer
        )