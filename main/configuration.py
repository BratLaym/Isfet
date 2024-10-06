from core.utilities.scripts.collection import Collection
from core.utilities.scripts.document import Document
from main.documents.Authorization.Autorization import Authorization
from main.documents.Menu.Menu import Menu
from main.documents.Role.GiveRole import GiveRole
from main.documents.WaitVerefity.WaitVerefity import WaitVerefity
from main.setUpDefinerPosition import setUpDefinerPosition
from main.objects.user import User
from main.documents.Root.Root import Root
from main.linked_tables.linked_tables import (
    users_roles,
)

TABLES: dict[str, str] = {
    "users": User.sql,
    "users_roles": users_roles
}


DOCUMENTS: tuple[Document] = (
    Root(),
    Authorization(),
    WaitVerefity(),
    Menu(),
    GiveRole(),
)


def configurate():
    setUpDefinerPosition()

    Collection(DOCUMENTS)
