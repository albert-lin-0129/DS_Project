from graphParser import GraphParser
from ltp import LTP
import entity


def ltp_data():
    """将句子处理成语义依存图"""

    ltp = LTP()
    # 分词
    seg, hidden = ltp.seg(["他叫汤姆去拿外衣。"])   # [['他', '叫', '汤姆', '去', '拿', '外衣', '。']]
    # 词性标注
    pos = ltp.pos(hidden)  # [['r', 'v', 'nh', 'v', 'v', 'n', 'wp']]
    # 命名实体识别
    ner = ltp.ner(hidden)  # [[('Nh', 2, 2)]]
    # tag, start, end = ner[0][0]
    # print(tag, ":", "".join(seg[0][start:end + 1]))
    # 语义角色标注
    srl = ltp.srl(hidden, keep_empty=False)  # (1, [('ARG0', 0, 0), ('ARG1', 2, 2), ('ARG2', 3, 5)])
    # 依存句法分析
    # dep = ltp.dep(hidden)
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
    sdp = ltp.sdp(hidden, mode='graph')

    return sdp, pos, seg, ner, srl


def entity_extraction(seg, ner):
    for i in range(len(ner)):
        ner_list = ner[i]
        for entity in ner_list:
            tag, start, end = entity
            print(tag, ":", "".join(seg[i][start:end + 1]))


def triple_extraction(seg, srl):
    for srl_ent in srl:
        print(srl_ent)

def node_extraction(seg, pos):
    """从语义依存图中提取出节点的名字和节点类型"""
    seg[0] = [str(i) for i in seg[0]]
    pos[0] = [str(i) for i in pos[0]]

    return seg[0], pos[0]


def relation_extraction(sdp,nodes):
    pass
    """
    提取出节点间的关系，将节点与关系整合成三元组，并存放在列表中。
    （node1,node2,relation)
    """
    rel = []
    for tuple in sdp[0]:
        # 根据索引提取出节点和关系
        index1 = int(tuple[0]) - 1
        index2 = int(tuple[1]) - 1
        node1 = nodes[index1]
        node2 = nodes[index2]
        relation = str(tuple[2])

        # 将节点和关系添加到3元组中
        triple = []
        triple.append(node1)
        triple.append(node2)
        triple.append(relation)

        # 将3元组整合到列表中
        rel.append(triple)

    return rel


if __name__ == '__main__':
    ent = entity.Entity()
    dic = {"0": ent}
    for x in dic:
        print(x)
        print(dic[x])
    # sdp, pos, seg, ner, srl = ltp_data()
    # # print(sdp)
    # # print(pos)
    # # print(seg)
    # node_name, node_type = node_extraction(seg, pos)
    # nodes = []
    # for i in range(len(node_name)):
    #     node = [node_type[i], node_name[i]]
    #     nodes.append(node)
    # print(nodes)
    #
    # rel = relation_extraction(sdp, nodes)
    # relations = []
    # for triple in rel:
    #     relation = [triple[0], str(triple[2]), triple[1]]
    #     relations.append(relation)
    # print(relations)

