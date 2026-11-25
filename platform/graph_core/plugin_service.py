from importlib.metadata import entry_points


class  PluginService:

    def __init__(self):
        self.plugins = {}

    def load_plugins(self,group:str):
        found_plugins = []

        for ep in entry_points(group=group):
            plugin_class = ep.load()
            plugin = plugin_class()
            found_plugins.append(plugin)

        self.plugins[group] = found_plugins