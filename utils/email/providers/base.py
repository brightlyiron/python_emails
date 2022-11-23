from abc import ABCMeta, abstractmethod


class BaseProvider(metaclass=ABCMeta):
    @abstractmethod
    def send_email(self, content: str, receiver: str):
        raise NotImplementedError()
