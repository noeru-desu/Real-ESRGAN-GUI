'''
Author       : noeru_desu
Date         : 2021-12-19 18:15:34
LastEditors  : noeru_desu
LastEditTime : 2021-12-25 20:21:46
Description  : 覆写窗口
'''
# from concurrent.futures import ThreadPoolExecutor
from os import getcwd
from os.path import isdir, join, split, splitext
from sys import version

from pynvml import nvmlInit
from wx import (CANCEL, DIRP_CHANGE_DIR, DIRP_DIR_MUST_EXIST, FD_CHANGE_DIR,
                FD_FILE_MUST_EXIST, FD_OPEN, FD_PREVIEW, HELP, ICON_ERROR,
                ICON_INFORMATION, ICON_QUESTION, ICON_WARNING, ID_OK,
                STAY_ON_TOP, YES_NO, App, DirDialog, FileDialog, MessageDialog)

from real_esrgan_gui import BRANCH, OPEN_SOURCE_URL, SUB_VERSION_NUMBER, VERSION_BATCH, VERSION_NUMBER, VERSION_TYPE
from real_esrgan_gui.frame.controls import EXE_MODE, PYTHON_MODE, Controls
from real_esrgan_gui.frame.design_frame import MainFrame as DesignFrame
from real_esrgan_gui.frame.drag import DragExeFile, DragInputFile, DragModelDir, DragOutputDir
from real_esrgan_gui.models.config import Config
from real_esrgan_gui.models.runner import Runner
from real_esrgan_gui.utils.exit_processor import ExitProcessor
from real_esrgan_gui.utils.logger import Logger


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
        self.logger = Logger('real-esrgan')
        self.logger.info(f'Python {version}')
        self.logger.info(f'You are using Image encryptor GUI {VERSION_NUMBER}-{SUB_VERSION_NUMBER} (branch: {BRANCH}) (batch: {VERSION_BATCH})')
        self.logger.info(f'Open source at {OPEN_SOURCE_URL}')
        self.controls = Controls(self)
        self.exit_processor = ExitProcessor()
        self.processor = Runner(self)
        self.config = Config(self)
        self.exit_processor.register(lambda on_exit: on_exit(), self.processor.on_exit)
        self.exit_processor.register(lambda save_config: save_config(), self.config.save_config)
        self.executableFilePath.SetDropTarget(DragExeFile(self))
        self.inputPath.SetDropTarget(DragInputFile(self))
        self.outputPath.SetDropTarget(DragOutputDir(self))
        self.modelDir.SetDropTarget(DragModelDir(self))
        # self.thread_pool = ThreadPoolExecutor(cpu_count())
        # self.exit_processor.register(lambda thread_pool: thread_pool.shutdown(wait=False, cancel_futures=True), self.thread_pool)

        self.logger.info('窗口初始化完成')

    @classmethod
    def run(cls):
        """
        运行入口函数
        """
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
            executable_file_path = self.select_file('选择可执行文件', 'EXE/Python files (*.exe;*.py)|*.exe;*.py')
        else:
            executable_file_path = file
        if not executable_file_path:
            return
        dir_name, file_name = split(executable_file_path)
        suffix = splitext(file_name)[1]
        if suffix == '.py':
            self.controls.mode = PYTHON_MODE
            self.pythonSpecificPanel.Enable()
            self.ncnnVulkanSpecificPanel.Disable()
        elif suffix == '.exe':
            self.controls.mode = EXE_MODE
            self.ncnnVulkanSpecificPanel.Enable()
            self.pythonSpecificPanel.Disable()
        else:
            return
        self.controls.executable_file_path = executable_file_path
        model_dir = join(dir_name, 'models')
        if isdir(model_dir):
            self.controls.model_dir = model_dir
            self.controls.gen_model_list()
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
        self.refresh_interface(event)

    def check_tile_size(self, event):
        if 32 > self.controls.tile_size > 0:
            self.controls.tile_size = 32
        self.refresh_interface(event)

    def refresh_interface(self, event):
        if self.controls.input_path and self.executableFilePath:
            self.controls.gen_cmd()

    def start_proc(self, event):
        self.processor.run()

    def kill_proc(self, event):
        self.processor.terminate()

    def reset_config(self, event):
        self.config.reset_config()

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

    def info(self, message, title='信息'):
        self.logger.info(f'[{title}]{message}')
        with MessageDialog(self, message, title, style=ICON_INFORMATION | STAY_ON_TOP) as dialog:
            dialog.ShowModal()

    def question(self, message, title='问题'):
        self.logger.info(f'[{title}]{message}')
        with MessageDialog(self, message, title, style=ICON_QUESTION | STAY_ON_TOP) as dialog:
            dialog.ShowModal()

    def warning(self, message, title='警告'):
        self.logger.warning(f'[{title}]{message}')
        with MessageDialog(self, message, title, style=ICON_WARNING | STAY_ON_TOP)as dialog:
            dialog.ShowModal()

    def error(self, message, title='错误'):
        self.logger.error(f'[{title}]{message}')
        with MessageDialog(self, message, title, style=ICON_ERROR | STAY_ON_TOP) as dialog:
            dialog.ShowModal()

    def confirmation_frame(self, message, title='确认', style=YES_NO | CANCEL, yes='是', no='否', cancel='取消', help=None):
        if help is not None:
            style = YES_NO | CANCEL | HELP
        else:
            style = YES_NO | CANCEL
        with MessageDialog(self, message, title, style=style | STAY_ON_TOP) as dialog:
            if help is not None:
                dialog.SetOKLabel(help)
            dialog.SetYesNoCancelLabels(yes, no, cancel)
            return dialog.ShowModal()

    def exit(self, event):
        self.logger.info('窗口退出')
        self.Destroy()
        exit()
