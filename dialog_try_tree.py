
import wx

from xyView.tree_old import HyperTreeListDemo
#---------------------------------------------------------------------------

class SamplePane(wx.Panel):
    """
    Just a simple test window to put into the LabelBook.
    """
    def __init__(self, parent, colour, label):

        wx.Panel.__init__(self, parent, style=0)#wx.BORDER_SUNKEN)
        self.SetBackgroundColour(colour)
#         self.SetBackgroundColour(wx.Colour(255,255,255))

        static = wx.StaticText(self, -1, label, pos=(10, 10))
#---------------------------------------------------------------------------


#---------------------------------------------------------------------------
class TestPanelDialog(wx.Dialog):
    def __init__(
            self, parent, id, title, log):

        wx.Dialog.__init__(self)
        self.log = log
        self.Create(parent, id, title, size=wx.DefaultSize, pos=wx.DefaultPosition,
            style=wx.DEFAULT_DIALOG_STYLE, name='dialog')
        # contents
#         panel = SamplePane(self, wx.RED, "try panel in a dialog")
        panel = SamplePane(self, self.log)

#---------------------------------------------------------------------------

class TestLog:
    def WriteText(self, text):
        if text[-1:] == '\n':
            text = text[:-1]
#         wx.LogMessage(text)
        print (text)
    write = WriteText
#---------------------------------------------------------------------------

def main():
    app = wx.App()
    
    win = HyperTreeListDemo(None, TestLog())
    win.Show(True)
    
#     dlg = TestPanelDialog(None, -1,"Testing Panel" ,TestLog())
#     dlg.CenterOnScreen()
#     val = dlg.ShowModal()
#     dlg.Destroy()
    
    app.MainLoop()

#---------------------------------------------------------------------------

#----------------------------------------------------------------------------

if __name__ == '__main__':
    main()


#----------------------------------------------------------------------------
