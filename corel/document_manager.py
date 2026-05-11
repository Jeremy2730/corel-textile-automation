def abrir_documento(app, ruta):

    try:

        doc = app.OpenDocument(ruta)

        print(f"📂 Abierto: {ruta}")

        return doc

    except Exception as e:

        print("❌ Error abriendo documento:", e)

        return None