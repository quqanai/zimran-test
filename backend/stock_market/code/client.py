from httpx import AsyncClient

from code.config import settings


class FinnhubClient(AsyncClient):
    def __init__(self):
        super().__init__(
            base_url='https://finnhub.io/api/v1',
            headers={
                'x-finnhub-token': settings.finnhub_api_key,
            },
        )

    async def get_company_news(self, symbol: str):
        response = await self.get(
            '/company-news',
            params={
                'symbol': symbol,
                'from': '2022-09-01',
                'to': '2022-09-11',
            },
        )
        return response.json()
