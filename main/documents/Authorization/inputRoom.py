from core.controll_data.session import Session
from core.utilities.event import Event
from core.utilities.message.message import Message
from core.utilities.scripts.document import Document
from core.utilities.scripts.frame import Frame
from core.utilities.scripts.script import Script


class InputRoom(Frame):
    def __init__(self, back: Document) -> None:
        super().__init__(
            "input_room",
            [Script(self.logic, r"^((1[234])|([234][1-9]))\s*[АаБб]$")],
            default_script=Script(self._default)
        )
        self.back = back

    def _default(self, event: Event, session: Session):
        return Message(
            "Напишите комнату (например 41Б)",
            event.chat_id
            )

    def logic(self, event: Event, session: Session) -> Message:
        data: str = event.data.upper().replace(" ", "")
        session.execute(
            """UPDATE users
            SET block = ?, room = ?
            WHERE chat_id = ?""",
            (data[:-1], data[-1], event.chat_id)
        )
        return self.back.start(event, session)
