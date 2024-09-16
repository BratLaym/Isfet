import sqlite3
from core.message.message import Message
from core.cmd.command import Command
from core.module.registerModules import RegisterModules
from core.patern.singleton import Singleton
from core.requesthandler.update import Update
from core.requesthandler.connection import Connection
from core.module.baseModule import Module


class RequestHanler(metaclass=Singleton):
    """Обработчик запросов
    """
    def __init__(self, modules: dict[str, Module]) -> None:
        # реестор модулей
        self._modules: RegisterModules = RegisterModules(modules)

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
    ) -> Command:
        query: str = "SELECT verefity, area \
            FROM user WHERE chat_id =  ?"

        select_result: sqlite3.Cursor = session.execute(
            query,
            (update.chat_id, )
        ).fetchone()
        area: str = "Authorization"

        if (select_result):
            update.verifity = select_result[0]
            area = select_result[1]
        else:
            query = """INSERT INTO user (
                verefity, chat_id, tg, area
                )
                VALUES (?, ?, ?, ?)"""
            session.execute(
                query,
                (
                    update.verifity,
                    update.chat_id,
                    update.user_tg,
                    area
                )
            )

        value: str
        if (update.data[0] == '/'):
            value = update.data[1:]
        else:
            value = update.data

        cmd: Command = self._modules.findCommand(
            area,
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
        result: Message | list[Message] = cmd.execution(data, session)
        if (isinstance(result, Message)):
            return [result]
        return result
