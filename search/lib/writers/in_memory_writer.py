import pickle
import typing as t
from collections import defaultdict
from pathlib import Path

from search.lib.data import Literal, LiteralRecord
from search.lib.writers import BaseWriter


class InMemoryWriter(BaseWriter):
    def __init__(self, filepath: Path) -> None:
        self._data: t.DefaultDict[Literal, t.List[LiteralRecord]] = defaultdict(list)
        self._filepath = filepath

    def write(self, doc_id: int, literal: Literal) -> int:
        self._data[literal].append(literal.build_record(doc_id))
        return 0

    def flush(self) -> None:
        with self._filepath.open(mode="w") as file_obj:
            pickle.dump(self._data, file_obj)
