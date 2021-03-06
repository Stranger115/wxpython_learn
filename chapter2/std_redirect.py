#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/22 15:19
# @Author  : xuqiuying
# @FileName: std_redirect.py

#!/usr/bin/env python
import wx
import sys

class Frame(wx.Frame):
    def __init__(self, parent, id, title):
        print 'Frame __init__'
        wx.Frame.__init__(self, parent, id, title, size=(300, 100))
        panel = wx.Panel(self, -1)
        button = wx.Button(panel, -1, "Close", pos=(130, 15), size=(40, 40))

        # (event, handler, source=None, id=wx.ID_ANY, id2=wx.ID_ANY)
        # source 是产生该事件的源窗口部件 在触发事件的窗口部件与用作事件处理器的窗口部件不相同时使用
        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)  # 1 绑定框架关闭事件
        self.Bind(wx.EVT_BUTTON, self.OnCloseMe, button)  # 2 绑定按钮事件

    def OnCloseMe(self, event):
        self.Close(True)

    def OnCloseWindow(self, event):
        self.Destroy()


class App(wx.App):
    def __init__(self, redirect=True, filename=None):
        print 'App __init__'
        wx.App.__init__(self, redirect, filename)
    # 初始化时调用
    def OnInit(self):
        print 'OnInit'  # 输出到stdout
        self.frame = Frame(parent=None, id=-1, title='Startup') # 创建框架
        self.frame.Show()
        self.SetTopWindow(self.frame)
        print >> sys.stderr, 'A pretend error message'  # 输出到stderr
        return True

    # 最后一个窗口被关闭后调用
    def OnExit(self):
        print 'OnExit'
        # False: 最后窗口被关闭后wxPython程序应仍可运行
        self.SetExitOnFrameDelete(False)
        wx.Exit()


if __name__ == '__main__':
    # 当在重定向开始以后到主事件结束这段时间出现print
    # redirect: False 输出到python控制台
    # redirect: True 默认值则 输出到wxPython窗口中
    app = App(False)  # 文本重定向从这开始
    print 'before MainLoop'
    app.MainLoop()  # 进入主事件循环
    print 'after MainLoop'