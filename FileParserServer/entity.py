class Entity:
    e_id = 0
    tag_list = {'Nh': "人名", 'Ni': "机构名", 'Ns': '地名'}

    def __init__(self):
        self.id = Entity.e_id
        Entity.e_id += 1

        self.name = ""
        self.category = ""
        self.tag = ""
