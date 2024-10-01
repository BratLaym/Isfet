from core.controll_data.session import Session
from core.utilities.event import Event
from core.utilities.message.message import Message
from core.utilities.scripts.document import Document
from core.utilities.scripts.frame import Frame
from core.utilities.scripts.script import Script


class InputName(Frame):
    def __init__(self, back: Document) -> None:
        super().__init__(
            "input_name",
            [Script(self.logic, r"^[А-яЁё]+\s+[А-яЁё]+$")],
            default_script=Script(self._default)
        )
        self.back = back

    def _default(self, event: Event, session: Session):
        return Message(
            "Напишите фамилию имя (например Ивонов Иван)",
            event.chat_id
            )

    def logic(self, event: Event, session: Session) -> Message:
        session.execute(
            """UPDATE user
            SET name = ?
            WHERE chat_id = ?""",
            (
                " ".join(map(lambda w: w.capitalize(), event.data.split())),
                event.chat_id
            )
        )
        return self.back.start(event, session)
