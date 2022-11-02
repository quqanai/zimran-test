from datetime import date

from fastapi import HTTPException, status
from tortoise.exceptions import DoesNotExist

from code.exceptions import UnsupportedSymbol
from code.models import News
from code.services import CompanyNewsListService


async def get_news(page: int = 1, page_size: int = 5):
    return await News.all().limit(page_size).order_by('-published_at')


async def get_news_by_symbol(
    symbol: str, page: int = 1, page_size: int = 5,
    date_from: date = None, date_to: date = None,
):
    service = CompanyNewsListService(symbol, page, page_size, date_from, date_to)

    try:
        return await service.do()
    except UnsupportedSymbol:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


async def get_news_by_id(news_id: int):
    try:
        return await News.get(id=news_id)
    except DoesNotExist:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
