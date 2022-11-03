from abc import ABCMeta, abstractmethod
from email.message import EmailMessage

from aiosmtplib import send

from code.config import settings
from ._base import BaseService


class EmailService(BaseService, metaclass=ABCMeta):
    @abstractmethod
    def _get_email(self): ...

    @abstractmethod
    def _get_subject(self): ...

    @abstractmethod
    def _get_content(self): ...

    def _get_message(self):
        message = EmailMessage()
        message['From'] = settings.email_username
        message['To'] = self._get_email()
        message['Subject'] = self._get_subject()
        message.set_content(self._get_content())
        return message

    def _get_auth_kwargs(self):
        return {
            'hostname': settings.email_host,
            'port': settings.email_port,
            'username': settings.email_username,
            'password': settings.email_password,
            'use_tls': True,
        }

    async def do(self):
        message = self._get_message()
        await send(message, **self._get_auth_kwargs())
