import unittest

from graph_api.plugin import (
    Plugin,
    DataSourcePlugin,
    VisualizerPlugin
)


class TestPluginAPI(unittest.TestCase):

    def test_plugin_is_abstract(self):
        with self.assertRaises(TypeError):
            Plugin()

    def test_data_source_is_abstract(self):
        with self.assertRaises(TypeError):
            DataSourcePlugin()

    def test_visualizer_is_abstract(self):
        with self.assertRaises(TypeError):
            VisualizerPlugin()

if __name__ == "__main__":
    unittest.main()
