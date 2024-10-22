from core.controll_data.session import Session
from core.utilities.event import Event
from core.utilities.message.message import Message
from core.utilities.scripts.frame import Frame
from core.utilities.scripts.script import Script
from core.utilities.singleton import Singleton


class Document(metaclass=Singleton):
    def __init__(
        self,
        name: str = "default_doc",
        frames: dict[str, Frame] | list[Frame] = [],
        start_script: Script = Script(),
        default_frame: Frame = Frame()
    ) -> None:
        self.name = name
        self._frames: dict[str, Frame] = dict()
        self._default_frame: Frame = default_frame
        self.start_script: Script = start_script

        if (isinstance(frames, dict)):
            self._frames = frames
        else:
            for _name, frame in map(
                lambda frame: (frame.name, frame),
                frames
            ):
                self._frames[_name] = frame

    def find(
        self,
        frame: str | None = None,
        value: str = "",
        handwritten: bool | None = None
     ) -> Script | None:
        if (frame is None):
            return self.start_script
        result: Frame | None = self._frames.get(frame)
        if (result is None):
            result = self._default_frame
        return result.find(value, handwritten)

    def start(self, event: Event, session: Session) -> list[Message] | Message:
        return self.start_script.execution(event, session)
