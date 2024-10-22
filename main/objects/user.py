from core.controll_data.session import Session


class User:
    sql = """id	INTEGER NOT NULL UNIQUE,
verefity  BOOLEAN NOT NULL DEFAULT FALSE,
chat_id	INTEGER NOT NULL UNIQUE,
tg	TEXT NOT NULL UNIQUE,
name  TEXT UNIQUE,
gender    TEXT,
letter_class  TEXT,
block	INTEGER,
room	TEXT,
PRIMARY KEY(id)"""

    def __init__(
        self,
        id_: int,
        verefity: bool,
        chat_id: int,
        tg: str,
        name: str | None,
        gender: int | None,
        letter: str | None,
        block: int | None,
        room: str | None
    ) -> None:
        self.id_: int = id_
        self.verefity: bool = verefity
        self.chat_id: int = chat_id
        self.tg: str = tg
        self.name: str | None = name
        self.gender: int | None = gender
        self.letter: str | None = letter
        self.block: int | None = block
        self.room: str | None = room

    def info(self):
        for value in [
            self.name,
            self.gender,
            self.letter,
            str(self.block) + self.room if (self.room) else None
        ]:
            yield value

    def roles(self, session: Session):
        return session.execute(
            """
            SELECT * FROM roles AS r
            JOIN users_roles AS ur ON s.id = ur.role_id
            WHERE ur.user_id = ?
            """,
            (self.id_,)
        ).fetchall()
