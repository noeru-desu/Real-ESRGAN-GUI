'''
Author       : noeru_desu
Date         : 2021-12-19 18:15:34
LastEditors  : noeru_desu
LastEditTime : 2022-01-09 15:17:10
Description  : 覆写窗口
'''
# from concurrent.futures import ThreadPoolExecutor
from os import getcwd
from os.path import split, splitext, isfile
from sys import version

from pynvml import nvmlInit
from wx import (CANCEL, DIRP_CHANGE_DIR, DIRP_DIR_MUST_EXIST, FD_CHANGE_DIR,
                FD_FILE_MUST_EXIST, FD_OPEN, FD_PREVIEW, ICON_ERROR,
                ICON_INFORMATION, ICON_QUESTION, ICON_WARNING, ID_OK,
                STAY_ON_TOP, YES_NO, ID_NO, HELP, App, DirDialog, FileDialog, MessageDialog)
# from urllib.request import getproxies

from real_esrgan_gui.constants import BRANCH, OPEN_SOURCE_URL, SUB_VERSION_NUMBER, VERSION_BATCH, VERSION_NUMBER, VERSION_TYPE, LOGGER_NAME
from real_esrgan_gui.frame.controls import EXE_MODE, PYTHON_MODE, Controls
from real_esrgan_gui.frame.design_frame import MainFrame as DesignFrame
from real_esrgan_gui.frame.drag import DragExeFile, DragInputFile, DragModelDir, DragOutputDir
from real_esrgan_gui.models.config import Config
# from real_esrgan_gui.models.downloader import Downloader
from real_esrgan_gui.models.runner import Runner
from real_esrgan_gui.utils.exit_processor import ExitProcessor
from real_esrgan_gui.utils.logger import Logger
# from real_esrgan_gui.utils.requests import Proxy


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

        self.processingSettingsPanel.Disable()
        self.IoSettingsPanel.Disable()

        # 实例化组件
        self.logger = Logger(LOGGER_NAME)
        self.logger.info(f'Python {version}')
        self.logger.info(f'You are using Image encryptor GUI {VERSION_NUMBER}-{SUB_VERSION_NUMBER} (branch: {BRANCH}) (batch: {VERSION_BATCH})')
        self.logger.info(f'Open source at {OPEN_SOURCE_URL}')
        self.controls = Controls(self)
        self.exit_processor = ExitProcessor()
        self.processor = Runner(self)
        self.config = Config(self)
        # self.downloader = Downloader(4, 12, 128, Proxy(getproxies()))
        self.exit_processor.register(self.processor.on_exit)
        self.exit_processor.register(self.config.save_config)
        self.executableFilePath.SetDropTarget(DragExeFile(self))
        self.inputPath.SetDropTarget(DragInputFile(self))
        self.outputPath.SetDropTarget(DragOutputDir(self))
        self.modelDir.SetDropTarget(DragModelDir(self))
        # self.thread_pool = ThreadPoolExecutor(cpu_count())
        # self.exit_processor.register(lambda thread_pool: thread_pool.shutdown(wait=False, cancel_futures=True), self.thread_pool)

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
            exe_file_path = self.select_file('选择可执行文件', 'EXE/Python files (*.exe;*.py;*.py*)|*.exe;*.py;*.py*')
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
        self.processingSettingsPanel.Enable()
        self.IoSettingsPanel.Enable()
        self.refresh_interface(event)

    def select_input_file(self, event=None, file=None):
        input_path = self.select_file('选择文件')
        if not input_path:
            return
        self.controls.input_path = input_path
        self.controls.output_path_is_dir = False
        self.controls.gen_output_path()
        self.refresh_interface(event)

    def select_input_dir(self, event):
        input_path = self.select_dir('选择文件夹')
        if not input_path:
            return
        self.controls.input_path = input_path
        self.controls.output_path_is_dir = True
        self.controls.gen_output_path()
        self.refresh_interface(event)

    def select_output_dir(self, event):
        output_path = self.select_dir('选择文件夹')
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
            self.warning('没有找到任何模型')
        else:
            self.info(f'共找到了{self.controls.model_num}个模型', '已重新搜索模型文件')
        self.refresh_interface(event)

    def check_tile_size(self, event):
        if 32 > self.controls.tile_size > 0:
            self.controls.tile_size = 32
        self.refresh_interface(event)

    def refresh_interface(self, event):
        self.controls.gen_cmd()

    def start_proc(self, event):
        if not self.controls.output_path_is_dir and isfile(self.controls.output_path):
            if self.warning('输出文件已存在，是否继续执行操作？(这将覆盖已有文件)', additional_style=YES_NO) == ID_NO:
                return
        self.processor.run()

    def kill_proc(self, event):
        self.processor.terminate()

    def reset_config(self, event):
        self.config.reset_config()

    def force_switch_cmd_mode(self, event):
        if self.controls.mode is EXE_MODE:
            self.controls.mode = PYTHON_MODE
        elif self.controls.mode is PYTHON_MODE:
            self.controls.mode = EXE_MODE
        else:
            return
        if self.controls.mode is not self.controls.default_mode:
            self.warning('如果所选的可执行文件不支持当前模式，将无法启动处理程序')

    # -----
    # 对话框
    # -----

    def select_file(self, title, wildcard=''):
        with FileDialog(self, title, style=FD_OPEN | FD_CHANGE_DIR | FD_PREVIEW | FD_FILE_MUST_EXIST, wildcard=wildcard) as dialog:
            if ID_OK == dialog.ShowModal():
                return dialog.GetPath()

    def select_dir(self, title):
        with DirDialog(self, title, style=DIRP_CHANGE_DIR | DIRP_DIR_MUST_EXIST) as dialog:
            if ID_OK == dialog.ShowModal():
                return dialog.GetPath()

    def dialog(self, message, title, style):
        with MessageDialog(self, message, title, style=style) as dialog:
            return dialog.ShowModal()

    def info(self, message, title='信息', additional_style=None):
        style = ICON_INFORMATION | STAY_ON_TOP
        if additional_style is not None:
            style |= additional_style
        self.logger.info(f'[{title}]{message}')
        return self.dialog(message, title, style)

    def question(self, message, title='问题', additional_style=None):
        self.logger.info(f'[{title}]{message}')
        style = ICON_QUESTION | STAY_ON_TOP
        if additional_style is not None:
            style |= additional_style
        return self.dialog(message, title, style)

    def warning(self, message, title='警告', additional_style=None):
        self.logger.warning(f'[{title}]{message}')
        style = ICON_WARNING | STAY_ON_TOP
        if additional_style is not None:
            style |= additional_style
        return self.dialog(message, title, style)

    def error(self, message, title='错误', additional_style=None):
        self.logger.error(f'[{title}]{message}')
        style = ICON_ERROR | STAY_ON_TOP
        if additional_style is not None:
            style |= additional_style
        return self.dialog(message, title, style)

    def confirmation_frame(self, message, title='确认', additional_style=None, yes='是', no='否', cancel='取消', help=None):
        if additional_style is not None:
            style = YES_NO | additional_style
        else:
            style = YES_NO
        with MessageDialog(self, message, title, style=style | STAY_ON_TOP) as dialog:
            if CANCEL in style:
                dialog.SetYesNoCancelLabels(yes, no, cancel)
            else:
                dialog.SetYesNoLabels(yes, no)
            if HELP in style:
                dialog.SetHelpLabel(help)
            return dialog.ShowModal()

    def exit(self, event):
        self.logger.info('窗口退出')
        self.Destroy()
        exit()
