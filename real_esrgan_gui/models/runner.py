'''
Author       : noeru_desu
Date         : 2021-12-19 18:04:57
LastEditors  : noeru_desu
LastEditTime : 2022-01-09 15:32:46
Description  : popen相关
'''
from os import rename, remove
from os.path import split, splitext, isfile
from shlex import split as shlex_split
from subprocess import PIPE, STDOUT, Popen
from typing import TYPE_CHECKING
from traceback import format_exc
from real_esrgan_gui.constants import PYTHON_MODE

from real_esrgan_gui.utils.thread import ThreadManager, ThreadExecutionError

if TYPE_CHECKING:
    from real_esrgan_gui.frame.main_frame import MainFrame


class ProcessExited(Exception):
    pass


class Runner(object):
    def __init__(self, frame: 'MainFrame'):
        self.frame = frame
        self.process: Popen = None
        self.thread_manager = ThreadManager('Real-ESRGAN')
        self.python_mode_processor = PythonModeProcessor(frame)
        self.vulkan_mode_processor = VulkanModeProcessor(frame)

    def check_files(self):
        if not self.frame.controls.check_exe_file():
            self.frame.controls.print('选择的可执行文件不存在!')
            return False
        if not self.frame.controls.check_input_file():
            self.frame.controls.print('选择的待处理文件不存在!')
            return False
        if not self.frame.controls.check_output_file():
            self.frame.controls.print('选择的保存文件夹不存在!')
            return False
        if not self.frame.controls.check_model_dir():
            self.frame.controls.print('选择的模型文件夹不存在!')
            return False
        if not self.frame.controls.check_model_name():
            self.frame.controls.print('选择的模型文件不存在!')
            return False
        return True

    def run(self):
        if not self.frame.controls.cmd_text or not self.check_files():
            return
        self.frame.startProcBtn.Disable()
        self.frame.killProcBtn.Enable()
        self.process = Popen(shlex_split(self.frame.controls.cmd_text), cwd=split(self.frame.controls.exe_file_path)[0], stdin=PIPE, stdout=PIPE, stderr=STDOUT)
        self.frame.controls.cls()
        self.frame.controls.set_proc_progress(0)
        self.frame.controls.print('执行的命令行如下'.center(60, '-'))
        self.frame.controls.print(self.frame.controls.cmd_text)
        self.frame.controls.print(''.ljust(73, '-'))
        self.frame.controls.print(f'处理程序的PID: {self.process.pid}')
        if self.frame.controls.mode is PYTHON_MODE:
            self.python_mode_processor.on_proc_start()
        self.thread_manager.start_new(self._loop, self._callback)

    def send(self, text: str):
        if self.process.returncode is None:
            self.process.stdin.write(text.encode())
            self.process.stdin.flush()

    def _receive(self) -> str:
        try:
            text: bytes = next(iter(self.process.stdout))
        except StopIteration:
            raise ProcessExited()
        else:
            return text.decode().strip('\n\r')

    def _receive_iter(self):
        try:
            for i in iter(self.process.stdout):
                yield i.decode().strip('\n\r')
        except StopIteration:
            raise ProcessExited()

    def _loop(self):
        is_python_mode = self.frame.controls.mode is PYTHON_MODE
        processor = self.python_mode_processor if is_python_mode else self.vulkan_mode_processor
        try:
            for index, result in enumerate(self._receive_iter()):
                self.frame.controls.print(result)
                processor.on_receive(index, result)
        except ProcessExited:
            pass
        except Exception:
            self.frame.warning(format_exc(), '处理消息时出现意外错误')
        self.process.wait()
        if self.process.returncode == 0:
            self.frame.controls.print('处理程序已退出')
            self.frame.controls.set_proc_progress(10000)
            if is_python_mode:
                self.python_mode_processor.on_proc_successfully()
        else:
            self.frame.controls.print(f'处理程序非正常退出，返回代码: {self.process.returncode}')

    def terminate(self):
        if self.process.returncode is None:
            self.process.terminate()

    def on_exit(self):
        if self.process is not None and self.process.returncode is None:
            self.process.terminate()
            self.process.wait()

    def _callback(self, err: 'ThreadExecutionError', r):
        if isinstance(err, ThreadExecutionError):
            self.frame.controls.print('监视线程出现未捕获错误，自动结束处理进程。错误如下')
            self.frame.controls.print(err.formated_exc)
            self.terminate()
        self.process.stdin.close()
        self.process.stdout.close()
        self.frame.startProcBtn.Enable()
        self.frame.killProcBtn.Disable()


class BasicModeProcessor(object):
    def __init__(self, frame: 'MainFrame'):
        self.frame = frame

    def on_proc_start(self):
        pass

    def on_receive(self, index, info):
        pass

    def on_proc_successfully(self):
        pass


class PythonModeProcessor(BasicModeProcessor):
    def on_proc_start(self):
        self.frame.controls.print('Python版本启动速度较慢，请耐心等待')

    def on_receive(self, index: int, info: str):
        if index % 5:
            return
        info = info.strip()
        if info.startswith('Tile'):
            proc, all_proc = info.lstrip('Tile').split('/')
            self.frame.controls.set_proc_progress(int(int(proc) / int(all_proc) * 10000))

    def on_proc_successfully(self):
        if self.frame.controls.output_path_is_dir:
            return
        name, suffix = splitext(self.frame.controls.input_path)
        new_file = f'{name}_out{suffix}'
        if not isfile(new_file):
            return
        if isfile(self.frame.controls.output_path):
            remove(self.frame.controls.output_path)
        rename(new_file, self.frame.controls.output_path)


class VulkanModeProcessor(BasicModeProcessor):
    def on_receive(self, index: int, info: str):
        if info.endswith('%'):
            self.frame.controls.set_proc_progress(int(info.rstrip('%').replace('.', '', 1)))
