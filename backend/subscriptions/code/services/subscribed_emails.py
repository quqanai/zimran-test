from code.models import Subscription
from ._base import BaseService


class SubscribedEmailsService(BaseService):
    def __init__(self, symbol: str):
        self._symbol = symbol

    async def _get_subscribed_emails(self):
        return await Subscription.filter(symbol=self._symbol).values_list('email', flat=True)

    async def do(self):
        return await self._get_subscribed_emails()
