from core.module.baseModule import Module, BaseModule
from core.cmd.command import Command


class RegisterModules:
    def __init__(self) -> None:
        # иниацилизируем модули
        self._base_module = BaseModule()
        self._modules: list[Module] = [
            self._base_module
        ]

    def findCommand(
        self,
        value: str,
        handwritten: bool,
        defoult: str = ""
    ) -> Command:
        for module in self._modules:
            result = module.findCommand(value, handwritten)
            if (result is not None):
                return result
        return self._base_module.default_cmd
