from core.module.baseModule import Module, BaseModule
from core.cmd.command import Command


class RegisterModules:
    def __init__(self, modules: dict[str, Module]) -> None:
        # иниацилизируем модули
        self._base_module = BaseModule()
        self._modules: dict[str, Module] = dict()
        for area in modules:
            print(modules[area])
            self._modules[area] = modules[area]()

    def findCommand(
        self,
        area: str,
        value: str,
        handwritten: bool
    ) -> Command:
        result = self._modules[area].findCommand(value, handwritten)
        if (result is not None):
            return result
        return self._base_module.default_cmd
