
import unittest
from unittest.mock import MagicMock, patch

from graph_core.plugin_service import PluginService


class TestPluginService(unittest.TestCase):

    @patch("graph_core.plugin_service.entry_points")
    def test_load_plugins(self, mock_entry_points):
        fake_plugin = object()

        fake_class = MagicMock(return_value=fake_plugin)
        fake_entry_point = MagicMock()
        fake_entry_point.load.return_value = fake_class

        mock_entry_points.return_value = [fake_entry_point]

        service = PluginService()
        service.load_plugins("graph_modular_engine.data_sources")

        self.assertEqual(
            service.plugins["graph_modular_engine.data_sources"],
            [fake_plugin]
        )

        mock_entry_points.assert_called_once_with(
            group="graph_modular_engine.data_sources"
        )
        fake_entry_point.load.assert_called_once()
        fake_class.assert_called_once_with()


if __name__ == "__main__":
    unittest.main()
