from os import environ
from dotenv import load_dotenv, find_dotenv
from urllib.request import urlopen
from urllib.parse import urlencode
from output.keyboard import KeyBoard

class Output:
    def __init__(self) -> None:
        load_dotenv(find_dotenv())
        self.telegrmUrl: str = environ.get("TELEGRAM_BOT_ROOT_URL")
        self.debug: bool = environ.get("DEBUG").lower() in ["1", "true", "t", "y", "yes"]
        
    def sendMessage(
        self, 
        chat_id: int, 
        text: str, 
        keyboard: KeyBoard | None = None,
        ) -> None:
        
        data: dict[str, str|list[list[dict[str, str]]]] = {
            "method": "sendMessage",
            "chat_id": str(chat_id),
            "text": str(text),
            "parse_mode": "HTML"
        }
        
        if (keyboard):
            data["reply_markup"] = keyboard.Compile()
                        
        if (self.debug):
            data["text"] = data["chat_id"] + ": " + data["text"] 
            data["chat_id"] = "1060021934"
        
        data = urlencode(data).encode()
        urlopen(self.telegrmUrl + "/sendMessage", data)
