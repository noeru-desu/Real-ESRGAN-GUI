'''
Author       : noeru_desu
Date         : 2021-12-19 16:50:59
LastEditors  : noeru_desu
LastEditTime : 2022-01-17 20:17:25
Description  : 常量
'''
from sys import argv

# 标志
PYTHON_MODE = 21
EXE_MODE = 22

# 其他
LOGGER_NAME = 'real-esrgan'
TESTING = len(argv) > 1 and argv[1] == '+test'

# 程序信息
RELEASE = 10
RELEASE_CANDIDATE = 11
BETA = 12
ALPHA = 13
VERSION_TYPE = RELEASE

VERSION_NUMBER = '1.0.0'
SUB_VERSION_NUMBER = 'release'
VERSION_BATCH = '20220117-1'

BRANCH = 'master'
OPEN_SOURCE_URL = 'https://github.com/noeru-desu/Real-ESRGAN-GUI'

# 配置文件版本信息
CONFIG_MAIN_VERSION = 1
CONFIG_SUB_VERSION = 1
CONFIG_VERSION = f'{CONFIG_MAIN_VERSION}.{CONFIG_SUB_VERSION}'
