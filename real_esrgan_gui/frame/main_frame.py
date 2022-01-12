'''
Author       : noeru_desu
Date         : 2021-12-19 18:15:34
LastEditors  : noeru_desu
LastEditTime : 2022-01-12 20:42:32
Description  : 覆写窗口
'''
# from concurrent.futures import ThreadPoolExecutor
from os import getcwd
from os.path import isfile, split, splitext
from sys import version
from typing import TYPE_CHECKING

from pynvml import nvmlInit
from wx import ID_NO, YES_NO, App
# from urllib.request import getproxies

from real_esrgan_gui.constants import BRANCH, LOGGER_NAME, OPEN_SOURCE_URL, SUB_VERSION_NUMBER, VERSION_BATCH, VERSION_NUMBER, VERSION_TYPE
from real_esrgan_gui.frame.controls import EXE_MODE, PYTHON_MODE, Controls
from real_esrgan_gui.frame.design_frame import MainFrame as DesignFrame
from real_esrgan_gui.frame.dialog import Dialog
from real_esrgan_gui.frame.drag import DragExeFile, DragInputFile, DragModelDir, DragOutputDir
from real_esrgan_gui.models.config import Config
from real_esrgan_gui.models.runner import Runner
from real_esrgan_gui.utils.exit_processor import ExitProcessor
from real_esrgan_gui.utils.logger import Logger
from real_esrgan_gui.utils.thread import ThreadPoolExecutor
# from real_esrgan_gui.models.downloader import Downloader
# from real_esrgan_gui.utils.requests import Proxy

if TYPE_CHECKING:
    from wx import CommandEvent


class MainFrame(DesignFrame):
    """
    主窗口类
    """

    def __init__(self, parent):
        super().__init__(parent)
        self.run_path = getcwd()
        if VERSION_TYPE > 0:
            self.SetTitle(f'Real ESRGAN GUI {VERSION_NUMBER}-{SUB_VERSION_NUMBER} (branch: {BRANCH})')
        else:
            self.SetTitle(f'Real ESRGAN GUI {VERSION_NUMBER}')

        self.settingsPanel.Disable()
        self.IoSettingsPanel.Disable()

        # 实例化组件
        self.logger = Logger(LOGGER_NAME)
        self.logger.info(f'Python {version}')
        self.logger.info(f'You are using Image encryptor GUI {VERSION_NUMBER}-{SUB_VERSION_NUMBER} (branch: {BRANCH}) (batch: {VERSION_BATCH})')
        self.logger.info(f'Open source at {OPEN_SOURCE_URL}')
        self.universal_thread_pool = ThreadPoolExecutor(8, 'universal_thread_pool')
        self.dialog = Dialog(self)
        self.controls = Controls(self)
        self.exit_processor = ExitProcessor()
        self.processor = Runner(self)
        self.config = Config(self)
        # self.downloader = Downloader(4, 12, 128, Proxy(getproxies()))
        self.exit_processor.register(self.processor.on_exit)
        self.exit_processor.register(self.config.save_config)
        self.exit_processor.register(self.universal_thread_pool.shutdown, wait=False, cancel_futures=True)
        self.executableFilePath.SetDropTarget(DragExeFile(self))
        self.inputPath.SetDropTarget(DragInputFile(self))
        self.outputPath.SetDropTarget(DragOutputDir(self))
        self.modelDir.SetDropTarget(DragModelDir(self))

        self.logger.info('窗口初始化完成')

    @classmethod
    def run(cls):
        nvmlInit()
        app = App(useBestVisual=True)
        self = cls(None)

        self.Show()

        app.MainLoop()

    # -----
    # 事件
    # -----

    def select_executable_file(self, event=None, file=None):
        if file is None:
            exe_file_path = self.dialog.select_file('选择可执行文件', 'EXE/Python files (*.exe;*.py;*.py*)|*.exe;*.py;*.py*')
        else:
            exe_file_path = file
        if not exe_file_path:
            return
        self.controls.exe_file_dir, file_name = split(exe_file_path)
        suffix = splitext(file_name)[1]
        if suffix.startswith('.py'):
            self.controls.mode = PYTHON_MODE
            self.controls.default_mode = PYTHON_MODE
        elif suffix == '.exe':
            self.controls.mode = EXE_MODE
            self.controls.default_mode = EXE_MODE
        else:
            self.controls.exe_file_dir = None
            return
        self.controls.exe_file_path = exe_file_path
        self.settingsPanel.Enable()
        self.IoSettingsPanel.Enable()
        self.refresh_interface(event)

    def select_input_file(self, event=None, file=None):
        input_path = self.dialog.select_file('选择文件')
        if not input_path:
            return
        self.controls.input_path = input_path
        self.controls.output_path_is_dir = False
        self.controls.gen_output_path()
        self.refresh_interface(event)

    def select_input_dir(self, event):
        input_path = self.dialog.select_dir('选择文件夹')
        if not input_path:
            return
        self.controls.input_path = input_path
        self.controls.output_path_is_dir = True
        self.controls.gen_output_path()
        self.refresh_interface(event)

    def select_output_dir(self, event):
        output_path = self.dialog.select_dir('选择文件夹')
        if not output_path:
            return
        self.controls.output_path = output_path
        self.refresh_interface(event)

    def regen_output_path(self, event):
        self.controls.gen_output_path()
        self.refresh_interface(event)

    def regen_model_list(self, event):
        self.controls.gen_model_list()
        if self.controls.model_num == 0:
            self.dialog.warning('没有找到任何模型')
        else:
            self.dialog.info(f'共找到了{self.controls.model_num}个模型', '已重新搜索模型文件')
        self.refresh_interface(event)

    def check_tile_size(self, event):
        if 32 > self.controls.tile_size > 0:
            self.controls.tile_size = 32
        self.refresh_interface(event)

    def refresh_interface(self, event):
        self.controls.gen_cmd()

    def start_proc(self, event):
        if not self.controls.output_path_is_dir and isfile(self.controls.output_path):
            if self.dialog.question('输出文件已存在，是否继续执行操作？(这将覆盖已有文件)', additional_style=YES_NO) == ID_NO:
                return
        self.processor.run()

    def kill_proc(self, event):
        self.processor.terminate()

    def reset_config(self, event):
        self.config.reset_config()

    def debug_tip(self, event: 'CommandEvent'):
        if event.IsChecked():
            if self.dialog.question('确认启动调试模式？', additional_style=YES_NO) == ID_NO:
                self.controls.cmd_debug = False

    def force_switch_cmd_mode(self, event):
        if self.controls.mode is EXE_MODE:
            self.controls.mode = PYTHON_MODE
        elif self.controls.mode is PYTHON_MODE:
            self.controls.mode = EXE_MODE
        else:
            return
        if self.controls.mode is not self.controls.default_mode:
            self.dialog.warning('如果所选的可执行文件不支持当前模式，将无法启动处理程序')

    def exit(self, event):
        self.logger.info('窗口退出')
        self.Destroy()
        exit()
