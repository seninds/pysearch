from itertools import chain, count

from search.lib.data import ParsedDocument
from search.lib.indexers import BaseIndexer
from search.lib.writers import BaseWriter


class Indexer(BaseIndexer):
    def __init__(self, writer: BaseWriter) -> None:
        self._writer = writer
        self._doc_id = count(start=1, step=1)
        self._mem_size = 0
        self._literals_count = 0
        self._unique_literals_count = 0
        self._docs_count = 0

    def index(self, doc: ParsedDocument) -> None:
        doc_id = next(self._doc_id)
        self._docs_count += 1
        for literal in chain((doc.uri,), doc.str_literals, doc.tag_literals):
            self._unique_literals_count += 1 if literal in self._writer else 0
            self._mem_size += self._writer.write(doc_id, literal)
            self._literals_count += 1

    def flush(self) -> None:
        self._writer.flush()
