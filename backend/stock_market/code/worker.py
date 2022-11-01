import asyncio
from datetime import datetime

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from tortoise import Tortoise

from code.config import TORTOISE_CONFIG
from code.consts import SYMBOLS
from code.services import CompanyNewsUpdateService


async def update_company_news():
    tasks = (
        CompanyNewsUpdateService(symbol).do()
        for symbol in SYMBOLS
    )
    await asyncio.gather(*tasks)


scheduler = AsyncIOScheduler(timezone='UTC')
scheduler.add_job(
    update_company_news,
    'interval', hours=1, next_run_time=datetime.utcnow(),
)


def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(
        Tortoise.init(config=TORTOISE_CONFIG),
    )
    scheduler.start()
    loop.run_forever()


if __name__ == '__main__':
    main()
