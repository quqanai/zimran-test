from ._email import EmailService


class EmailSendService(EmailService):
    def __init__(self, email: str, subject: str, content: str):
        self._email = email
        self._subject = subject
        self._content = content

    def _get_email(self):
        return self._email

    def _get_subject(self):
        return self._subject

    def _get_content(self):
        return self._content
