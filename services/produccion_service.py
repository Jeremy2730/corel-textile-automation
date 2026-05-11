def ejecutar_produccion(
    corel,
    doc_base,
    doc_resultado,
    pedido
):

    print("\n🚀 Iniciando producción...\n")

    corel.filtrar_tallas(
        doc_resultado,
        pedido
    )

    corel.duplicar_paginas(
        doc_resultado,
        pedido
    )

    corel.limpiar_piezas_por_producto(
        doc_resultado,
        pedido
    )

    corel.transferir_diseno(
        doc_base,
        doc_resultado,
        pedido
    )

    print("\n✅ Producción finalizada")