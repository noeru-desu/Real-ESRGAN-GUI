'''
Author       : noeru_desu
Date         : 2021-11-05 19:42:33
LastEditors  : noeru_desu
LastEditTime : 2022-01-01 09:06:20
Description  : 线程相关类
'''
from functools import wraps as functools_wraps
from concurrent.futures import ThreadPoolExecutor as TPE
from ctypes import c_long, py_object, pythonapi
from threading import Thread as threading_Thread
from typing import Callable
from traceback import format_exc

from real_esrgan_gui.utils.misc_util import copy_signature


class ThreadExecutionError(Exception):
    def __init__(self, exc, formated_exc):
        super().__init__('An error occurred during thread execution')
        self.exception = exc
        self.formated_exc = formated_exc


class ThreadKilled(SystemExit):
    pass


class ThreadTerminationFailed(Exception):
    pass


class ThreadIsRunningError(Exception):
    pass


class Thread(threading_Thread):
    def __init__(self, callback: Callable, callback_args=(), callback_kwargs=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if callback_kwargs is None:
            callback_kwargs = {}
        self._callback = callback
        self._callback_args = callback_args
        self._callback_kwargs = callback_kwargs

    def run(self):
        result = None
        try:
            result = self._target(*self._args, **self._kwargs)
        except Exception as e:
            if self._callback is not None:
                self._callback(ThreadExecutionError(e, format_exc()), result, *self._callback_args, **self._callback_kwargs)
        except ThreadKilled as e:
            if self._callback is not None:
                self._callback(e, result, *self._callback_args, **self._callback_kwargs)
        else:
            if self._callback is not None:
                self._callback(None, result, *self._callback_args, **self._callback_kwargs)
        finally:
            del self._target, self._args, self._kwargs


class ThreadManager(object):
    def __init__(self, thread_name: str = 'Worker', force: bool = False, raise_error=SystemExit):
        self.thread_name = thread_name
        self._force = force
        self._thread = None
        self._raise_error = raise_error
        self.exit_signal = False

    def start_new(self, target: Callable, callback: Callable = None, args=(), kwargs=None, callback_args=(), callback_kwargs=None):
        if not self._force and self.is_running:
            raise ThreadIsRunningError
        if self.is_running and not self.kill():
            raise ThreadTerminationFailed
        self.exit_signal = False
        self._thread = Thread(callback, callback_args, callback_kwargs, target=target, name=self.thread_name, args=args, kwargs=kwargs, daemon=True)
        self._thread.start()

    def kill(self):
        if self._thread.is_alive():
            res = pythonapi.PyThreadState_SetAsyncExc(c_long(self._thread.ident), py_object(self._raise_error))
            if res != 1 and res != 0:
                pythonapi.PyThreadState_SetAsyncExc(self._thread.ident, None)
                return False
        return True

    def set_exit_signal(self, signal: bool = True):
        self.exit_signal = signal

    @property
    def is_running(self):
        return False if self._thread is None else self._thread.is_alive()


class ThreadPoolExecutor(TPE):
    def __init__(self, max_workers=None, thread_name_prefix='thread_pool', initializer=None, initargs=()):
        super().__init__(max_workers, thread_name_prefix, initializer, initargs)

    def multithreading(self):
        def wrapper(func):
            @functools_wraps(func)
            def wrap(*args, **kwargs):
                return self.submit(fn=func, args=args, kwargs=kwargs)
            # bring the signature of the func to the wrap function
            # so inspect.getfullargspec(func) works correctly
            copy_signature(wrap, func)
            wrap.original = func  # access this field to get the original function
            return wrap
        return wrapper
