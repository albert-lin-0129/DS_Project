class Relation:
    r_id = 0

    def __init__(self):
        self.id = Relation.r_id
        Relation.r_id += 1

        self.name = ""
        self.the_first_e_id = 0
        self.the_second_e_id = 0
        self.p_id = 0
        self.source_id = ""
        self.target_id = ""
        self.source = ""
        self.target = ""
        self.type = ""
        self.hash_id = ""

    def __str__(self):
        return "id: " + str(self.id) + ", name: " + self.name + ", first: " + str(self.the_first_e_id) + ", second: " + str(self.the_second_e_id)

    def to_dic(self):
        dic = {"rid": self.id, "pid": self.p_id, "source_id": self.source_id,
               "target_id": self.target_id, "source": self.source, "target": self.target,
               "relation": self.name, "type": "connection", "hash_id": self.hash_id}
        return dic
