class Relation:
    r_id = 0

    def __init__(self):
        self.id = Relation.r_id
        Relation.r_id += 1

        self.name = ""
        self.the_first_e_id = 0
        self.the_second_e_id = 0
