import os
import random
import flask.scaffold
import pythoncom
from flask import Flask, request
from werkzeug.datastructures import FileStorage
from win32com import client as wc
import docxUtils
import factory
import utilsInterface
from pdfToDocx import PDF2Word

flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func
from flask_restplus import Api, Resource, fields

app = Flask(__name__)
api = Api(app, title="FileParserAPI", description="APIs for file parser server")
load_file_ns = api.namespace('LoadFile', description="Api for uploading files", path='/')
word_parser_ns = api.namespace('Parser', description="Apis for Word file parser", path='/')

# 定义上传文件类型及保存路径
pwd = os.path.dirname(__file__)
ALLOWED_EXTENSIONS = {'doc', 'docx', 'wps', 'pdf'}
UPLOAD_FOLDER = os.path.join(pwd, 'WPWPOI/files/')

# 文件上传参数
upload_parser = api.parser()
upload_parser.add_argument('file', location='files',
                           type=FileStorage, required=True)

# 文档唯一标识字典
token_dict = dict()


@load_file_ns.route('/LoadFile')
class LoadFile(Resource):
    """
    上传doc、docx、wps、pdf文件并返回唯一标识符
    返回数据类型：{"code":0, "msg":"Uploaded successfully", "data":{"token":（6位数字）}}
    """

    @staticmethod
    def is_valid_file(filename):
        if filename.split(".")[-1] in ALLOWED_EXTENSIONS:
            return True
        return False

    @staticmethod
    def format_transfer(file_path, b_delete_origin_file=True):
        """
        将文件形式转换为特定形式
        注：需要windows机环境并装有office word
        """
        # doc -> docx
        if file_path.endswith("doc"):
            #win32程序初始化
            pythoncom.CoInitialize()
            word = wc.Dispatch("Word.Application")
            doc = word.Documents.Open(file_path)
            rename = os.path.splitext(file_path)[0] + ".docx"
            doc.SaveAs(os.path.abspath(os.path.join(file_path, rename)), 12)  # 12表示docx格式
            doc.Close()
            word.Quit()
        # pdf -> docx
        elif file_path.endswith("pdf"):
            pdf2word = PDF2Word()
            try:
                pdf2word.convertPDF(file_path, UPLOAD_FOLDER)
            except:
                print("pdf2word crawler failed")
                pdf2word.pdf2docx(file_path, str(file_path).split(".")[0] + ".docx")
        else:
            return
        if b_delete_origin_file:
            os.remove(file_path)

    @staticmethod
    def token_initializer():
        code = []
        for i in range(6):
            code.append(str(random.randint(0, 9)))
        return ''.join(code)

    @api.expect(upload_parser)
    def post(self):
        args = upload_parser.parse_args()
        uploaded_file = args['file']
        if self.is_valid_file(uploaded_file.filename):
            file_save_path = os.path.join(UPLOAD_FOLDER, uploaded_file.filename)
            uploaded_file.save(os.path.join(file_save_path))
            self.format_transfer(file_save_path)
            while True:
                temp = self.token_initializer()
                if not (temp in token_dict.keys()):
                    token_dict[temp] = uploaded_file.filename.split(".")[0] + ".docx"
                    key = temp
                    break
            print(token_dict)
            return {"code": 0, "msg": "Uploaded successfully", "data": {"token": key}}, 200
        else:
            return {"code": 1, "msg": "Uploaded failed", "data": {}}, 400


@word_parser_ns.route('/word_parser/<token>/all_paragraphs')
class ParseAllParagraphs(Resource):
    """
    获取到指定token的文档中全部段落信息
    返回数据类型：{ “code”：0， “msg”：“Parsed all paragraphs successfully”, “data”：[{ “paragraphText”：“概述”， “paragraphId”:1},……]}
    """

    @staticmethod
    def parse_all_paragraphs(filename):
        utils = factory.Factory.get_utils(filename)
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        file = utils.get_file(file_path)
        data = utils.parse_all_paragraphs(file)
        return data

    def get(self, token):
        if token in token_dict.keys():
            return {"code": 0, "msg": "Parsed all paragraphs successfully",
                    "data": self.parse_all_paragraphs(token_dict[token])}, 200
        else:
            return {"code": 1, "msg": "Invalid token", "data": []}, 400


@word_parser_ns.route('/word_parser/<token>/all_tables')
class ParseAllTables(Resource):
    """
    获取到指定token的文档中全部表格信息
    返回数据类型：{ “code”：0， “msg”：“Parsed all tables successfully”, “data”：[{“textBefore”：“表格如下：”，“docParagraphs”:[{“paragraphText”：“序号”，“paragraphId”:88 }]……},……]}
    """

    @staticmethod
    def parse_all_tables(filename):
        utils = factory.Factory.get_utils(filename)
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        file = utils.get_file(file_path)
        data = utils.parse_all_tables(file)
        return data

    def get(self, token):
        if token in token_dict.keys():
            return {"code": 0, "msg": "Parsed all tables successfully",
                    "data": self.parse_all_tables(token_dict[token])}, 200
        else:
            return {"code": 1, "msg": "Invalid token", "data": []}, 400


@word_parser_ns.route('/word_parser/<token>/all_pics')
class ParseAllPics(Resource):
    """
    获取到指定token的文档中全部图片信息
    返回数据类型：{ “code”：0， “msg”：“Parsed all pictures successfully”, “data”：[{“textBefore”：“图片如下：”， “height”:220 ……},……]}
    """

    @staticmethod
    def parse_all_pics(filename):
        utils = factory.Factory.get_utils(filename)
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        file = utils.get_file(file_path)
        data = utils.parse_all_pics(file)
        return data

    def get(self, token):
        if token in token_dict.keys():
            return {"code": 0, "msg": "Parsed all pictures successfully",
                    "data": self.parse_all_pics(token_dict[token])}, 200
        else:
            return {"code": 1, "msg": "Invalid token", "data": []}, 400


@word_parser_ns.route('/word_parser/<token>/all_titles')
class ParseAllTitles(Resource):
    """
    获取到指定token的文档中全部标题信息
    返回数据类型：{ “code”：0， “msg”：“Parsed all titles successfully”, “data”：[{“paragraphText”：“1、引言”， “paragraphId”:1， “lvl”：1 ……},……]}
    """

    @staticmethod
    def parse_all_titles(filename):
        utils = factory.Factory.get_utils(filename)
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        file = utils.get_file(file_path)
        data = utils.parse_all_titles(file)
        return data

    def get(self, token):
        if token in token_dict.keys():
            return {"code": 0, "msg": "Parsed all titles successfully",
                    "data": self.parse_all_titles(token_dict[token])}, 200
        else:
            return {"code": 1, "msg": "Invalid token", "data": []}, 400


@word_parser_ns.route('/word_parser/<token>/paragraph/<paragraph_id>')
class ParseParagraphById(Resource):
    """
    获取到指定token的文档中指定paragraph_id的段落下的详细信息
    返回数据类型：{ “code”：0， “msg”：“Parsed paragraph by id successfully”, “data”：{“paragraphText”：“概述”，“paragraphId”:1 ……}}
    """

    @staticmethod
    def parse_paragraph_by_id(filename, pid):
        utils = factory.Factory.get_utils(filename)
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        file = utils.get_file(file_path)
        data = utils.parse_paragraph_by_id(file, pid)
        return data

    def get(self, token, paragraph_id):
        if token in token_dict.keys():
            try:
                return {"code": 0, "msg": "Parsed paragraph by id successfully",
                        "data": self.parse_paragraph_by_id(token_dict[token], int(paragraph_id))}, 200
            except:
                return {"code": 1, "msg": "Invalid paragraph id", "data": []}, 400
        else:
            return {"code": 1, "msg": "Invalid token", "data": []}, 400


@word_parser_ns.route('/word_parser/<token>/paragraph/<paragraph_id>/paragraphs_type')
class ParseParagraphsTypeById(Resource):
    """
    获取到指定token的文档中指定paragraph_id的段落下的详细段落格式信息
    返回数据类型：{ “code”：0， “msg”：“Parsed paragraphs type by id successfully”, “data”：“paragraphId”:1,“lvl”：1,“indentFromLeft”：2……}}
    """

    @staticmethod
    def parse_paragraphs_type_by_id(filename, pid):
        utils = factory.Factory.get_utils(filename)
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        file = utils.get_file(file_path)
        data = utils.parse_paragraphs_type_by_id(file, pid)
        return data

    def get(self, token, paragraph_id):
        if token in token_dict.keys():
            try:
                return {"code": 0, "msg": "Parsed paragraph stype by id successfully",
                        "data": self.parse_paragraph_stype_by_id(token_dict[token], int(paragraph_id))}, 200
            except:
                return {"code": 1, "msg": "Invalid paragraph id", "data": []}, 400
        else:
            return {"code": 1, "msg": "Invalid token", "data": []}, 400


@word_parser_ns.route('/word_parser/<token>/paragraph/<paragraph_id>/fonts_type')
class ParseParagraphFontsTypeById(Resource):
    """
    获取到指定token的文档中指定paragraph_id的段落下的详细字体格式信息
    返回数据类型：{ “code”：0， “msg”：“Parsed paragraph fonts type by id successfully”, “data”：[{“paragraphId”:1, “paragrapText”：“中国”, “lvl”：1, “fontAlignment”：2, “fontSize”：28 ……,……]}
    """

    @staticmethod
    def parse_paragraph_fonts_type_by_id(filename, pid):
        utils = factory.Factory.get_utils(filename)
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        file = utils.get_file(file_path)
        data = utils.parse_paragraph_fonts_type_by_id(file, pid)
        return data

    def get(self, token, paragraph_id):
        if token in token_dict.keys():
            try:
                return {"code": 0, "msg": "Parsed paragraph font stype by id successfully",
                        "data": self.parse_paragraph_font_stype_by_id(token_dict[token], int(paragraph_id))}, 200
            except:
                return {"code": 1, "msg": "Invalid paragraph id", "data": []}, 400
        else:
            return {"code": 1, "msg": "Invalid token", "data": []}, 400


@word_parser_ns.route('/word_parser/<token>/title/<paragraph_id>/all_paragraphs')
class ParseParagraphByTitleId(Resource):
    """
    获取到指定token的文档中指定paragraph_id的标题下的全部段落信息
    返回数据类型：{ “code”：0， “msg”：“Parsed paragraph by title id successfully”, “data”：[{“paragraphText”：“概述”, “paragraphId”:1……},……]}
    """

    @staticmethod
    def parse_paragraph_by_title_id(filename, pid):
        utils = factory.Factory.get_utils(filename)
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        file = utils.get_file(file_path)
        data = utils.parse_paragraph_by_title_id(file, pid)

        return data

    def get(self, token, paragraph_id):
        if token in token_dict.keys():
            try:
                return {"code": 0, "msg": "Parsed paragraph by title id successfully",
                        "data": self.parse_paragraph_by_title_id(token_dict[token], int(paragraph_id))}, 200
            except:
                return {"code": 1, "msg": "Invalid paragraph id", "data": []}, 400
        else:
            return {"code": 1, "msg": "Invalid token", "data": []}, 400


@word_parser_ns.route('/word_parser/<token>/title/<paragraph_id>/all_pics')
class ParseParagraphPicsByTitleId(Resource):
    """
    获取到指定token的文档中指定paragraph_id的标题下的全部图片信息
    返回数据类型：{ “code”：0， “msg”：“Parsed paragraph pictures by title id successfully”, “data”：[{“textBefore”：“图片如下：”， “height”:220……},……]}
    """

    @staticmethod
    def parse_paragraph_pics_by_title_id(filename, pid):
        utils = factory.Factory.get_utils(filename)
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        file = utils.get_file(file_path)
        data = utils.parse_paragraph_pics_by_title_id(file, pid)
        return data

    def get(self, token, paragraph_id):
        if token in token_dict.keys():
            try:
                return {"code": 0, "msg": "Parsed paragraph pictures by title id successfully",
                        "data": self.parse_paragraph_pics_by_title_id(token_dict[token], int(paragraph_id))}, 200
            except:
                return {"code": 1, "msg": "Invalid paragraph id", "data": []}, 400
        else:
            return {"code": 1, "msg": "Invalid token", "data": []}, 400


@word_parser_ns.route('/word_parser/<token>/title/<paragraph_id>/all_tables')
class ParseParagraphTablesByTitleId(Resource):
    """
    获取到指定token的文档中指定paragraph_id的标题下的全部表格信息
    返回数据类型：{ “code”：0， “msg”：“Parsed paragraph tables by title id successfully”, “data”：[{“textBefore”：“表格如下：”，“docParagraphs”:[{“paragraphText”：“序号”，“paragraphId”:88}]……},……]}
    """

    @staticmethod
    def parse_paragraph_tables_by_title_id(filename, pid):
        utils = factory.Factory.get_utils(filename)
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        file = utils.get_file(file_path)
        data = utils.parse_paragraph_tables_by_title_id(file, pid)
        return data

    def get(self, token, paragraph_id):
        if token in token_dict.keys():
            try:
                return {"code": 0, "msg": "Parsed paragraph tables by title id successfully",
                        "data": self.parse_paragraph_tables_by_title_id(token_dict[token], int(paragraph_id))}, 200
            except:
                return {"code": 1, "msg": "Invalid paragraph id", "data": []}, 400
        else:
            return {"code": 1, "msg": "Invalid token", "data": []}, 400


@word_parser_ns.route('/word_parser/<token>')
class DeleteFile(Resource):
    """
    删除指定token文档的内容
    """

    def delete_file(self, filename):
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        print("removing" + file_path)
        os.remove(file_path)


    def delete(self, token):
        if token in token_dict.keys():
            self.delete_file(token_dict[token])
            del token_dict[token]
            return {"code": 0, "msg": "success", "data": {"result": "true"}}, 200
        else:
            return {"code": 1, "msg": "Invalid token", "data": []}, 400


if __name__ == '__main__':
    app.run(debug=True)
