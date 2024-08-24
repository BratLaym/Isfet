from output.key import Key
from json import dumps

class KeyBoard:
    def __init__(self, *keybard_lines: list[Key]) -> None:
        self._list_keyboards_lines: list[list[Key]|None] = []
        self._custom_keyboards_lines: list[list[Key]|None] = keybard_lines

    def appendListKeyboardLines(self, *keys: Key) -> None:
        for key in keys:
            if (self._list_keyboards_lines[-1].__len__() == 2):
                self._list_keyboards_lines.append([])    
            append_list: list[dict[str, str]] = self._list_keyboards_lines[-1]
            append_list.append(key)
            
    def appendCustomKeyboard(self, *keyboard_lines: list[Key]):
        for keyboard_line in keyboard_lines:
            self._custom_keyboards_lines.append(keyboard_lines)

    def setCustomKeyboard(self, *keyboard_lines: list[Key]):
        self._custom_keyboards_lines = keyboard_lines

    def Compile(self) -> list[list[dict[str]: str]]:        
        def convert_keyboard_lines(keyboards_lines: list[list[Key]]) -> str:
            return [
                [
                    key.getDict()
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
        