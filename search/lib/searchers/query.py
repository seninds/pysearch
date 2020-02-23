import typing as t
from dataclasses import dataclass

from search.lib.data import Literal


@dataclass
class Query:
    terms: t.List[Literal]
    flags: QueryFlags


class QueryFlags(t.NamedTuple):
    case_insensitive: bool = True
