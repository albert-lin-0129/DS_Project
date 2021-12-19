from ltp import LTP
import os
from gensim.models import Word2Vec
from gensim.test.utils import datapath
import app
import gensim
import factory
import entity
import graph
import relation
import JsonStorage
import sys

pwd = os.path.dirname(__file__)
DATA_FOLDER = os.path.join(pwd, 'WPWPOI/data')
UPLOAD_FOLDER = os.path.join(pwd, 'WPWPOI/files')
CUSTOM_DICT_FOLDER = os.path.join(pwd, 'CustomDict')


class GraphParser:

    def __init__(self):
        # 默认加载 Small 模型
        self.ltp = LTP()
        for f_name in os.listdir(CUSTOM_DICT_FOLDER):
            filePath = os.path.join(CUSTOM_DICT_FOLDER, f_name)
            self.ltp.init_dict(filePath)
        # 分词 [['他', '叫', '汤姆', '去', '拿', '外衣', '。']]
        self.seg = []
        # 词性标注 [['r', 'v', 'nh', 'v', 'v', 'n', 'wp']]
        self.pos = []
        # 命名实体识别 [[('Nh', 2, 2)]]
        self.ner = []
        # 语义角色标注 [[(1, [('ARG0', 0, 0), ('ARG1', 2, 2), ('ARG2', 3, 5)])]]
        self.srl = []
        # 语义依存分析（图）
        # [
        #     [
        #         (1, 2, 'Agt'),
        #         (2, 0, 'Root'),   # 叫 --|Root|--> ROOT
        #         (3, 2, 'Datv'),
        #         (4, 2, 'eEfft'),
        #         (5, 4, 'eEfft'),
        #         (6, 5, 'Pat'),
        #         (7, 2, 'mPunc')
        #     ]
        # ]
        self.sdp = []
        self.hidden = None
        self.relation_dic = {}
        self.entity_dic = {}
        self.graph = graph.Graph()

    def parse(self, parse_str):
        self.seg, self.hidden = self.ltp.seg(parse_str)
        self.pos = self.ltp.pos(self.hidden)
        self.ner = self.ltp.ner(self.hidden)
        self.srl = self.ltp.srl(self.hidden, keep_empty=False)
        self.sdp = self.ltp.sdp(self.hidden, mode='graph')
        # result = ""
        # for i in range(len(segment)):
        #     for j in range(len(segment[i])):
        #         if pos[i][j] != 'wp':
        #             result += segment[i][j] + " "

        # print(segment)
        # return segment
        # dep = NLPParser.ltp.dep(hidden)
        # return dep

    def entity_extraction(self):
        print("解析entity......")
        for i in range(len(self.seg)):
            for j in range(len(self.seg[i])):
                if self.pos[i][j] == "wp":
                    continue
                entity_obj = entity.Entity()
                name = self.seg[i][j]
                tag = self.pos[i][j]
                entity_obj.name = name
                entity_obj.tag = tag
                entity_obj.p_id = self.graph.id
                self.entity_dic[name] = entity_obj
                # tag, start, end = ent
                # rel = relation.Relation()
                # print(tag, ":", "".join(self.seg[i][start:end + 1]))

        # for i in range(len(self.sdp)):
        #     sdp_list = self.sdp[i]
        #     for ent in sdp_list:
        #         tag, start, end = ent

    def relation_extraction(self):
        print("解析relation......")
        for i in range(len(self.srl)):
            for j in range(len(self.srl[i])):
                rel = relation.Relation()
                rel.name = self.seg[i][self.srl[i][j][0]]
                for ent in self.srl[i][j][1]:
                    tag, start, end = ent
                    key = self.seg[i][start]
                    if self.entity_dic.__contains__(key):
                        if tag == "A0":
                            rel.source_id = self.entity_dic[key].id
                            rel.source = self.entity_dic[key].name
                        if tag == "A1":
                            rel.target_id = self.entity_dic[key].id
                            rel.target = self.entity_dic[key].name
                    else:
                        continue
                    self.relation_dic[rel.id] = rel

        for i in range(len(self.sdp)):
            for j in range(len(self.sdp[i])):
                start, end, tag = self.sdp[i][j]
                rel = relation.Relation()
                rel.name = tag
                if tag.lower() == "root":
                    continue

                key = self.seg[i][start - 1]
                if self.entity_dic.__contains__(key):
                    rel.the_first_e_id = self.entity_dic[key].id
                    rel.the_second_e_id = self.entity_dic[key].id
                else:
                    continue
                self.relation_dic[rel.id] = rel

        for rel_key in self.relation_dic.keys():
            if self.entity_dic.__contains__(rel_key):
                del self.entity_dic[rel_key]

                # print(self.seg[i][srl_ent[0]])
                # ent_list = srl_ent[1]
                # for ent in ent_list:
                #     des, start, end = ent
                #     print(des, ":", "".join(self.seg[i][start:end + 1]))

    def relation_exception(self):
        pass

    def construct_graph(self, g_name, parse_str, g_id):
        self.graph.g_name = g_name
        self.graph.id = g_id
        self.parse(parse_str)
        self.entity_extraction()
        self.relation_extraction()
        # for entity_key in parser.entity_dic:
        #     print(str(entity_key) + ": " + str(parser.entity_dic[entity_key]))
        # for relation_key in parser.relation_dic:
        #     print(str(relation_key) + ": " + str(parser.relation_dic[relation_key]))
        return graph


class Word2VecParser:

    @staticmethod
    def parse(train_file_name, save_model_file):
        model = Word2Vec(corpus_file=train_file_name, min_count=2)
        model.save(save_model_file + ".model")
        # model.wv.save_word2vec_format(save_model_file + ".bin", binary=True)  # 以二进制类型保存模型以便重用


if __name__ == '__main__':
    filePath = sys.argv[1]
    p_id = int(sys.argv[2])
    utils = factory.Factory.get_docx()
    result = ""

    # filePath = os.path.join(UPLOAD_FOLDER, "test.docx")
    # app.LoadFile.format_transfer(filePath)
    # filePath = filePath.split('.')[0] + ".docx"
    # print(filePath)
    file = utils.get_file(filePath)
    paragraphs = utils.get_paragraphs(file)
    parser = GraphParser()
    parser_str = []
    for p in paragraphs:
        parser_str.append(p.text)
    parser.construct_graph("test", parser_str, p_id)
    JsonStorage.JsonExporter.export_json(filePath.replace(".docx", ".json"), [parser.graph], parser.entity_dic.values(), parser.relation_dic.values())

    # for i in range(len(seg)):
    #     seg_ent = seg[i]
    #     for j in range(len(seg_ent)):
    #         print("(", seg[i][j], " - ", pos[i][j], ")", end=", ")
    #     print()
    # NLPParser.entity_extraction(seg, ner)
    # NLPParser.relation_extraction(seg, srl)

    # count = 0
    # for f_name in os.listdir(UPLOAD_FOLDER):
    #     if count == 200:
    #         break
    #     count += 1
    #     filePath = os.path.join(DATA_FOLDER, f_name)
    #     app.LoadFile.format_transfer(filePath)
    #     filePath = filePath.split('.')[0] + ".docx"
    #     print(filePath)
    #     try:
    #         file = utils.get_file(filePath)
    #         paragraphs = utils.get_paragraphs(file)
    #         parser = NLPParser()
    #         for p in paragraphs:
    #             result += NLPParser.parse(p.text) + "\n"
    #     except:
    #         pass

    entity = entity.Entity()

    # segment_file_name = 'segment.txt'
    # save_model_name = 'test'
    # # with open(segment_file_name, 'w', encoding="utf-8") as f2:
    # #     f2.write(result)
    # #
    # # Word2VecParser.parse(segment_file_name, save_model_name)
    # model_out = Word2Vec.load(save_model_name + ".model")
    # print(len(model_out.wv.vectors))
    # # for data in model_out.wv.index_to_key:
    # #     print(data)
    # # 计算两个词的相似度/相关程度
    # # y1 = model_out.wv.similarity("被告", "朱新梅")
    # # y2 = model_out.wv.similarity("被告", "郭继兴")
    # # print(y1)
    # # print(y2)
    # y = model_out.wv.n_similarity(["原告", "安慧敏"], ["被告", "崔冬茜"])
    # print(y)
    # y_total = model_out.wv.most_similar("判决结果", topn=10)
    # for item in y_total:
    #     print(item[0], item[1])

