# from sqlite3 import Cursor
# from core.cmd.command import Command
# from core.message.message import Message
# from core.module.baseModule import Module
# from core.utilities.update import Update
# from main.modules.Autorization import AuthorizationModule


# class Authorization_input_room(Module):
#     def __init__(self) -> None:
#         super().__init__()
#         self._commands = [
#             Command(
#                 r"^((1[234])|([234][1-9]))\s*[АаБб]$",
#                 self._input
#             ),
#             Command(
#                 r".*",
#                 self._default
#             )
#         ]

#     def _default(self, data: Update, session: Cursor):
#         return Message("Напишите комнату (например 41Б)", data.chat_id)

#     def _input(self, data: Update, session: Cursor):
#         value = data.data.upper().replace(" ", "")
#         session.execute(
#             """UPDATE user SET
#             area = ?,
#             block = ?,
#             room = ?
#             WHERE chat_id = ?""",
#             ("Authorization", value[:-1], value[-1], data.chat_id)
#         )
#         return AuthorizationModule()._start_logic(data, session)
