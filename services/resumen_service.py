def mostrar_resumen_produccion(pedido):

    print("\n📦 Producción generada:\n")

    total = 0

    for item in pedido:

        talla = item["talla"]
        cantidad = item["cantidad"]
        producto = item["producto"]

        print(
            f"{talla} → "
            f"{cantidad} unidades "
            f"({producto})"
        )

        total += cantidad

    print(f"\n✅ Total páginas: {total}")