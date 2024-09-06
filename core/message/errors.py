from core.message.message import Message

class ErrorVerifyAccess(Message):
    def  __init__(self, chat_id: int) -> None:
        super().__init__(
            "Простите, у вас недостаточно прав для этого действия", 
            chat_id
            )

class ErrorCommandNotFound(Message):
    def __init__(self, chat_id: int) -> None:
        super().__init__(
            "Простите, сообщение не распознано", 
            chat_id
            )