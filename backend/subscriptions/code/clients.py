from httpx import AsyncClient

from code.config import settings


class StockMarketClient(AsyncClient):
    def __init__(self):
        super().__init__(base_url=settings.stock_market_url)

    async def get_company_news(self, symbol: str):
        response = await self.get(
            f'/companies/{symbol}/news',
            params={
                'page': 1,
                'size': 5,
            },
        )
        return response.json()
