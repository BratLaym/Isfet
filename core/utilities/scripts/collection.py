from core.utilities.scripts.document import Document
from core.utilities.singleton import Singleton


class Collection(metaclass=Singleton):
    def __init__(
        self,
        documents: dict[str, Document] | list[Document] = dict()
    ) -> None:
        self._documents: dict[str, Document] = dict()
        if (isinstance(documents, dict)):
            self._documents = documents
        else:
            for name, doc in map(
                lambda doc: (doc.name, doc),
                documents
            ):
                self._documents[name] = doc
        self._default_document = Document()

    def find(
        self,
        document: str | None = None
    ) -> Document:
        result = self._documents.get(document)
        if (result is None):
            result = self._default_document
        return result
