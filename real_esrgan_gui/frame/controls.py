'''
Author       : noeru_desu
Date         : 2021-12-18 21:01:55
LastEditors  : noeru_desu
LastEditTime : 2022-01-12 20:49:53
Description  : 设置信息
'''
from os import walk
from os.path import exists, isdir, isfile, join, split, splitext
from typing import TYPE_CHECKING

from pynvml import nvmlDeviceGetCount
from wx import NOT_FOUND
# from wx.core import BLACK, RED

from real_esrgan_gui.constants import PYTHON_MODE, EXE_MODE

if TYPE_CHECKING:
    from real_esrgan_gui.frame.main_frame import MainFrame


class ItemNotFoundError(Exception):
    pass


class Controls(object):
    "控件/控制器"
    def __init__(self, frame: 'MainFrame'):
        self._mode = None
        self.default_mode = None
        self.output_path_is_dir = False
        self.exe_file_dir = None
        self.frame = frame
        self.frame.GpuId.Max = nvmlDeviceGetCount() - 1

    # ----------
    # properties
    # ----------

    @property
    def exe_file_path(self) -> str:
        return self.frame.executableFilePath.Value

    @exe_file_path.setter
    def exe_file_path(self, v):
        self.frame.executableFilePath.Value = v

    @property
    def input_path(self) -> str:
        return self.frame.inputPath.Value

    @input_path.setter
    def input_path(self, v):
        self.frame.inputPath.Value = v

    @property
    def output_path(self) -> str:
        return self.frame.outputPath.Value

    @output_path.setter
    def output_path(self, v):
        self.frame.outputPath.Value = v

    @property
    def output_naming_format(self) -> str:
        return self.frame.outputNamingFormat.Value

    @output_naming_format.setter
    def output_naming_format(self, v):
        self.frame.outputNamingFormat.Value = v

    @property
    def saving_format(self) -> str:
        return self.frame.savingFormat.Value

    @saving_format.setter
    def saving_format(self, v):
        self.frame.savingFormat.Value = v

    @property
    def scale_rate(self) -> float:
        return self.frame.scaleRate.Value

    @scale_rate.setter
    def scale_rate(self, v):
        self.frame.scaleRate.Value = v

    @property
    def face_enhance(self) -> bool:
        return self.frame.useFaceEnhance.Value

    @face_enhance.setter
    def face_enhance(self, v):
        self.frame.useFaceEnhance.Value = v

    @property
    def half_precision(self) -> bool:
        return self.frame.useHalfPrecision.Value

    @half_precision.setter
    def half_precision(self, v):
        self.frame.useHalfPrecision.Value = v

    @property
    def model_dir(self) -> str:
        return self.frame.modelDir.Path

    @model_dir.setter
    def model_dir(self, v):
        self.frame.modelDir.Path = v

    @property
    def model_name(self) -> str:
        return self.frame.modelNames.GetStringSelection()

    @model_name.setter
    def model_name(self, v):
        item_id = self.frame.modelNames.FindString(v)
        if item_id is NOT_FOUND:
            raise ItemNotFoundError(f'There is no item named {v} in the Choice')
        self.frame.modelNames.Selection = item_id

    @property
    def model_num(self):
        return self.frame.modelNames.Count

    @property
    def tta(self) -> bool:
        return self.frame.useTtaMode.Value

    @tta.setter
    def tta(self, v):
        self.frame.useTtaMode.Value = v

    @property
    def gpu_id(self) -> int:
        return self.frame.GpuId.Value

    @gpu_id.setter
    def gpu_id(self, v):
        self.frame.GpuId.Value = v

    @property
    def tile_size(self) -> int:
        return self.frame.tileSize.Value

    @tile_size.setter
    def tile_size(self, v):
        self.frame.tileSize.Value = v

    @property
    def verbose_output(self) -> bool:
        return self.frame.useVerboseOutput.Value

    @verbose_output.setter
    def verbose_output(self, v):
        self.frame.useVerboseOutput.Value = v

    @property
    def loading_thread_count(self) -> int:
        return self.frame.loadingThreadCount.Value

    @loading_thread_count.setter
    def loading_thread_count(self, v):
        self.frame.loadingThreadCount.Value = v

    @property
    def processing_thread_count(self) -> int:
        return self.frame.processingThreadCount.Value

    @processing_thread_count.setter
    def processing_thread_count(self, v):
        self.frame.processingThreadCount.Value = v

    @property
    def saving_thread_count(self) -> int:
        return self.frame.savingThreadCount.Value

    @saving_thread_count.setter
    def saving_thread_count(self, v):
        self.frame.savingThreadCount.Value = v

    @property
    def cmd_text(self) -> str:
        return self.frame.cmdText.Value

    @cmd_text.setter
    def cmd_text(self, v):
        self.frame.cmdText.Value = v

    @property
    def cmd_mode(self) -> str:
        return self.frame.cmdMode.LabelText

    @cmd_mode.setter
    def cmd_mode(self, v):
        self.frame.cmdMode.LabelText = v

    @property
    def cmd_debug(self) -> bool:
        return self.frame.cmdDebug.Value

    @cmd_debug.setter
    def cmd_debug(self, v):
        self.frame.cmdDebug.Value = v

    @property
    def ignore_message_exception(self) -> bool:
        return self.frame.ignoreMessageException.Value

    @ignore_message_exception.setter
    def ignore_message_exception(self, v):
        self.frame.ignoreMessageException.Value = v

    @property
    def mode(self):
        return self._mode

    @mode.setter
    def mode(self, v):
        if v is PYTHON_MODE:
            self.frame.ncnnVulkanSpecificPanel.Hide()
            self.frame.pythonSpecificPanel.Show()
            self.frame.controls.cmd_mode = 'Python模式'
            self.frame.modelDir.Disable()
        elif v is EXE_MODE:
            self.frame.pythonSpecificPanel.Hide()
            self.frame.ncnnVulkanSpecificPanel.Show()
            self.frame.controls.cmd_mode = 'exe模式'
            self.frame.modelDir.Enable()
        else:
            assert False, f'Unknown mode: {v}'
        self._mode = v
        model_dir = join(self.exe_file_dir, 'models' if v is EXE_MODE else 'experiments\\pretrained_models')
        if isdir(model_dir):
            self.model_dir = model_dir
        self.gen_model_list()
        self.gen_cmd()
        self.frame.processingSettingsPanel.Layout()
        self.frame.cmdPanel.Layout()

    # ------
    # checks
    # ------

    def _checker(self, text, target, checker):
        if not text:
            return False
        if checker(text):
            # target.SetForegroundColour(BLACK)
            return True
        else:
            # target.SetForegroundColour(RED)
            return False

    def check_exe_file(self):
        return self._checker(self.exe_file_path, self.frame.executableFilePath, isfile)

    def check_input_file(self):
        return self._checker(self.input_path, self.frame.inputPath, exists)

    def check_output_file(self):
        return self._checker(self.output_path if self.output_path_is_dir else split(self.output_path)[0], self.frame.outputPath, isdir)

    def check_model_dir(self):
        return self._checker(self.model_dir, self.frame.modelDir, isdir)

    def check_model_name(self):
        return self._checker(join(self.model_dir, f'{self.model_name}.pth' if self.mode is PYTHON_MODE else f'{self.model_name}.bin'), self.frame.modelNames, isfile)

    # ---------
    # functions
    # ---------

    def set_proc_progress(self, v):
        self.frame.processingProgress.Value = v

    def clr_model_list(self):
        self.frame.modelNames.Clear()

    def gen_model_list(self):
        if not self.model_dir:
            return
        self.clr_model_list()
        target_suffix = '.pth' if self.mode is PYTHON_MODE else '.bin'
        for i in next(walk(self.model_dir))[2]:
            name, suffix = splitext(i)
            if suffix != target_suffix:
                continue
            self.frame.modelNames.Append(name)
        self.frame.modelNames.Select(0)

    def gen_output_path(self):
        if not self.input_path:
            return
        kwargs = {
            'orig_name': '',
            'model_name': self.model_name,
            'scale': str(self.scale_rate),
            'half_precision': '(half-precision)' if self.half_precision else '',
            'face_enhance': '(face-enhance)' if self.face_enhance else '',
            'tta': '(tta)' if self.tta else ''
        }
        if self.output_path_is_dir:
            self.output_path = join(self.input_path, f'{self.output_naming_format.format(**kwargs)}')
        else:
            dir, file = split(self.input_path)
            kwargs['orig_name'], suffix = splitext(file)
            self.output_path = join(dir, f'{self.output_naming_format.format(**kwargs)}{suffix if self.saving_format == "同输入" else self.saving_format}')

    def gen_cmd(self):
        """生成cmd命令行并输出至界面"""
        if not (self.model_name and self.input_path and self.exe_file_path):
            self.frame.cmdText.Clear()
            return
        if self.mode is PYTHON_MODE:
            output_path = self.output_path if self.output_path_is_dir else split(self.output_path)[0]
            self.cmd_text = 'py "{0}" -i "{1}" -o "{2}" -n {3} -s {4} -t {5} --ext {6} {7} {8}'.format(
                self.exe_file_path, self.input_path, output_path, self.model_name,
                self.scale_rate, self.tile_size, 'auto' if self.saving_format == '同输入' else self.saving_format,
                '--face_enhance' if self.face_enhance else '',
                '--half' if self.half_precision else ''
            ).rstrip()
        elif self.mode is EXE_MODE:
            self.cmd_text = '"{0}" -i "{1}" -o "{2}" -m "{3}" -n {4} -g {5} -t {6} -j {7}:{8}:{9} {10} {11}'.format(
                self.exe_file_path, self.input_path, self.output_path, self.model_dir,
                self.model_name, self.gpu_id, self.tile_size, self.loading_thread_count,
                self.processing_thread_count, self.saving_thread_count,
                '-x' if self.tta else '',
                '-v' if self.verbose_output else ''
            ).rstrip()

    def print(self, text, start='', end='\n'):
        """向界面内的输出框打印信息"""
        self.frame.programOutput.AppendText(f'{text}{start}{end}')

    def cls(self):
        """清空界面内的输出框"""
        self.frame.programOutput.Clear()
