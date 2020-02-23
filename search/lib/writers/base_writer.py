from abc import ABC, abstractmethod

from search.lib.data import Literal


class BaseWriter(ABC):
    @abstractmethod
    def write(self, doc_id: int, literal: Literal) -> int:
        pass

    @abstractmethod
    def flush(self) -> None:
        pass

    @abstractmethod
    def __contains__(self, literal: Literal) -> bool:
        pass
