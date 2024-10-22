from core.controll_data.session import Session
from core.utilities.event import Event
from core.utilities.message.message import Message
from core.utilities.scripts.document import Document
from core.utilities.scripts.script import Script
from main.documents.SelectPeople.SelectPeople import SelectPeople


class GiveRole(Document):
    def __init__(self) -> None:
        super().__init__(
            "GiveRole",
            start_script=Script(self.logic_start)
        )

    def logic_start(
        self,
        event: Event,
        session: Session
    ) -> list[Message] | Message:
        session.set(event.chat_id, "doc", "GiveRole")
        return SelectPeople().start(event, session)
