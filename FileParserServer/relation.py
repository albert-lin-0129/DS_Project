class Relation:
    r_id = 0

    def __init__(self, _p_id=0, _name="", _first=0, _second=0):
        self.id = Relation.r_id
        Relation.r_id += 1

        self.name = _name
        self.the_first_e_id = _first
        self.the_second_e_id = _second
        self.p_id = _p_id
        self.source_id = _first.id
        self.target_id = _second.id
        self.source = _first.name
        self.target = _second.name
        self.type = ""
        self.hash_id = self.id

    def __str__(self):
        return "id: " + str(self.id) + ", name: " + self.name + ", first: " + str(self.the_first_e_id) + ", second: " + str(self.the_second_e_id)

    def to_dic(self):
        dic = {"rid": self.id, "pid": self.p_id, "source_id": self.source_id,
               "target_id": self.target_id, "source": self.source, "target": self.target,
               "relation": self.name, "type": self.type, "hash_id": self.hash_id}
        return dic
