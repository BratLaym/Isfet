from core.utilities.scripts.script import Script


class Frame:
    def __init__(
        self,
        name: str = "default_name",
        scripts: list[Script] = [],
        default_script: Script = Script()
    ) -> None:
        self._scripts: list[Script] = scripts
        self._default_script = default_script
        self.name: str = name

    def find(self, value: str, handwritten: bool | None) -> Script | None:
        for script in self._scripts:
            if (script.test(value, handwritten)):
                return script
        return self._default_script
