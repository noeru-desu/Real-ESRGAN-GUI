# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Real ESRGAN GUI", pos = wx.DefaultPosition, size = wx.Size( 755,650 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL, name = u"Image Encryptor" )

        self.SetSizeHints( wx.Size( 755,650 ), wx.Size( -1,-1 ) )
        self.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tahoma" ) )
        self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

        bSizer10 = wx.BoxSizer( wx.VERTICAL )

        sbSizer6 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"核心程序" ), wx.VERTICAL )

        bSizer3611 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText1811 = wx.StaticText( sbSizer6.GetStaticBox(), wx.ID_ANY, u"可执行文件(.exe或.py*)路径", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
        self.m_staticText1811.Wrap( -1 )

        bSizer3611.Add( self.m_staticText1811, 0, wx.ALIGN_CENTER, 0 )

        self.executableFilePath = wx.TextCtrl( sbSizer6.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
        self.executableFilePath.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
        self.executableFilePath.SetToolTip( u"Real ESRGAN的可执行文件路径，后缀可为.exe或.py*(即.py/.pyc/.pyd等)，分别对应不同的处理模式" )

        bSizer3611.Add( self.executableFilePath, 5, wx.ALL|wx.EXPAND, 5 )

        self.selectExecutableFile = wx.Button( sbSizer6.GetStaticBox(), wx.ID_ANY, u"选择可执行文件", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer3611.Add( self.selectExecutableFile, 0, wx.ALIGN_CENTER, 5 )

        self.downloadFile = wx.Button( sbSizer6.GetStaticBox(), wx.ID_ANY, u"下载核心程序", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.downloadFile.Hide()

        bSizer3611.Add( self.downloadFile, 0, wx.ALIGN_CENTER, 2 )


        sbSizer6.Add( bSizer3611, 1, wx.EXPAND, 5 )


        bSizer10.Add( sbSizer6, 0, wx.ALL|wx.EXPAND, 3 )

        self.IoSettingsPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        sbSizer8 = wx.StaticBoxSizer( wx.StaticBox( self.IoSettingsPanel, wx.ID_ANY, u"输入和输出设置" ), wx.VERTICAL )

        bSizer9 = wx.BoxSizer( wx.HORIZONTAL )

        bSizer151 = wx.BoxSizer( wx.VERTICAL )

        bSizer3 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText18 = wx.StaticText( sbSizer8.GetStaticBox(), wx.ID_ANY, u"输入路径", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText18.Wrap( -1 )

        bSizer3.Add( self.m_staticText18, 0, wx.ALIGN_CENTER|wx.ALL, 0 )

        self.m_staticText2 = wx.StaticText( sbSizer8.GetStaticBox(), wx.ID_ANY, u"（文件或文件夹）", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )

        bSizer3.Add( self.m_staticText2, 0, wx.ALIGN_CENTER|wx.ALL, 0 )


        bSizer151.Add( bSizer3, 0, wx.ALIGN_CENTER, 0 )


        bSizer151.Add( ( 0, 0), 0, wx.ALL, 4 )

        self.m_staticText181 = wx.StaticText( sbSizer8.GetStaticBox(), wx.ID_ANY, u"输出路径", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText181.Wrap( -1 )

        bSizer151.Add( self.m_staticText181, 1, wx.ALIGN_CENTER, 0 )


        bSizer9.Add( bSizer151, 1, wx.EXPAND, 5 )

        bSizer16 = wx.BoxSizer( wx.VERTICAL )

        self.inputPath = wx.TextCtrl( sbSizer8.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
        self.inputPath.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
        self.inputPath.SetToolTip( u"待处理的文件路径" )

        bSizer16.Add( self.inputPath, 1, wx.ALL|wx.EXPAND, 5 )

        self.outputPath = wx.TextCtrl( sbSizer8.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
        self.outputPath.SetToolTip( u"文件的输出路径，在Python模式下，会先将文件保存为{orig_name}_out.{suffix}，带处理程序运行完成后自动重命名为目标文件名" )

        bSizer16.Add( self.outputPath, 0, wx.ALL|wx.EXPAND, 5 )


        bSizer9.Add( bSizer16, 5, wx.EXPAND, 5 )

        bSizer173 = wx.BoxSizer( wx.VERTICAL )

        bSizer16 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer173.Add( bSizer16, 1, wx.EXPAND, 5 )

        bSizer17 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer173.Add( bSizer17, 1, wx.EXPAND, 5 )


        bSizer9.Add( bSizer173, 0, wx.EXPAND, 5 )

        gSizer3 = wx.GridSizer( 0, 2, 0, 0 )

        self.m_button1 = wx.Button( sbSizer8.GetStaticBox(), wx.ID_ANY, u"选择文件", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer3.Add( self.m_button1, 0, wx.ALIGN_CENTER, 5 )

        self.m_button41 = wx.Button( sbSizer8.GetStaticBox(), wx.ID_ANY, u"选择文件夹", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer3.Add( self.m_button41, 0, wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_button11 = wx.Button( sbSizer8.GetStaticBox(), wx.ID_ANY, u"选择文件夹", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer3.Add( self.m_button11, 0, wx.ALIGN_CENTER, 5 )

        self.m_button4 = wx.Button( sbSizer8.GetStaticBox(), wx.ID_ANY, u"生成路径", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_button4.SetToolTip( u"重新根据[输出文件名规则]生成目标文件名" )

        gSizer3.Add( self.m_button4, 0, wx.ALIGN_CENTER, 5 )


        bSizer9.Add( gSizer3, 0, wx.EXPAND, 5 )


        sbSizer8.Add( bSizer9, 0, wx.EXPAND, 5 )

        bSizer12 = wx.BoxSizer( wx.HORIZONTAL )

        sbSizer21 = wx.StaticBoxSizer( wx.StaticBox( sbSizer8.GetStaticBox(), wx.ID_ANY, u"输出文件格式" ), wx.VERTICAL )

        savingFormatChoices = [ u"同输入", u".png", u".jpg", u".webp" ]
        self.savingFormat = wx.ComboBox( sbSizer21.GetStaticBox(), wx.ID_ANY, u"png", wx.DefaultPosition, wx.DefaultSize, savingFormatChoices, 0 )
        self.savingFormat.SetSelection( 0 )
        self.savingFormat.SetToolTip( u"选择保存格式，[同输入]即与输入的文件的后缀名相同" )

        sbSizer21.Add( self.savingFormat, 0, wx.ALL|wx.EXPAND, 5 )


        bSizer12.Add( sbSizer21, 0, 0, 5 )


        bSizer12.Add( ( 0, 0), 0, wx.ALL, 5 )

        sbSizer12 = wx.StaticBoxSizer( wx.StaticBox( sbSizer8.GetStaticBox(), wx.ID_ANY, u"输出文件命名规则" ), wx.VERTICAL )

        self.outputNamingFormat = wx.TextCtrl( sbSizer12.GetStaticBox(), wx.ID_ANY, u"{orig_name}({model_name})({scale}){half_precision}{face_enhance}{tta}", wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
        self.outputNamingFormat.SetToolTip( u"输出文件的命名规则(自动生成文件名时使用)\n{orig_name} - 源文件名称(不含后缀)\n{model_name} - 使用的模型名称\n{scale} - 缩放倍率\n{half_precision} - 如果启用了[半精度]则为[(half_precision)]，反之则为空\n{face_enhance} - 同上，如果启用了[面部增强]则为[(face_enhance)]\n{tta} - 同上，如果启用了[TTA模式]则为[(tta)]" )

        sbSizer12.Add( self.outputNamingFormat, 1, wx.ALL|wx.EXPAND, 3 )


        bSizer12.Add( sbSizer12, 3, wx.EXPAND, 5 )


        bSizer12.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        sbSizer8.Add( bSizer12, 0, wx.EXPAND, 5 )


        self.IoSettingsPanel.SetSizer( sbSizer8 )
        self.IoSettingsPanel.Layout()
        sbSizer8.Fit( self.IoSettingsPanel )
        bSizer10.Add( self.IoSettingsPanel, 0, wx.ALL|wx.EXPAND, 3 )

        self.settingsPanel = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.processingSettingsPanel = wx.Panel( self.settingsPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer22 = wx.BoxSizer( wx.HORIZONTAL )

        bSizer14 = wx.BoxSizer( wx.VERTICAL )

        sbSizer71 = wx.StaticBoxSizer( wx.StaticBox( self.processingSettingsPanel, wx.ID_ANY, u"模型" ), wx.VERTICAL )

        self.modelDir = wx.DirPickerCtrl( sbSizer71.GetStaticBox(), wx.ID_ANY, wx.EmptyString, u"选择包含模型文件的文件夹", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE|wx.DIRP_DIR_MUST_EXIST )
        self.modelDir.SetToolTip( u"Real ESRGAN使用的模型所在的文件夹" )

        sbSizer71.Add( self.modelDir, 0, wx.ALL|wx.EXPAND, 3 )

        bSizer15 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText7 = wx.StaticText( sbSizer71.GetStaticBox(), wx.ID_ANY, u"模型名称", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText7.Wrap( -1 )

        bSizer15.Add( self.m_staticText7, 0, wx.ALL, 5 )

        modelNamesChoices = []
        self.modelNames = wx.Choice( sbSizer71.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, modelNamesChoices, 0 )
        self.modelNames.SetSelection( 0 )
        self.modelNames.SetToolTip( u"自动扫描模型文件夹生成的可用模型列表" )

        bSizer15.Add( self.modelNames, 1, wx.ALIGN_CENTER, 5 )


        bSizer15.Add( ( 0, 0), 0, wx.ALL, 2 )

        self.m_button20 = wx.Button( sbSizer71.GetStaticBox(), wx.ID_ANY, u"刷新模型列表", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_button20.SetToolTip( u"重新扫描模型文件夹并生成可用模型列表" )

        bSizer15.Add( self.m_button20, 0, wx.ALIGN_CENTER, 0 )


        sbSizer71.Add( bSizer15, 0, wx.EXPAND, 5 )


        bSizer14.Add( sbSizer71, 0, wx.EXPAND, 5 )

        bSizer21 = wx.BoxSizer( wx.HORIZONTAL )

        sbSizer10 = wx.StaticBoxSizer( wx.StaticBox( self.processingSettingsPanel, wx.ID_ANY, u"单元(Tile)大小" ), wx.VERTICAL )

        self.tileSize = wx.SpinCtrl( self.processingSettingsPanel, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL|wx.SP_ARROW_KEYS, 0, 10000, 0 )
        self.tileSize.SetToolTip( u"在处理时将图片分为 N * N 大小的多个子图片分步处理，以降低显存占用。对于Vulkan模式，0代表自动选择。对于Python模式，0代表不进行分割，这将在显存不足时出现错误" )

        sbSizer10.Add( self.tileSize, 0, wx.EXPAND, 5 )


        bSizer21.Add( sbSizer10, 1, wx.EXPAND, 5 )

        self.resetConfigBtn = wx.Button( self.processingSettingsPanel, wx.ID_ANY, u"重置配置", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.resetConfigBtn.SetToolTip( u"重置设置面板" )

        bSizer21.Add( self.resetConfigBtn, 0, wx.ALIGN_BOTTOM|wx.ALL, 3 )


        bSizer14.Add( bSizer21, 0, wx.EXPAND, 5 )


        bSizer22.Add( bSizer14, 2, wx.EXPAND, 5 )


        bSizer22.Add( ( 0, 0), 0, wx.ALL, 4 )

        self.pythonSpecificPanel = wx.Panel( self.processingSettingsPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.pythonSpecificPanel.Hide()
        self.pythonSpecificPanel.SetMaxSize( wx.Size( 220,-1 ) )

        sbSizer81 = wx.StaticBoxSizer( wx.StaticBox( self.pythonSpecificPanel, wx.ID_ANY, u"Python脚本特有功能" ), wx.VERTICAL )

        gSizer2 = wx.GridSizer( 0, 2, 0, 0 )

        self.m_staticText4 = wx.StaticText( sbSizer81.GetStaticBox(), wx.ID_ANY, u"缩放倍率", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText4.Wrap( -1 )

        gSizer2.Add( self.m_staticText4, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_LEFT|wx.ALL, 5 )

        self.scaleRate = wx.SpinCtrlDouble( sbSizer81.GetStaticBox(), wx.ID_ANY, u"4", wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 100, 4.000000, 0.1 )
        self.scaleRate.SetDigits( 2 )
        self.scaleRate.SetToolTip( u"精确缩放倍率" )

        gSizer2.Add( self.scaleRate, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.EXPAND, 0 )

        self.useFaceEnhance = wx.CheckBox( sbSizer81.GetStaticBox(), wx.ID_ANY, u"面部增强", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.useFaceEnhance.SetToolTip( u"使用" )

        gSizer2.Add( self.useFaceEnhance, 0, wx.ALL, 5 )

        self.useHalfPrecision = wx.CheckBox( sbSizer81.GetStaticBox(), wx.ID_ANY, u"半精度", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer2.Add( self.useHalfPrecision, 0, wx.ALL, 5 )


        sbSizer81.Add( gSizer2, 1, wx.EXPAND, 5 )


        self.pythonSpecificPanel.SetSizer( sbSizer81 )
        self.pythonSpecificPanel.Layout()
        sbSizer81.Fit( self.pythonSpecificPanel )
        bSizer22.Add( self.pythonSpecificPanel, 1, wx.EXPAND, 5 )

        self.ncnnVulkanSpecificPanel = wx.Panel( self.processingSettingsPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.ncnnVulkanSpecificPanel.SetMaxSize( wx.Size( 220,-1 ) )

        sbSizer82 = wx.StaticBoxSizer( wx.StaticBox( self.ncnnVulkanSpecificPanel, wx.ID_ANY, u"NCNN-Vulkan特有功能" ), wx.HORIZONTAL )

        bSizer24 = wx.BoxSizer( wx.VERTICAL )

        sbSizer9 = wx.StaticBoxSizer( wx.StaticBox( sbSizer82.GetStaticBox(), wx.ID_ANY, u"使用的GPU ID" ), wx.VERTICAL )

        self.GpuId = wx.SpinCtrl( self.ncnnVulkanSpecificPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL|wx.SP_ARROW_KEYS, 0, 10000, 0 )
        sbSizer9.Add( self.GpuId, 0, wx.EXPAND, 5 )


        bSizer24.Add( sbSizer9, 1, wx.EXPAND, 5 )

        self.useTtaMode = wx.CheckBox( sbSizer82.GetStaticBox(), wx.ID_ANY, u"TTA模式", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.useTtaMode.SetToolTip( u"TTA(Test-Time Augmentation - 测试时数据增强)以8倍的处理时间换取极少的PSNR(Peak Signal to Noise Ratio - 峰值信噪比)提升 " )

        bSizer24.Add( self.useTtaMode, 0, wx.ALL, 5 )

        self.useVerboseOutput = wx.CheckBox( sbSizer82.GetStaticBox(), wx.ID_ANY, u"详细输出", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.useVerboseOutput.SetToolTip( u"输出更加详细的处理信息" )

        bSizer24.Add( self.useVerboseOutput, 0, wx.ALL, 5 )


        sbSizer82.Add( bSizer24, 1, 0, 5 )


        sbSizer82.Add( ( 0, 0), 0, wx.ALL, 4 )

        sbSizer11 = wx.StaticBoxSizer( wx.StaticBox( sbSizer82.GetStaticBox(), wx.ID_ANY, u"线程数" ), wx.VERTICAL )

        bSizer174 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText8 = wx.StaticText( self.ncnnVulkanSpecificPanel, wx.ID_ANY, u"加载", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText8.Wrap( -1 )

        bSizer174.Add( self.m_staticText8, 0, wx.ALIGN_CENTER|wx.ALL, 2 )

        self.loadingThreadCount = wx.SpinCtrl( self.ncnnVulkanSpecificPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL|wx.SP_ARROW_KEYS, 0, 100, 1 )
        bSizer174.Add( self.loadingThreadCount, 1, 0, 5 )


        sbSizer11.Add( bSizer174, 0, wx.EXPAND, 5 )


        sbSizer11.Add( ( 0, 0), 1, 0, 5 )

        bSizer171 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText81 = wx.StaticText( self.ncnnVulkanSpecificPanel, wx.ID_ANY, u"处理", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText81.Wrap( -1 )

        bSizer171.Add( self.m_staticText81, 0, wx.ALIGN_CENTER|wx.ALL, 2 )

        self.processingThreadCount = wx.SpinCtrl( self.ncnnVulkanSpecificPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL|wx.SP_ARROW_KEYS, 0, 100, 2 )
        bSizer171.Add( self.processingThreadCount, 1, 0, 5 )


        sbSizer11.Add( bSizer171, 0, wx.EXPAND, 5 )


        sbSizer11.Add( ( 0, 0), 1, 0, 5 )

        bSizer172 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText82 = wx.StaticText( self.ncnnVulkanSpecificPanel, wx.ID_ANY, u"保存", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText82.Wrap( -1 )

        bSizer172.Add( self.m_staticText82, 0, wx.ALIGN_CENTER|wx.ALL, 2 )

        self.savingThreadCount = wx.SpinCtrl( self.ncnnVulkanSpecificPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL|wx.SP_ARROW_KEYS, 0, 100, 2 )
        bSizer172.Add( self.savingThreadCount, 1, 0, 5 )


        sbSizer11.Add( bSizer172, 0, wx.EXPAND, 5 )


        sbSizer82.Add( sbSizer11, 1, wx.EXPAND, 5 )


        self.ncnnVulkanSpecificPanel.SetSizer( sbSizer82 )
        self.ncnnVulkanSpecificPanel.Layout()
        sbSizer82.Fit( self.ncnnVulkanSpecificPanel )
        bSizer22.Add( self.ncnnVulkanSpecificPanel, 1, wx.EXPAND, 5 )


        bSizer22.Add( ( 0, 0), 0, wx.ALL, 4 )

        sbSizer18 = wx.StaticBoxSizer( wx.StaticBox( self.processingSettingsPanel, wx.ID_ANY, u"程序控制" ), wx.VERTICAL )

        self.startProcBtn = wx.Button( sbSizer18.GetStaticBox(), wx.ID_ANY, u"开始处理", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.startProcBtn.SetToolTip( u"启动Real ESRGAN处理进程" )

        sbSizer18.Add( self.startProcBtn, 0, wx.ALL, 3 )

        self.killProcBtn = wx.Button( sbSizer18.GetStaticBox(), wx.ID_ANY, u"结束进程", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.killProcBtn.Enable( False )
        self.killProcBtn.SetToolTip( u"强制结束Real ESRGAN处理进程" )

        sbSizer18.Add( self.killProcBtn, 0, wx.ALL, 3 )


        sbSizer18.Add( ( 0, 0), 1, 0, 5 )


        bSizer22.Add( sbSizer18, 0, wx.EXPAND, 5 )


        self.processingSettingsPanel.SetSizer( bSizer22 )
        self.processingSettingsPanel.Layout()
        bSizer22.Fit( self.processingSettingsPanel )
        self.settingsPanel.AddPage( self.processingSettingsPanel, u"转换质量和处理设置", True )
        self.m_panel8 = wx.Panel( self.settingsPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer24 = wx.BoxSizer( wx.HORIZONTAL )

        sbSizer14 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel8, wx.ID_ANY, u"程序控制(Runner)" ), wx.VERTICAL )

        self.ignoreMessageException = wx.CheckBox( sbSizer14.GetStaticBox(), wx.ID_ANY, u"忽略消息处理异常", wx.DefaultPosition, wx.DefaultSize, 0 )
        sbSizer14.Add( self.ignoreMessageException, 0, wx.ALL|wx.EXPAND, 5 )


        bSizer24.Add( sbSizer14, 0, 0, 5 )


        self.m_panel8.SetSizer( bSizer24 )
        self.m_panel8.Layout()
        bSizer24.Fit( self.m_panel8 )
        self.settingsPanel.AddPage( self.m_panel8, u"高级设置", False )

        bSizer10.Add( self.settingsPanel, 0, wx.ALL|wx.EXPAND, 3 )

        self.cmdPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        cmdSizer = wx.BoxSizer( wx.HORIZONTAL )


        cmdSizer.Add( ( 0, 0), 0, wx.ALL, 3 )

        self.cmdMode = wx.StaticText( self.cmdPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.cmdMode.Wrap( -1 )

        cmdSizer.Add( self.cmdMode, 0, wx.ALIGN_CENTER, 5 )

        self.cmdText = wx.TextCtrl( self.cmdPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTER|wx.TE_READONLY )
        self.cmdText.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
        self.cmdText.SetToolTip( u"点击[开始处理]时运行的命令行" )

        cmdSizer.Add( self.cmdText, 1, wx.ALL, 5 )

        self.m_button19 = wx.Button( self.cmdPanel, wx.ID_ANY, u"强制切换模式", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_button19.SetToolTip( u"强制切换可执行文件模式，在错误的模式下无法启动程序" )

        cmdSizer.Add( self.m_button19, 0, wx.ALIGN_CENTER, 5 )


        cmdSizer.Add( ( 0, 0), 0, wx.ALL, 3 )


        self.cmdPanel.SetSizer( cmdSizer )
        self.cmdPanel.Layout()
        cmdSizer.Fit( self.cmdPanel )
        bSizer10.Add( self.cmdPanel, 0, wx.EXPAND, 5 )

        self.processingProgress = wx.Gauge( self, wx.ID_ANY, 10000, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL|wx.GA_SMOOTH )
        self.processingProgress.SetValue( 0 )
        self.processingProgress.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
        self.processingProgress.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

        bSizer10.Add( self.processingProgress, 0, wx.ALL|wx.EXPAND, 5 )

        self.programOutput = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY )
        self.programOutput.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Verdana" ) )
        self.programOutput.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

        bSizer10.Add( self.programOutput, 1, wx.ALL|wx.EXPAND, 5 )


        self.SetSizer( bSizer10 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind( wx.EVT_CLOSE, self.exit )
        self.Bind( wx.EVT_SIZE, self.resize_image )
        self.selectExecutableFile.Bind( wx.EVT_BUTTON, self.select_executable_file )
        self.downloadFile.Bind( wx.EVT_BUTTON, self.download_file )
        self.outputPath.Bind( wx.EVT_TEXT_ENTER, self.refresh_interface )
        self.m_button1.Bind( wx.EVT_BUTTON, self.select_input_file )
        self.m_button41.Bind( wx.EVT_BUTTON, self.select_input_dir )
        self.m_button11.Bind( wx.EVT_BUTTON, self.select_output_dir )
        self.m_button4.Bind( wx.EVT_BUTTON, self.regen_output_path )
        self.savingFormat.Bind( wx.EVT_COMBOBOX, self.regen_output_path )
        self.outputNamingFormat.Bind( wx.EVT_TEXT_ENTER, self.regen_output_path )
        self.modelDir.Bind( wx.EVT_DIRPICKER_CHANGED, self.regen_model_list )
        self.modelNames.Bind( wx.EVT_CHOICE, self.regen_output_path )
        self.m_button20.Bind( wx.EVT_BUTTON, self.regen_model_list )
        self.tileSize.Bind( wx.EVT_SPINCTRL, self.check_tile_size )
        self.resetConfigBtn.Bind( wx.EVT_BUTTON, self.reset_config )
        self.scaleRate.Bind( wx.EVT_SPINCTRLDOUBLE, self.regen_output_path )
        self.useFaceEnhance.Bind( wx.EVT_CHECKBOX, self.refresh_interface )
        self.useHalfPrecision.Bind( wx.EVT_CHECKBOX, self.refresh_interface )
        self.useTtaMode.Bind( wx.EVT_CHECKBOX, self.regen_output_path )
        self.useVerboseOutput.Bind( wx.EVT_CHECKBOX, self.refresh_interface )
        self.loadingThreadCount.Bind( wx.EVT_SPINCTRL, self.refresh_interface )
        self.processingThreadCount.Bind( wx.EVT_SPINCTRL, self.refresh_interface )
        self.savingThreadCount.Bind( wx.EVT_SPINCTRL, self.refresh_interface )
        self.startProcBtn.Bind( wx.EVT_BUTTON, self.start_proc )
        self.killProcBtn.Bind( wx.EVT_BUTTON, self.kill_proc )
        self.m_button19.Bind( wx.EVT_BUTTON, self.force_switch_cmd_mode )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def exit( self, event ):
        event.Skip()

    def resize_image( self, event ):
        event.Skip()

    def select_executable_file( self, event ):
        event.Skip()

    def download_file( self, event ):
        event.Skip()

    def refresh_interface( self, event ):
        event.Skip()

    def select_input_file( self, event ):
        event.Skip()

    def select_input_dir( self, event ):
        event.Skip()

    def select_output_dir( self, event ):
        event.Skip()

    def regen_output_path( self, event ):
        event.Skip()



    def regen_model_list( self, event ):
        event.Skip()



    def check_tile_size( self, event ):
        event.Skip()

    def reset_config( self, event ):
        event.Skip()









    def start_proc( self, event ):
        event.Skip()

    def kill_proc( self, event ):
        event.Skip()

    def force_switch_cmd_mode( self, event ):
        event.Skip()


###########################################################################
## Class DownloaderFrame
###########################################################################

class DownloaderFrame ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 760,502 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )


        self.Centre( wx.BOTH )

    def __del__( self ):
        pass


