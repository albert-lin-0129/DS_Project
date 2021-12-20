class Entity:
    e_id = 0
    tag_list = {'Nh': "人名", 'Ni': "机构名", 'Ns': '地名'}

    def __init__(self, _name="", _tag="", p_id=0):
        self.id = Entity.e_id
        Entity.e_id += 1

        self.name = _name
        self.category = ""
        self.tag = ""
        self.p_id = 0
        self.property = "{}"
        self.tag = _tag
        self.p_id = p_id
        self.property = ""

    def __str__(self):
        return "id: " + str(self.id) + ", name: " + self.name + ", category: " + self.category + ", tag: " + self.tag

    def to_dic(self):
        dic = {"eid": self.id, "pid": self.p_id, "name": self.name, "type": "Character",
               "property": self.property}
        return dic
