from core.controll_data.session import Session
from core.utilities.event import Event
from core.utilities.message.message import Message
from core.utilities.scripts.document import Document
from core.utilities.scripts.script import Script


class WaitVerefity(Document):
    def __init__(self) -> None:
        super().__init__(
            "WaitVerefity",
            start_script=Script(self.loop)
        )

    def loop(
        self,
        event: Event,
        session: Session
    ) -> list[Message] | Message:

        # if (sum([
        #         line[0]
        #         for line in session.execute(
        #             "SELECT 1 FROM user"
        #         ).fetchall()
        # ]) == 1):
        #     session.execute("UPDATE user SET verefity = ?", (1,))
        #     return

        return Message(
            "Ожидайте подтверждения данных",
            event.chat_id
        )
