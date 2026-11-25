import unittest

from datetime import date
from graph_api.graph_element import GraphElement

class TestGraphElement(unittest.TestCase):
    def test_attribute_values_keep_their_types(self):
        element = GraphElement("element1")
        values = {
            "count": 5,
            "weight": 2.5,
            "name":"Tara",
            "created": date(2026, 11, 25)
        }
        for name, value in values.items():
            with self.subTest(name=name):
                element.set_attribute(name, value)
                stored = element.get_attributes()[name]

                self.assertEqual(stored, value)
                self.assertIs(type(stored), type(value))

    def test_invalid_update_preserves_previous_value(self):
        element = GraphElement("element1")
        element.set_attribute("count", 5)

        for invalid_value in (True, None, [], {}):
            with self.subTest(value=invalid_value):
                with self.assertRaises(TypeError):
                    element.set_attribute("count", invalid_value)

                self.assertEqual(element.get_attributes()["count"], 5)


    def test_attribute_copy_does_not_modify_original(self):
        element = GraphElement("element1")
        element.set_attribute("count", 5)

        attributes = element.get_attributes()
        attributes["count"] = 99
        attributes["extra"] = "new"

        self.assertEqual(element.get_attributes(), {"count": 5})

    def test_existing_attribute_can_be_updated(self):
        element = GraphElement("element1")
        element.set_attribute("count", 5)
        element.set_attribute("count", 8)

        self.assertEqual(element.get_attributes(), {"count": 8})

    def test_removing_attribute_preserves_other_attributes(self):
        element = GraphElement("element1")
        element.set_attribute("count", 5)
        element.set_attribute("name", "Tara")

        element.remove_attribute("count")

        self.assertEqual(element.get_attributes(), {"name": "Tara"})

        with self.assertRaises(KeyError):
            element.remove_attribute("count")

        self.assertEqual(element.get_attributes(), {"name": "Tara"})