from sqlite3 import Cursor
from core.cmd.command import Command
from core.message.message import Message
from core.module.baseModule import Module
from core.requesthandler.update import Update
from main.modules.Autorization import AuthorizationModule


class Authorization_input_name(Module):
    def __init__(self) -> None:
        super().__init__()
        self._commands = [
            Command(
                r"^[А-яЁё]+\s+[А-яЁё]+$",
                self._input
            ),
            Command(
                r".*",
                self._default
            )
        ]

    def _default(self, data: Update, session: Cursor):
        return Message(
            "Напишите фамилию имя (например Ивонов Иван)",
            data.chat_id
            )

    def _input(self, data: Update, session: Cursor):
        session.execute(
            """UPDATE user SET
            area = ?,
            name = ?
            WHERE chat_id = ?""",
            (
                "Authorization",
                " ".join(
                    map(
                        lambda s: s.capitalize(),
                        data.data.lower().split()
                    )
                ),
                data.chat_id
             )
        )
        return AuthorizationModule()._start_logic(data, session)
