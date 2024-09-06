from core.cmd.type import Typecmd

class Command:
    def __init__(self, name: str, typeCommand: Typecmd, logic) -> None:
        self._name: str = name
        self._type: Typecmd = typeCommand
        self._logic = logic
        
    def getType(self) -> None | Typecmd:
        return self._type
    
    def getName(self) -> str:
        return self._names
    
    def test(self, value: bool, handwritten: bool) -> bool:
        return self._type.test(value, handwritten)
    
    def execution(self, *args, **kwargs):
        return self._logic(*args, **kwargs)