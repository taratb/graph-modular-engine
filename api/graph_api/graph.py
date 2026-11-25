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


    # Nodes
    #_______________________________________________________________________________
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


    # Edges
    # _______________________________________________________________________________

    def get_edge(self, edge_id: str) -> Edge:
        return self._edges[edge_id]


    def get_edges(self) -> list[Edge]:
        return list(self._edges.values())

    def add_edge(self, edge: Edge) -> None:
        if not isinstance(edge, Edge):
            raise TypeError("edge must be an Edge object")
        edge_id = edge.get_id()
        if edge_id in self._edges:
            raise ValueError(f"Edge with id {edge_id} already exists")

        source_id = edge.get_source_id()
        target_id = edge.get_target_id()

        if source_id not in self._nodes or target_id not in self._nodes:
            raise ValueError(f"both edge endpoints must exist")

        for existing in self._edges.values():
            existing_pair = (existing.get_source_id(), existing.get_target_id())

            same_direction = existing_pair == (source_id, target_id)
            reverse_direction = existing_pair == (target_id, source_id)

            if same_direction or (not self.directed and reverse_direction):
                raise ValueError(f"parallel edges are not allowed")

        self._edges[edge_id] = edge


    def remove_edge(self, edge_id: str) -> None:
        del self._edges[edge_id]

