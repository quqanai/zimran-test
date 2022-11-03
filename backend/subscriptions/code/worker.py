import asyncio

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from tortoise import Tortoise

from code.config import TORTOISE_CONFIG
from code.consts import ChannelNames
from code.services import DailyNotificationCreate, NewsSummaryCreate, SubscribedEmailsService


async def create_daily_notifications():
    emails = await SubscribedEmailsService().do()

    for email in emails:
        news = await NewsSummaryCreate(email).do()

        if not news:
            continue

        await DailyNotificationCreate(ChannelNames.NOTIFICATIONS_EMAIL, news, email).do()


scheduler = AsyncIOScheduler(timezone='UTC')
scheduler.add_job(create_daily_notifications, 'cron', hour=13)


def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(
        Tortoise.init(config=TORTOISE_CONFIG),
    )
    scheduler.start()
    loop.run_forever()


if __name__ == '__main__':
    main()
