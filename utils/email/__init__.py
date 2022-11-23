from utils.email.providers.base import BaseProvider
from utils.email.providers.google import GoogleProvider


class Email(object):
    provider: BaseProvider = GoogleProvider()

    def send_email(self, content: str, receiver: str):
        return self.provider.send_email(content, receiver)
