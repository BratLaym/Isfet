from core.message.keyboard.replyKeyBoard import ReplyKeyBoard
from core.message.keyboard.inlineKeyBoard import InlineKeyBoard
from urllib.parse import urlencode


class Message:
    def __init__(
        self,
        text: str,
        chat_id: int,
        keyboard: ReplyKeyBoard | InlineKeyBoard | None = None
    ) -> None:
        self._text = text
        self._caht_id = chat_id
        self._keyboard = keyboard

    def compile(self) -> str:
        message = {
            "text": self._text,
            "chat_id": self._caht_id,
        }

        if (self._keyboard):
            message["reply_markup"] = self._keyboard.compile()

        message = urlencode(message).encode()
        return message
