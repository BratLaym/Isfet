class Key:
    def __init__(self, text: str, callback_data: str) -> None:
        self._data = {
            "text": text,
            "callback_data": callback_data
        }
        
    def setText(self, text: str) -> None:
        self._data["text"] = str(text)

    def setCallback_data(self, callback_data: str) -> None:
        self._data["callback_data"] = str(callback_data)
        
    def getDict(self) -> dict[str, str]:
        return self._data
        