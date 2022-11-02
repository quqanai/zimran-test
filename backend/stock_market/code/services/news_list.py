from code.models import News
from ._base import BaseService
from ._mixins import PaginationMixin


class NewsListService(PaginationMixin, BaseService):
    async def _get_news(self):
        offset = self._get_offset()
        return await (
            News.all()
                .offset(offset)
                .limit(self._page_size)
                .order_by('-published_at')
                .values('id', 'title', 'content', 'published_at', 'image_url')  # noqa: C812
        )

    async def do(self):
        return await self._get_news()
