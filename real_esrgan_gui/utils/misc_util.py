'''
Author       : noeru_desu
Date         : 2021-08-28 18:35:58
LastEditors  : noeru_desu
LastEditTime : 2022-01-14 15:08:59
Description  : 一些小东西
'''
from functools import wraps as functools_wraps
from concurrent.futures import (CancelledError, ProcessPoolExecutor,
                                ThreadPoolExecutor)
from inspect import signature
from os import system, walk
from os.path import normpath
from time import time
from traceback import print_exc
from typing import Callable


def pause():
    """输入cmd命令以暂停"""
    system('pause>nul')


def walk_file_generator(path, topdown=False):
    '''
    :description: 获取目录下的所有文件
    :param path: 需要遍历的文件夹
    :param topdown: 是否遍历子目录
    :return: 生成器返回(文件所在的相对路径, 文件名)元组
    '''
    path = normpath(path)
    path_len = len(path) + 1
    if topdown:
        for top, dirs, files in walk(path):
            yield top[path_len:], files
    else:
        top, dirs, files = next(walk(path))
        yield '', files


def cal_formula_string(formula_string: str, **format):
    '''
    :description: 将字符串转换为公式后运算
    :param formula_string: 需要格式化的字符串
    :param format: 格式化时需要的变量
    :return: (运算结果, 错误提示)元组
    '''
    try:
        result = int(eval(formula_string.format(**format)))
    except SyntaxError:
        return None, '输入的公式有误，请确保输入了正确的运算符'
    except NameError:
        return None, '输入内容不为 纯数字/运算符/变量'
    except KeyError as e:
        return None, f'未知的变量: {str(e)}。当前提供: {", ".join(format.keys())}'
    except Exception as e:
        return None, f'运算输入的公式时出现错误: {repr(e)}'
    else:
        return result, None


def timeit(fn):
    def wrap(*args, **kwargs):
        start = time()
        fn(*args, **kwargs)
        print(f'{fn.__name__}运行时间: {time() - start}')
    return wrap


class ThreadTaskManager(ThreadPoolExecutor):
    def __init__(self, max_workers: int = ..., *args, **kwargs):
        if 'thread_name_prefix' not in kwargs:
            kwargs['thread_name_prefix'] = 'worker_thread'
        super().__init__(max_workers, *args, **kwargs)
        self.task_dict = {}

    def create_tag(self, tag_name: str, single: bool, overwrite: bool = True):
        self.task_dict[tag_name] = {
            'single': single,
            'overwrite': overwrite,
            'futures': None if single else []
        }

    def add_task(self, tag_name, future, callback=None, *callback_args, **callback_kwargs):
        future.add_done_callback(lambda future: self.callback(tag_name, future, callback, *callback_args, **callback_kwargs))
        if self.task_dict[tag_name]['single']:
            self.task_dict[tag_name]['futures'] = future
        else:
            self.task_dict[tag_name]['futures'].append(future)

    def callback(self, tag_name, future, callback=None, *callback_args, **callback_kwargs):
        if callback is not None:
            try:
                callback(future, tag_name, *callback_args, **callback_kwargs)
            except Exception:
                print_exc()
        self.del_future(tag_name, future)

    def cancel_task(self, tag_name=None, future=None) -> bool:
        if future is not None:
            if future.running():
                return False
            if not future.done():
                return future.cancel()
        elif tag_name is None:
            return True

        if self.task_dict[tag_name]['futures'] is not None:
            if self.task_dict[tag_name]['single']:
                if self.task_dict[tag_name]['futures'].running():
                    return False
                if not self.task_dict[tag_name]['futures'].done():
                    return self.task_dict[tag_name]['futures'].cancel()
            else:
                all_cancelled = True
                for i in self.task_dict[tag_name]['futures']:
                    if i.done():
                        continue
                    if i.running():
                        all_cancelled = False
                        continue
                    if not i.cancel():
                        all_cancelled = False
                return all_cancelled

        return True

    def check_tag(self, tag_name):
        if not self.task_dict[tag_name]['futures']:
            return None
        if self.task_dict[tag_name]['overwrite']:
            if self.cancel_task(tag_name):
                return None
            else:
                if self.task_dict[tag_name]['single']:
                    return '已有一个无法打断的任务正在进行'
                else:
                    return '任务列表没有被完全取消'
        else:
            return '已有一个任务正在进行'

    def del_future(self, tag_name, futures=None):
        if not (futures is None or self.task_dict[tag_name]['single']):
            self.task_dict[tag_name]['futures'].remove(futures)
        else:
            self.task_dict[tag_name]['futures'] = None


class ProcessTaskManager(ProcessPoolExecutor):
    def __init__(self, max_workers: int = ..., *args, **kwargs):
        super().__init__(max_workers, *args, **kwargs)
        self.watchdog = ThreadTaskManager(max_workers, thread_name_prefix='process_pool_watchdog')
        self.task_dict = {}

    def create_tag(self, tag_name: str, single: bool, overwrite: bool = True):
        self.watchdog.create_tag(tag_name, single, overwrite)
        self.task_dict[tag_name] = {
            'single': single,
            'overwrite': overwrite,
            'futures': None if single else []
        }

    def add_task(self, tag_name, future, callback=None, *callback_args, **callback_kwargs):
        if self.task_dict[tag_name]['single']:
            self.task_dict[tag_name]['futures'] = future
        else:
            self.task_dict[tag_name]['futures'].append(future)
        self.watchdog.add_task(tag_name, self.watchdog.submit(self.wait, future), self.callback, future, callback, *callback_args, **callback_kwargs)

    def wait(self, future):
        try:
            error = future.exception()
        except CancelledError:
            pass
        if error is not None:
            print(error)

    def callback(self, watchdog_future, tag_name, future, callback=None, *callback_args, **callback_kwargs):
        if callback is not None:
            try:
                callback(future, tag_name, *callback_args, **callback_kwargs)
            except Exception:
                print_exc()
        self.del_future(tag_name, future)

    def cancel_task(self, tag_name=None, future=None):
        if future is not None:
            if future.running():
                return False
            if not future.done():
                if future.cancel():
                    self.watchdog.cancel_task(tag_name, future)
                    return True
                else:
                    return False
        elif tag_name is None:
            return True

        if self.task_dict[tag_name]['futures'] is not None:
            if self.task_dict[tag_name]['single']:
                if self.task_dict[tag_name]['futures'].running():
                    return False
                if not self.task_dict[tag_name]['futures'].done():
                    if self.task_dict[tag_name]['futures'].cancel():
                        self.watchdog.cancel_task(tag_name)
                        return True
                    else:
                        return False
            else:
                all_cancelled = True
                for i in self.task_dict[tag_name]['futures']:
                    if i.done():
                        continue
                    if i.running():
                        all_cancelled = False
                        continue
                    if not i.cancel():
                        all_cancelled = False
                    else:
                        self.watchdog.cancel_task(tag_name, i)
                return all_cancelled

        return True

    def check_tag(self, tag_name):
        if not self.task_dict[tag_name]['futures']:
            return None
        if self.task_dict[tag_name]['overwrite']:
            if self.cancel_task(tag_name):
                return None
            else:
                if self.task_dict[tag_name]['single']:
                    return '已有一个无法打断的任务正在进行'
                else:
                    return '任务列表没有被完全取消'
        else:
            return '已有一个任务正在进行'

    def del_future(self, tag_name, futures=None):
        if not (futures is None or self.task_dict[tag_name]['single']):
            self.task_dict[tag_name]['futures'].remove(futures)
        else:
            self.task_dict[tag_name]['futures'] = None


def walk_file(path, topdown=False, filter=None) -> tuple[int, list[tuple[list, list]]]:
    '''
    :description: 获取目录下的所有文件
    :param path: 需要遍历的文件夹
    :param topdown: 是否遍历子目录
    :return: 返回(文件个数, [(文件所在的相对路径列表, 文件名列表)元组]列表)元组
    '''
    result = []
    file_num = 0
    if filter is None:
        for r, fl in walk_file_generator(path, topdown):
            file_num += len(fl)
            result.append((r, fl))
    else:
        for r, fl in walk_file_generator(path, topdown):
            fl = [i for i in fl if i.split('.')[-1] in filter]
            file_num += len(fl)
            result.append((r, fl))
    return file_num, result


def copy_signature(target: Callable, origin: Callable) -> Callable:
    """
    Copy the function signature of origin into target
    """
    # https://stackoverflow.com/questions/39926567/python-create-decorator-preserving-function-arguments
    target.__signature__ = signature(origin)
    return target


def in_try(func):
    @functools_wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception:
            print_exc()
        copy_signature(wrapper, func)
        wrapper.original = func
    return wrapper


def gen_parameter_str(args, kwargs):
    if args:
        delimiter = ', '
    else:
        delimiter = ''
    return f'{", ".join(args)}{delimiter}{", ".join(f"{k}={v}" for k, v in kwargs.items())}'
