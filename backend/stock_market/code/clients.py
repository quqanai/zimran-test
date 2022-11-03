from datetime import date

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

    async def get_company_profile(self, symbol: str):
        response = await self.get(
            '/stock/profile2',
            params={'symbol': symbol},
        )
        return response.json()

    async def get_company_news(self, symbol: str, date_from: date, date_to: date):
        response = await self.get(
            '/company-news',
            params={
                'symbol': symbol,
                'from': date_from.isoformat(),
                'to': date_to.isoformat(),
            },
        )
        return response.json()
