from corel_api import CorelAPI

corel = CorelAPI()

if corel.conectar():

    # 📂 pedir ruta al usuario
    ruta_archivos = input("📂 Ingresa la ruta donde están los archivos .cdr: ").strip()

    ruta_base = ruta_archivos + r"\diseno_base.cdr"
    ruta_tallas = ruta_archivos + r"\plantilla_tallas.cdr"

    # 📂 abrir documentos
    doc_base = corel.abrir_documento(ruta_base)
    doc_tallas = corel.abrir_documento(ruta_tallas)

    if not doc_base or not doc_tallas:
        print("❌ No se pudieron abrir los archivos")
        exit()

    # 🆕 crear resultado
    pedido_nombre = input("🧾 Nombre del pedido: ").strip()
    ruta_guardado = input("💾 ¿Dónde guardar el pedido?: ").strip()
    doc_resultado = corel.copiar_archivo_base(
        ruta_tallas,
        pedido_nombre,
        ruta_guardado
    )
    pedido = {
        "4XL": 2,
        "3XL": 1,
        "16": 3
    }

    corel.filtrar_tallas(doc_resultado, pedido)
    corel.duplicar_paginas(doc_resultado, pedido)