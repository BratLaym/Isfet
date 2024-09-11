import sqlite3
from typing import Callable
from re import fullmatch

from core.message.message import Message

from core.requesthandler.update import Update


class Command:
    """Хранит индификатор и логику комманды
    """
    def __init__(
        self,
        definition: str,
        handwritten: bool,
        logic: Callable[[Update, sqlite3.Cursor],
                        list[Message]]
                ) -> None:
        self._regx: str = definition
        self._handwritten: bool | None = handwritten
        self._logic: Callable[[Update, sqlite3.Cursor],
                              list[Message]] = logic

    def test(self, value: str, handwritten: bool) -> bool:
        """
        проверяет на соотвестви типу команды
        Args:
            value (str): _description_
            handwritten (bool): _description_

        Returns:
            compliant: bool
        """
        matcning = fullmatch(self._regx, value)
        if (self._handwritten is None):
            return matcning
        else:
            return matcning and self._handwritten == handwritten

    def execution(
        self,
        data: Update,
        session: sqlite3.Cursor
    ) -> list[Message]:
        return self._logic(data, session)
