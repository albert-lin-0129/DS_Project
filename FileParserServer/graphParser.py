from ltp import LTP
import os
from gensim.models import Word2Vec
from gensim.test.utils import datapath
import app
import gensim
import factory

pwd = os.path.dirname(__file__)
DATA_FOLDER = os.path.join(pwd, 'WPWPOI/data')
UPLOAD_FOLDER = os.path.join(pwd, 'WPWPOI/files')


class NLPParser:
    ltp = LTP()  # 默认加载 Small 模型

    @staticmethod
    def parse(parse_str):
        segment, hidden = NLPParser.ltp.seg([parse_str])
        pos = NLPParser.ltp.pos(hidden)
        result = ""
        for i in range(len(segment)):
            for j in range(len(segment[i])):
                if pos[i][j] != 'wp':
                    result += segment[i][j] + " "
        return result
        # print(segment)
        # return segment
        # dep = NLPParser.ltp.dep(hidden)
        # return dep


class Word2VecParser:

    @staticmethod
    def parse(train_file_name, save_model_file):
        model = Word2Vec(corpus_file=train_file_name, min_count=2)
        model.save(save_model_file + ".model")
        # model.wv.save_word2vec_format(save_model_file + ".bin", binary=True)  # 以二进制类型保存模型以便重用


if __name__ == '__main__':
    # utils = factory.Factory.get_docx()
    # result = ""

    # filePath = os.path.join(UPLOAD_FOLDER, "test.docx")
    # app.LoadFile.format_transfer(filePath)
    # filePath = filePath.split('.')[0] + ".docx"
    # print(filePath)
    # file = utils.get_file(filePath)
    # paragraphs = utils.get_paragraphs(file)
    # parser = NLPParser()
    # for p in paragraphs:
    #     result += NLPParser.parse(p.text) + "\n"

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

    segment_file_name = 'segment.txt'
    save_model_name = 'test'
    # with open(segment_file_name, 'w', encoding="utf-8") as f2:
    #     f2.write(result)
    #
    # Word2VecParser.parse(segment_file_name, save_model_name)
    model_out = Word2Vec.load(save_model_name + ".model")
    print(len(model_out.wv.vectors))
    # for data in model_out.wv.index_to_key:
    #     print(data)
    # 计算两个词的相似度/相关程度
    # y1 = model_out.wv.similarity("被告", "朱新梅")
    # y2 = model_out.wv.similarity("被告", "郭继兴")
    # print(y1)
    
    # print(y2)
    y = model_out.wv.n_similarity(["原告", "安慧敏"], ["被告", "崔冬茜"])
    print(y)
    y_total = model_out.wv.most_similar("判决结果", topn=10)
    for item in y_total:
        print(item[0], item[1])


