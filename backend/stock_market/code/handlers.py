from datetime import date

from fastapi import HTTPException, status

from code.exceptions import NewsNotFound, UnsupportedSymbol
from code.services import CompanyNewsListService, NewsDetailsService, NewsListService


async def get_news(page: int = 1, page_size: int = 5):
    return await NewsListService(page, page_size).do()


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
    service = NewsDetailsService(news_id)

    try:
        return await service.do()
    except NewsNotFound:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
