# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.0-4761b0c)
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

        self.SetSizeHints( wx.Size( 755,650 ), wx.Size( 755,650 ) )
        self.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
        self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

        bSizer10 = wx.BoxSizer( wx.VERTICAL )

        sbSizer6 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"核心程序" ), wx.VERTICAL )

        bSizer3611 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText1811 = wx.StaticText( sbSizer6.GetStaticBox(), wx.ID_ANY, u"可执行文件(.exe或.py)路径", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
        self.m_staticText1811.Wrap( -1 )

        bSizer3611.Add( self.m_staticText1811, 1, wx.ALIGN_CENTER, 0 )

        self.executableFilePath = wx.TextCtrl( sbSizer6.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
        bSizer3611.Add( self.executableFilePath, 5, wx.ALL|wx.EXPAND, 5 )

        self.selectExecutableFile = wx.Button( sbSizer6.GetStaticBox(), wx.ID_ANY, u"选择可执行文件", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer3611.Add( self.selectExecutableFile, 1, wx.ALIGN_CENTER, 5 )


        sbSizer6.Add( bSizer3611, 1, wx.ALL|wx.EXPAND, 5 )


        bSizer10.Add( sbSizer6, 0, wx.ALL|wx.EXPAND, 5 )

        self.IoSettingsPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        sbSizer8 = wx.StaticBoxSizer( wx.StaticBox( self.IoSettingsPanel, wx.ID_ANY, u"输入和输出设置" ), wx.VERTICAL )

        bSizer9 = wx.BoxSizer( wx.VERTICAL )

        bSizer36 = wx.BoxSizer( wx.HORIZONTAL )

        bSizer3 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText18 = wx.StaticText( sbSizer8.GetStaticBox(), wx.ID_ANY, u"输入路径", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText18.Wrap( -1 )

        bSizer3.Add( self.m_staticText18, 0, wx.ALIGN_CENTER|wx.ALL, 0 )

        self.m_staticText2 = wx.StaticText( sbSizer8.GetStaticBox(), wx.ID_ANY, u"（文件或文件夹）", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )

        bSizer3.Add( self.m_staticText2, 0, wx.ALIGN_CENTER|wx.ALL, 0 )


        bSizer36.Add( bSizer3, 1, 0, 0 )

        self.inputPath = wx.TextCtrl( sbSizer8.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
        bSizer36.Add( self.inputPath, 5, wx.ALL|wx.EXPAND, 5 )

        gSizer1 = wx.GridSizer( 0, 2, 0, 0 )

        self.m_button1 = wx.Button( sbSizer8.GetStaticBox(), wx.ID_ANY, u"选择文件", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer1.Add( self.m_button1, 0, wx.ALIGN_CENTER, 5 )

        self.m_button41 = wx.Button( sbSizer8.GetStaticBox(), wx.ID_ANY, u"选择文件夹", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer1.Add( self.m_button41, 0, wx.ALIGN_CENTER, 5 )


        bSizer36.Add( gSizer1, 1, wx.EXPAND, 5 )


        bSizer9.Add( bSizer36, 0, wx.EXPAND, 5 )

        bSizer361 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText181 = wx.StaticText( sbSizer8.GetStaticBox(), wx.ID_ANY, u"输出路径", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
        self.m_staticText181.Wrap( -1 )

        bSizer361.Add( self.m_staticText181, 1, wx.ALIGN_CENTER, 0 )

        self.outputPath = wx.TextCtrl( sbSizer8.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
        bSizer361.Add( self.outputPath, 5, wx.ALL|wx.EXPAND, 5 )

        self.m_button11 = wx.Button( sbSizer8.GetStaticBox(), wx.ID_ANY, u"选择文件夹", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer361.Add( self.m_button11, 1, wx.ALIGN_CENTER, 5 )


        bSizer9.Add( bSizer361, 0, wx.EXPAND, 5 )

        bSizer12 = wx.BoxSizer( wx.HORIZONTAL )

        bSizer13 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_panel4 = wx.Panel( sbSizer8.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.m_panel4.Enable( False )
        self.m_panel4.Hide()

        sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel4, wx.ID_ANY, u"文件夹内自动选择的文件格式(:分隔)" ), wx.VERTICAL )

        self.autoSelectedFormat = wx.TextCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, u"png:jpg:jpeg:tif:tiff:bmp:tga", wx.DefaultPosition, wx.DefaultSize, 0 )
        sbSizer2.Add( self.autoSelectedFormat, 1, wx.ALL|wx.EXPAND, 3 )


        self.m_panel4.SetSizer( sbSizer2 )
        self.m_panel4.Layout()
        sbSizer2.Fit( self.m_panel4 )
        bSizer13.Add( self.m_panel4, 0, wx.EXPAND, 5 )

        sbSizer21 = wx.StaticBoxSizer( wx.StaticBox( sbSizer8.GetStaticBox(), wx.ID_ANY, u"输出文件格式" ), wx.VERTICAL )

        savingFormatChoices = [ u"同输入", u".png", u".jpg", u".webp" ]
        self.savingFormat = wx.ComboBox( sbSizer21.GetStaticBox(), wx.ID_ANY, u"png", wx.DefaultPosition, wx.DefaultSize, savingFormatChoices, 0 )
        self.savingFormat.SetSelection( 0 )
        sbSizer21.Add( self.savingFormat, 0, wx.ALL|wx.EXPAND, 5 )


        bSizer13.Add( sbSizer21, 1, wx.EXPAND, 5 )


        bSizer13.Add( ( 0, 0), 0, wx.ALL, 5 )

        sbSizer12 = wx.StaticBoxSizer( wx.StaticBox( sbSizer8.GetStaticBox(), wx.ID_ANY, u"输出文件命名规则" ), wx.VERTICAL )

        self.outputNamingFormat = wx.TextCtrl( sbSizer12.GetStaticBox(), wx.ID_ANY, u"{orig_name}({model_name})({scale}){tta}", wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
        self.outputNamingFormat.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Segoe UI" ) )

        sbSizer12.Add( self.outputNamingFormat, 1, wx.ALL|wx.EXPAND, 3 )


        bSizer13.Add( sbSizer12, 4, wx.EXPAND, 5 )


        bSizer12.Add( bSizer13, 1, wx.EXPAND, 5 )


        bSizer12.Add( ( 0, 0), 1, wx.ALL, 5 )

        self.m_button4 = wx.Button( sbSizer8.GetStaticBox(), wx.ID_ANY, u"重新生成输出路径", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer12.Add( self.m_button4, 0, 0, 5 )


        bSizer9.Add( bSizer12, 1, wx.EXPAND, 5 )


        sbSizer8.Add( bSizer9, 0, wx.EXPAND, 5 )


        self.IoSettingsPanel.SetSizer( sbSizer8 )
        self.IoSettingsPanel.Layout()
        sbSizer8.Fit( self.IoSettingsPanel )
        bSizer10.Add( self.IoSettingsPanel, 1, wx.EXPAND |wx.ALL, 5 )

        self.processingSettingsPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        sbSizer7 = wx.StaticBoxSizer( wx.StaticBox( self.processingSettingsPanel, wx.ID_ANY, u"转换质量和处理设置" ), wx.HORIZONTAL )

        bSizer14 = wx.BoxSizer( wx.VERTICAL )

        sbSizer71 = wx.StaticBoxSizer( wx.StaticBox( sbSizer7.GetStaticBox(), wx.ID_ANY, u"模型" ), wx.VERTICAL )

        self.modelDir = wx.DirPickerCtrl( sbSizer71.GetStaticBox(), wx.ID_ANY, wx.EmptyString, u"选择包含模型文件的文件夹", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
        sbSizer71.Add( self.modelDir, 0, wx.ALL, 3 )

        bSizer15 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText7 = wx.StaticText( sbSizer71.GetStaticBox(), wx.ID_ANY, u"模型名称", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText7.Wrap( -1 )

        bSizer15.Add( self.m_staticText7, 0, wx.ALL, 5 )

        modelNamesChoices = []
        self.modelNames = wx.Choice( sbSizer71.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, modelNamesChoices, 0 )
        self.modelNames.SetSelection( 0 )
        bSizer15.Add( self.modelNames, 1, wx.ALIGN_CENTER, 5 )


        sbSizer71.Add( bSizer15, 1, wx.EXPAND, 5 )


        bSizer14.Add( sbSizer71, 0, wx.EXPAND, 5 )

        sbSizer10 = wx.StaticBoxSizer( wx.StaticBox( sbSizer7.GetStaticBox(), wx.ID_ANY, u"单元(Tile)大小" ), wx.VERTICAL )

        self.tileSize = wx.SpinCtrl( self.processingSettingsPanel, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL|wx.SP_ARROW_KEYS, 0, 10000, 0 )
        sbSizer10.Add( self.tileSize, 0, wx.EXPAND, 5 )


        bSizer14.Add( sbSizer10, 0, wx.EXPAND, 5 )


        sbSizer7.Add( bSizer14, 0, wx.EXPAND, 5 )


        sbSizer7.Add( ( 0, 0), 0, wx.ALL, 5 )

        self.pythonSpecificPanel = wx.Panel( sbSizer7.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        sbSizer81 = wx.StaticBoxSizer( wx.StaticBox( self.pythonSpecificPanel, wx.ID_ANY, u"Python脚本特有功能" ), wx.VERTICAL )

        gSizer2 = wx.GridSizer( 0, 2, 0, 0 )

        self.m_staticText4 = wx.StaticText( sbSizer81.GetStaticBox(), wx.ID_ANY, u"缩放倍率", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText4.Wrap( -1 )

        gSizer2.Add( self.m_staticText4, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_LEFT|wx.ALL, 5 )

        self.scaleRate = wx.SpinCtrlDouble( sbSizer81.GetStaticBox(), wx.ID_ANY, u"4", wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 100, 4.000000, 0.1 )
        self.scaleRate.SetDigits( 2 )
        gSizer2.Add( self.scaleRate, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.useFaceEnhance = wx.CheckBox( sbSizer81.GetStaticBox(), wx.ID_ANY, u"面部增强", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer2.Add( self.useFaceEnhance, 0, wx.ALL, 5 )

        self.useHalfPrecision = wx.CheckBox( sbSizer81.GetStaticBox(), wx.ID_ANY, u"半精度", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer2.Add( self.useHalfPrecision, 0, wx.ALL, 5 )


        sbSizer81.Add( gSizer2, 1, wx.EXPAND, 5 )


        self.pythonSpecificPanel.SetSizer( sbSizer81 )
        self.pythonSpecificPanel.Layout()
        sbSizer81.Fit( self.pythonSpecificPanel )
        sbSizer7.Add( self.pythonSpecificPanel, 0, wx.EXPAND, 5 )


        sbSizer7.Add( ( 0, 0), 0, wx.ALL, 5 )

        self.ncnnVulkanSpecificPanel = wx.Panel( sbSizer7.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        sbSizer82 = wx.StaticBoxSizer( wx.StaticBox( self.ncnnVulkanSpecificPanel, wx.ID_ANY, u"NCNN-Vulkan特有功能" ), wx.HORIZONTAL )

        bSizer24 = wx.BoxSizer( wx.VERTICAL )

        bSizer16 = wx.BoxSizer( wx.HORIZONTAL )

        sbSizer9 = wx.StaticBoxSizer( wx.StaticBox( sbSizer82.GetStaticBox(), wx.ID_ANY, u"使用的GPU ID" ), wx.VERTICAL )

        self.GpuId = wx.SpinCtrl( self.ncnnVulkanSpecificPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL|wx.SP_ARROW_KEYS, 0, 10000, 0 )
        sbSizer9.Add( self.GpuId, 0, wx.EXPAND, 5 )


        bSizer16.Add( sbSizer9, 0, wx.EXPAND, 5 )


        bSizer16.Add( ( 0, 0), 0, wx.ALL, 5 )


        bSizer24.Add( bSizer16, 0, wx.EXPAND, 5 )

        self.useTtaMode = wx.CheckBox( sbSizer82.GetStaticBox(), wx.ID_ANY, u"TTA模式", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer24.Add( self.useTtaMode, 0, wx.ALL, 5 )

        self.useVerboseOutput = wx.CheckBox( sbSizer82.GetStaticBox(), wx.ID_ANY, u"详细输出", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer24.Add( self.useVerboseOutput, 0, wx.ALL, 5 )


        sbSizer82.Add( bSizer24, 1, wx.EXPAND, 5 )

        sbSizer11 = wx.StaticBoxSizer( wx.StaticBox( sbSizer82.GetStaticBox(), wx.ID_ANY, u"线程数" ), wx.VERTICAL )

        bSizer17 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText8 = wx.StaticText( self.ncnnVulkanSpecificPanel, wx.ID_ANY, u"加载", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText8.Wrap( -1 )

        bSizer17.Add( self.m_staticText8, 0, wx.ALIGN_CENTER|wx.ALL, 2 )

        self.loadingThreadCount = wx.SpinCtrl( self.ncnnVulkanSpecificPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL|wx.SP_ARROW_KEYS, 0, 100, 1 )
        bSizer17.Add( self.loadingThreadCount, 0, 0, 5 )


        sbSizer11.Add( bSizer17, 0, wx.EXPAND, 5 )


        sbSizer11.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        bSizer171 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText81 = wx.StaticText( self.ncnnVulkanSpecificPanel, wx.ID_ANY, u"处理", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText81.Wrap( -1 )

        bSizer171.Add( self.m_staticText81, 0, wx.ALIGN_CENTER|wx.ALL, 2 )

        self.processingThreadCount = wx.SpinCtrl( self.ncnnVulkanSpecificPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL|wx.SP_ARROW_KEYS, 0, 100, 2 )
        bSizer171.Add( self.processingThreadCount, 0, 0, 5 )


        sbSizer11.Add( bSizer171, 0, wx.EXPAND, 5 )


        sbSizer11.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        bSizer172 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText82 = wx.StaticText( self.ncnnVulkanSpecificPanel, wx.ID_ANY, u"保存", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText82.Wrap( -1 )

        bSizer172.Add( self.m_staticText82, 0, wx.ALIGN_CENTER|wx.ALL, 2 )

        self.savingThreadCount = wx.SpinCtrl( self.ncnnVulkanSpecificPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL|wx.SP_ARROW_KEYS, 0, 100, 2 )
        bSizer172.Add( self.savingThreadCount, 0, 0, 5 )


        sbSizer11.Add( bSizer172, 0, wx.EXPAND, 5 )


        sbSizer82.Add( sbSizer11, 0, wx.EXPAND, 5 )


        self.ncnnVulkanSpecificPanel.SetSizer( sbSizer82 )
        self.ncnnVulkanSpecificPanel.Layout()
        sbSizer82.Fit( self.ncnnVulkanSpecificPanel )
        sbSizer7.Add( self.ncnnVulkanSpecificPanel, 0, wx.EXPAND, 5 )


        sbSizer7.Add( ( 0, 0), 0, wx.ALL, 5 )

        sbSizer18 = wx.StaticBoxSizer( wx.StaticBox( sbSizer7.GetStaticBox(), wx.ID_ANY, u"程序控制" ), wx.VERTICAL )

        self.startProcBtn = wx.Button( sbSizer18.GetStaticBox(), wx.ID_ANY, u"开始处理", wx.DefaultPosition, wx.DefaultSize, 0 )
        sbSizer18.Add( self.startProcBtn, 0, wx.ALL, 3 )

        self.killProcBtn = wx.Button( sbSizer18.GetStaticBox(), wx.ID_ANY, u"结束进程", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.killProcBtn.Enable( False )

        sbSizer18.Add( self.killProcBtn, 0, wx.ALL, 3 )

        self.m_staticline1 = wx.StaticLine( sbSizer18.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        sbSizer18.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )

        self.resetConfigBtn = wx.Button( sbSizer18.GetStaticBox(), wx.ID_ANY, u"重置配置", wx.DefaultPosition, wx.DefaultSize, 0 )
        sbSizer18.Add( self.resetConfigBtn, 0, wx.ALL, 3 )


        sbSizer7.Add( sbSizer18, 0, wx.EXPAND, 5 )


        self.processingSettingsPanel.SetSizer( sbSizer7 )
        self.processingSettingsPanel.Layout()
        sbSizer7.Fit( self.processingSettingsPanel )
        bSizer10.Add( self.processingSettingsPanel, 1, wx.EXPAND |wx.ALL, 5 )

        self.cmdText = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTER|wx.TE_READONLY )
        bSizer10.Add( self.cmdText, 0, wx.ALL|wx.EXPAND, 5 )

        self.processingProgress = wx.Gauge( self, wx.ID_ANY, 10000, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL|wx.GA_SMOOTH )
        self.processingProgress.SetValue( 0 )
        bSizer10.Add( self.processingProgress, 0, wx.ALL|wx.EXPAND, 5 )

        self.programOutput = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY )
        bSizer10.Add( self.programOutput, 1, wx.ALL|wx.EXPAND, 5 )


        self.SetSizer( bSizer10 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind( wx.EVT_CLOSE, self.exit )
        self.Bind( wx.EVT_SIZE, self.resize_image )
        self.selectExecutableFile.Bind( wx.EVT_BUTTON, self.select_executable_file )
        self.m_button1.Bind( wx.EVT_BUTTON, self.select_input_file )
        self.m_button41.Bind( wx.EVT_BUTTON, self.select_input_dir )
        self.outputPath.Bind( wx.EVT_TEXT_ENTER, self.refresh_interface )
        self.m_button11.Bind( wx.EVT_BUTTON, self.select_output_dir )
        self.savingFormat.Bind( wx.EVT_COMBOBOX, self.regen_output_path )
        self.outputNamingFormat.Bind( wx.EVT_TEXT_ENTER, self.regen_output_path )
        self.m_button4.Bind( wx.EVT_BUTTON, self.regen_output_path )
        self.modelDir.Bind( wx.EVT_DIRPICKER_CHANGED, self.regen_model_list )
        self.modelNames.Bind( wx.EVT_CHOICE, self.refresh_interface )
        self.tileSize.Bind( wx.EVT_SPINCTRL, self.check_tile_size )
        self.scaleRate.Bind( wx.EVT_SPINCTRLDOUBLE, self.refresh_interface )
        self.useFaceEnhance.Bind( wx.EVT_CHECKBOX, self.refresh_interface )
        self.useHalfPrecision.Bind( wx.EVT_CHECKBOX, self.refresh_interface )
        self.useTtaMode.Bind( wx.EVT_CHECKBOX, self.refresh_interface )
        self.useVerboseOutput.Bind( wx.EVT_CHECKBOX, self.refresh_interface )
        self.loadingThreadCount.Bind( wx.EVT_SPINCTRL, self.refresh_interface )
        self.processingThreadCount.Bind( wx.EVT_SPINCTRL, self.refresh_interface )
        self.savingThreadCount.Bind( wx.EVT_SPINCTRL, self.refresh_interface )
        self.startProcBtn.Bind( wx.EVT_BUTTON, self.start_proc )
        self.killProcBtn.Bind( wx.EVT_BUTTON, self.kill_proc )
        self.resetConfigBtn.Bind( wx.EVT_BUTTON, self.reset_config )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def exit( self, event ):
        event.Skip()

    def resize_image( self, event ):
        event.Skip()

    def select_executable_file( self, event ):
        event.Skip()

    def select_input_file( self, event ):
        event.Skip()

    def select_input_dir( self, event ):
        event.Skip()

    def refresh_interface( self, event ):
        event.Skip()

    def select_output_dir( self, event ):
        event.Skip()

    def regen_output_path( self, event ):
        event.Skip()



    def regen_model_list( self, event ):
        event.Skip()


    def check_tile_size( self, event ):
        event.Skip()









    def start_proc( self, event ):
        event.Skip()

    def kill_proc( self, event ):
        event.Skip()

    def reset_config( self, event ):
        event.Skip()


