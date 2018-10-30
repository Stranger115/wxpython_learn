#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/22 15:06
# @Author  : xuqiuying
# @FileName: show_picture.py


"""Hello, wxPython! program."""
import wx


class Frame(wx.Frame):  # wx.Frame子类
    """Frame class that displays an image."""

    def __init__(self, image, parent=None, id=-1,
                 pos=wx.DefaultPosition,
                 title='Hello, wxPython!'):  # 图像参数
        """Create a Frame instance and display image."""
        #  图像转位图
        temp = image.ConvertToBitmap()
        # 位图尺寸
        size = temp.GetWidth(), temp.GetHeight()
        # 框架匹配位图尺寸
        wx.Frame.__init__(self, parent, id, title, pos, size)
        # 显示该位图
        self.bmp = wx.StaticBitmap(parent=self, bitmap=temp)


class App(wx.App):  # wx.App子类
    """Application class."""

    def OnInit(self):
        # 图像处理
        image = wx.Image('girl.jpg', wx.BITMAP_TYPE_JPEG)
        self.frame = Frame(image)
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True


def main():  # 7
    app = App()
    app.MainLoop()


if __name__ == '__main__':
    main()
