from sqlite3 import Cursor
from core.cmd.command import Command
from core.message.message import Message
from core.module.baseModule import Module
from core.requesthandler.update import Update


class Root(Module):
    def __init__(self) -> None:
        super().__init__()
        self._commands = [
            Command(
                r".*",
                self.default
            )
        ]

    def default(self, data: Update, session: Cursor) -> Message:
        return Message("plug", data.chat_id)
