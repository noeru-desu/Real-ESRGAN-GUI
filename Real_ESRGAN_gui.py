#! python3.10
'''
Author       : noeru_desu
Date         : 2021-12-17 20:12:51
LastEditors  : noeru_desu
LastEditTime : 2022-01-08 20:00:13
Description  : 启动程序
'''
from sys import argv, exit
from warnings import filterwarnings

from real_esrgan_gui.frame.main_frame import MainFrame

filterwarnings('error')


if __name__ == '__main__':
    if len(argv) > 1 and argv[1] == '+test':
        exit()
    MainFrame.run()
