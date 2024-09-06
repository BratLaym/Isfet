from core.cmd.command import Command 
from core.cmd.type import SimpleQuery
from core.message.message import Message

class Module:
    def __init__(self) -> None:
        # иницилизируем команды
        self._commands: list[Command] = []
        
    def findCommand(self, value: str, handwritten: bool) -> Command | None:
        for command in self._commands:
            if (command.test(value, handwritten)):
                return command
        return None
            
class BaseModule(Module):
    def __init__(self) -> None:
        self._commands: list[Command] = [
            Command("start", SimpleQuery(), self.lofic_start)
        ]
        
    def lofic_start(user, data: list[str]) -> Message:
        return Message(" ".join(data), user.chat_id)