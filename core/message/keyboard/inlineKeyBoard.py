from core.message.keyboard.key import Key
from json import dumps


class InlineKeyBoard:
    def __init__(
        self,
        keyboard: list[list[Key]] = [],
        list_keyboard: list[Key] = []
    ) -> None:
        self._list_keyboards: list[Key] = list_keyboard
        self._keyboard: list[list[Key] | None] = keyboard

    def appendKeyboard(self, *keyboard_lines: list[Key]):
        for keyboard_line in keyboard_lines:
            self._keyboard.append(keyboard_line)

    def setKeyboard(self, *keyboard_lines: list[Key]):
        self._keyboard = keyboard_lines

    def appendCustomKeyboard(self, *keyboard_lines: list[Key]):
        for keyboard_line in keyboard_lines:
            self._keyboard.append(keyboard_line)

    def setCustomKeyboard(self, *keyboard_lines: list[Key]):
        self._keyboard = keyboard_lines

    def compile(self) -> list[list[dict[str]: str]]:
        custom_keyboard = [
            [
                key.getInlineKey()
                for key in line
            ]
            for line in self._keyboard
        ]

        list_keyboard = [
            [
                self._list_keyboards[i * 2].getInlineKey(),
                self._list_keyboards[i * 2 + 1].getInlineKey()
            ]
            for i in range(self._list_keyboards.__len__() // 2)
        ]

        if (self._list_keyboards.__len__() % 2):
            list_keyboard.append([
                self._list_keyboards[-1].getInlineKey()
            ])

        return dumps(
            {
                "inline_keyboard": [
                    *list_keyboard,
                    *custom_keyboard
                ]
            }
        )
