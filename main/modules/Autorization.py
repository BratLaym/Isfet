from sqlite3 import Cursor
from typing import Any
from core.cmd.command import Command
from core.module.baseModule import Module
from core.requesthandler.update import Update
from core.message.message import Message
from main.objects.user import User
from core.message.keyboard.replyKeyBoard import ReplyKeyBoard
from core.message.keyboard.key import Key


class AuthorizationModule(Module):
    def __init__(self):
        self._commands = [
            Command(
                r"start",
                self._start_logic
            ),
            Command(
                r"((Изменить )|(Ввести )).*",
                self._push_input_button
            ),
            Command(
                r"Сохранить",
                self.save
            ),
            Command(
                r".*",
                self._default,
            ),
        ]

        self._text_buttons = [
            ["фамилию имя", "фамилия имя", "name"],
            ["пол", "Пол", "gender"],
            ["класс", "класс", "letter_class"],
            ["комнату", "комната", "room"],
        ]

    def _start_logic(self, data: Update, session: Cursor) -> Message:
        keyboard: ReplyKeyBoard = ReplyKeyBoard([])

        query: str = """SELECT * FROM user WHERE chat_id = ?"""
        res_select: Any = session.execute(query, (data.chat_id,)).fetchone()
        user: User = User(*res_select)

        text_msg: str = ""
        full_form: bool = True
        for id, value in enumerate(user.info()):
            full_form &= value is not None
            text_msg += self._append_button(id, value, keyboard)

        if (full_form):
            keyboard.appendKeyboard([Key("Сохранить")])

        text_msg += "Введите данные:"
        return Message(text_msg, data.chat_id, keyboard)

    def _append_button(
        self,
        id: int,
        value: Any,
        keyboard: ReplyKeyBoard
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

    def _default(self, data: Update, session: Cursor):
        return Message("Выберите, какие данные хотите ввести", data.chat_id)

    def _push_input_button(self, data: Update, session: Cursor) -> Message:
        value: str = data.data.replace("Ввести ", "").replace("Изменить ", "")
        id_button: int = -1
        for id, values in enumerate(self._text_buttons):
            if (value in values):
                id_button = id
                break
        if (id_button == -1):
            return self._default(data, session)
        session.execute(
            """UPDATE user SET area = ?
            WHERE chat_id = ?""",
            (f"Authorization_input_{self._text_buttons[id][2]}", data.chat_id)
        )
        return Message(
            f"Напишите {self._text_buttons[id][0]}",
            data.chat_id,
            ReplyKeyBoard([])
        )

    def save(self, data: Update, session: Cursor) -> Message:
        query: str = """SELECT * FROM user WHERE chat_id = ?"""
        res_select: Any = session.execute(query, (data.chat_id,)).fetchone()
        user: User = User(*res_select)

        full_form: bool = True
        for value in user.info():
            full_form &= value is not None

        if (not full_form):
            self._default(data, session)

        session.execute(
            """UPDATE user SET
            area = ?
            WHERE chat_id = ?""",
            ("Root", data.chat_id)
        )

        return Message("plug", data.chat_id, ReplyKeyBoard([]))
