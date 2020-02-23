from search.lib.searchers import BaseSearcher, Query, Response


class Searcher(BaseSearcher):
    def search(self, query: Query) -> Response:
        pass
