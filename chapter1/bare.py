#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/22 14:37
# @Author  : xuqiuying
# @FileName: bare.py

import wx
# 可使用bare.__doc__读取该注释
""" a simple wxPython program"""


class Frame(wx.Frame):
    pass


# 每个程序必须有一个app对象和至少一个frame对象
class App(wx.App):  # 子类化wxPython程序
    # 若子类不定义__init__()，则自动调用父类__init()
    def OnInit(self):  # 一个应用程序的初始化方式
        # （parent, id, title）parent:必须，其他为可选参数
        self.frame = Frame(parent=None, title='Bare')
        # frame.show(True)默认参数True, 使frame可见，否则不可见
        # frame.Hide 等同于 frame.show(False)
        self.frame.Show()
        # 设定顶级窗口，（顶级窗口：在其上没有父容器）
        # 若未设定则默认为明确定义的第一个框架为顶级窗口
        self.SetTopWindow(self.frame)
        return True


# 当应用程序启动时OnInit会被wx.App直接调用
app = App()  # 创建一个应用程序的实例

# GUI响应用户的鼠标和键盘事件
app.MainLoop()  # 进入程序的主事件循环