from .graph_element import GraphElement

class Edge(GraphElement):
    def __init__(self, edge_id:str, source_id:str, target_id:str):
        super().__init__(edge_id)

        if not isinstance(source_id, str) or not isinstance(target_id, str):
            raise TypeError("edge endpoint IDs must be string")

        self._source_id = source_id
        self._target_id = target_id

    def get_source_id(self) -> str:
        return self._source_id

    def get_target_id(self) -> str:
        return self._target_id