###############################################################################
# Name: piece.py                                                            #
# Purpose: GUI library utilities.                                               # 
###############################################################################

# import xyView
from xyView.constant import *

class MessageDialog(wx.MessageDialog):
    
    def __init__(self, parent=None, message="Message", caption=wx.MessageBoxCaptionStr, style=wx.OK|wx.CANCEL|wx.CENTRE, name=wx.DialogNameStr, pos=wx.DefaultPosition, size=wx.DefaultSize, backColour=None, *args, **kwargs):

        wx.MessageDialog.__init__(self, parent=parent, message=message, caption=caption,  style=style, *args, **kwargs)
        self.parent = parent
        
        if backColour == None:
            backColour = self.getDefaultBackColour()
        self.SetBackgroundColour(backColour)
    
    @classmethod
    def getDefaultBackColour(cls):
        return DEFAULT_BACKGROUND_COLOR


class Dialog(wx.Dialog):
    
    def __init__(self, parent=None, id=-1, title="Dialog", pos=wx.DefaultPosition, size=wx.DefaultSize, style=wx.DEFAULT_DIALOG_STYLE, name=wx.DialogNameStr, backColour=None, *args, **kwargs):
        wx.Dialog.__init__(self, parent=parent, id=id, title=title, pos=pos, size=size, style=style, name=name, *args, **kwargs)

        self.parent = parent
        
        if backColour == None:
            backColour = self.getDefaultBackColour()
        self.SetBackgroundColour(backColour)
    
    @classmethod
    def getDefaultBackColour(cls):
        return DEFAULT_BACKGROUND_COLOR

    


class UIPieces(object):
    """
    An abstract class.   GUI library utilities
    """
    __instance = None

    def __init__(self, 
                 name="GUI Piece", 
                 info = {},
                 *args, **kwargs):
        self.name = name
        self.info = info
        self.log = None
        self.backColour = DEFAULT_BACKGROUND_COLOR
#         self.caption = xyView.__product__
#         self.backColour = self.getDefaultBackColour()

    # ----------------------------------------------------------
    # UI piece
    # ----------------------------------------------------------
    @classmethod
    def getDefaultBackColour(cls):
        return DEFAULT_BACKGROUND_COLOR
    
    def set_log(self, log):
        self.log = log
    
    def show_message(self, msg):
        if self.log:
            self.log.WriteText(msg)
        else:
            print (msg)
    
    def file_dir(self, panel, sizer, button, label, id=-1, txt=''):
#        print "panel = ", panel
#        print "sizer = ", sizer
#        sizer = wx.FlexGridSizer(cols=2, hgap=10, vgap=5) 
        
        label_to = wx.StaticText(panel, -1, label)
        
        sizer_to = wx.BoxSizer(wx.HORIZONTAL)
        txt_to = wx.TextCtrl(panel, -1, txt, size=(250, -1))
        bt_to = wx.Button(panel, id, "..", size=(20, 20))
        
        panel.Bind(wx.EVT_BUTTON, button, bt_to)
        sizer_to.Add(txt_to, flag=wx.ALL, border=0)
        sizer_to.Add(bt_to, flag=wx.ALL, border=1)

        sizer.Add(label_to, 0, wx.ALIGN_RIGHT|wx.CENTER, 5 )
        sizer.Add(sizer_to, 0, wx.ALIGN_LEFT|wx.CENTER, 5)

        return txt_to
    # ----------------------------------------------------------
    # dialog
    # ----------------------------------------------------------

    def dialog_choice(self, parent=None, msg='List of Choice', name='Single Choice Dialog', lst=['nothing'], log=None):
        selection = False
        dlg = wx.SingleChoiceDialog(parent, msg, name, lst, wx.CHOICEDLG_STYLE)
        dlg.SetBackgroundColour(self.backColour)
        if dlg.ShowModal() == wx.ID_OK:
            selection = dlg.GetStringSelection()
            msg = 'selection: -> %s\n' % selection
            self.show_message(msg)
            
        dlg.Destroy()
        return selection

    def dialog_multi_choice(self, parent=None, msg='List of Choice', name='MultiChoice Dialog', lst=['nothing'], log=None):
        selections = False
        dlg = wx.MultiChoiceDialog(parent, msg, name, lst)
        dlg.SetBackgroundColour(self.backColour)
        if (dlg.ShowModal() == wx.ID_OK):
            selections = dlg.GetSelections()
            strings = [lst[x] for x in selections]
            msg = "Selections: -> %s\n" % (strings)
            self.show_message(msg)
            
        dlg.Destroy()
        return strings

    
    def dialog_info(self, msg, caption='Information'):
        dlg = MessageDialog(None, msg, caption, wx.OK|wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()      
    
    def dialog_error(self, msg, caption="Error Occur"):
        dlg = MessageDialog(None, msg, caption, wx.OK|wx.ICON_ERROR|wx.STAY_ON_TOP)
        dlg.ShowModal()
        dlg.Destroy()      
    
    def dialog_question(self, msg, caption='Question'):
        ans = False
        dlg = MessageDialog(None, msg, caption, wx.YES_NO|wx.ICON_EXCLAMATION|wx.STAY_ON_TOP)
    
        val = dlg.ShowModal()
    
        if val == wx.ID_YES:
            ans = True
        else:
            ans = False
    
        dlg.Destroy()
        return ans
    
    
    def dialog_message(self, msg, caption=None):
        import  wx.lib.dialogs
    
        if not caption:
            caption = self.caption
            
        dlg = wx.lib.dialogs.ScrolledMessageDialog(None, msg, caption, size=(400,600))
        dlg.ShowModal()
    

    # ----------------------------------------------------------
    #  info
    # ----------------------------------------------------------
    
    
    
UI_PIECE = UIPieces()

if __name__ == '__main__':
    
    app = wx.App(redirect=True)   # Error messages go to popup window
    UI_PIECE.show_question_dialog(msg="msg\n\nmsg", caption="Message")
#    top = wx.Frame(None, title="Hello World", size=(300,200))
#    top.Show()
    app.MainLoop()


