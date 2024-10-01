from core.controll_data.session import Session
from core.requesthandler.definerPosition import DefinerPosition
from core.utilities.event import Event


def setUpDefinerPosition():
    def define_position(event: Event, session: Session) -> tuple[str, None]:
        select: None | tuple[str] = session.execute(
            """
            SELECT doc FROM user
            WHERE chat_id = ?""",
            (event.chat_id,)
        ).fetchone()

        if (select is None):
            return "Root", None
        else:
            frame = session.get(event.chat_id, "frame")
            print(select[0].split('/')[-1], frame)
            return select[0].split('/')[-1], frame

    DefinerPosition(define_position)
