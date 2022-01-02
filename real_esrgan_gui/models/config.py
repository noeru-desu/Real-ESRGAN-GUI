'''
Author       : noeru_desu
Date         : 2021-12-25 18:53:36
LastEditors  : noeru_desu
LastEditTime : 2022-01-02 10:00:38
Description  : 配置文件
'''
from os import remove, rename
from os.path import join, isfile, isdir
from typing import TYPE_CHECKING
from traceback import print_exc

from real_esrgan_gui import CONFIG_VERSION, CONFIG_MAIN_VERSION, CONFIG_SUB_VERSION
from real_esrgan_gui.frame.controls import ItemNotFoundError
from real_esrgan_gui.utils.json import Json

if TYPE_CHECKING:
    from real_esrgan_gui.frame.main_frame import MainFrame


class Config(Json):
    def __init__(self, frame: 'MainFrame'):
        self.frame = frame
        self.default = self.config
        config_file = join(frame.run_path, 'config.json')
        have_config_file = isfile(config_file)
        super().__init__(config_file, default_json=self.default)
        if self.error is not None:
            error_config_file = join(frame.run_path, 'error_config.json')
            self.frame.logger.warning('配置文件不符合json格式，已生成新的配置文件(错误的配置文件已重命名为 error_config.json)')
            if isfile(error_config_file):
                remove(error_config_file)
            rename(config_file, error_config_file)
            super().__init__(config_file, default_json=self.default)
        self.check_config()
        if not have_config_file:
            return
        try:
            self.backtrack_interface(resize_window=True)
        except Exception:
            print_exc()
            self.frame.logger.error('将配置文件中的配置应用到界面时出现错误，停止操作')

    @property
    def config(self):
        return {
            'window_size': list(self.frame.Size),
            'exe_file': self.frame.controls.exe_file_path,
            'settings': {
                'saving_format': self.frame.controls.saving_format,
                'output_naming_format': self.frame.controls.output_naming_format,
                'model_dir': self.frame.controls.model_dir,
                'model_name': self.frame.controls.model_name,
                'tile_size': self.frame.controls.tile_size,
                'python_version': {
                    'scale_rate': self.frame.controls.scale_rate,
                    'face_enhance': self.frame.controls.face_enhance,
                    'half_precision': self.frame.controls.half_precision
                },
                'ncnn_vulkan_version': {
                    'gpu_id': self.frame.controls.gpu_id,
                    'tta_mode': self.frame.controls.tta,
                    'verbose_output': self.frame.controls.verbose_output,
                    'thread_count': [self.frame.controls.loading_thread_count, self.frame.controls.processing_thread_count, self.frame.controls.saving_thread_count]
                }
            },
            'config_version': CONFIG_VERSION
        }

    def check_config(self):
        self.main_version, self.sub_version = (int(i) for i in self['config_version'].split('.'))
        if self.main_version > CONFIG_MAIN_VERSION:
            self.frame.logger.error('配置文件版本不兼容(过高)，重新生成配置文件')
            self.save(self.default)
        elif self.sub_version < CONFIG_SUB_VERSION:
            self._bump_version()
        elif self.main_version < CONFIG_MAIN_VERSION:
            pass

    def save_config(self):
        self.save(self.config)

    def reset_config(self):
        self.save(self.default)
        self.backtrack_interface()

    def backtrack_interface(self, resize_window=False):
        if resize_window:
            self.frame.Size = self['window_size']
        have_exe_file = isfile(self['exe_file'])
        if have_exe_file:
            self.frame.select_executable_file(file=self['exe_file'])

        self.frame.controls.saving_format = self['settings']['saving_format']

        self.frame.controls.output_naming_format = self['settings']['output_naming_format']

        if isdir(self['settings']['model_dir']):
            old_model_dir = self.frame.controls.model_dir
            self.frame.controls.model_dir = self['settings']['model_dir']
            self.frame.controls.gen_model_list()
            try:
                self.frame.controls.model_name = self['settings']['model_name']
            except ItemNotFoundError:
                self.frame.logger.error(f"没有在指定的文件夹找到指定的模型: {self['settings']['model_name']}")
                self.frame.controls.model_dir = old_model_dir
                if isdir(old_model_dir):
                    self.frame.controls.gen_model_list()

        self.frame.controls.tile_size = self['settings']['tile_size']

        self.frame.controls.scale_rate = self['settings']['python_version']['scale_rate']

        self.frame.controls.face_enhance = self['settings']['python_version']['face_enhance']

        self.frame.controls.half_precision = self['settings']['python_version']['half_precision']

        self.frame.controls.gpu_id = self['settings']['ncnn_vulkan_version']['gpu_id']

        self.frame.controls.tta = self['settings']['ncnn_vulkan_version']['tta_mode']

        self.frame.controls.verbose_output = self['settings']['ncnn_vulkan_version']['verbose_output']

        self.frame.controls.loading_thread_count, self.frame.controls.processing_thread_count, self.frame.controls.saving_thread_count = self['settings']['ncnn_vulkan_version']['thread_count']

    def _bump_version(self):
        if self.sub_version == 0:
            self._v_10_to_11()

    def _v_10_to_11(self):
        self['window_size'] = tuple(self.frame.Size)
        if self['settings']['output_naming_format'] == '{orig_name}({model_name})({scale}){tta}':
            self['settings']['output_naming_format'] = '{orig_name}({model_name})({scale}){half_precision}{face_enhance}{tta}'
