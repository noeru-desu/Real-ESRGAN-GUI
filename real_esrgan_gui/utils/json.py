'''
Author       : noeru_desu
Date         : 2021-12-20 21:01:16
LastEditors  : noeru_desu
LastEditTime : 2021-12-25 19:13:29
Description  : json包装
'''
from json import JSONDecodeError, dump, load
from os import makedirs
from os.path import exists, isfile, join


class Json(dict):
    def __init__(self, file: str, folder: str = None, default_json: dict = None, separators=(', ', ': ')):
        self.separators = separators
        if folder is None:
            self.path = file
        else:
            if not exists(folder):
                makedirs(folder)
            self.path = join(folder, file)
        if isfile(self.path):
            with open(self.path, encoding='utf-8') as f:
                try:
                    super().__init__(load(f))
                except JSONDecodeError as e:
                    return e
        else:
            if default_json is not None:
                super().__init__(default_json)
            else:
                super().__init__()
            self.save()

    def save(self, replaced_dict: dict = None, use_indent: bool = True):
        if replaced_dict is not None:
            super().__init__(replaced_dict)
        with open(self.path, 'w', encoding='utf-8') as f:
            if use_indent:
                dump(self.copy(), f, indent=4, ensure_ascii=False)
            else:
                dump(self.copy(), f, separators=self.separators, ensure_ascii=False)

    def format_json_decode_error(self, e: JSONDecodeError, file_name='json文件', line_end='\n'):
        return '加载{1}时出现问题{0}错误原因: {2}{0}错误字符定位: 第{3}行，第{4}列(文件中第{5}个字符)'.format(
            line_end, file_name, e.msg, e.lineno, e.colno, e.pos
        )
