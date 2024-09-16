from sqlite3 import Cursor
from core.cmd.command import Command
from core.message.message import Message
from core.module.baseModule import Module
from core.requesthandler.update import Update
from main.modules.Autorization import AuthorizationModule


class Authorization_input_gender(Module):
    def __init__(self) -> None:
        super().__init__()
        self._commands = [
            Command(
                r"[мМжЖ]$",
                self._input
            ),
            Command(
                r".*",
                self._default
            )
        ]

    def _default(self, data: Update, session: Cursor):
        return Message("Напишите пол (М или Ж)", data.chat_id)

    def _input(self, data: Update, session: Cursor):
        session.execute(
            """UPDATE user SET
            area = ?,
            gender = ?
            WHERE chat_id = ?""",
            ("Authorization", data.data.upper(), data.chat_id)
        )
        return AuthorizationModule()._start_logic(data, session)
