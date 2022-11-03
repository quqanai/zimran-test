from ._rabbitmq import RabbitMQService


class NotificationCreateService(RabbitMQService):
    def __init__(self, queue_name: str, symbol: str, company_name: str, emails: list[str]):
        super().__init__(queue_name)
        self._symbol = symbol
        self._company_name = company_name
        self._emails = emails

    def _get_payload(self):
        return {
            'subject': f'Prosperi. {self._company_name} ({self._symbol})',
            'content': f'{self._company_name} news are available',
            'emails': self._emails,
        }
