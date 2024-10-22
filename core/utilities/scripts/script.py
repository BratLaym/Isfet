from typing import Callable
from re import fullmatch
from core.utilities.message.message import Message
from core.utilities.event import Event
from core.controll_data.session import Session
from core.utilities.message.errors import ErrorNotFound


class Script:
    def __init__(
        self,
        logic: Callable[
            [Event, Session], list[Message] | Message
         ] = lambda ev, se: ErrorNotFound(ev.chat_id),

        definition: str | None = None,
        handwritten: bool | None = None

     ) -> None:
        self._regx: str | None = definition
        self._handwritten: bool | None = handwritten
        self._logic: Callable[[Event, Session],
                              list[Message] | Message] = logic

    def test(self, value: str, handwritten: bool | None) -> bool:
        if (self._regx is not None):
            matcning: bool = bool(fullmatch(self._regx, value))
        else:
            True
        if (self._handwritten is not None):
            m_handwritten: bool = self._handwritten == handwritten
        else:
            True
        return matcning and m_handwritten

    def execution(
        self,
        data: Event,
        session: Session
    ) -> list[Message] | Message:
        return self._logic(data, session)
