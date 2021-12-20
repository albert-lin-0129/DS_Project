import entity
import relation

class Graph:
    g_id = 0

    def __init__(self):
        self.id = Graph.g_id
        Graph.g_id += 1

        self.entity_dic = {}
        self.relation_dic = {}
        self.name = ""
        self.uid = 1

    def to_dic(self):
        dic = {"id": self.id, "uid": self.uid, "name": self.name}
        return dic

    def add_entity(self, _name="", _tag=""):
        entity_obj = entity.Entity(_name, _tag, self.id)
        self.entity_dic[entity_obj.e_id] = entity_obj
        return entity_obj

    def add_relation(self, _name, _first_entity, _second_entity):
        rel = relation.Relation(self.id, _name, _first_entity, _second_entity)
        self.relation_dic[rel.id] = rel
        return rel
