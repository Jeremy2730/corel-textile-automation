# corel/personalization/zone_manager.py

from utils.logger import log_warning


class ZoneManager:

    def __init__(self):

        self.page_cache = {}

    def build_page_cache(self, page):

        cache = {}

        for shape in page.Shapes:

            try:

                name = shape.Name.strip()

                if name.startswith("zona_"):

                    cache[name] = shape

            except Exception:
                continue

        self.page_cache[page.Index] = cache

    def get_zone(
        self,
        page,
        zone_name
    ):

        if page.Index not in self.page_cache:

            self.build_page_cache(page)

        zone = (
            self.page_cache[page.Index]
            .get(zone_name)
        )

        if not zone:

            log_warning(
                f"Zona no encontrada: {zone_name}"
            )

        return zone