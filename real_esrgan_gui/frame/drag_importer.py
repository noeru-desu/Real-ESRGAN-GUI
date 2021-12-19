'''
Author       : noeru_desu
Date         : 2021-11-06 19:06:56
LastEditors  : noeru_desu
LastEditTime : 2021-12-19 16:42:05
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


class DragOutputFile(FileDropTarget):
    def __init__(self, frame: 'MainFrame'):
        super().__init__()
        self.frame = frame

    def OnDropFiles(self, x, y, filenames):
        try:
            filename = tuple(filenames)[0]
            if isfile(filename):
                return
            self.frame.controls.output_path = filename
            self.frame.refresh_interface(None)
        except RuntimeError:
            return False
        else:
            return True
