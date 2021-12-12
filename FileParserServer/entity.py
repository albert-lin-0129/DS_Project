class Entity:
    e_id = 0

    def __init__(self):
        self.id = Entity.e_id
        Entity.e_id += 1

        self.name = ""
        self.category = ""
