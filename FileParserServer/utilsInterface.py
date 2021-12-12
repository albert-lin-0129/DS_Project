class UtilsInterface:

    @staticmethod
    def parse_paragraphs_type_by_id(file, pid):
        """
        需要返回一个字典，里面key是格式特征，value是内容
        """
        # TODO
        pass

    @staticmethod
    def parse_paragraph_fonts_type_by_id(file, pid):
        """
        需要返回一个字典，里面key是字体信息，value是内容
        """
        # TODO
        pass

    @staticmethod
    def parse_paragraph_by_id(file, pid):
        """
        需要返回一个字典，里面key是特征，value是内容
        """
        # TODO
        pass

    @staticmethod
    def parse_all_paragraphs(file):
        """
        需要返回一个字典类型的数组，每个字典是一个段落内容
        """
        # TODO
        pass

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
        # TODO
        pass

    @staticmethod
    def parse_paragraph_by_title_id(file, pid):
        """
        需要返回一个字典类型的数组，里面key是标题特征，value是内容
        """
        # TODO
        pass

    @staticmethod
    def parse_paragraph_pics_by_title_id(file, pid):
        """
        需要返回一个字典类型的数组，里面key是图片特征，value是内容
        """
        # TODO
        pass

    @staticmethod
    def parse_paragraph_tables_by_title_id(file, pid):
        """
        需要返回一个字典类型的数组，里面key是表格特征，value是内容
        """
        # TODO
        pass