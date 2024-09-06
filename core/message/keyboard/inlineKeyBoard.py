from core.message.keyboard.key import Key
from core.message.keyboard.keyBoard import KeyBoard
from json import dumps

class InlineKeyBoard(KeyBoard):
    def __init__(self, keyboard: list[list[Key]], list_keyboard: list[Key]) -> None:
        super().__init__(keyboard)
        self._list_keyboard: list[Key] = list_keyboard
            
    def appendCustomKeyboard(self, *keyboard_lines: list[Key]):
        for keyboard_line in keyboard_lines:
            self._custom_keyboards_lines.append(keyboard_line)

    def setCustomKeyboard(self, *keyboard_lines: list[Key]):
        self._custom_keyboards_lines = keyboard_lines

    def compile(self) -> list[list[dict[str]: str]]:        
        def convert_keyboard_lines(keyboards_lines: list[list[Key]]) -> str:
            return [
                [
                    key.getInlineKey()
                    for key in line
                ]
                for line in keyboards_lines
            ]
        
        return dumps(
            {
                "inline_keyboard": [
                    *convert_keyboard_lines(self._list_keyboards_lines),
                    *convert_keyboard_lines(self._custom_keyboards_lines)
                ]
            }
        )
        