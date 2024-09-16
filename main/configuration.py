from main.modules.Root import Root
from main.modules.Autorization import AuthorizationModule
from main.modules.Authorization_input.name import Authorization_input_name
from main.modules.Authorization_input.gender import Authorization_input_gender
from main.modules.Authorization_input.letter_class import (
    Authorization_input_letter_class
)
from main.modules.Authorization_input.room import Authorization_input_room

TABLES = {
    "user": """"id"	INTEGER NOT NULL UNIQUE,
"verefity"  BOOLEAN NOT NULL DEFAULT FALSE,
"chat_id"	INTEGER NOT NULL UNIQUE,
"tg"	TEXT NOT NULL UNIQUE,
"area" TEXT NOT NULL,
"name"  TEXT,
"gender"    TEXT,
"letter_class"  TEXT,
"block"	INTEGER,
"room"	TEXT,
PRIMARY KEY("id")"""
}

MODULES = {
    "Authorization": AuthorizationModule,
    "Authorization_input_name": Authorization_input_name,
    "Authorization_input_gender": Authorization_input_gender,
    "Authorization_input_letter_class": Authorization_input_letter_class,
    "Authorization_input_room": Authorization_input_room,
    "Root": Root,
}
