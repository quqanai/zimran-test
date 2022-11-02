from tortoise.exceptions import DoesNotExist

from code.exceptions import NewsNotFound
from code.models import News
from ._base import BaseService


class NewsDetailsService(BaseService):
    def __init__(self, news_id: int):
        self._news_id = news_id

    async def _get_news(self):
        try:
            return await (
                News.get(id=self._news_id)
                    .values(
                        'id', 'title', 'content', 'published_at', 'image_url',
                        'company__name', 'company__logo_url',
                    )  # noqa: C812
            )
        except DoesNotExist:
            raise NewsNotFound

    async def do(self):
        return await self._get_news()
