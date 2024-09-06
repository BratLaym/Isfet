from core.message.message import Message
from core.cmd.command import Command
from core.module.registerModules import RegisterModules


class RequestHanler: 
    """Обработчик запросов
    """
    def __init__(self) -> None:
        # реестор модулей
        self._modules = RegisterModules()
    
    def processing(self, update: dict) -> list[Message]:
        cmd: Command
        data: dict[str, str | int] 
        
        # определяем команду и пользователя
        cmd, data = self._configurateCommand(update)
        # user = self.configurateUser(update)
        return self._cmd_executions(cmd, data)
    
    def _configurateUser(self):
        pass
        
    # определение команды
    def _configurateCommand(self, update: dict[str, str | dict]) -> tuple[Command, dict[str, str | int]]:
        cmd: str
        data = dict[str, str | int]

        # обрабатываем по разному handwritten и callback
        if (update.get("callback_query")):
            cmd = self._modules.findCommand(update["callback_query"]["data"], False)
            data =  {
                "text": update["callback_query"]["data"],
                "msg_id": int(update["callback_query"]["message"]["message_id"]),
                "chat_id": int(update["callback_query"]["message"]["chat"]["id"])
            }
        else:
            # cmd = self._modules.findCommand(update["message"]["text"], True)
            def plug(data) -> list[Message]:
                return [
                    Message(
                        data["text"],
                        data["chat_id"]
                    )
                ]
            cmd = Command("plug", "", plug)
            data =  {
                "text": update["message"]["text"],
                "msg_id": int(update["message"]["message_id"]),
                "chat_id": int(update["message"]["chat"]["id"])
            }
        return cmd, data
                    
    def _verify_access(self, user, cmd) -> bool:
        # получаем список ролей с доступом
        # получаем список ролей пользователя
        # возращаем факт песечения списков
        return True 
    
    def _cmd_executions(self, cmd: Command, data: dict[str, str | int]) -> list[Message]:
        # вызываем логику команды и возращаем результат
        return cmd.execution(data)
