from dataclasses import dataclass


@dataclass
class Response:
    doc_id: int
    uri: str
