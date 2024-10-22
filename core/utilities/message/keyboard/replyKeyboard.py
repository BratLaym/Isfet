from core.utilities.message.keyboard.key import Key
from json import dumps


class ReplyKeyboard:
    def __init__(
        self,
        keyboard: list[list[Key]] = [],
        is_persistent: bool = False,
        resize_keyboard: bool = False,
        one_time_keyboard: bool = False,
        list_keyboard: list[Key] = []
    ) -> None:

        self._is_persistent: bool = is_persistent
        self._resize_keyboard: bool = resize_keyboard
        self._one_time_keyboard: bool = one_time_keyboard
        self._keyboard: list[list[Key]] = keyboard
        self._list_keyboards: list[Key] = list_keyboard

    def appendKeyboard(self, *keyboard_lines: list[Key]):
        for keyboard_line in keyboard_lines:
            self._keyboard.append(keyboard_line)

    def setKeyboard(self, *keyboard_lines: list[Key]):
        self._keyboard = keyboard_lines

    def compile(self) -> list[list[dict[str]: str]]:
        keyboard = [
            [
                self._list_keyboards[i * 2].getReplyKey(),
                self._list_keyboards[i * 2 + 1].getReplyKey()
            ]
            for i in range(self._list_keyboards.__len__() // 2)
        ]
        if (self._list_keyboards.__len__() % 2):
            keyboard.append([
                self._list_keyboards[-1].getInlineKey()
            ])

        keyboard += [
            [
                key.getReplyKey()
                for key in row
            ]
            for row in self._keyboard
        ]

        if (keyboard.__len__()):
            return dumps({
                "keyboard": keyboard,
                "is_persistent": self._is_persistent,
                "resize_keyboard": self._resize_keyboard,
                "one_time_keyboard": self._one_time_keyboard
            })
        else:
            return dumps({
                "remove_keyboard": True
            })
