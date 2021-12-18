class Relation:
    r_id = 0

    def __init__(self):
        self.id = Relation.r_id
        Relation.r_id += 1

        self.name = ""
        self.the_first_e_id = 0
        self.the_second_e_id = 0

    def __str__(self):
        return "id: " + str(self.id) + ", name: " + self.name + ", first: " + str(self.the_first_e_id) + ", second: " + str(self.the_second_e_id)