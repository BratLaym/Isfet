from core.utilities.message.keyboard.replyKeyboard import ReplyKeyboard
from core.utilities.message.keyboard.inlineKeyboard import InlineKeyboard
from urllib.parse import urlencode


class Message:
    def __init__(
        self,
        text: str,
        chat_id: int,
        keyboard: ReplyKeyboard | InlineKeyboard | None = None,
        msg_id: int | None = None
    ) -> None:
        self._text = text
        self._caht_id = chat_id
        self._keyboard = keyboard
        self.msg_id = msg_id

    def compile(self) -> str:
        message = {
            "text": self._text,
            "chat_id": self._caht_id,
        }

        if (self._keyboard):
            message["reply_markup"] = self._keyboard.compile()

        message = urlencode(message).encode()
        return message

    def method(self) -> str:
        if (self.msg_id is None):
            return "/sendMessage"
        return "/editMessageText"
