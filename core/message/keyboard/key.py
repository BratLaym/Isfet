class Key:
    def __init__(self, text: str, callback_data: str = "") -> None:
        self._data: dict[str, str] = {
            "text": text,
            "callback_data": callback_data
        }
        
    def setText(self, text: str) -> None:
        self._data["text"] = str(text)

    def setCallback_data(self, callback_data: str) -> None:
        self._data["callback_data"] = str(callback_data)
        
    def getInlineKey(self) -> dict[str, str]:
        return self._data
    
    def getReplyKey(self) -> dict[str, str]:
        return {
            "text": self._data["text"]
        }
        