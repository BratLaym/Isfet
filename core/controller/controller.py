from core.requesthandler.update import Update
from ping.ping import Ping
from output.postMessage import PostMessage
from core.requesthandler.requesthandler import RequestHanler
from core.module.baseModule import Module


class Controller:
    def __init__(self, *modules: list[Module]) -> None:
        self._input = Ping()
        self._output = PostMessage()
        self._core = RequestHanler()

    def startPiling(self) -> None:
        while True:
            if ((update := self._input.getValue()) != -1):
                for message in self._core.processing(Update(update)):
                    self._output.sendMessage(message)
