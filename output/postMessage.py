from os import environ
from dotenv import load_dotenv, find_dotenv
from urllib.request import urlopen
from core.message.message import Message

class PostMessage:
    def __init__(self) -> None:
        load_dotenv(find_dotenv())
        self.telegrmUrl: str = environ.get("TELEGRAM_BOT_ROOT_URL")
        self.debug: bool = environ.get("DEBUG").lower() in ["1", "true", "t", "y", "yes"]
        
    def sendMessage(self, *messages: Message) -> None:
        for message in messages:
            urlopen(self.telegrmUrl + "/sendMessage", message.compile())
            
         