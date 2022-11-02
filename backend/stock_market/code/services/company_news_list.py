from datetime import datetime, timedelta
from typing import Optional

from fastapi_pagination import Params

from code.consts import SYMBOLS
from code.exceptions import UnsupportedSymbol
from code.models import News
from ._pagination import PaginationService


class CompanyNewsListService(PaginationService):
    def __init__(
        self, symbol: str, params: Params,
        date_from: Optional[datetime], date_to: Optional[datetime],
    ):
        super().__init__(params)
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

    def _get_query(self):
        filter_kwargs = self._get_filter_kwargs()
        return News.filter(**filter_kwargs).order_by('-published_at')

    async def do(self):
        self._validate()
        return await super().do()
