
from graph_api.graph import Graph
from graph_api.node import Node
from graph_api.plugin import DataSourcePlugin


class StubDataSource(DataSourcePlugin):

    def name(self) -> str:
        return "Stub Data Source"

    def identifier(self) -> str:
        return "stub-source"

    def load(self, **kwargs) -> Graph:
        graph = Graph()
        graph.add_node(Node("test-node"))
        return graph
