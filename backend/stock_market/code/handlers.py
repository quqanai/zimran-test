from datetime import date

from fastapi import Depends, HTTPException, status
from fastapi_pagination import Params

from code.exceptions import NewsNotFound, UnsupportedSymbol
from code.services import CompanyNewsListService, NewsDetailsService, NewsListService


async def get_news(params: Params = Depends()):
    return await NewsListService(params).do()


async def get_news_by_symbol(
    symbol: str, params: Params = Depends(),
    date_from: date = None, date_to: date = None,
):
    service = CompanyNewsListService(symbol, params, date_from, date_to)

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
