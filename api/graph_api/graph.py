from .node import Node
from .edge import Edge

class Graph:
    def __init__(self, directed:bool = False):
        if not isinstance(directed, bool):
            raise TypeError("directed must be a bool")

        self._directed = directed
        self._nodes: dict[str, Node] = {}
        self._edges: dict[str, Edge] = {}

    @property
    def directed(self) -> bool:
        return self._directed