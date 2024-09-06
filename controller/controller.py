from os import environ
from dotenv import load_dotenv, find_dotenv
from ping.ping import Ping
from output.postMessage import PostMessage
from time import sleep
from core.requesthandler.requesthandler import RequestHanler

class Controller:
    def __init__(self) -> None:
        self.input = Ping()
        self.output = PostMessage()
        self.core = RequestHanler()
    
    def startPiling(self) -> None:
        while True:
            if ((update := self.input.getValue()) != -1):
                for message in self.core.processing(update):
                    self.output.sendMessage(message)