from abc import ABC, abstractmethod
from typing import Any


class IImplementer(ABC):

    @abstractmethod
    def connect_api(self) -> None:
        pass


class SMSImplementer(IImplementer):

    def connect_api(self) -> None:
        print(f'getting api from sms server')


class EmailImplementer(IImplementer):

    def connect_api(self) -> None:
        print(f'getting api from email server')


class INotifier(ABC):

    @abstractmethod
    def get_info(self) -> None:
        pass


class SMSNotifier(INotifier):

    def __init__(self, implementer: SMSImplementer) -> None:
        self.implementer = implementer

    def get_info(self) -> None:
        return self.implementer.connect_api()


class EmailNotifier(INotifier):

    def __init__(self, implementer: EmailImplementer) -> None:
        self.implementer = implementer

    def get_info(self) -> None:
        return self.implementer.connect_api()


sms = SMSNotifier(SMSImplementer())
sms.get_info()

email = EmailNotifier(EmailImplementer())
email.get_info()