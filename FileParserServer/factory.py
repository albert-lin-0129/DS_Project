import docxUtils


class Factory:
    @staticmethod
    def get_utils(filename):
        s = filename.split('.')
        if s[1] == "docx":
            return docxUtils.DocxUtils

    @staticmethod
    def get_docx():
        return docxUtils.DocxUtils
