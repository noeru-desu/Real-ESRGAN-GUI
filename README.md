# Real-ESRGAN-GUI
(WIP) 给[Real-ESRGAN](https://github.com/xinntao/Real-ESRGAN)写的的图形界面启动器

## 运行源代码

Python版本：`3.9`

>因为wxPython尚不支持Python 3.10

`requirements.txt`包含所有依赖库名称

启动`Real_ESRGAN_gui.py`即可

## 自动构建

Actions页面的CI中可下载自动构建的可执行文件包

>目前CI仅测试程序能否正常启动，没有测试各项功能是否可使用或是否存在Bug

packaged代表被打包为单文件版本

unpackaged代表没有被打包的版本

启动速度上，没有被打包的版本启动更快，Nuitka编译的版本比PyInstaller打包的版本更快

性能上，Nuitka编译的版本比PyInstaller打包的版本更好
