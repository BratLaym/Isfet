from core.utilities.message.message import Message


class ErrorNotFound(Message):
    def __init__(self, chat_id: int) -> None:
        super().__init__(
                         "Простите, произошла ошибка: команда не распознона",
                         chat_id
                         )
