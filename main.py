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
    pedido_nombre = input("🧾 Nombre del archivo resultado: ").strip()
    ruta_guardado = input("💾 ¿Dónde guardar el archivo generado?: ").strip()
    doc_resultado = corel.copiar_archivo_base(
        ruta_tallas,
        pedido_nombre,
        ruta_guardado
    )

    # 📦 pedido
    pedido_texto = input("📦 Cantidades por talla (ej: 4XL:2,): ").strip()

    pedido = {}

    items = pedido_texto.split(",")

    for item in items:

        item = item.strip()

        # ignorar vacíos
        if not item:
            continue

        try:

            talla, cantidad = item.split(":")

            talla = talla.strip().upper()

            # 🔥 aliases de tallas
            aliases = {
                "XXL": "2XL",
                "XXXL": "3XL",
                "XXXXL": "4XL",
                "XXXXXL": "5XL"
            }

            # convertir alias
            if talla in aliases:
                talla = aliases[talla]

            cantidad = int(cantidad.strip())

            pedido[talla] = cantidad

        except:
            print(f"❌ Formato inválido: {item}")

    print(pedido)

    # 🔥 producción
    corel.filtrar_tallas(doc_resultado, pedido)
    corel.duplicar_paginas(doc_resultado, pedido)
    corel.transferir_diseno(doc_base, doc_resultado)
    #corel.listar_shapes(doc_base)