from abc import ABC, abstractmethod


class IAPIHandler(ABC):

    @abstractmethod
    def connect_api(self):
        pass


class SMSImplementer(IAPIHandler):

    def connect_api(self):
        print(f'getting api from sms server')


class EmailImplementer(IAPIHandler):

    def connect_api(self):
        print(f'getting api from email server')


class INotifier(ABC):

    @abstractmethod
    def get_info(self):
        pass


class SMSNotifier(INotifier):

    def __init__(self, implementer: SMSImplementer) -> None:
        self.implementer = implementer

    def get_info(self):
        return self.implementer.connect_api()


class EmailNotifier(INotifier):

    def __init__(self, implementer: EmailImplementer) -> None:
        self.implementer = implementer

    def get_info(self):
        return self.implementer.connect_api()


sms = SMSNotifier(SMSImplementer())
sms.get_info()

email = EmailNotifier(EmailImplementer())
email.get_info()