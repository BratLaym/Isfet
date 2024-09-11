class Update:
    def __init__(self, update: dict[str, str | dict]) -> None:
        self.data: str
        self.user_tg: str
        self.msg_id: int
        self.chat_id: int
        self.verifity: bool = False
        self.handwritten: bool
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
