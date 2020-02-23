import typing as t
from dataclasses import dataclass, field
from enum import Enum, unique


@unique
class LiteralType(Enum):
    STR = 1
    TAG = 2


@dataclass(frozen=True)
class LiteralRecord:
    doc_id: int
    pos: t.Optional[int] = None


@dataclass(frozen=True)
class Literal:
    type: LiteralType = field(init=False)
    value: str

    def build_record(self, doc_id: int) -> LiteralRecord:
        raise NotImplementedError


@dataclass(frozen=True)
class StrLiteral(Literal):

    type = LiteralType.STR
    pos: int

    def build_record(self, doc_id: int) -> LiteralRecord:
        return LiteralRecord(doc_id, self.pos)


@dataclass(frozen=True)
class TagLiteral(Literal):
    type = LiteralType.TAG

    def build_record(self, doc_id: int) -> LiteralRecord:
        return LiteralRecord(doc_id)
