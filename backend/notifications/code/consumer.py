import asyncio
import json

from aio_pika import connect_robust

from code.config import settings
from code.services import EmailSendService

QUEUE_NAME = 'notifications.email'


async def process(message):
    payload = json.loads(message.body.decode())

    async with message.process():
        for email in payload['emails']:
            await EmailSendService(email, payload['subject'], payload['content']).do()


async def main() -> None:
    connection = await connect_robust(settings.rabbitmq_url)

    channel = await connection.channel()
    await channel.set_qos(prefetch_count=100)

    queue = await channel.declare_queue(QUEUE_NAME, auto_delete=True)
    await queue.consume(process)

    try:
        await asyncio.Future()
    finally:
        await connection.close()


if __name__ == '__main__':
    asyncio.run(main())
