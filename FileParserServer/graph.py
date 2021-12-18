class Graph:
    g_id = 0

    def __init__(self):
        self.id = Graph.g_id
        Graph.g_id += 1

        self.relations = {}
        self.entity = {}
        self.name = ""
