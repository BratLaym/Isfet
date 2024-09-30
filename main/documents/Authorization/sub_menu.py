# from core.controll_data.session import Session
# from core.utilities.event import Event
# from core.utilities.message.message import Message
from core.utilities.scripts.frame import Frame
from core.utilities.scripts.script import Script


class SubMenu(Frame):
    def __init__(self) -> None:
        super().__init__(
            "SubMenu",
            [
                Script(
                    # logic=self.pressButton
                )
            ]
        )
        self._text_buttons = [
            ["фамилию имя", "фамилия имя", "name"],
            ["пол", "Пол", "gender"],
            ["класс", "класс", "letter_class"],
            ["комнату", "комната", "room"],
        ]

    # def pressButton(
    #     self,
    #     event: Event,
    #     session: Session
    # ) -> list[Message] | Message:
    #     data: str = event.data.replace("Измен
    # ить ", "").replace("Ввести ", "")

    #     res:
    #     for text in self._text_buttons:
    #         if (data in text):
    #             res =
