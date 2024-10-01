from core.utilities.scripts.collection import Collection
from core.utilities.scripts.document import Document
from main.documents.Authorization.Autorization import Authorization
from main.documents.WaitVerefity.WaitVerefity import WaitVerefity
from main.setUpDefinerPosition import setUpDefinerPosition
from main.objects.user import User
from main.documents.Root.Root import Root

TABLES: dict[str, str] = {
    "user": User.sql
}


DOCUMENTS: tuple[Document] = (
    Root(),
    Authorization(),
    WaitVerefity()
)


def configurate():
    setUpDefinerPosition()

    Collection(DOCUMENTS)
