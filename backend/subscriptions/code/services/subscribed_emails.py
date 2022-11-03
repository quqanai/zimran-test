from code.models import Subscription
from ._base import BaseService


class SubscribedEmailsService(BaseService):
    def __init__(self, symbol: str = None):
        self._symbol = symbol

    def _get_filter_kwargs(self):
        filter_kwargs = {}

        if self._symbol:
            filter_kwargs['symbol'] = self._symbol

        return filter_kwargs

    async def _get_subscribed_emails(self):
        filter_kwargs = self._get_filter_kwargs()
        return await (
            Subscription.filter(**filter_kwargs)
                        .distinct()
                        .values_list('email', flat=True)  # noqa: C812
        )

    async def do(self):
        return await self._get_subscribed_emails()
