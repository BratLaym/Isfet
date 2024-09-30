from typing import Any
from core.controll_data.controller_data import ControllerData
from core.controll_data.session import Session
from core.requesthandler.definerPosition import DefinerPosition
from core.utilities.event import Event
from core.utilities.message.message import Message
from core.utilities.scripts.script import Script
from core.utilities.singleton import Singleton
from core.utilities.scripts.collection import Collection


class RequestHanler(metaclass=Singleton):
    def processing(self, event: dict[str, Any]) \
            -> list[Message]:
        event: Event = Event(event)
        session: Session = ControllerData().create_session()

        script: Script = self._configurate(event, session)
        result: list[Message] = self._executions(
            script,
            event,
            session
        )
        ControllerData().commit()
        return result

    def _configurate(
        self,
        event: Event,
        session: Session
    ) -> Script:
        document: str | None = None
        frame: str | None = None
        document, frame = DefinerPosition().define(event, session)

        event.data = event.data.replace('/', "")

        script: Script = Collection().find(
            document
        ).find(frame, event.data, event.handwritten)
        return script

    def _executions(
        self,
        script: Script,
        event: Event,
        session: Session
    ) -> list[Message]:

        result: Message | list[Message] = script.execution(event, session)
        if (isinstance(result, Message)):
            return [result]
        return result
