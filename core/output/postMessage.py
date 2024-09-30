from os import environ
from dotenv import load_dotenv, find_dotenv
from urllib.request import urlopen
from core.utilities.singleton import Singleton
from core.utilities.message.message import Message


class PostMessages(metaclass=Singleton):
    def __init__(self) -> None:
        load_dotenv(find_dotenv())
        self.telegrmUrl: str = environ.get("TELEGRAM_BOT_ROOT_URL")
        self.debug: bool = (
            environ.get("DEBUG").lower() in ["1", "true", "t", "y", "yes"]
        )

    def sendMessages(self, messages: list[Message]) -> None:
        for message in messages:
            urlopen(self.telegrmUrl + message.method(), message.compile())
