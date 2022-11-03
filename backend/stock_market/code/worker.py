import asyncio

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from tortoise import Tortoise

from code.config import TORTOISE_CONFIG
from code.consts import QUEUE_NAME, SYMBOLS
from code.services import CompanyNewsUpdateService, CompanyUpdateService, SubscriptionNotifyService


async def update_company_news(is_initial: bool = False):
    for symbol in SYMBOLS:
        company = await CompanyUpdateService(symbol).do()
        await CompanyNewsUpdateService(company, is_initial).do()

        if not is_initial:
            await SubscriptionNotifyService(QUEUE_NAME, company).do()


scheduler = AsyncIOScheduler(timezone='UTC')
scheduler.add_job(update_company_news, 'interval', hours=1)


def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(
        Tortoise.init(config=TORTOISE_CONFIG),
    )
    loop.run_until_complete(
        update_company_news(is_initial=True),
    )
    scheduler.start()
    loop.run_forever()


if __name__ == '__main__':
    main()
