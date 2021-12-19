'''
Author       : noeru_desu
Date         : 2021-12-19 19:06:56
LastEditors  : noeru_desu
LastEditTime : 2021-12-19 20:27:21
Description  : 拖放处理
'''
from os.path import isdir, isfile
from typing import TYPE_CHECKING

from wx import FileDropTarget

if TYPE_CHECKING:
    from real_esrgan_gui.frame.main_frame import MainFrame


class DragExeFile(FileDropTarget):
    def __init__(self, frame: 'MainFrame'):
        super().__init__()
        self.frame = frame

    def OnDropFiles(self, x, y, filenames):
        try:
            filename = tuple(filenames)[0]
            if isfile(filename):
                self.frame.select_executable_file(file=filename)
        except RuntimeError:
            return False
        else:
            return True


class DragInputFile(FileDropTarget):
    def __init__(self, frame: 'MainFrame'):
        super().__init__()
        self.frame = frame

    def OnDropFiles(self, x, y, filenames):
        try:
            filename = tuple(filenames)[0]
            self.frame.controls.input_path = filename
            self.frame.controls.output_path_is_dir = isdir(filename)
            self.frame.controls.gen_output_path()
            self.frame.refresh_interface(None)
        except RuntimeError:
            return False
        else:
            return True


class DragOutputDir(FileDropTarget):
    def __init__(self, frame: 'MainFrame'):
        super().__init__()
        self.frame = frame

    def OnDropFiles(self, x, y, filenames):
        try:
            filename = tuple(filenames)[0]
            if not isdir(filename):
                return True
            self.frame.controls.output_path = filename
            self.frame.refresh_interface(None)
        except RuntimeError:
            return False
        else:
            return True


class DragModelDir(FileDropTarget):
    def __init__(self, frame: 'MainFrame'):
        super().__init__()
        self.frame = frame

    def OnDropFiles(self, x, y, filenames):
        try:
            filename = tuple(filenames)[0]
            if not isdir(filename):
                return True
            self.frame.controls.model_dir = filename
            self.frame.regen_model_list(None)
        except RuntimeError:
            return False
        else:
            return True
