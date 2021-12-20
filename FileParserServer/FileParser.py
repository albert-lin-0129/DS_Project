# -*- coding: utf-8 -*-
"""
@file : FileParser.py
@author: zhangchilu
@time: 2021/12/19 18:23
"""
# -*- coding: UTF-8 -*-
"""
1.加载一个指定路径文件夹内的所有txt内容
2.把解析出来的指定内容写入Excel表格
"""
import xlrd
import xlwt
from xlutils.copy import copy
import os
import re
from ltp import LTP
import sys

sys.path.append(".")
import graph
import factory
import relation
import entity



pwd = os.path.dirname(__file__)
DATA_FOLDER = os.path.join(pwd, 'WPWPOI/data')
UPLOAD_FOLDER = os.path.join(pwd, 'WPWPOI/files')
CUSTOM_DICT_FOLDER = os.path.join(pwd, 'CustomDict')

ltp = LTP(device="cpu")
for f_name in os.listdir(CUSTOM_DICT_FOLDER):
    filePath = os.path.join(CUSTOM_DICT_FOLDER, f_name)
    ltp.init_dict(filePath)

# 加载某文件夹下的所有TXT文件，返回其绝对路径
def loadTXT(file_path):
    txt_files = []  # 保存文件地址和名称
    files = os.listdir(file_path)
    for _file in files:
        if not os.path.splitext(_file)[1] == '.docx':  # 判断是否为docx文件
            continue
        abso_path = os.path.join(file_path, _file)
        txt_files.append(abso_path)
    return txt_files


def extractor_direct(file_string):
    yiju = ""
    anyou = ""
    anqing = ""
    wenhao = ""
    # 以上变量的value将为[]
    fayuan_name = ""
    pancaishu_name = ""
    panjue = ""
    qingqiu = ""
    jiaodian = ""
    #  ############################定义列表[]和字典{}
    beigao = []
    yuangao = []
    shenpanyuan = []
    peishenyaun = []

    fayuan_name1 = []
    pancaishu_name1 = []
    panjue1 = []
    qingqiu1 = []
    jiaodian1 = []
    falv1 = []
    fatiao1 = []
    tiaotexts1 = []

    shenpanzhang = []
    zhuli = []
    shuji = []
    jingyingzhe = []
    disanren = []

    info = {}  # ***************变量info=dict字典*************************************************

    text = file_string
    headers = text.split("\n")

    #  ***************header查找******
    for index, one in enumerate(headers):
        header = one.split(" ")

        key = "审判长"
        if key in one:
            v = re.sub(r"\s+", " ", one)
            v = v.split("审判长")[-1]
            shenpanzhang.append(v)
            info[key] = shenpanzhang
            continue

        # 查找审判员
        key = "审判员"
        if key in one:
            v = re.sub(r"\s+", " ", one)
            v = v.split("审判员")[-1]
            shenpanyuan.append(v)
            info[key] = shenpanyuan
            continue

            # 查找人民陪审员
        key = "人民陪审员"
        if key in one:
            v = re.sub(r"\s+", " ", one)
            v = v.split("人民陪审员")[-1]
            peishenyaun.append(v)
            info[key] = peishenyaun
            continue

            # 查找法官助理
        key = "法官助理"
        if key in one:
            v = re.sub(r"\s+", " ", one)
            v = v.split("法官助理")[-1]
            zhuli.append(v)
            info[key] = zhuli
            continue

            # 查找书记员
        key = "书记员"
        if key in one:
            v = re.sub(r"\s+", " ", one)
            v = v.split("书记员")[-1]
            shuji.append(v)
            info[key] = shuji
            continue

            #  ################################################################
    for index, one in enumerate(headers):
        if re.sub(r"\s*", "", one) == "民事判决书":
            fayuan_name = headers[index - 1]
            fayuan_name = re.sub(r"\s+", "", fayuan_name)
            pancaishu_name = "民事判决书"
            break
        elif re.sub(r"\s*", "", one) == "民事裁定书":
            fayuan_name = headers[index - 1]
            fayuan_name = re.sub(r"\s+", "", fayuan_name)
            pancaishu_name = "民事裁定书"
            break

    for index, one in enumerate(headers):
        if re.findall(r"依照(.*)规定", one):
            yiju = re.findall(r"依照(.*)规定", one)

    text1 = re.sub(r"\s+", "", text)
    text2 = re.split(r"\s+|[，,:：.。;；]+", text1)
    text3 = re.split(r"\s+|[。]+", text1)

    for index, one in enumerate(text2):  # 对于text2中的每个元素分别取出，且命名为index、one
        if re.findall(r"法院民事..书(.*)原告", one):
            wenhao = re.findall(r"法院民事..书(.*)原告", one)
        if re.findall(r"原告.+被告.+纠纷一案", one):
            anqing = re.findall(r"原告.+被告.+纠纷一案", one)
            anyou = re.findall(
                r"垄断纠纷|垄断协议纠纷|横向垄断协议纠纷|纵向垄断协议纠|滥用市场支配地位纠纷|垄断定价纠纷|掠夺定价纠纷|拒绝交易纠纷|限定交易纠纷|捆绑交易纠纷|差别待遇纠纷|经营者集中纠纷", one)

    for index, one in enumerate(text3):
        if re.findall(r"原告.+被告.+纠纷一案.+立案", one):
            anqing = re.findall(r"原告.+被告.+纠纷一案.+立案", one)
            anyou = re.findall(
                r"垄断纠纷|垄断协议纠纷|横向垄断协议纠纷|纵向垄断协议纠纷|滥用市场支配地位纠纷|垄断定价纠纷|掠夺定价纠纷|拒绝交易纠纷|限定交易纠纷|捆绑交易纠纷|差别待遇纠纷|经营者集中纠纷", one)

        #  查找诉讼请求
        if "诉讼请求：" in one:
            qingqiu = re.sub(r"\s+", " ", one)
            qingqiu = qingqiu.split("：")[-1]
            continue
        elif "判令：" in one:
            qingqiu = re.sub(r"\s+", " ", one)
            qingqiu = qingqiu.split("：")[-1]
            continue
        #  查找焦点问题
        if "本案的焦点问题" in one:
            jiaodian = re.sub(r"\s+", " ", one)
            jiaodian = jiaodian.split("：")[-1]
            continue
        #  查找裁判结果
        if "裁定如下：" in one:
            panjue = re.sub(r"\s+", " ", one)
            panjue = panjue.split("：")[-1]
            continue
        elif "判决如下：" in one:
            panjue = re.sub(r"\s+", " ", one)
            panjue = panjue.split("：")[-1]
            continue

    #  ############################################查找法律、法条
    if len(yiju) != 0:

        yijutext1 = yiju[0]
        yijutext2 = re.split(r"，|,|、", yijutext1)  # 以符号分割

        for index, one in enumerate(yijutext2):
            if re.findall(r"《.*》", one):
                falv1 = re.findall(r"《.*》", one)

        if len(yijutext2) > 1:
            yijutext3 = re.sub(r"之", "", yijutext1)
            yijutext3 = re.split(r"，|,|《", yijutext3)
            for index, one in enumerate(yijutext3):
                if re.findall(r".*》第.+条", one):
                    fatiao = re.findall(r".*》第.+条", one)
                    fatiao1.append(fatiao)
                    fatiao1.append(fatiao)
                    tiaohead = one.split("》")[0]
                    tiaotexts = one.split("》")[1]
                    tiaotext1 = tiaotexts.split("、")
                    for i, p in enumerate(tiaotext1):
                        tiaotext = '《' + tiaohead + '》' + p
                        tiaotexts1.append(tiaotext)
        else:
            tiaotexts1.append(yijutext1)

    #  ##########

    info["案情"] = anqing
    info["案由"] = anyou
    info["裁判依据"] = yiju
    info["案件字号"] = wenhao
    #  以上value是[]

    fayuan_name1.append(fayuan_name)
    pancaishu_name1.append(pancaishu_name)
    panjue1.append(panjue)
    qingqiu1.append(qingqiu)
    jiaodian1.append(jiaodian)

    info["裁判结果"] = panjue1
    info["审理法院"] = fayuan_name1
    info["文书类型"] = pancaishu_name1
    info["本案的焦点问题"] = jiaodian1
    info["诉讼请求"] = qingqiu1

    info["法律依据"] = falv1
    info["法条依据"] = tiaotexts1

    #  ##########
    disclosure = re.split(r"\s+|[，。 ]+", text)
    counter = -1
    for one in disclosure[1:]:
        counter += 1
        text = re.split(r"\n", one)
        for index, item in enumerate(text):
            cc = -1

            #  查找4原告
            cc += 1
            key = "原告："  # 关键词key="原告"
            if key in item:  # 如果关键词在item
                # flag[cc] = False
                v = re.sub(r"\s+", " ", item)  # 变量v=在item中删去\s换行符等
                v = v.split("：")[-1]  # 变量v=删去“：”后的后一个v
                yuangao.append(v)
                info[key] = yuangao  # 将变量v的值以key名加入字典info中
                continue  # 如果关键词在item中则继续循环,直到没有此关键词。

            # 查找5被告
            cc += 1
            key = "被告："
            if key in item:
                v = re.sub(r"\s+", " ", item)
                v = v.split("：")[-1]
                beigao.append(v)
                info[key] = beigao
                continue  # 如果关键词在item中则继续循环,直到没有此关键词。

            # 查找14经营者
            cc += 1
            key = "经营者："
            if key in item:
                v = re.sub(r"\s+", " ", item)
                v = v.split("：")[-1]
                jingyingzhe.append(v)
                info[key] = jingyingzhe
                continue
            # 查找15第三人
            cc += 1
            key = "第三人："
            if key in item:
                v = re.sub(r"\s+", " ", item)
                v = v.split("：")[-1]
                disanren.append(v)
                info[key] = disanren
                continue


    return info


# 提取TXT文件内容
def extractor_ltp(file_string, p_id):
    file_string.replace(" ", "")

    new_graph = graph.Graph()
    new_graph.id = p_id
    root_entity = new_graph.add_entity("法案", "Root")

    name_list = {}  # 载入实体名 避免重复载入

    info_keys_noun1 = ["原告", "被告", "委托代理人", "负责人"]
    info_keys_noun2 = ["审判长", "代理审判员", "审判员", "书记员", "人民陪审员", "法官助理", "陪审员", "审判员"]

    text = file_string
    headers = text.split("\n")
    seg_list, hidden_list = ltp.seg(headers)
    pos_list = ltp.pos(hidden_list)
    # sdp = ltp.sdp(hidden, mode='graph')

    state = 0


    for seg_ind, seg in enumerate(seg_list):
        refered_entity = None  # 捕获到的entity
        for single_word in seg:
            single_word.replace(" ", "")
            single_word.replace("\t", "")
        for index in range(len(seg)):
            first_word = seg[0]
            word = seg[index]
            if word in name_list.keys():
                refered_entity = name_list[word]
            # if word in ["，", "。", "", " ", "(", ")"]:
            #     continue
            if state == 0 and pos_list[seg_ind][index] == "ns":
                e = new_graph.add_entity("".join(seg), "ns")
                new_graph.add_relation("审理法院", root_entity, e)
                break
            elif state == 0 and word.endswith("书"):
                e = new_graph.add_entity("".join(seg), "ns")
                new_graph.add_relation("文书类型", root_entity, e)
                break
            elif state == 0 and word.endswith("号"):
                e = new_graph.add_entity("".join(seg), "ns")
                new_graph.add_relation("文书编号", root_entity, e)
                break
            elif state == 2 and (first_word not in info_keys_noun1 or first_word == "原告"):
                state = 3
            elif (state == 0 or state == 1 or state == 2) and word in info_keys_noun1:
                target_entity = None
                entity_name = ""
                temp_str = ""
                entity_info_dic = {}  # 描述entity信息
                b_search_name = True
                b_search_location = False
                other_info = ""
                while index + 1 < len(seg):
                    index = index + 1
                    if pos_list[seg_ind][index] == "nh" and b_search_name:  # 人名
                        entity_name += seg[index]
                    elif "住" in seg[index]:  # 终止人名搜索 属性填充
                        entity_info_dic["住址"] = ""
                        b_search_location = True
                        b_search_name = False
                    elif seg[index] in ["男", "女"]:
                        entity_info_dic["性别"] = seg[index]
                        b_search_name = False
                    elif "族" in seg[index]:
                        entity_info_dic["民族"] = seg[index]
                        b_search_name = False
                    elif "年" in seg[index] or "月" in seg[index] or "日" in seg[index]:
                        temp_str += seg[index]
                        b_search_name = False
                    elif "出生" == seg[index] or "生" == seg[index]:
                        entity_info_dic["生日"] = temp_str
                        temp_str = ""
                        b_search_name = False
                    elif b_search_name and pos_list[seg_ind][index] not in ["v", "wp"]:
                        entity_name += seg[index]
                    elif b_search_location and pos_list[seg_ind][index] not in ["v", "wp"]:
                        entity_info_dic["住址"] += seg[index]
                    elif pos_list[seg_ind][index] not in ["v", "wp"]:
                        other_info += seg[index]
                        b_search_name = False
                        b_search_location = False
                    else:
                        b_search_name = False
                        b_search_location = False

                if entity_name != "" and entity_name not in name_list:
                    target_entity = new_graph.add_entity(entity_name, "nh")
                    new_graph.add_relation(word, root_entity, target_entity)
                    name_list[entity_name] =target_entity
                    for key in entity_info_dic.keys():
                        new_entity = new_graph.add_entity(entity_info_dic[key], "n")
                        new_graph.add_relation(key, target_entity, new_entity)
                if state == 0:
                    state = 1
                if state == 1 and word != "原告":
                    state = 2

            if state == 3 and word in info_keys_noun2:
                target_entity = None
                entity_name = ""
                entity_info_dic = {}  # 描述entity信息
                b_search_name = True
                b_search_location = False
                other_info = ""
                while index + 1 < len(seg):
                    index = index + 1
                    if pos_list[seg_ind][index] == "nh" and b_search_name:  # 人名
                        entity_name += seg[index]
                    elif "住" in seg[index]:  # 终止人名搜索 属性填充
                        entity_info_dic["住址"] = ""
                        b_search_location = True
                        b_search_name = False
                    elif seg[index] in ["男", "女"]:
                        entity_info_dic["性别"] = seg[index]
                        b_search_name = False
                    elif "族" in seg[index]:
                        entity_info_dic["民族"] = seg[index]
                        b_search_name = False
                    elif b_search_name and pos_list[seg_ind][index] not in ["v", "wp"]:
                        entity_name += seg[index]
                    elif b_search_location and pos_list[seg_ind][index] not in ["v", "wp"]:
                        entity_info_dic["住址"] += seg[index]
                    elif pos_list[seg_ind][index] not in ["v", "wp"]:
                        other_info += seg[index]
                        b_search_name = False
                        b_search_location = False
                    else:
                        b_search_name = False
                        b_search_location = False
                if entity_name != "" and entity_name not in name_list:
                    target_entity = new_graph.add_entity(entity_name, "nh")
                    new_graph.add_relation(word, root_entity, target_entity)
                    name_list[entity_name] = target_entity
                    for key in entity_info_dic.keys():
                        new_entity = new_graph.add_entity(entity_info_dic[key], "n")
                        new_graph.add_relation(key, target_entity, new_entity)
            if state == 3 and word in ["给付", "赔偿"]:
                money_type = ""
                money_num = ""
                while index + 1 < len(seg):
                    index = index + 1
                    if seg[index].endswith("费") or seg[index] in ["合计", "共"]:
                        money_type = seg[index]
                    elif pos_list[seg_ind][index] == "m":
                        money_num = seg[index]
                    elif seg[index] in ["元", "人民币"] and money_num != "" and money_type != "":
                        new_entity_type = new_graph.add_entity(money_type, "n")
                        new_entity_count = new_graph.add_entity(money_num + seg[index], "n")
                        if refered_entity is not None:
                            new_graph.add_relation("赔偿", refered_entity, new_entity_type)
                        else:
                            new_graph.add_relation("赔偿", root_entity, new_entity_type)
                        new_graph.add_relation("共计", new_entity_type, new_entity_count)
            if state == 3 and word == "《":
                b_seach_law_name = True
                law_name = ""
                # law_num_temp = ""
                while index + 1 < len(seg):
                    index = index + 1
                    if seg[index] == "》":
                        b_seach_law_name = False
                    elif b_seach_law_name:
                        law_name += seg[index]
                    new_entity_type = new_graph.add_entity(law_name, "n")
                    new_graph.add_relation("相关法条", root_entity, new_entity_type)
                    break
    return new_graph



def run(filePath, p_id):
    utils = factory.Factory.get_docx()
    result = ""

    # filePath = os.path.join(UPLOAD_FOLDER, "test2.docx")
    file = utils.get_file(filePath)
    paragraphs = utils.get_paragraphs(file)
    parser_str = []
    for p in paragraphs:
        parser_str.append(p.text)

    info = extractor_direct("\n".join(parser_str))
    graph = extractor_ltp("\n".join(parser_str), p_id)
    return graph

