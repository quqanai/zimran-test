from fastapi import HTTPException, status

from code.consts import SYMBOLS
from code.models import News
from code.services import CompanyNewsUpdateService


async def get_company_news(symbol: str):
    if symbol.upper() not in set(SYMBOLS):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    # await CompanyNewsUpdateService().do()
    return await News.all()
