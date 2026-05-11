from utils.logger import (
    log_info,
    log_error
)


def listar_shapes_documento(doc):

    try:

        for page in doc.Pages:

            log_info(
                f"\n📄 Página: {page.Name}"
            )

            for shape in page.Shapes:

                try:

                    log_info(
                        f" - Nombre: {shape.Name} | "
                        f"Tipo: {shape.Type}"
                    )

                except Exception:

                    log_error(
                        "Error leyendo shape"
                    )

    except Exception as e:

        log_error(
            f"Error listando shapes: {e}"
        )