from tortoise.exceptions import IntegrityError

from code.exceptions import SubscriptionAlreadyExists
from code.models import Subscription
from ._base import BaseService


class SubscriptionCreateService(BaseService):
    def __init__(self, email: str, symbol: str):
        self._email = email
        self._symbol = symbol

    async def _create_subscription(self):
        try:
            return await Subscription.create(email=self._email, symbol=self._symbol)
        except IntegrityError:
            raise SubscriptionAlreadyExists

    async def do(self):
        return await self._create_subscription()
