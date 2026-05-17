from config.productos import PRODUCTOS

from corel_api import CorelAPI
from corel.page_manager import obtener_nombres_paginas

from services.pedido_service import crear_pedido
from services.produccion_service import ejecutar_produccion
from services.ui_service import (mostrar_tallas)


corel = CorelAPI()

if corel.conectar():

    ruta_archivos = input(
        "📂 Ingresa la ruta donde están los archivos .cdr: "
    ).strip()

    ruta_base = ruta_archivos + r"\diseno_base.cdr"
    ruta_tallas = ruta_archivos + r"\plantilla_tallas.cdr"

    doc_base = corel.abrir_documento(ruta_base)
    doc_tallas = corel.abrir_documento(ruta_tallas)

    if not doc_base or not doc_tallas:

        print("❌ No se pudieron abrir los archivos")

        exit()

    pedido_nombre = input(
        "🧾 Nombre del archivo resultado: "
    ).strip()

    ruta_guardado = input(
        "💾 ¿Dónde guardar el archivo generado?: "
    ).strip()

    doc_resultado = corel.copiar_archivo_base(
        ruta_tallas,
        pedido_nombre,
        ruta_guardado
    )

    tallas_existentes = obtener_nombres_paginas(
        doc_tallas
    )

    tallas_base = corel.obtener_tallas_base(
        doc_base
    )

    mostrar_tallas(tallas_existentes)
    print("\nDEBUG TALLAS BASE:")
    print(tallas_base)

    pedido = crear_pedido(
        tallas_existentes,
        tallas_base
    )

    if len(pedido) == 0:

        print("❌ No hay pedidos válidos")

        exit()

    ejecutar_produccion(
        corel,
        doc_base,
        doc_resultado,
        pedido
    )