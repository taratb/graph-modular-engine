import unittest

from graph_api.graph import Graph
from graph_api.node import Node
from graph_api.edge import Edge

class TestGraph(unittest.TestCase):

    # for node operations
    #____________________________________________________________________
    def test_duplicate_node_does_not_replace_original(self):
        graph = Graph()
        original = Node("n1")
        graph.add_node(original)

        with self.assertRaises(ValueError):
            graph.add_node(Node("n1"))

        self.assertIs(graph.get_node("n1"), original)

    def test_removing_node_preserves_other_nodes(self):
        graph = Graph()
        graph.add_node(Node("n1"))
        remaining_node = Node("n2")
        graph.add_node(remaining_node)

        graph.remove_node("n1")

        with self.assertRaises(KeyError):
            graph.get_node("n1")

        self.assertEqual(graph.get_nodes(), [remaining_node])

    def test_connected_node_cannot_be_removed(self):
        graph = Graph()
        node = Node("n1")
        graph.add_node(node)
        graph.add_node(Node("n2"))
        edge = Edge("e1", "n1", "n2")
        graph.add_edge(edge)

        with self.assertRaises(ValueError):
            graph.remove_node("n1")

        self.assertIs(graph.get_node("n1"), node)
        self.assertIs(graph.get_edge("e1"), edge)


    # for edge operations
    # ____________________________________________________________________

    def test_removing_edge_preserves_nodes(self):
        graph = Graph()
        source = Node("n1")
        target = Node("n2")
        graph.add_node(source)
        graph.add_node(target)
        edge = Edge("e1", "n1", "n2")
        graph.add_edge(edge)

        self.assertIs(graph.get_edge("e1"), edge)

        graph.remove_edge("e1")

        self.assertEqual(graph.get_edges(), [])
        with self.assertRaises(KeyError):
            graph.get_edge("e1")
        self.assertIs(graph.get_node("n1"), source)
        self.assertIs(graph.get_node("n2"), target)

    def test_missing_endpoint_rejects_edge(self):
        graph = Graph()
        graph.add_node(Node("n1"))

        with self.assertRaises(ValueError):
            graph.add_edge(Edge("e1", "n1", "missing"))

        self.assertEqual(graph.get_edges(), [])

    def test_directed_graph_allows_opposite_edges(self):
        graph = Graph(directed=True)
        graph.add_node(Node("n1"))
        graph.add_node(Node("n2"))

        forward = Edge("e1", "n1", "n2")
        backward = Edge("e2", "n2", "n1")
        graph.add_edge(forward)
        graph.add_edge(backward)

        self.assertIs(graph.get_edge("e1"), forward)
        self.assertIs(graph.get_edge("e2"), backward)

    def test_undirected_graph_rejects_reversed_edge(self):
        graph = Graph(directed=False)
        graph.add_node(Node("n1"))
        graph.add_node(Node("n2"))
        original = Edge("e1", "n1", "n2")
        graph.add_edge(original)

        with self.assertRaises(ValueError):
            graph.add_edge(Edge("e2", "n2", "n1"))

        self.assertEqual(graph.get_edges(), [original])

    def test_self_loop_blocks_node_removal(self):
        graph = Graph()
        graph.add_node(Node("n1"))
        loop = Edge("e1", "n1", "n1")
        graph.add_edge(loop)

        with self.assertRaises(ValueError):
            graph.remove_node("n1")

        self.assertIs(graph.get_edge("e1"), loop)

        graph.remove_edge("e1")
        graph.remove_node("n1")

        self.assertEqual(graph.get_nodes(), [])


    def test_duplicate_edge_id_does_not_replace_original(self):
        graph = Graph()
        for node_id in ("n1", "n2", "n3"):
            graph.add_node(Node(node_id))

        original = Edge("e1", "n1", "n2")
        graph.add_edge(original)

        with self.assertRaises(ValueError):
            graph.add_edge(Edge("e1", "n2", "n3"))

        self.assertEqual(graph.get_edges(), [original])

    def test_parallel_edges_are_rejected(self):
        for directed in (False, True):
            with self.subTest(directed=directed):
                graph = Graph(directed=directed)
                graph.add_node(Node("n1"))
                graph.add_node(Node("n2"))
                original = Edge("e1", "n1", "n2")
                graph.add_edge(original)

                with self.assertRaises(ValueError):
                    graph.add_edge(Edge("e2", "n1", "n2"))

                self.assertEqual(graph.get_edges(), [original])