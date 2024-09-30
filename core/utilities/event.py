from typing import Any


class Event:
    def __init__(self, update: Any) -> None:
        self.data: str
        self.user_tg: str
        self.msg_id: int
        self.chat_id: int
        self.handwritten: bool
        self.error: bool = False
        try:
            if (update.get("callback_query") is not None):
                self.data = update["callback_query"]["data"]
                self.msg_id = int(
                    update["callback_query"]["message"]["message_id"]
                    )
                self.chat_id = int(
                    update["callback_query"]["message"]["chat"]["id"]
                    )
                self.user_tg = (
                    update["callback_query"]["message"]["chat"]["username"]
                    )
                self.handwritten = False
            else:
                self.data = update["message"]["text"]
                self.msg_id = int(update["message"]["message_id"])
                self.chat_id = int(update["message"]["chat"]["id"])
                self.user_tg = update["message"]["chat"]["username"]
                self.handwritten = True
        except KeyError:
            self.error = True

    def __bool___(self):
        return self.error
