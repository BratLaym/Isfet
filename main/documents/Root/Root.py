from core.controll_data.session import Session
from core.utilities.event import Event
from core.utilities.message.message import Message
from core.utilities.scripts.document import Document
from core.utilities.scripts.script import Script
from main.documents.Authorization.Autorization import Authorization


class Root(Document):
    def __init__(self) -> None:
        super().__init__(
            "Root",
            start_script=Script(self.logic_start)
        )

    def logic_start(
        self,
        event: Event,
        session: Session
    ) -> list[Message] | Message:
        verefity: tuple[int] | int | None = session.execute(
            """SELECT verefity FROM user
            WHERE chat_id = ?""",
            (event.chat_id,)
        ).fetchone()

        if (isinstance(verefity, tuple)):
            verefity = verefity[0]

        if (verefity):
            return Message("plug", event.chat_id)
        else:
            session.execute(
                """INSERT INTO user (verefity, chat_id, tg)
                VALUES (0, ?, ?)""",
                (event.chat_id, event.user_tg)
            )
            return Authorization().start(event, session)
