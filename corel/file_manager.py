import shutil
import os


def copiar_archivo_base(
    app,
    ruta_origen,
    nombre_archivo,
    carpeta_destino
):

    ruta_destino = os.path.join(
        carpeta_destino,
        f"{nombre_archivo}.cdr"
    )

    shutil.copy(
        ruta_origen,
        ruta_destino
    )

    print(
        f"📁 Archivo copiado: "
        f"{ruta_destino}"
    )

    return app.OpenDocument(
        ruta_destino
    )