from core.controll_data.session import Session
from core.utilities.event import Event
from core.utilities.message.message import Message
from core.utilities.scripts.document import Document
from core.utilities.scripts.script import Script
from main.documents.Authorization.Autorization import Authorization
from main.documents.Menu.Menu import Menu
from main.documents.WaitVerefity.WaitVerefity import WaitVerefity


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
            """SELECT verefity FROM users
            WHERE chat_id = ?""",
            (event.chat_id,)
        ).fetchone()

        if (isinstance(verefity, tuple)):
            verefity = verefity[0]

        if (verefity is None):
            session.execute(
                """INSERT INTO users (verefity, chat_id, tg)
                VALUES (0, ?, ?)""",
                (event.chat_id, event.user_tg)
            )
            return Authorization().start(event, session)
        if (verefity == 1):
            return Menu().start(event, session)
        if (verefity == -1):
            return WaitVerefity().start(event, session)
        return Authorization().start(event, session)
