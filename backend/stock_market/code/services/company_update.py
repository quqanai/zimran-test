from code.clients import FinnhubClient
from code.models import Company
from ._base import BaseService


class CompanyUpdateService(BaseService):
    def __init__(self, symbol: str):
        self._symbol = symbol

    async def _fetch_company_profile(self):
        async with FinnhubClient() as client:
            return await client.get_company_profile(self._symbol)

    def _parse_company(self, company: dict):
        return {
            'name': company['name'],
            'logo_url': company['logo'],
            'symbol': self._symbol,
        }

    async def _save_company(self, parsed_company: dict):
        company, _ = await Company.update_or_create(**parsed_company)
        return company

    async def do(self):
        company = await self._fetch_company_profile()
        parsed_company = self._parse_company(company)
        return await self._save_company(parsed_company)
