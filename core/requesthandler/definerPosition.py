from typing import Callable

from core.controll_data.session import Session
from core.utilities.event import Event
from core.utilities.singleton import Singleton


class DefinerPosition(metaclass=Singleton):
    def __init__(
        self,
        logic: Callable[[Event, Session], tuple[str | None]]
    ) -> None:
        self.logic: Callable[[Event, Session], tuple[str | None]] = logic

    def define(self, event: Event, session: Session) -> tuple[str, None]:
        return self.logic(event, session)
