from re import fullmatch

class Typecmd:
    """
    Класс для определиния типа команды\n
    проверяет по способу отправки и совпадением с регулярным выражением
    """
    def __init__(self, definition: str,  handwritten: bool | None) -> None:
        self._regx: str = definition
        self._handwritten: bool | None = handwritten
    
    def test(self, value: str, handwritten: bool) -> bool:
        """
        проверяет на соотвестви типу команды
        Args:
            value (str): _description_
            handwritten (bool): _description_

        Returns:
            compliant: bool
        """
        
        matcning = fullmatch(self._regx, value)
        if (self._handwritten == None):
            return matcning 
        else:
            return matcning and self._handwritten == handwritten
    
class SimpleQuery(Typecmd):
    def __init__(self) -> None:
        super().__init__(r".*", None)
        