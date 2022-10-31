from datetime import datetime

from code.clients import FinnhubClient
from code.consts import SYMBOLS
from code.models import News
from ._base import BaseService


class CompanyNewsUpdateService(BaseService):
    async def _fetch_company_news(self, symbol: str):
        async with FinnhubClient() as client:
            return await client.get_company_news(symbol)

    def _parse_news(self, news: dict):
        parsed_news = {
            'id': news['id'],
            'symbol': news['related'],
            'title': news['headline'],
            'content': None,
            'image_url': None,
            'published_at': datetime.fromtimestamp(news['datetime']),
        }

        if news['summary']:
            parsed_news['content'] = news['summary']

        if news['image']:
            parsed_news['image_url'] = news['image']

        return parsed_news

    async def _save_company_news(self, parsed_news):
        objects = (News(**news) for news in parsed_news)
        await News.bulk_create(
            objects,
            on_conflict=['id'],
            update_fields=['symbol', 'title', 'content', 'image_url', 'published_at'],
        )

    async def do(self):
        for symbol in SYMBOLS:
            news = await self._fetch_company_news(symbol)
            parsed_news = map(self._parse_news, news)
            await self._save_company_news(parsed_news)
