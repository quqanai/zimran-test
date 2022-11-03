from code.clients import StockMarketClient
from code.models import Subscription
from ._base import BaseService


class NewsSummaryCreate(BaseService):
    def __init__(self, email: str):
        self._email = email

    async def _get_subscribed_symbols(self):
        return await Subscription.filter(email=self._email).values_list('symbol', flat=True)

    async def _get_news(self, symbol: str):
        async with StockMarketClient() as client:
            json = await client.get_company_news(symbol)

        return json['items']

    async def do(self):
        symbols = await self._get_subscribed_symbols()

        for symbol in symbols:
            return await self._get_news(symbol)
