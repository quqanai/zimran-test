from code.models import News
from ._pagination import PaginationService


class NewsListService(PaginationService):
    def _get_query(self):
        return News.all().order_by('-published_at')
