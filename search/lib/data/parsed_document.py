import typing as t
from dataclasses import dataclass, field

from search.lib.data.literal import StrLiteral, TagLiteral


@dataclass(frozen=True)
class ParsedDocument:
    uri: TagLiteral
    str_literals: t.List[StrLiteral] = field(default_factory=list)
    tag_literals: t.List[TagLiteral] = field(default_factory=list)
