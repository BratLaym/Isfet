from core.controll_data.session import Session
from core.utilities.event import Event
from core.utilities.message.keyboard.key import Key
from core.utilities.message.keyboard.replyKeyboard import ReplyKeyboard
from core.utilities.message.message import Message
from core.utilities.scripts.document import Document
from core.utilities.scripts.script import Script
from main.documents.SelectPeople.pressName import PressName


class SelectPeople(Document):
    def __init__(self) -> None:
        super().__init__(
            "SelectPeople",
            [
                PressName()
            ],
            start_script=Script(self.start_logic)
        )

    def start_logic(
        self,
        event: Event,
        session: Session
    ) -> list[Message] | Message:

        byClass: None | str = session.get(event.chat_id, "byClass")
        byVerefity: None | int = session.get(event.chat_id, "byVerefity")
        names: list[str] = self.get_names(session, byClass, byVerefity)
        session.set(event.chat_id, "select/people", names)

        format_name: list[Key] = []
        for name in names:
            format_name.append(Key(name))

        keyboard: ReplyKeyboard = ReplyKeyboard(list_keyboard=format_name)

        session.set(event.chat_id, "doc", "SelectPeople")
        session.set(event.chat_id, "frame", "pressName")

        return Message(
            "Выберите людей",
            event.chat_id,
            keyboard
        )

    def get_names(
        self,
        session: Session,
        byClass: str | None = None,
        byVerefity: int | None = 1
            ) -> list[str]:
        names: list[tuple[str]]
        if (byVerefity is None):
            byVerefity = 1

        if (byClass is not None):
            names = session.execute(
                """
                SELECT name FROM users
                WHERE verefity = ? AND letter_class = ?
                """,
                (byVerefity, byClass)
            ).fetchall()
        else:
            names = session.execute(
                """
                SELECT name FROM users
                WHERE verefity = ?
                """,
                (byVerefity,)
            ).fetchall()

        format_names = list(map(lambda tupl_name: tupl_name[0], names))
        return format_names
