from copy import deepcopy
from datetime import date
import math
import operator
import re

from graph_api.graph import Graph


class GraphQueryService:
    _comparators = {
        "==": operator.eq,
        "!=": operator.ne,
        ">": operator.gt,
        ">=": operator.ge,
        "<": operator.lt,
        "<=": operator.le,
    }
    _filter_pattern = re.compile(
        r"^\s*(?P<attribute>[^<>=!]+?)\s*(?P<operator>==|!=|>=|<=|>|<)\s*(?P<value>.+?)\s*$"
    )

    def __init__(self, graph: Graph):
        if not isinstance(graph, Graph):
            raise TypeError("graph must be a Graph object")

        self.original_graph = graph
        self.current_graph = graph

    def search(self, query: str) -> Graph:
        if not isinstance(query, str):
            raise TypeError("search query must be a string")
        if not query.strip():
            raise ValueError("search query cannot be empty")

        text = query.strip().casefold()
        matching_ids = set()

        for node in self.current_graph.get_nodes():
            attributes = node.get_attributes()
            if any(text in name.casefold() or text in str(value).casefold()
                   for name, value in attributes.items()):
                matching_ids.add(node.get_id())

        return self._create_subgraph(matching_ids)

    def filter(self, query: str) -> Graph:
        if not isinstance(query, str):
            raise TypeError("filter query must be a string")

        match = self._filter_pattern.fullmatch(query)
        if match is None:
            raise ValueError("filter format must be: attribute operator value")

        attribute = match.group("attribute").strip()
        raw_value = match.group("value").strip()
        compare = self._comparators[match.group("operator")]
        matching_ids = set()

        for node in self.current_graph.get_nodes():
            attributes = node.get_attributes()
            if attribute not in attributes:
                continue

            value = attributes[attribute]
            expected = self._convert_value(raw_value, value)
            if compare(value, expected):
                matching_ids.add(node.get_id())

        return self._create_subgraph(matching_ids)

    def reset(self) -> Graph:
        self.current_graph = self.original_graph
        return self.current_graph

    @staticmethod
    def _convert_value(raw_value: str, attribute_value: int | float | str | date):
        if len(raw_value) >= 2 and raw_value[0] == raw_value[-1] and raw_value[0] in ('"', "'"):
            raw_value = raw_value[1:-1]

        if type(attribute_value) is date:
            try:
                return date.fromisoformat(raw_value)
            except ValueError as error:
                raise ValueError(f"invalid date: {raw_value} (expected YYYY-MM-DD)") from error

        if type(attribute_value) in (int, float):
            try:
                number = int(raw_value) if re.fullmatch(r"[+-]?\d+", raw_value) else float(raw_value)
            except ValueError as error:
                raise ValueError(f"invalid numeric value: {raw_value}") from error
            if isinstance(number, float) and not math.isfinite(number):
                raise ValueError(f"invalid numeric value: {raw_value}")
            return number

        return raw_value

    def _create_subgraph(self, matching_ids: set[str]) -> Graph:
        subgraph = Graph(directed=self.current_graph.directed)

        for node in self.current_graph.get_nodes():
            if node.get_id() in matching_ids:
                subgraph.add_node(deepcopy(node))

        for edge in self.current_graph.get_edges():
            if edge.get_source_id() in matching_ids and edge.get_target_id() in matching_ids:
                subgraph.add_edge(deepcopy(edge))

        self.current_graph = subgraph
        return subgraph
