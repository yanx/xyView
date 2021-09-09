import os
import wx
import wx.adv
import wx.lib.mixins.inspection
from wx.adv import SplashScreen as SplashScreen
from xyView.base.aui_example import MainAUI

#---------------------------------------------------------------------------


class Log:
    def WriteText(self, text):
        if text[-1:] == '\n':
            text = text[:-1]
        wx.LogMessage(text)
    write = WriteText


class MySplashScreen(SplashScreen):
    def __init__(self):
        bmp = wx.Image("whimlogo.png").ConvertToBitmap()
        SplashScreen.__init__(self, bmp,
                                 wx.adv.SPLASH_CENTRE_ON_SCREEN | wx.adv.SPLASH_TIMEOUT,
                                 5000, None, -1)
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        self.fc = wx.CallLater(2000, self.ShowMain)


    def OnClose(self, evt):
        # Make sure the default handler runs too so this window gets
        # destroyed
        evt.Skip()
        self.Hide()

        # if the timer is still running then go ahead and show the
        # main frame now
        if self.fc.IsRunning():
            self.fc.Stop()
            self.ShowMain()


    def ShowMain(self):
        
        MainAUI(None, Log())
#         frame = AuiFrame(None)
#         frame.Show()
#         if self.fc.IsRunning():
#             self.Raise()
# #         wx.CallAfter(frame.ShowTip)


#---------------------------------------------------------------------------

class MyApp(wx.App, wx.lib.mixins.inspection.InspectionMixin):
    def OnInit(self):

        self.InitInspection()  # for the InspectionMixin base class
        wx.SystemOptions.SetOption("mac.window-plain-transition", 1)
        self.SetAppName("xyView Base Frame")
        splash = MySplashScreen()
        splash.Show()
        return True

#---------------------------------------------------------------------------

def main():
    try:
        demoPath = os.path.dirname(__file__)
        os.chdir(demoPath)
    except:
        pass
    app = MyApp(False)
    app.MainLoop()

#---------------------------------------------------------------------------

#----------------------------------------------------------------------------

if __name__ == '__main__':
    main()


#----------------------------------------------------------------------------
