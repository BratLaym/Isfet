from core.controll_data.session import Session
from core.utilities.event import Event
from core.utilities.message.keyboard.key import Key
from core.utilities.message.keyboard.replyKeyboard import ReplyKeyboard
from core.utilities.message.message import Message
from core.utilities.scripts.document import Document
from core.utilities.scripts.script import Script
from main.documents.Menu.transfer import Transfer
from main.static.menu import HIERARCHY
from main.static.roles import ROLES_PREMISSION


class Menu(Document):
    def __init__(self) -> None:
        super().__init__(
            "Menu",
            {
                "transfer": Transfer()
            },
            start_script=Script(self.logic_start)
        )

    def logic_start(
        self,
        event: Event,
        session: Session
    ) -> list[Message] | Message:
        session.set(event.chat_id, "doc", "Menu")
        session.set(event.chat_id, "frame", "transfer")

        keyboard: ReplyKeyboard = self.get_keyboard(event, session)

        return Message(
            "Выберите действте:",
            event.chat_id,
            keyboard
        )

    def get_keyboard(
        self,
        event: Event,
        session: Session,
        position: str = "root"
    ) -> ReplyKeyboard:
        keys: None | dict[str, list[list[Key]]] = session.get(
            event.chat_id, "keyboard"
        )
        if (keys is None):
            keys = self.create_keyboard(event, session)
            session.set(event.chat_id, "keyboard", keys)

        return ReplyKeyboard(keys[position])

    def create_keyboard(
        self,
        event: Event,
        session: Session
    ) -> dict[str, list[list[Key]]]:
        struct_keyboard: dict[str, list[list[Key]]] = dict()
        allows: list[int] = self.get_allows(event, session)

        self.creating(struct_keyboard, allows)

        return struct_keyboard

    def creating(
        self,
        struct_keyboard: dict[str, list[list[Key]]],
        allows: list[int],
        position: str = "root"
     ) -> None:
        if (isinstance(HIERARCHY[position], int)):
            return [Key(position)] if (HIERARCHY[position] in allows) else []

        keyboard: list[list[Key]] = list()

        for button in HIERARCHY[position]:
            keyboard.append(self.creating(struct_keyboard, allows, button))

        if (keyboard.__len__() > 1 or position == "root"):
            struct_keyboard[position] = keyboard
            return [Key(position)]
        if (keyboard.__len__() == 1):
            return keyboard
        return []

    def get_allows(self, event: Event, session: Session):
        roles = session.execute(
            """
            SELECT ur.role_id
            FROM users_roles AS ur
            JOIN users AS u ON ur.user_id = u.id
            WHERE u.chat_id = ?
            """,
            (event.chat_id,)
        ).fetchall()

        allows = list()
        for role in roles:
            allows += ROLES_PREMISSION[role[0]]

        return allows
