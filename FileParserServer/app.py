import os
from flask import Flask, request
import flask.scaffold
from werkzeug.datastructures import FileStorage
import random

flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func
from flask_restplus import Api, Resource, fields

app = Flask(__name__)
api = Api(app, title="FileParserAPI", description="APIs for file parser server")
load_file_ns = api.namespace('LoadFile', description="Api for uploading files", path='/')
word_parser_ns = api.namespace('WordParser', description="Apis for Word file parser", path='/')

# 定义上传文件类型及保存路径
pwd = os.path.dirname(__file__)
ALLOWED_EXTENSIONS = {'doc', 'docx', 'wps', 'pdf'}
UPLOAD_FOLDER = os.path.join(pwd, 'WPWPOI/files')

# 文件上传参数
upload_parser = api.parser()
upload_parser.add_argument('file', location='files',
                           type=FileStorage, required=True)

# 文档唯一标识字典
token_dict = dict()


@load_file_ns.route('/load_file')
class load_file(Resource):
    '''
    上传doc、docx、wps、pdf文件并返回唯一标识符
    返回数据类型：{"code":0, "msg":"Uploaded successfully", "data":{"token":（6位数字）}}
    '''

    def isValidFile(self, filename):
        if filename.split(".")[-1] in ALLOWED_EXTENSIONS:
            return True
        return False

    def tokenInitializer(self):
        code = []
        for i in range(6):
            code.append(str(random.randint(0, 9)))
        return ''.join(code)

    @api.expect(upload_parser)
    def post(self):
        args = upload_parser.parse_args()
        uploaded_file = args['file']
        if self.isValidFile(uploaded_file.filename):
            uploaded_file.save(os.path.join(UPLOAD_FOLDER, uploaded_file.filename))
            key = int
            while True:
                temp = self.tokenInitializer()
                if not (temp in token_dict.keys()):
                    token_dict[temp] = uploaded_file.filename
                    key = temp
                    break
            return {"code": 0, "msg": "Uploaded successfully", "data": {"token": key}}, 200
        else:
            return {"code": 1, "msg": "Uploaded failed", "data": {}}, 400


@word_parser_ns.route('/word_parser/<token>/all_paragraphs')
class parse_all_paragraphs(Resource):
    '''
    获取到指定token的文档中全部段落信息
    返回数据类型：{ “code”：0， “msg”：“Parsed all paragraphs successfully”, “data”：[{ “paragraphText”：“概述”， “paragraphId”:1},……]}
    '''

    def parse_all_paragraphs(self, filename):
        data = []
        with open(os.path.join(UPLOAD_FOLDER, filename), 'r') as f:
            # TODO
            pass
        return data

    def get(self, token):
        if token in token_dict.keys():
            return {"code": 0, "msg": "Parsed all paragraphs successfully",
                    "data": self.parse_all_paragraphs(token_dict[token])}, 200
        else:
            return {"code": 1, "msg": "Invalid token", "data": []}, 400


@word_parser_ns.route('/word_parser/<token>/all_tables')
class parse_all_tables(Resource):
    '''
    获取到指定token的文档中全部表格信息
    返回数据类型：{ “code”：0， “msg”：“Parsed all tables successfully”, “data”：[{“textBefore”：“表格如下：”，“docParagraphs”:[{“paragraphText”：“序号”，“paragraphId”:88 }]……},……]}
    '''

    def parse_all_tables(self, filename):
        data = []
        with open(os.path.join(UPLOAD_FOLDER, filename), 'r') as f:
            # TODO
            pass
        return data

    def get(self, token):
        if token in token_dict.keys():
            return {"code": 0, "msg": "Parsed all tables successfully",
                    "data": self.parse_all_tables(token_dict[token])}, 200
        else:
            return {"code": 1, "msg": "Invalid token", "data": []}, 400


@word_parser_ns.route('/word_parser/<token>/all_pics')
class parse_all_pics(Resource):
    '''
    获取到指定token的文档中全部图片信息
    返回数据类型：{ “code”：0， “msg”：“Parsed all pictures successfully”, “data”：[{“textBefore”：“图片如下：”， “height”:220 ……},……]}
    '''

    def parse_all_pics(self, filename):
        data = []
        with open(os.path.join(UPLOAD_FOLDER, filename), 'r') as f:
            # TODO
            pass
        return data

    def get(self, token):
        if token in token_dict.keys():
            return {"code": 0, "msg": "Parsed all pictures successfully",
                    "data": self.parse_all_pics(token_dict[token])}, 200
        else:
            return {"code": 1, "msg": "Invalid token", "data": []}, 400


@word_parser_ns.route('/word_parser/<token>/all_titles')
class parse_all_titles(Resource):
    '''
    获取到指定token的文档中全部标题信息
    返回数据类型：{ “code”：0， “msg”：“Parsed all titles successfully”, “data”：[{“paragraphText”：“1、引言”， “paragraphId”:1， “lvl”：1 ……},……]}
    '''

    def parse_all_titles(self, filename):
        data = []
        with open(os.path.join(UPLOAD_FOLDER, filename), 'r') as f:
            # TODO
            pass
        return data

    def get(self, token):
        if token in token_dict.keys():
            return {"code": 0, "msg": "Parsed all titles successfully",
                    "data": self.parse_all_titles(token_dict[token])}, 200
        else:
            return {"code": 1, "msg": "Invalid token", "data": []}, 400


@word_parser_ns.route('/word_parser/<token>/paragraph/<paragraph_id>')
class parse_paragraph_by_id(Resource):
    '''
    获取到指定token的文档中指定paragraph_id的段落下的详细信息
    返回数据类型：{ “code”：0， “msg”：“Parsed paragraph by id successfully”, “data”：{“paragraphText”：“概述”，“paragraphId”:1 ……}}
    '''

    def parse_paragraph_by_id(self, filename, pid):
        data = []
        with open(os.path.join(UPLOAD_FOLDER, filename), 'r') as f:
            # TODO
            pass
        return data

    def get(self, token, paragraph_id):
        if token in token_dict.keys():
            try:
                return {"code": 0, "msg": "Parsed paragraph by id successfully",
                        "data": self.parse_paragraph_by_id(token_dict[token], paragraph_id)}, 200
            except:
                return {"code": 1, "msg": "Invalid paragraph id", "data": []}, 400
        else:
            return {"code": 1, "msg": "Invalid token", "data": []}, 400


@word_parser_ns.route('/word_parser/<token>/paragraph/<paragraph_id>/paragraph_stype')
class parse_paragraph_stype_by_id(Resource):
    '''
    获取到指定token的文档中指定paragraph_id的段落下的详细段落格式信息
    返回数据类型：{ “code”：0， “msg”：“Parsed paragraph stype by id successfully”, “data”：“paragraphId”:1,“lvl”：1,“indentFromLeft”：2……}}
    '''

    def parse_paragraph_stype_by_id(self, filename, pid):
        data = []
        with open(os.path.join(UPLOAD_FOLDER, filename), 'r') as f:
            # TODO
            pass
        return data

    def get(self, token, paragraph_id):
        if token in token_dict.keys():
            try:
                return {"code": 0, "msg": "Parsed paragraph stype by id successfully",
                        "data": self.parse_paragraph_stype_by_id(token_dict[token], paragraph_id)}, 200
            except:
                return {"code": 1, "msg": "Invalid paragraph id", "data": []}, 400
        else:
            return {"code": 1, "msg": "Invalid token", "data": []}, 400


@word_parser_ns.route('/word_parser/<token>/paragraph/<paragraph_id>/font_stype')
class parse_paragraph_font_stype_by_id(Resource):
    '''
    获取到指定token的文档中指定paragraph_id的段落下的详细字体格式信息
    返回数据类型：{ “code”：0， “msg”：“Parsed paragraph font stype by id successfully”, “data”：[{“paragraphId”:1, “paragrapText”：“中国”, “lvl”：1, “fontAlignment”：2, “fontSize”：28 ……,……]}
    '''

    def parse_paragraph_font_stype_by_id(self, filename, pid):
        data = []
        with open(os.path.join(UPLOAD_FOLDER, filename), 'r') as f:
            # TODO
            pass
        return data

    def get(self, token, paragraph_id):
        if token in token_dict.keys():
            try:
                return {"code": 0, "msg": "Parsed paragraph font stype by id successfully",
                        "data": self.parse_paragraph_font_stype_by_id(token_dict[token], paragraph_id)}, 200
            except:
                return {"code": 1, "msg": "Invalid paragraph id", "data": []}, 400
        else:
            return {"code": 1, "msg": "Invalid token", "data": []}, 400


@word_parser_ns.route('/word_parser/<token>/title/<paragraph_id>/all_paragraphs')
class parse_paragraph_by_title_id(Resource):
    '''
    获取到指定token的文档中指定paragraph_id的标题下的全部段落信息
    返回数据类型：{ “code”：0， “msg”：“Parsed paragraph by title id successfully”, “data”：[{“paragraphText”：“概述”, “paragraphId”:1……},……]}
    '''

    def parse_paragraph_by_title_id(self, filename, pid):
        data = []
        with open(os.path.join(UPLOAD_FOLDER, filename), 'r') as f:
            # TODO
            pass
        return data

    def get(self, token, paragraph_id):
        if token in token_dict.keys():
            try:
                return {"code": 0, "msg": "Parsed paragraph by title id successfully",
                        "data": self.parse_paragraph_by_title_id(token_dict[token], paragraph_id)}, 200
            except:
                return {"code": 1, "msg": "Invalid paragraph id", "data": []}, 400
        else:
            return {"code": 1, "msg": "Invalid token", "data": []}, 400


@word_parser_ns.route('/word_parser/<token>/title/<paragraph_id>/all_pics')
class parse_paragraph_pics_by_title_id(Resource):
    '''
    获取到指定token的文档中指定paragraph_id的标题下的全部图片信息
    返回数据类型：{ “code”：0， “msg”：“Parsed paragraph pictures by title id successfully”, “data”：[{“textBefore”：“图片如下：”， “height”:220……},……]}
    '''

    def parse_paragraph_pics_by_title_id(self, filename, pid):
        data = []
        with open(os.path.join(UPLOAD_FOLDER, filename), 'r') as f:
            # TODO
            pass
        return data

    def get(self, token, paragraph_id):
        if token in token_dict.keys():
            try:
                return {"code": 0, "msg": "Parsed paragraph pictures by title id successfully",
                        "data": self.parse_paragraph_pics_by_title_id(token_dict[token], paragraph_id)}, 200
            except:
                return {"code": 1, "msg": "Invalid paragraph id", "data": []}, 400
        else:
            return {"code": 1, "msg": "Invalid token", "data": []}, 400


@word_parser_ns.route('/word_parser/<token>/title/<paragraph_id>/all_tables')
class parse_paragraph_tables_by_title_id(Resource):
    '''
    获取到指定token的文档中指定paragraph_id的标题下的全部表格信息
    返回数据类型：{ “code”：0， “msg”：“Parsed paragraph tables by title id successfully”, “data”：[{“textBefore”：“表格如下：”，“docParagraphs”:[{“paragraphText”：“序号”，“paragraphId”:88}]……},……]}
    '''

    def parse_paragraph_tables_by_title_id(self, filename, pid):
        data = []
        with open(os.path.join(UPLOAD_FOLDER, filename), 'r') as f:
            # TODO
            pass
        return data

    def get(self, token, paragraph_id):
        if token in token_dict.keys():
            try:
                return {"code": 0, "msg": "Parsed paragraph tables by title id successfully",
                        "data": self.parse_paragraph_tables_by_title_id(token_dict[token], paragraph_id)}, 200
            except:
                return {"code": 1, "msg": "Invalid paragraph id", "data": []}, 400
        else:
            return {"code": 1, "msg": "Invalid token", "data": []}, 400


@word_parser_ns.route('/word_parser/<token>')
class delete_file(Resource):
    '''
    删除指定token文档的内容
    '''

    def delete_file(self, filename):
        # TODO
        pass

    def delete(self, token):
        if token in token_dict.keys():
            delete_file(token_dict[token])
            return {"code": 0, "msg": "success", "data": {"result": "true"}}, 200
        else:
            return {"code": 1, "msg": "Invalid token", "data": []}, 400


if __name__ == '__main__':
    app.run(debug=True)
