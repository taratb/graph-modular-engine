import unittest

from graph_api.graph import Graph
from graph_api.node import Node

class TestGraph(unittest.TestCase):
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