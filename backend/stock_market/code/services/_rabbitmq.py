from abc import ABCMeta, abstractmethod
import json

from aio_pika import connect_robust, Message

from code.config import settings
from ._base import BaseService


class RabbitMQService(BaseService, metaclass=ABCMeta):
    def __init__(self, queue_name: str):
        self._queue_name = queue_name

    @abstractmethod
    def _get_payload(self): ...

    def _get_message(self):
        payload = self._get_payload()
        return Message(json.dumps(payload).encode())

    async def do(self):
        connection = await connect_robust(settings.rabbitmq_url)
        message = self._get_message()

        async with connection:
            channel = await connection.channel()
            queue = await channel.declare_queue(self._queue_name, auto_delete=True)
            await channel.default_exchange.publish(message, routing_key=queue.name)
