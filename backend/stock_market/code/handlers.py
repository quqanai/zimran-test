from datetime import date, timedelta

from fastapi import HTTPException, status

from code.consts import SYMBOLS
from code.models import News


async def get_news_by_symbol(symbol: str, date_from: date, date_to: date):
    if symbol.upper() not in set(SYMBOLS):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return await News.filter(
        symbol=symbol, published_at__gte=date_from, published_at__lte=date_to + timedelta(days=1),
    )
