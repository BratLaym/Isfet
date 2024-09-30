from typing import Any
from core.utilities.singleton import Singleton


class Cash(metaclass=Singleton):
    _cash: dict[int, dict[str, Any]] = dict()

    def get(self, chat_id: int, value: Any) -> Any:
        result = self._cash.get(chat_id)
        if (result is None):
            return None
        return result.get(value)

    def __getitem__(self, args: tuple[Any]) -> Any:
        self._cash.get(*args)
