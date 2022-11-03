from ._rabbitmq import RabbitMQService


class DailyNotificationCreate(RabbitMQService):
    def __init__(self, queue_name: str, news: list, email: str):
        super().__init__(queue_name)
        self._news = news
        self._email = email

    def _get_content(self):
        rows = []

        for idx, news in enumerate(self._news, start=1):
            rows.append(f"{idx}. {news['title']}\n{news['content']}")

        return '\n\n'.join(rows)

    def _get_payload(self):
        return {
            'subject': 'Prosperi. Daily summary',
            'content': self._get_content(),
            'emails': [self._email],
        }
