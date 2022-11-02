from datetime import datetime, timedelta
from typing import Optional

from code.consts import SYMBOLS
from code.exceptions import UnsupportedSymbol
from code.models import News
from ._base import BaseService
from ._mixins import PaginationMixin


class CompanyNewsListService(PaginationMixin, BaseService):
    def __init__(
        self, symbol: str, page: int, page_size: int,
        date_from: Optional[datetime], date_to: Optional[datetime],
    ):
        super().__init__(page, page_size)
        self._symbol = symbol.upper()
        self._date_from = date_from
        self._date_to = date_to

    def _validate(self):
        if self._symbol not in set(SYMBOLS):
            raise UnsupportedSymbol

    def _get_filter_kwargs(self):
        kwargs = {'company__symbol': self._symbol}

        if self._date_from:
            kwargs['published_at__gte'] = self._date_from

        if self._date_to:
            kwargs['published_at__lte'] = self._date_to + timedelta(days=1)

        return kwargs

    async def _get_company_news(self, filter_kwargs: dict):
        offset = self._get_offset()
        return await (
            News.filter(**filter_kwargs)
                .order_by('-published_at')
                .offset(offset)
                .limit(self._page_size)
                .values('id', 'title', 'content', 'published_at', 'image_url')  # noqa: C812
        )

    async def do(self):
        self._validate()
        filter_kwargs = self._get_filter_kwargs()
        return await self._get_company_news(filter_kwargs)
