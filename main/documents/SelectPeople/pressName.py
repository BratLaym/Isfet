from core.controll_data.session import Session
from core.utilities.event import Event
from core.utilities.message.keyboard.key import Key
from core.utilities.message.keyboard.replyKeyboard import ReplyKeyboard
from core.utilities.message.message import Message
from core.utilities.scripts.frame import Frame
from core.utilities.scripts.script import Script


class PressName(Frame):
    def __init__(self):
        super().__init__(
            "pressName",
            default_script=Script(self.press)
        )

    def press(
        self,
        event: Event,
        session: Session,
    ) -> list[Message] | Message:

        name = session.get(event.chat_id, "select/people")
        format_name: list[str] = list(map(lambda user: Key(user[0]), name))
        keyboard: ReplyKeyboard = ReplyKeyboard(list_keyboard=format_name)

        return Message()
