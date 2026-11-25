from .attribute_types import AttributeValue
from datetime import date

class GraphElement:
    def __init__(self, element_id:str):
        if not isinstance(element_id, str):
            raise TypeError("element id must be a string")

        self._id = element_id
        self._attributes: dict[str, AttributeValue] = {}

    def get_id(self) -> str:
        return self._id

    def set_attributes(self, name:str, value:AttributeValue) -> None:
        if not isinstance(name, str):
            raise TypeError("name must be a string")

        if type(value) not in (int, float, str, date):
            raise TypeError("value must be int, float, str or date")

        self._attributes[name] = value


    def get_attributes(self) -> dict[str, AttributeValue]:
        return self._attributes.copy()

    def remove_attribute(self, name:str) -> None:
        del self._attributes[name]