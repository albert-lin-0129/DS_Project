from ltp import LTP
import os
import factory

pwd = os.path.dirname(__file__)
UPLOAD_FOLDER = os.path.join(pwd, 'WPWPOI/files')


class NLPParser:
    ltp = LTP()  # 默认加载 Small 模型

    @staticmethod
    def parse(parse_str):
        segment, hidden = NLPParser.ltp.seg([parse_str])
        print(segment)
        dep = NLPParser.ltp.dep(hidden)
        return dep


if __name__ == '__main__':
    filePath = os.path.join(UPLOAD_FOLDER, "test.docx")
    utils = factory.Factory.get_utils(filePath)
    file = utils.get_file(filePath)
    paragraphs = utils.get_paragraphs(file)
    parser = NLPParser()
    for p in paragraphs:
        print(NLPParser.parse(p.text))


