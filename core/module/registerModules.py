from core.module.baseModule import Module, BaseModule
from core.cmd.command import Command

class RegisterModules:
    def __init__(self) -> None:
        # иниацилизируем модули
        self._modules: list[Module] = [
            BaseModule()
        ]
        
    def findCommand(self, value: str, handwritten: bool, defoult: str="") -> Command:
        for module in self._modules: 
            result = module.findComma0nd(value, handwritten)
            if (result != None):
                return result
        for module in self._modules:
            result = module.findCommand(defoult, False)
            if (result != None):
                return result
        
        