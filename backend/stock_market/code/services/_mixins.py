class PaginationMixin:
    def __init__(self, page: int, page_size: int):
        self._page = page
        self._page_size = page_size

    def _get_offset(self):
        return self._page_size * (self._page - 1)
