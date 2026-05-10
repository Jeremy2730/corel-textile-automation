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

    # 🔥 detectar tallas existentes en plantilla
    tallas_existentes = []

    for page in doc_tallas.Pages:

        tallas_existentes.append(
            page.Name.strip().upper()
        )

    # 🔥 detectar tallas disponibles en diseño base
    tallas_base = corel.obtener_tallas_base(doc_base)

    print("\n🎨 Tallas disponibles en diseño base:\n")

    for t in tallas_base:
        print(f" - {t}")

    print("\n📏 Tallas disponibles en plantilla:\n")

    for t in tallas_existentes:
        print(f" - {t}")

    # 📦 productos disponibles
    productos_disponibles = [
        "camiseta",
        "buso",
        "uniforme",
        "uniforme_largo",
        "pantaloneta"
    ]

    print("\n📦 Productos disponibles:\n")

    for p in productos_disponibles:
        print(f" - {p}")

    pedido_texto = input(
        "📦 Cantidades por talla, cantidad, producto (ej: 4XL:2:producto): "
    ).strip()

    pedido = []

    items = pedido_texto.split(",")

    for item in items:

        item = item.strip()

        if not item:
            continue

        try:

            talla, cantidad, producto = item.split(":")

            talla = talla.strip().upper()

            aliases = {
                "XXL": "2XL",
                "XXXL": "3XL",
                "XXXXL": "4XL",
                "XXXXXL": "5XL"
            }

            if talla in aliases:
                talla = aliases[talla]

            cantidad = int(cantidad.strip())

            producto = producto.strip().lower()

            # 🔥 validar talla plantilla
            if talla not in tallas_existentes:

                print(
                    f"⚠️ La talla {talla} no existe en plantilla"
                )

                continue

            # 🔥 validar producto
            if producto not in productos_disponibles:

                print(
                    f"⚠️ Producto inválido: {producto}"
                )

                continue

            # 🔥 validar tallas especiales
            tallas_especiales = ["4XL", "5XL"]

            if talla in tallas_especiales:

                if talla not in tallas_base:

                    print(
                        f"⚠️ No existe diseño base para talla especial {talla}"
                    )

                    continue

            pedido.append({

                "talla": talla,
                "cantidad": cantidad,
                "producto": producto
            })

        except:
            print(f"❌ Formato inválido: {item}")

    print(pedido)

    if len(pedido) == 0:
        print("❌ No hay pedidos válidos")
        exit()

    # 🔥 producción
    corel.filtrar_tallas(doc_resultado, pedido)
    corel.duplicar_paginas(doc_resultado, pedido)
    corel.limpiar_piezas_por_producto(doc_resultado, pedido)
    corel.transferir_diseno(doc_base, doc_resultado, pedido)
    #corel.listar_shapes(doc_base)