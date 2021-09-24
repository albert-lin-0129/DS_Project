import os
from docx import Document
import utilsInterface

pwd = os.path.dirname(__file__)
UPLOAD_FOLDER = os.path.join(pwd, 'WPWPOI/files')


class DocxUtils(utilsInterface.UtilsInterface):

    @staticmethod
    def parse_paragraphs_type_by_id(file, pid):
        """
        需要返回一个字典，里面key是格式特征，value是内容
        """
        res = {}
        paragraph_format = file.paragraphs[pid].paragraph_format
        res["paragraphAlignment"] = paragraph_format.alignment
        res["first_line_indent"] = paragraph_format.first_line_indent
        res["keep_together"] = paragraph_format.keep_together
        res["keep_with_next"] = paragraph_format.keep_with_next
        res["left_indent"] = paragraph_format.left_indent
        res["line_spacing"] = paragraph_format.line_spacing
        if paragraph_format.line_spacing is not None:
            res["line_spacing"] = paragraph_format.line_spacing.pt
        return res

    @staticmethod
    def parse_paragraph_fonts_type_by_id(file, pid):
        """
        需要返回一个字典，里面key是字体信息，value是内容
        """
        res = {}
        runs = file.paragraphs[pid].runs
        for run in runs:
            if run.font is not None:
                res["paragraphFont"] = run.font.name
                res["fontSize"] = run.font.size
                if run.font.size is not None:
                    res["fontSize"] = run.font.size.pt
                res["fontItalic"] = run.font.italic
                res["fontColor"] = run.font.color.rgb
                res["fontBold"] = run.font.bold
        return res

    @staticmethod
    def parse_paragraph_by_title_id(file, pid):
        """
        需要返回一个字典，里面key是标题特征，value是内容
        """
        # TODO
        pass

    @staticmethod
    def parse_paragraph_pics_by_title_id(file, pid):
        """
        需要返回一个字典，里面key是图片特征，value是内容
        """
        # TODO
        pass

    @staticmethod
    def parse_paragraph_tables_by_title_id(file, pid):
        """
        需要返回一个字典，里面key是表格特征，value是内容
        """
        # TODO
        pass

    @staticmethod
    def parse_paragraph_by_id(file, pid):
        """
        需要返回一个字典，里面key是特征，value是内容
        """
        res = {}
        paragraph = file.paragraphs[pid]
        res["paragraphId"] = pid
        res["paragraphText"] = paragraph.text

        dic = DocxUtils.parse_paragraphs_type_by_id(file, pid)
        for key in dic.keys():
            res[key] = dic[key]
        dic = DocxUtils.parse_paragraph_fonts_type_by_id(file, pid)
        for key in dic.keys():
            res[key] = dic[key]

        return res

    @staticmethod
    def parse_all_paragraphs(file):
        """
        需要返回一个字典类型的数组，每个字典是一个段落内容
        """
        res = []
        for index in range(0, len(file.paragraphs)):
            res.append(DocxUtils.parse_paragraph_by_id(file, index))
        return res

    @staticmethod
    def parse_all_tables(file):
        """
        需要返回一个字典类型的数组，每个字典是一个表格内容
        """
        # TODO
        pass

    @staticmethod
    def parse_all_images(file):
        """
        需要返回一个字典类型的数组，每个字典是一个图片内容
        """
        # TODO
        pass

    @staticmethod
    def parse_all_titles(file):
        """
        需要返回一个字典类型的数组，每个字典是一个标题内容
        """
        # TODO
        pass

    @staticmethod
    def get_file(path):
        """
        需要返回一个file，就是解析后的一个类，之后传入每一个方法中
        docx就是Document类
        """
        return Document(path)

    # @staticmethod
    # def get_paragraphs(document):
    #     paragraphs = {}
    #     i = 0
    #     for paragraph in document.paragraphs:
    #         # print(paragraph.text)
    #         paragraphs[i] = paragraph
    #         i += 1
    #     return paragraphs
    #
    # @staticmethod
    # def get_tables(document):
    #     tables = {}
    #     i = 0
    #     for table in document.tables:
    #         # print(paragraph.text)
    #         tables[i] = table
    #         i += 1
    #     return tables
    #
    # @staticmethod
    # def parse_paragraph_type(paragraph):
    #     print(paragraph.text)
    #     print(paragraph.paragraph_format.alignment)
    #     print(paragraph.paragraph_format.first_line_indent)
    #     print(paragraph.style.font.name)
    #
    # @staticmethod
    # def parse_images(document):
    #     """
    #     image需要知道这张图片的段落位置以及
    #     """
    #     dict_rel = document.part._rels
    #     for rel in dict_rel:
    #         rel = dict_rel[rel]
    #         if "image" in rel.target_ref:
    #             print(rel.target_part)


if __name__ == '__main__':
    filePath = os.path.join(UPLOAD_FOLDER, "test.docx")
    # print(DocxUtils.parse_all_paragraphs(DocxUtils.get_file(filePath)))
    print(DocxUtils.parse_paragraph_by_id(DocxUtils.get_file(filePath), 1))

    # docx = Document(filePath)

    # doc_pars = DocxUtils.get_paragraphs(docx)
    # print(doc_pars)
    # DocxUtils.parse_images(docx)
    # DocxUtils.parse_paragraph_type(doc_pars[1])
