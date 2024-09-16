from sqlite3 import Cursor
from core.cmd.command import Command
from core.message.message import Message
from core.module.baseModule import Module
from core.requesthandler.update import Update
from main.modules.Autorization import AuthorizationModule


class Authorization_input_letter_class(Module):
    def __init__(self) -> None:
        super().__init__()
        self._commands = [
            Command(
                r"^(8(\s*[аА])?)|(9\s*[абАБ])|((1[01])\s*[абАБвВ])$",
                self._input
            ),
            Command(
                r".*",
                self._default
            )
        ]

    def _default(self, data: Update, session: Cursor):
        return Message("Напишите класс (например 10Б)", data.chat_id)

    def _input(self, data: Update, session: Cursor):
        session.execute(
            """UPDATE user SET
            area = ?,
            letter_class = ?
            WHERE chat_id = ?""",
            ("Authorization", data.data.upper().replace(" ", ""), data.chat_id)
        )
        return AuthorizationModule()._start_logic(data, session)
