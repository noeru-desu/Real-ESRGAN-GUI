'''
Author       : noeru_desu
Date         : 2021-12-19 18:04:57
LastEditors  : noeru_desu
LastEditTime : 2021-12-19 20:24:03
Description  : popen相关
'''
from os.path import split
from subprocess import STDOUT, Popen, PIPE
from shlex import split as shlex_split
from typing import TYPE_CHECKING

from real_esrgan_gui.utils.thread import ThreadManager

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
        self.frame.stopProcBtn.Enable()
        self.frame.killProcBtn.Enable()
        self.process = Popen(shlex_split(self.frame.controls.cmd_text), cwd=split(self.frame.controls.executable_file_path)[0], stdin=PIPE, stdout=PIPE, stderr=STDOUT)
        self.thread_manager.start_new(self._main_loop, self._on_stop)

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
            return text.decode().rstrip('\n\r').lstrip('\n\r')

    def _main_loop(self):
        self.frame.controls.cls()
        self.frame.controls.set_proc_progress(0)
        self.frame.controls.print('----------执行的命令行如下----------')
        self.frame.controls.print(self.frame.controls.cmd_text)
        self.frame.controls.print('-----------------------------------')
        self.frame.controls.print(f'处理程序的PID: {self.process.pid}')
        while True:
            try:
                result = self._receive()
            except ProcessExited:
                break
            else:
                self.frame.controls.print(result)
                try:
                    self.frame.controls.set_proc_progress(int(result.strip('%').replace('.', '')))
                except ValueError:
                    pass
        self.process.wait()
        self.frame.controls.print(f'处理程序已退出，返回代码: {self.process.returncode}')
        if self.process.returncode == 0:
            self.frame.controls.set_proc_progress(10000)

    def stop(self):
        if self.process.returncode is None:
            self.process.send_signal('^C')

    def terminate(self):
        if self.process.returncode is None:
            self.process.terminate()

    def _on_stop(self, error, result):
        self.process.stdout.close()
        self.frame.startProcBtn.Enable()
        self.frame.stopProcBtn.Disable()
        self.frame.killProcBtn.Disable()

    def on_exit(self):
        if self.process is not None and self.process.returncode is None:
            self.process.terminate()
            self.process.wait()
