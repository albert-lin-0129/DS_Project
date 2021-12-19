import json

class JsonExporter:

    def __init__(self):
        input_str = json.dumps()
        self.str = ""

    def export_node(self, node_list):
        for node in node_list:
            self.str 