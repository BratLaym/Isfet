from core.utilities.singleton import Singleton
from core.controll_data.controller_data import ControllerData
from core.utilities.message.message import Message
from core.piling.piling import Piling
from core.output.postMessage import PostMessages
from core.requesthandler.requesthandler import RequestHanler


class Controller(metaclass=Singleton):
    def __init__(
        self,
        tables: dict[str, str]
    ) -> None:
        self._input = Piling()
        self._output = PostMessages()
        self._logic = RequestHanler()
        self._data = ControllerData(tables)

    def runbot(self) -> None:
        for event in self._input.start():
            result: list[Message] = self._logic.processing(event)
            self._output.sendMessages(result)
