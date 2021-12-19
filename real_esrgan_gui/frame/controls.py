'''
Author       : noeru_desu
Date         : 2021-12-18 21:01:55
LastEditors  : noeru_desu
LastEditTime : 2021-12-19 15:56:42
Description  : 设置信息
'''
from os import walk
from os.path import split, splitext, join
from typing import TYPE_CHECKING

from pynvml import nvmlDeviceGetCount

if TYPE_CHECKING:
    from real_esrgan_gui.frame.main_frame import MainFrame

PYTHON_MODE = 2
EXE_MODE = 3


class Controls(object):
    "控件/控制器"
    def __init__(self, frame: 'MainFrame'):
        self.mode = None
        self.output_path_is_dir = False
        self.frame = frame
        self.frame.GpuId.Max = nvmlDeviceGetCount() - 1

    @property
    def executable_file_path(self) -> str:
        return self.frame.executableFilePath.Value

    @executable_file_path.setter
    def executable_file_path(self, v):
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

    def gen_output_path(self):
        if not self.input_path:
            return
        kwargs = {
            'orig_name': '',
            'model_name': self.model_name,
            'scale': str(self.scale_rate),
            'tta': '(tta)' if self.tta else ''
        }
        if self.output_path_is_dir:
            self.output_path = join(self.input_path, f'{self.output_naming_format.format(**kwargs)}')
        else:
            dir, file = split(self.input_path)
            kwargs['orig_name'], suffix = splitext(file)
            self.output_path = join(dir, f'{self.output_naming_format.format(**kwargs)}{suffix if self.saving_format == "同输入" else self.saving_format}')

    @property
    def output_naming_format(self) -> str:
        return self.frame.outputNamingFormat.Value

    @property
    def auto_selected_formats(self) -> list:
        return self.frame.autoSelectedFormats.Value.split(':')

    @property
    def saving_format(self) -> str:
        return self.frame.savingFormat.Value

    @property
    def scale_rate(self) -> float:
        return self.frame.scaleRate.Value

    @scale_rate.setter
    def scale_rate(self, v):
        self.frame.scaleRate.Enable(v)

    @property
    def face_enhance(self):
        return self.frame.useFaceEnhance.Value

    @property
    def half_precision(self):
        return self.frame.useHalfPrecision.Value

    @property
    def model_dir(self) -> str:
        return self.frame.modelDir.Path

    @model_dir.setter
    def model_dir(self, v):
        self.frame.modelDir.Path = v

    @property
    def model_name(self) -> str:
        return self.frame.modelNames.GetStringSelection()

    def clr_model_list(self):
        self.frame.modelNames.Clear()

    def gen_model_list(self):
        self.frame.modelNames.Clear()
        names = []
        for i in next(walk(self.model_dir))[2]:
            name = splitext(i)[0]
            if name in names:
                continue
            names.append(name)
            self.frame.modelNames.Append(name)
        self.frame.modelNames.Select(0)

    @property
    def tta(self) -> bool:
        return self.frame.useTtaMode.Value

    @tta.setter
    def tta(self, v):
        self.frame.useTtaMode.Value = v

    @property
    def gpu_id(self) -> int:
        return self.frame.GpuId.Value

    @property
    def tile_size(self) -> int:
        return self.frame.tileSize.Value

    @tile_size.setter
    def tile_size(self, v):
        self.frame.tileSize.Value = v

    @property
    def verbose_output(self) -> bool:
        return self.frame.useVerboseOutput.Value

    @property
    def loading_thread_count(self) -> int:
        return self.frame.loadingThreadCount.Value

    @property
    def processing_thread_count(self) -> int:
        return self.frame.processingThreadCount.Value

    @property
    def saving_thread_count(self) -> int:
        return self.frame.savingThreadCount.Value

    @property
    def cmd_text(self) -> str:
        return self.frame.cmdText.Value

    @cmd_text.setter
    def cmd_text(self, v):
        self.frame.cmdText.Value = v

    def gen_cmd(self):
        if self.mode is PYTHON_MODE:
            output_path = self.output_path if self.output_path_is_dir else split(self.output_path)[0]
            self.cmd_text = '"{0}" -i "{1}" -o "{2}" -n {3} -s {4} -t {5} --ext {6} {7} {8}'.format(
                self.executable_file_path, self.input_path, output_path, self.model_name,
                self.scale_rate, self.tile_size, 'auto' if self.saving_format == '同输入' else self.saving_format,
                '--face_enhance' if self.face_enhance else '',
                '--half' if self.half_precision else ''
            ).strip(' ')
        elif self.mode is EXE_MODE:
            self.cmd_text = '"{0}" -i "{1}" -o "{2}" -m "{3}" -n {4} -g {5} -t {6} -j {7}:{8}:{9} {10} {11}'.format(
                self.executable_file_path, self.input_path, self.output_path, self.model_dir,
                self.model_name, self.gpu_id, self.tile_size, self.loading_thread_count,
                self.processing_thread_count, self.saving_thread_count,
                '-x' if self.tta else '',
                '-v' if self.verbose_output else ''
            ).strip(' ')
