from typing import Any
from core.controll_data.session import Session
from core.utilities.event import Event
from core.utilities.message.keyboard.replyKeyboard import ReplyKeyboard
from core.utilities.message.message import Message
from core.utilities.scripts.frame import Frame
from core.utilities.scripts.script import Script
from main.documents.Menu.Menu import Menu
from main.objects.user import User
from main.static.roles import ADMIN


class SubMenu(Frame):
    def __init__(self) -> None:
        super().__init__(
            "sub_menu",
            [
                Script(
                    self.save,
                    r"Сохранить"
                ),
                Script(
                    self.pressButton,
                    r"((Изменить)|(Ввести))\s\w+.*"
                )
            ]
        )
        self._text_buttons = [
            ["фамилию имя", "фамилия имя", "name", "например Ивонов Иван"],
            ["пол", "Пол", "gender", "М или Ж"],
            ["класс", "класс", "class", "например 10Б"],
            ["комнату", "комната", "room", "например 41Б"],
        ]

    def pressButton(
        self,
        event: Event,
        session: Session
    ) -> list[Message] | Message:
        data: str = event.data.replace("Изменить ", "").replace("Ввести ", "")

        res: Message
        for text in self._text_buttons:
            if (data in text):
                res = Message(
                    f"Введите {text[0]} ({text[3]})",
                    event.chat_id,
                    ReplyKeyboard()
                )
                break
        else:
            res = Message(
                "нераспознано, пожалуйста, выберите из предложеннго",
                event.chat_id
            )

        session.set(event.chat_id, "frame", "input_" + text[2])

        return res

    def save(
        self,
        event: Event,
        session: Session
    ) -> list[Message] | Message:
        query: str = """SELECT * FROM users WHERE chat_id = ?"""
        res_select: Any = session.execute(query, (event.chat_id,)).fetchone()
        user: User = User(*res_select)

        full_form: bool = True
        for value in user.info():
            full_form &= value is not None
        if (not full_form):
            return Message("Введены не все данные", event.chat_id)

        session.execute(
            """
            UPDATE users
            SET verefity = -1
            WHERE chat_id = ?
            """,
            (event.chat_id,)
        )
        session.set(event.chat_id, "frame", None)

        if (user.id_ == 1):
            session.execute(
                """
                INSERT INTO users_roles
                VALUES (?, ?)
                """,
                (user.id_, ADMIN)
            )
            session.execute(
                """
                UPDATE users
                SET verefity = 1
                WHERE chat_id = ?
                """,
                (event.chat_id,)
            )
            return Menu().start(event, session)

        return Message(
            "Данные успешно сохранены, ожидайте верефикации",
            event.chat_id,
            ReplyKeyboard()
        )
