from core.message.keyboard.key import Key

class KeyBoard:
    def __init__(self, keyboard: list[list[Key]]) -> None:
        self._keyboard: list[list[Key]|None] = keyboard
            
    def appendKeyboard(self, *keyboard_lines: list[Key]):
        for keyboard_line in keyboard_lines:
            self._keyboard.append(keyboard_line)

    def setKeyboard(self, *keyboard_lines: list[Key]):
        self._keyboard = keyboard_lines
        
    def compile(self) -> str:
        return ""