from core.requesthandler.update import Update
from core.ping.ping import Ping
from core.output.postMessage import PostMessage
from core.requesthandler.requesthandler import RequestHanler
from core.module.baseModule import Module


class Controller:
    def __init__(self, modules: dict[str, Module]) -> None:
        self._input = Ping()
        self._output = PostMessage()
        self._core = RequestHanler(modules)

    def startPiling(self) -> None:
        while True:
            if ((update := self._input.getValue()) != -1):
                self._output.sendMessage(
                    *self._core.processing(Update(update))
                )
