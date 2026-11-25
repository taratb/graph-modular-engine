from graph_api.graph import Graph
from graph_api.plugin import VisualizerPlugin

class StubVisualizer(VisualizerPlugin):

    def name(self) -> str:
        return "Stub Visualizer"

    def identifier(self) -> str:
        return "stub-visualizer"

    def render(self, graph: Graph) -> str:
        return f"<div>Nodes: {len(graph.get_nodes())}</div>"