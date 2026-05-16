# corel/document_manager.py

def abrir_documento(app, ruta):

    try:

        doc = app.OpenDocument(ruta)
        doc.Unit = 7  # Establecer la unidad a milímetros

        print(f"📂 Abierto: {ruta}")

        return doc

    except Exception as e:

        print("❌ Error abriendo documento:", e)

        return None