from abc import ABC, abstractmethod

from search.lib.searchers import Query, Response


class BaseSearcher(ABC):
    @abstractmethod
    def search(self, query: Query) -> Response:
        pass
