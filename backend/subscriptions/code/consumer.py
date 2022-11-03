import asyncio
import json

from aio_pika import connect_robust, IncomingMessage
from tortoise import Tortoise

from code.config import settings, TORTOISE_CONFIG
from code.consts import ChannelNames
from code.services import NotificationCreateService, SubscribedEmailsService


async def process(message: IncomingMessage):
    payload = json.loads(message.body.decode())
    symbol, company_name = payload['symbol'], payload['company_name']

    emails = await SubscribedEmailsService(symbol).do()

    if not emails:
        return

    await NotificationCreateService(
        ChannelNames.NOTIFICATIONS_EMAIL, symbol, company_name, emails,
    ).do()


async def main():
    await Tortoise.init(config=TORTOISE_CONFIG)

    connection = await connect_robust(settings.rabbitmq_url)

    channel = await connection.channel()
    await channel.set_qos(prefetch_count=100)

    queue = await channel.declare_queue(ChannelNames.NEWS_UPDATE, auto_delete=True)
    await queue.consume(process)

    try:
        await asyncio.Future()
    finally:
        await connection.close()


if __name__ == '__main__':
    asyncio.run(main())
