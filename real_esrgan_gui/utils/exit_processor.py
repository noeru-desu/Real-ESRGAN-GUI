'''
Author       : noeru_desu
Date         : 2021-08-28 18:35:58
LastEditors  : noeru_desu
LastEditTime : 2022-01-14 15:13:49
Description  : 处理退出时的相关操作
'''
from atexit import register
from traceback import print_exc

from real_esrgan_gui.utils.misc_util import gen_parameter_str


class ExitProcessor(object):
    def __init__(self):
        register(self.exit)
        self.at_exit_func = []

    def register(self, func, *args, **kwargs):
        self.at_exit_func.append((func, args, kwargs))

    def exit(self):
        for func, args, kwargs in self.at_exit_func:
            try:
                func(*args, **kwargs)
            except Exception:
                print_exc()
                print(gen_exc_str(func, args, kwargs))


def gen_exc_str(func, args, kwargs):
    return '{0}: {1}\nargs: {2}\nkwargs: {3}\ncmd: {0}({4})'.format(
        func.__name__, func, args, kwargs, gen_parameter_str(args, kwargs)
    )
