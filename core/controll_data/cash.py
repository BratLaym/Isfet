from typing import Any
from core.utilities.singleton import Singleton


class Cash(metaclass=Singleton):
    _cash: dict[int, dict[str, Any]] = dict()

    def get(self, chat_id: int, key: Any) -> Any:
        result = self._cash.get(chat_id)
        if (result is None):
            return None
        return result.get(key)

    def set(self, chat_id: int, key: Any, value: Any):
        user: dict[Any, Any] | None = self._cash.get(chat_id)
        if (user is None):
            self._cash[chat_id] = user = dict()
        user[key] = value

    def __getitem__(self, args: tuple[Any]) -> Any:
        self._cash.get(*args)
