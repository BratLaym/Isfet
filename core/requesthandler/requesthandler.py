import sqlite3
from core.message.message import Message
from core.cmd.command import Command
from core.module.registerModules import RegisterModules
from core.patern.singleton import Singleton
from core.requesthandler.update import Update
from core.requesthandler.connection import Connection


class RequestHanler(metaclass=Singleton):
    """Обработчик запросов
    """
    def __init__(self) -> None:
        # реестор модулей
        self._modules: RegisterModules = RegisterModules()

    def processing(self, update: Update) -> list[Message]:
        cmd: Command

        connection: Connection = Connection()
        session: sqlite3.Cursor = connection.create_session()

        # определяем команду и пользователя
        cmd = self._configurate(update, session)
        result: list[Message] = self._cmd_executions(
            cmd,
            update,
            session
        )
        connection.commit()
        return result

    # определение команды
    def _configurate(
        self,
        update: Update,
        session: sqlite3.Cursor
    ) -> Update:
        query: str = "SELECT verefity, default_func \
            FROM user WHERE chat_id =  ?"

        select_result: sqlite3.Cursor = session.execute(
            query,
            (update.chat_id, )
        ).fetchone()

        default: str = "menu"
        if (select_result):
            update.verifity = select_result[0]
            default = select_result[1]
        else:
            query = "INSERT INTO user (verefity, chat_id, tg, default_func) \
                VALUES (?, ?, ?, ?)"
            session.execute(
                query,
                (
                    update.verifity,
                    update.chat_id,
                    update.user_tg,
                    default
                )
            )

        value: str
        if (update.data[0] == '/'):
            value = update.data[1:]
        else:
            value = default

        cmd: Command = self._modules.findCommand(
            value,
            update.handwritten
            )
        return cmd

    def _verify_access(self, user, cmd) -> bool:
        # получаем список ролей с доступом
        # получаем список ролей пользователя
        # возращаем факт песечения списков
        return True

    def _cmd_executions(
        self,
        cmd: Command,
        data: Update,
        session: sqlite3.Cursor
    ) -> list[Message]:
        # вызываем логику команды и возращаем результат
        return cmd.execution(data, session)
