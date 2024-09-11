from core.message.keyboard.key import Key
from core.message.keyboard.keyBoard import KeyBoard
from json import dumps


class ReplyKeyBoard(KeyBoard):
    def __init__(
        self,
        keyboard: list[list[Key]],
        is_persistent: bool = False,
        resize_keyboard: bool = False,
        one_time_keyboard: bool = False,
    ) -> None:

        super().__init__(keyboard)
        self._is_persistent: bool = is_persistent,
        self._resize_keyboard: bool = resize_keyboard,
        self._one_time_keyboard: bool = one_time_keyboard

    def compile(self) -> list[list[dict[str]: str]]:
        keyBoard = [
            [
                key.getReplyKey()
                for key in row
            ]
            for row in self._keyboard
        ]

        return dumps({
            "keyboard": keyBoard,
            "is_persistent": self._is_persistent,
            "resize_keyboard": self._resize_keyboard,
            "one_time_keyboard": self._one_time_keyboard
        })
