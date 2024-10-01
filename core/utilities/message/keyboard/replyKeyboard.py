from core.utilities.message.keyboard.key import Key
from json import dumps


class ReplyKeyboard:
    def __init__(
        self,
        keyboard: list[list[Key]] = [],
        is_persistent: bool = False,
        resize_keyboard: bool = False,
        one_time_keyboard: bool = False,
    ) -> None:

        self._is_persistent: bool = is_persistent
        self._resize_keyboard: bool = resize_keyboard
        self._one_time_keyboard: bool = one_time_keyboard
        self._keyboard: list[list[Key]] = keyboard

    def appendKeyboard(self, *keyboard_lines: list[Key]):
        for keyboard_line in keyboard_lines:
            self._keyboard.append(keyboard_line)

    def setKeyboard(self, *keyboard_lines: list[Key]):
        self._keyboard = keyboard_lines

    def compile(self) -> list[list[dict[str]: str]]:
        keyBoard = [
            [
                key.getReplyKey()
                for key in row
            ]
            for row in self._keyboard
        ]

        if (keyBoard.__len__()):
            return dumps({
                "keyboard": keyBoard,
                "is_persistent": self._is_persistent,
                "resize_keyboard": self._resize_keyboard,
                "one_time_keyboard": self._one_time_keyboard
            })
        else:
            return dumps({
                "remove_keyboard": True
            })
