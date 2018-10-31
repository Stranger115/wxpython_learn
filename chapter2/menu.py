#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/22 15:56
# @Author  : xuqiuying
# @FileName: menu.py

import wx


class P(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.SetBackgroundColour('White')


class ToolbarFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'Toolbars',
                          size=(300, 200))
        # panel = wx.Panel(self)
        # panel.SetBackgroundColour('White')
        self.c = [P]
        # 显示被各时间设置的文本
        # 创建状态栏, 宽度与框架相同，高度甴操作系统定
        statusBar = self.CreateStatusBar()
        # 命令按钮容器，自动放置于框架顶部
        toolbar = self.CreateToolBar()  # 2 创建工具栏
        images = wx.Image('../statics/file.png', wx.BITMAP_TYPE_PNG)

        toolbar.AddSimpleTool(wx.NewId(), images.ConvertToBitmap(),
                              'New', 'Long help for "New"')  # 3 给工具栏增加一个工具
        # 工具栏的按钮放置的位置
        toolbar.Realize()  # 4 准备显示工具栏

        menuBar = wx.MenuBar()  # 创建菜单栏
        # 创建两个菜单
        menu1 = wx.Menu()
        menuBar.Append(menu1, '&File')

        menu2 = wx.Menu()
        # 6 创建菜单的项目
        menu2.Append(wx.NewId(), '&Copy', 'Copy in status bar')
        menu2.Append(wx.NewId(), 'C&ut', '')
        menu2.Append(wx.NewId(), 'Paste', '')
        menu2.AppendSeparator()
        menu2.Append(wx.NewId(), '&Options...', 'Display Options')
        menuBar.Append(menu2, '&Edit')  # 在菜单栏上附上菜单
        menu3 = wx.Menu()
        menu3Item = menuBar.Append(menu3, '&Close')


        self.SetMenuBar(menuBar)  # 在框架上附上菜单栏

        self.Bind(wx.EVT_MENU, self.OnCloseMe, menu3Item)

    def OnCloseMe(self, event):
        self.close(True)

if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = ToolbarFrame(parent=None, id=-1)
    frame.Show()
    app.MainLoop()
