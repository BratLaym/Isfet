from core.controll_data.session import Session
from core.requesthandler.definerPosition import DefinerPosition
from core.utilities.event import Event


def setUpDefinerPosition():
    def define_position(event: Event, session: Session) -> tuple[str, None]:
        doc: None | str = session.get(event.chat_id, "doc")

        if (doc is None):
            return "Root", None
        else:
            frame = session.get(event.chat_id, "frame")
            print(doc.split('/')[-1], frame, event.chat_id, event.user_tg)
            return doc.split('/')[-1], frame

    DefinerPosition(define_position)
