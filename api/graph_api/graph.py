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

    def get_node(self, node_id: str) -> Node:
        return self._nodes[node_id]

    def get_nodes(self) -> list[Node]:
        return list(self._nodes.values())

    def add_node(self, node: Node) -> None:
        if not isinstance(node, Node):
            raise TypeError("node must be a Node object")

        node_id = node.get_id()

        if node_id in self._nodes:
            raise ValueError(f"Node with id {node_id} already exists")

        self._nodes[node_id] = node

    def remove_node(self, node_id: str) -> None:
        if node_id not in self._nodes:
            raise KeyError(node_id)

        for edge in self._edges.values():
            if node_id in (edge.get_source_id(), edge.get_target_id()):
                raise ValueError(f"Node {node_id} has edges and cannot be removed")

        del self._nodes[node_id]
