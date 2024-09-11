import sqlite3
from core.cmd.command import Command
from core.message.message import Message

from core.requesthandler.update import Update


class Module:
    def __init__(self) -> None:
        # иницилизируем команды
        self._commands: list[Command] = []

    def findCommand(self, value: str, handwritten: bool) -> Command | None:
        for command in self._commands:
            if (command.test(value, handwritten)):
                return command
        return None


class BaseModule(Module):
    def __init__(self) -> None:
        self.default_cmd = Command(r".*", None, self.logic_perrot)
        self._commands: list[Command] = [
            self.default_cmd
        ]

    def logic_perrot(
        self,
        data: Update,
        sesion: sqlite3.Cursor
    ) -> list[Message]:
        return [Message(data.data, data.chat_id)]
