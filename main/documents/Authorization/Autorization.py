from typing import Any
from core.controll_data.session import Session
from core.utilities.event import Event
from core.utilities.message.keyboard.key import Key
from core.utilities.message.keyboard.replyKeyboard import ReplyKeyboard
from core.utilities.message.message import Message
from core.utilities.scripts.document import Document
from core.utilities.scripts.script import Script
from main.documents.Authorization.inputClass import InputClass
from main.documents.Authorization.inputGender import InputGender
from main.documents.Authorization.inputName import InputName
from main.documents.Authorization.inputRoom import InputRoom
from main.documents.Authorization.sub_menu import SubMenu
from main.objects.user import User


class Authorization(Document):
    def __init__(self) -> None:
        super().__init__(
            "Authorization",
            [
                SubMenu(),
                InputName(self),
                InputGender(self),
                InputRoom(self),
                InputClass(self)
            ],
            Script(self._logic_start)
        )
        self._text_buttons = [
            ["фамилию имя", "фамилия имя", "name"],
            ["пол", "Пол", "gender"],
            ["класс", "класс", "letter_class"],
            ["комнату", "комната", "room"],
        ]

    def _logic_start(
        self,
        event: Event,
        session: Session
    ) -> list[Message] | Message:
        keyboard: ReplyKeyboard = ReplyKeyboard([])

        query: str = """SELECT * FROM users WHERE chat_id = ?"""
        res_select: Any = session.execute(query, (event.chat_id,)).fetchone()
        user: User = User(*res_select)

        text_msg: str = ""
        full_form: bool = True
        for id, value in enumerate(user.info()):
            full_form &= value is not None
            text_msg += self._append_button(id, value, keyboard)

        if (full_form):
            keyboard.appendKeyboard([Key("Сохранить")])

        session.set(event.chat_id, "doc", "Authorization")
        session.set(event.chat_id, "frame", "sub_menu")

        text_msg += "Введите данные:"
        return Message(text_msg, event.chat_id, keyboard)

    def _append_button(
        self,
        id: int,
        value: Any,
        keyboard: ReplyKeyboard
            ) -> str:
        text_button: str
        text_msg: str = ""
        if (value is not None):
            text_button = f"Изменить {self._text_buttons[id][0]}"
            text_msg = f"{self._text_buttons[id][1]}: {value}\n"
        else:
            text_button = f"Ввести {self._text_buttons[id][0]}"
        keyboard.appendKeyboard([Key(text_button, self._text_buttons[id][2])])
        return text_msg
