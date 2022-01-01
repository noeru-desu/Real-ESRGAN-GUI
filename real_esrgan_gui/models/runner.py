'''
Author       : noeru_desu
Date         : 2021-12-19 18:04:57
LastEditors  : noeru_desu
LastEditTime : 2022-01-01 11:10:25
Description  : popen相关
'''
from os.path import split
from shlex import split as shlex_split
from subprocess import PIPE, STDOUT, Popen
from typing import TYPE_CHECKING

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

    def run(self):
        if not self.frame.controls.cmd_text:
            return
        self.frame.startProcBtn.Disable()
        self.frame.killProcBtn.Enable()
        self.process = Popen(shlex_split(self.frame.controls.cmd_text), cwd=split(self.frame.controls.executable_file_path)[0], stdin=PIPE, stdout=PIPE, stderr=STDOUT)
        self.frame.controls.cls()
        self.frame.controls.set_proc_progress(0)
        self.frame.controls.print('执行的命令行如下'.center(60, '-'))
        self.frame.controls.print(self.frame.controls.cmd_text)
        self.frame.controls.print(''.ljust(68, '-'))
        self.frame.controls.print(f'处理程序的PID: {self.process.pid}')
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

    def _loop(self):
        while True:
            try:
                result = self._receive()
            except ProcessExited:
                break
            else:
                self.frame.controls.print(result)
                try:
                    if result.endswith('%'):
                        self.frame.controls.set_proc_progress(int(result.rstrip('%').replace('.', '', 1)))
                except ValueError:
                    pass
        self.process.wait()
        if self.process.returncode == 0:
            self.frame.controls.print('处理程序已退出')
            self.frame.controls.set_proc_progress(10000)
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
            self.frame.controls.print('监视线程出现错误，自动结束处理进程。错误如下')
            self.frame.controls.print(err.formated_exc)
            self.terminate()
        self.process.stdin.close()
        self.process.stdout.close()
        self.frame.startProcBtn.Enable()
        self.frame.killProcBtn.Disable()
