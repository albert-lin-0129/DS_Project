import json


class JsonExporter:

    @staticmethod
    def export_json(json_path, project_list, node_list, relation_list):
        json_list = {"project": [], "entity_list": [], "relation_list": []}
        for project in project_list:
            json_list["project"].append(project.to_dic())
        for node in node_list:
            json_list["entity_list"].append(node.to_dic())
        for relation in relation_list:
            json_list["relation_list"].append(relation.to_dic())
        # export_str = json.dumps(json_list)
        file_path = json_path
        with open(file_path, 'w', encoding="utf-8") as f:
            json.dump(json_list, f, ensure_ascii=False, indent=4)
