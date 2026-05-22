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

    if not doc_base:

        print("❌ No se pudo abrir diseno_base.cdr")

        exit()

    pedido_nombre = input(
        "🧾 Nombre del archivo resultado: "
    ).strip()

    ruta_guardado = input(
        "💾 ¿Dónde guardar el archivo generado?: "
    ).strip()

    nombre_jugador = input(
        "🧍 Nombre jugador: "
    ).strip().upper()

    numero_jugador = input(
        "🔢 Número jugador: "
    ).strip()

    doc_resultado = corel.copiar_archivo_base(
        ruta_tallas,
        pedido_nombre,
        ruta_guardado
    )

    tallas_existentes = obtener_nombres_paginas(
        doc_resultado
    )

    tallas_base = corel.obtener_tallas_base(
        doc_base
    )

    mostrar_tallas(tallas_existentes)


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
        pedido,
        nombre_jugador,
        numero_jugador
    )

    while True:

        print("\n==========")
        print("1. Cambiar nombre")
        print("2. Salir")
        print("==========")

        opcion = input(
            "Seleccione una opción: "
        ).strip()

        if opcion == "1":

            nuevo_nombre = input(
                "\nNuevo nombre: "
            ).strip().upper()

            for page in doc_resultado.Pages:

                corel.cambiar_nombre_jugador(
                    page,
                    nuevo_nombre
                )

            print(
                f"\n✅ Nombre actualizado: "
                f"{nuevo_nombre}"
            )

        elif opcion == "2":

            print(
                "\n✅ Finalizando sistema..."
            )

            break

        else:

            print(
                "\n❌ Opción inválida"
            )