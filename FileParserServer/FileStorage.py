class FileStorage:

    @staticmethod
    def store_data(storage_path, entity_list, relation_list):
        print(storage_path)
        characters_path = storage_path + "characters.txt"
        relation_path = storage_path + "relation.txt"
        characters_str = ""
        relation_str = ""
        for ent in entity_list:
            characters_str += ent.name + ","
        for rel in relation_list:
            relation_str += rel.name + ","
        with open(characters_path, 'w', encoding="utf-8") as f:
            f.write(characters_str)
        with open(relation_path, 'w', encoding="utf-8") as f:
            f.write(relation_str)
