import typing as t
from abc import ABC, abstractmethod

from search.lib.data import ParsedDocument


class BaseIndexer(ABC):
    @abstractmethod
    def index(self, doc: ParsedDocument) -> None:
        pass

    @abstractmethod
    def flush(self) -> None:
        pass
