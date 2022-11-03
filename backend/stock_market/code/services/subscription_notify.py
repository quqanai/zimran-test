from code.models import Company
from ._rabbitmq import RabbitMQService


class SubscriptionNotifyService(RabbitMQService):
    def __init__(self, queue_name: str, company: Company):
        super().__init__(queue_name)
        self._company = company

    def _get_payload(self):
        return {
            'symbol': self._company.symbol,
            'company_name': self._company.name,
        }
