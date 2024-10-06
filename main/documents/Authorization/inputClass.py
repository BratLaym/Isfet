from core.controll_data.session import Session
from core.utilities.event import Event
from core.utilities.message.message import Message
from core.utilities.scripts.document import Document
from core.utilities.scripts.frame import Frame
from core.utilities.scripts.script import Script


class InputClass(Frame):
    def __init__(self, back: Document) -> None:
        super().__init__(
            "input_class",
            [
                Script(
                    self.logic,
                    r"^(8(\s*[аА])?)|(9\s*[абАБ])|((1[01])\s*[абАБвВ])$"
                )
            ],
            default_script=Script(self._default)
        )
        self.back = back

    def _default(self, event: Event, session: Session):
        return Message(
            "Напишите класс (например 10Б)",
            event.chat_id
            )

    def logic(self, event: Event, session: Session) -> Message:
        session.execute(
            """UPDATE users
            SET letter_class = ?
            WHERE chat_id = ?""",
            (event.data.upper().replace(" ", ""), event.chat_id)
        )
        return self.back.start(event, session)
