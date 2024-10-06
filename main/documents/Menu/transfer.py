from core.controll_data.session import Session
from core.utilities.event import Event
from core.utilities.message.message import Message
from core.utilities.scripts.document import Document
from core.utilities.scripts.frame import Frame
from core.utilities.scripts.script import Script
from main.documents.Role.GiveRole import GiveRole


class Transfer(Frame):
    def __init__(self) -> None:
        super().__init__(
            "transfer",
            default_script=Script(self.button)
        )

    def button(
        self,
        event: Event,
        session: Session
    ) -> list[Message] | Message:
        buttons = {
            "give role": GiveRole
        }
        result: Document | None = buttons.get(event.data)
        if (result is None):
            return Message("не распознано", event.chat_id)

        return result().start(event, session)
