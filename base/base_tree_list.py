#!/usr/bin/env python
#   Tags: phoenix-port, py3-port

import os
import string

import wx
import wx.lib.colourselect as csel
import wx.lib.colourutils as cutils

import sys

from six import BytesIO

try:
    dirName = os.path.dirname(os.path.abspath(__file__))
except:
    dirName = os.path.dirname(os.path.abspath(sys.argv[0]))

sys.path.append(os.path.split(dirName)[0])

try:
    from agw import hypertreelist as HTL
    bitmapDir = "bitmaps/"
except ImportError: # if it's not there locally, try the wxPython lib.
    import wx.lib.agw.hypertreelist as HTL
    bitmapDir = "agw/bitmaps/"

# from xyView.base import images


ArtIDs = [ "None",
           "wx.ART_ADD_BOOKMARK",
           "wx.ART_DEL_BOOKMARK",
           "wx.ART_HELP_SIDE_PANEL",
           "wx.ART_HELP_SETTINGS",
           "wx.ART_HELP_BOOK",
           "wx.ART_HELP_FOLDER",
           "wx.ART_HELP_PAGE",
           "wx.ART_GO_BACK",
           "wx.ART_GO_FORWARD",
           "wx.ART_GO_UP",
           "wx.ART_GO_DOWN",
           "wx.ART_GO_TO_PARENT",
           "wx.ART_GO_HOME",
           "wx.ART_FILE_OPEN",
           "wx.ART_PRINT",
           "wx.ART_HELP",
           "wx.ART_TIP",
           "wx.ART_REPORT_VIEW",
           "wx.ART_LIST_VIEW",
           "wx.ART_NEW_DIR",
           "wx.ART_HARDDISK",
           "wx.ART_FLOPPY",
           "wx.ART_CDROM",
           "wx.ART_REMOVABLE",
           "wx.ART_FOLDER",
           "wx.ART_FOLDER_OPEN",
           "wx.ART_GO_DIR_UP",
           "wx.ART_EXECUTABLE_FILE",
           "wx.ART_NORMAL_FILE",
           "wx.ART_TICK_MARK",
           "wx.ART_CROSS_MARK",
           "wx.ART_ERROR",
           "wx.ART_QUESTION",
           "wx.ART_WARNING",
           "wx.ART_INFORMATION",
           "wx.ART_MISSING_IMAGE",
           "SmileBitmap"
           ]

keyMap = {
    wx.WXK_BACK : "WXK_BACK",
    wx.WXK_TAB : "WXK_TAB",
    wx.WXK_RETURN : "WXK_RETURN",
    wx.WXK_ESCAPE : "WXK_ESCAPE",
    wx.WXK_SPACE : "WXK_SPACE",
    wx.WXK_DELETE : "WXK_DELETE",
    wx.WXK_START : "WXK_START",
    wx.WXK_LBUTTON : "WXK_LBUTTON",
    wx.WXK_RBUTTON : "WXK_RBUTTON",
    wx.WXK_CANCEL : "WXK_CANCEL",
    wx.WXK_MBUTTON : "WXK_MBUTTON",
    wx.WXK_CLEAR : "WXK_CLEAR",
    wx.WXK_SHIFT : "WXK_SHIFT",
    wx.WXK_ALT : "WXK_ALT",
    wx.WXK_CONTROL : "WXK_CONTROL",
    wx.WXK_MENU : "WXK_MENU",
    wx.WXK_PAUSE : "WXK_PAUSE",
    wx.WXK_CAPITAL : "WXK_CAPITAL",
    wx.WXK_END : "WXK_END",
    wx.WXK_HOME : "WXK_HOME",
    wx.WXK_LEFT : "WXK_LEFT",
    wx.WXK_UP : "WXK_UP",
    wx.WXK_RIGHT : "WXK_RIGHT",
    wx.WXK_DOWN : "WXK_DOWN",
    wx.WXK_SELECT : "WXK_SELECT",
    wx.WXK_PRINT : "WXK_PRINT",
    wx.WXK_EXECUTE : "WXK_EXECUTE",
    wx.WXK_SNAPSHOT : "WXK_SNAPSHOT",
    wx.WXK_INSERT : "WXK_INSERT",
    wx.WXK_HELP : "WXK_HELP",
    wx.WXK_NUMPAD0 : "WXK_NUMPAD0",
    wx.WXK_NUMPAD1 : "WXK_NUMPAD1",
    wx.WXK_NUMPAD2 : "WXK_NUMPAD2",
    wx.WXK_NUMPAD3 : "WXK_NUMPAD3",
    wx.WXK_NUMPAD4 : "WXK_NUMPAD4",
    wx.WXK_NUMPAD5 : "WXK_NUMPAD5",
    wx.WXK_NUMPAD6 : "WXK_NUMPAD6",
    wx.WXK_NUMPAD7 : "WXK_NUMPAD7",
    wx.WXK_NUMPAD8 : "WXK_NUMPAD8",
    wx.WXK_NUMPAD9 : "WXK_NUMPAD9",
    wx.WXK_MULTIPLY : "WXK_MULTIPLY",
    wx.WXK_ADD : "WXK_ADD",
    wx.WXK_SEPARATOR : "WXK_SEPARATOR",
    wx.WXK_SUBTRACT : "WXK_SUBTRACT",
    wx.WXK_DECIMAL : "WXK_DECIMAL",
    wx.WXK_DIVIDE : "WXK_DIVIDE",
    wx.WXK_F1 : "WXK_F1",
    wx.WXK_F2 : "WXK_F2",
    wx.WXK_F3 : "WXK_F3",
    wx.WXK_F4 : "WXK_F4",
    wx.WXK_F5 : "WXK_F5",
    wx.WXK_F6 : "WXK_F6",
    wx.WXK_F7 : "WXK_F7",
    wx.WXK_F8 : "WXK_F8",
    wx.WXK_F9 : "WXK_F9",
    wx.WXK_F10 : "WXK_F10",
    wx.WXK_F11 : "WXK_F11",
    wx.WXK_F12 : "WXK_F12",
    wx.WXK_F13 : "WXK_F13",
    wx.WXK_F14 : "WXK_F14",
    wx.WXK_F15 : "WXK_F15",
    wx.WXK_F16 : "WXK_F16",
    wx.WXK_F17 : "WXK_F17",
    wx.WXK_F18 : "WXK_F18",
    wx.WXK_F19 : "WXK_F19",
    wx.WXK_F20 : "WXK_F20",
    wx.WXK_F21 : "WXK_F21",
    wx.WXK_F22 : "WXK_F22",
    wx.WXK_F23 : "WXK_F23",
    wx.WXK_F24 : "WXK_F24",
    wx.WXK_NUMLOCK : "WXK_NUMLOCK",
    wx.WXK_SCROLL : "WXK_SCROLL",
    wx.WXK_PAGEUP : "WXK_PAGEUP",
    wx.WXK_PAGEDOWN : "WXK_PAGEDOWN",
    wx.WXK_NUMPAD_SPACE : "WXK_NUMPAD_SPACE",
    wx.WXK_NUMPAD_TAB : "WXK_NUMPAD_TAB",
    wx.WXK_NUMPAD_ENTER : "WXK_NUMPAD_ENTER",
    wx.WXK_NUMPAD_F1 : "WXK_NUMPAD_F1",
    wx.WXK_NUMPAD_F2 : "WXK_NUMPAD_F2",
    wx.WXK_NUMPAD_F3 : "WXK_NUMPAD_F3",
    wx.WXK_NUMPAD_F4 : "WXK_NUMPAD_F4",
    wx.WXK_NUMPAD_HOME : "WXK_NUMPAD_HOME",
    wx.WXK_NUMPAD_LEFT : "WXK_NUMPAD_LEFT",
    wx.WXK_NUMPAD_UP : "WXK_NUMPAD_UP",
    wx.WXK_NUMPAD_RIGHT : "WXK_NUMPAD_RIGHT",
    wx.WXK_NUMPAD_DOWN : "WXK_NUMPAD_DOWN",
    wx.WXK_NUMPAD_PAGEUP : "WXK_NUMPAD_PAGEUP",
    wx.WXK_NUMPAD_PAGEDOWN : "WXK_NUMPAD_PAGEDOWN",
    wx.WXK_NUMPAD_END : "WXK_NUMPAD_END",
    wx.WXK_NUMPAD_BEGIN : "WXK_NUMPAD_BEGIN",
    wx.WXK_NUMPAD_INSERT : "WXK_NUMPAD_INSERT",
    wx.WXK_NUMPAD_DELETE : "WXK_NUMPAD_DELETE",
    wx.WXK_NUMPAD_EQUAL : "WXK_NUMPAD_EQUAL",
    wx.WXK_NUMPAD_MULTIPLY : "WXK_NUMPAD_MULTIPLY",
    wx.WXK_NUMPAD_ADD : "WXK_NUMPAD_ADD",
    wx.WXK_NUMPAD_SEPARATOR : "WXK_NUMPAD_SEPARATOR",
    wx.WXK_NUMPAD_SUBTRACT : "WXK_NUMPAD_SUBTRACT",
    wx.WXK_NUMPAD_DECIMAL : "WXK_NUMPAD_DECIMAL",
    wx.WXK_NUMPAD_DIVIDE : "WXK_NUMPAD_DIVIDE"
    }


#----------------------------------------------------------------------
def GetMondrianData():
    return \
'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00 \x00\x00\x00 \x08\x06\x00\
\x00\x00szz\xf4\x00\x00\x00\x04sBIT\x08\x08\x08\x08|\x08d\x88\x00\x00\x00qID\
ATX\x85\xed\xd6;\n\x800\x10E\xd1{\xc5\x8d\xb9r\x97\x16\x0b\xad$\x8a\x82:\x16\
o\xda\x84pB2\x1f\x81Fa\x8c\x9c\x08\x04Z{\xcf\xa72\xbcv\xfa\xc5\x08 \x80r\x80\
\xfc\xa2\x0e\x1c\xe4\xba\xfaX\x1d\xd0\xde]S\x07\x02\xd8>\xe1wa-`\x9fQ\xe9\
\x86\x01\x04\x10\x00\\(Dk\x1b-\x04\xdc\x1d\x07\x14\x98;\x0bS\x7f\x7f\xf9\x13\
\x04\x10@\xf9X\xbe\x00\xc9 \x14K\xc1<={\x00\x00\x00\x00IEND\xaeB`\x82'

def GetMondrianBitmap():
    return wx.Bitmap(GetMondrianImage())

def GetMondrianImage():
    stream = BytesIO(GetMondrianData())
    return wx.Image(stream)

def GetMondrianIcon():
    icon = wx.Icon()
    icon.CopyFromBitmap(GetMondrianBitmap())
    return icon


#----------------------------------------------------------------------
def GetSmilesData():
    return \
'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x10\x00\x00\x00\x10\x08\x06\
\x00\x00\x00\x1f\xf3\xffa\x00\x00\x00\x04sBIT\x08\x08\x08\x08|\x08d\x88\x00\
\x00\x02\x89IDAT8\x8dm\x93\xddK\x93a\x18\xc6\x7f\xef\xc7\xb3\xa6\xc3 aV\xcc\
\xad\x99\x8d\\\x08\x11AAd\x91\x95\x85F\'\x9dD\x8d\xa8\xe9\xb6X\x87\xe1\x7f\
\xd0A\xe2y\'\xe6I\x7f@\'!T\x96\'A\x10A\xf4!\xcc\xd1\xb7&DP \xba\xe5\xde\xd7\
\xed\xea\xc0\xcdF\xf9\xc0u\xf2<\xcf\xc5}\xdf\xd7u\xddX\xb6\xc3\xbfH\xa5.)\
\x1e\xdf)\xd7\xb5d\x8c\xadD"\xaa\\.\xa3\xcd\xfe\xda4\x9dl&\xad\xceHP\xbd\xbd\
\x9fx\xf0\xe0\x08\xe5\xf2eJ\xa5\x8b\xdc\xbf\xbf\x9f\xae\xaeGtFj\xcaf\xae\xa9\
\x99cY\xb6\x03\xc0\xe9S\xc7\x14\x8b\xfd\xe4\xce\x9d\xf3\x18\xe3\x01%`\x05\
\xa8\x02\x15\xe0#\xbe_ \x9f\xf7\x98\x9f?\xc2\xf4\x93\xe7\x16\xb0\xdeA6\x93V,\
\x06\x13\x13\xb71&\t\x84\xea\xc4F\xb1U\xa0\x8c1\x16\x13\x13[\x88\xc5\x9e\x91\
\xcd\\]\x7f\xb4l\x87h\xb4]\x9eW\x90\xf4E\xd2c\x8d\x8e\x8e\n\x90\x94\x92\x94\
\x12\xa0p8,\xa9UR\x8b<\x0fE;\x91e;\xb8\xd9LZ]]k\x18\xd3\x028@\x8d\xf1\xf1\
\xf1\xa6)\x97\xe8\xe9\xe9ann\x0eh\x05\xd50\x04\xb9q\xbd\xca\xe7\xf9\x94\xec\
\x99\x99\x87\x0c\rE\x80E\xe0#\xf0\xba\x89\\\x01\x16YXXh\xba\xabA\xa5\x95\xa1\
\x93m\xcc\xccLa\x19c\xabT\xba\x891m\xc0*\xc3\xc3\xdf\x99\x9c\xf46\x84\x83\
\x85\xba\xa0ur\xb5\nK\x1d\xf8\xab\x0e\xa1]\xf3\r\x1b\xbd\xba\xe2\xcbLN\xfa\
\xc0\x12\xf0\x0e(6\x91\x05Zcwg\x10\xfc\x16\xf0\x83\x00\xd8\xf1x\x84b\xf1\x1b\
\xf0\x03(\x92L\xbe\x04^\xd4+\xeb/\x19\x1f\xaa6\x9f\xbf/C\xb9\x8d\xe2\x9cE|W\
\x18\xb7\xbf\xff\x0cSS\xf7\xe8\xed\r\x00\xa2P\x80PH\x94\x1a\x85\xa9\x01kP\
\xb58\xb8\xaf\r}\x89@y+S\x8f\x7f\xd1\x7f\xfcd\xc3FK\x9e\xd7R\xb7i\xdd*\x05\
\x83\n\x04\x02r]G\xa1\xa0\xab\xfd\xdd\xed\xd2\xe2^\xa9\xd0\'\xef\xd5\tEw\x04\
\xb4\x11\xe5\xc1\xc14\xf9\xfc\xeaz\x9b\r\xfc\xf6\xa9\xf8>\xbecq8\xd9\xc1\xeb\
\xa7QX\x0e\xc3Z\x80\xfc\xad"\x83g\xce\xb1\x11$\xcbv\x18\x18\xe8\xd3\xc8\x08\
\xf2<$\xd5Q\xb5\xa5\x95m\xd2\xb7\xa4\xf4\xe1\x90\xbc7G5ra\x87\x06\x8e\x1f\
\xd0\x7f\xcb4\xfd\xe4\xb9\xe58\xc3tw\xc3\xd8\x18\xcc\xce\x82_q\xf0+6\xb3\xef\
W\x18\xbb\xfb\x95\xee\xb3/p\xb6\xf61\xfd\xec\xad\xb5\x11\x8b\xcdV4\x97K+\x91\
\xd8.\xe3"\xe3\xa2\xc4\x9e\x0e\xe52W6]\xe7?\xc6#-\xf1\x056\x98<\x00\x00\x00\
\x00IEND\xaeB`\x82'

def GetSmilesBitmap():
    return wx.Bitmap(GetSmilesImage())

def GetSmilesImage():
    stream = BytesIO(GetSmilesData())
    return wx.Image(stream)

#----------------------------------------------------------------------

def opj(path):
    """Convert paths to the platform-specific separator"""
    st = os.path.join(*tuple(path.split('/')))
    # HACK: on Linux, a leading / gets lost...
    if path.startswith('/'):
        st = '/' + st
    return st

#-----------------------------------------------------------------------------

#---------------------------------------------------------------------------
# Just A Dialog To Select Tree Items Icons
#---------------------------------------------------------------------------
class TreeIcons(wx.Dialog):

    def __init__(self, parent=None, id=-1, title="", pos=wx.DefaultPosition,
                 size=wx.DefaultSize, style=wx.DEFAULT_DIALOG_STYLE, oldpen=None,
                 bitmaps=None):

        wx.Dialog.__init__(self, parent, id, title, pos, size, style)

        self.bitmaps = [None, None, None, None]
        empty = wx.Bitmap(16, 16)
        self.parent = parent

        self.bitmaps[0] = wx.StaticBitmap(self, -1, empty)
        self.combonormal = wx.ComboBox(self, -1, choices=ArtIDs, style=wx.CB_DROPDOWN|wx.CB_READONLY)
        self.bitmaps[1] = wx.StaticBitmap(self, -1, empty)
        self.comboselected = wx.ComboBox(self, -1, choices=ArtIDs, style=wx.CB_DROPDOWN|wx.CB_READONLY)
        self.bitmaps[2] = wx.StaticBitmap(self, -1, empty)
        self.comboexpanded = wx.ComboBox(self, -1, choices=ArtIDs, style=wx.CB_DROPDOWN|wx.CB_READONLY)
        self.bitmaps[3] = wx.StaticBitmap(self, -1, empty)
        self.comboselectedexpanded = wx.ComboBox(self, -1, choices=ArtIDs, style=wx.CB_DROPDOWN|wx.CB_READONLY)
        self.okbutton = wx.Button(self, -1, "Ok")
        self.cancelbutton = wx.Button(self, -1, "Cancel")

        self.combonormal.SetSelection(bitmaps[0] >= 0 and bitmaps[0]+1 or 0)
        self.comboselected.SetSelection(bitmaps[1] >= 0 and bitmaps[1]+1 or 0)
        self.comboexpanded.SetSelection(bitmaps[2] >= 0 and bitmaps[2]+1 or 0)
        self.comboselectedexpanded.SetSelection(bitmaps[3] >= 0 and bitmaps[3]+1 or 0)

        self.GetBitmaps(bitmaps)

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_COMBOBOX, self.OnComboNormal, self.combonormal)
        self.Bind(wx.EVT_COMBOBOX, self.OnComboSelected, self.comboselected)
        self.Bind(wx.EVT_COMBOBOX, self.OnComboExpanded, self.comboexpanded)
        self.Bind(wx.EVT_COMBOBOX, self.OnComboSelectedExpanded, self.comboselectedexpanded)
        self.Bind(wx.EVT_BUTTON, self.OnOk, self.okbutton)
        self.Bind(wx.EVT_BUTTON, self.OnCancel, self.cancelbutton)


    def __set_properties(self):

        self.SetTitle("Item Icon Selector")
        self.okbutton.SetDefault()


    def __do_layout(self):

        mainsizer = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        gridsizer = wx.FlexGridSizer(cols=3, hgap=5, vgap=5)
        label_1 = wx.StaticText(self, -1, "Please Choose The Icons For This Item (All Are Optional):")
        label_1.SetFont(wx.Font(8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, ""))
        mainsizer.Add(label_1, 0, wx.ALL|wx.ADJUST_MINSIZE, 10)
        label_2 = wx.StaticText(self, -1, "TreeIcon_Normal:")
        gridsizer.Add(label_2, 0, wx.LEFT|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 5)
        gridsizer.Add(self.bitmaps[0], 0, wx.LEFT|wx.RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 5)
        gridsizer.Add(self.combonormal, 0, wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 0)
        label_3 = wx.StaticText(self, -1, "TreeIcon_Selected:")
        gridsizer.Add(label_3, 0, wx.LEFT|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 5)
        gridsizer.Add(self.bitmaps[1], 0, wx.LEFT|wx.RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 5)
        gridsizer.Add(self.comboselected, 0, wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 0)
        label_4 = wx.StaticText(self, -1, "TreeIcon_Expanded:")
        gridsizer.Add(label_4, 0, wx.LEFT|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 5)
        gridsizer.Add(self.bitmaps[2], 0, wx.LEFT|wx.RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 5)
        gridsizer.Add(self.comboexpanded, 0, wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 0)
        label_5 = wx.StaticText(self, -1, "TreeIcon_SelectedExpanded:")
        gridsizer.Add(label_5, 0, wx.LEFT|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 5)
        gridsizer.Add(self.bitmaps[3], 0, wx.LEFT|wx.RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 5)
        gridsizer.Add(self.comboselectedexpanded, 0, wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 0)
        gridsizer.AddGrowableCol(0)
        gridsizer.AddGrowableCol(1)
        gridsizer.AddGrowableCol(2)
        mainsizer.Add(gridsizer, 0, wx.ALL|wx.EXPAND, 5)
        sizer_2.Add(self.okbutton, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 20)
        sizer_2.Add((20, 20), 1, wx.ADJUST_MINSIZE, 0)
        sizer_2.Add(self.cancelbutton, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 20)
        mainsizer.Add(sizer_2, 1, wx.EXPAND, 0)
        self.SetAutoLayout(True)
        self.SetSizer(mainsizer)
        mainsizer.Fit(self)
        mainsizer.SetSizeHints(self)
        self.Layout()
        self.Centre()


    def OnComboNormal(self, event):

        input = event.GetSelection()
        self.GetBitmap(input, 0)
        event.Skip()


    def OnComboSelected(self, event):

        input = event.GetSelection()
        self.GetBitmap(input, 1)
        event.Skip()


    def OnComboExpanded(self, event):

        input = event.GetSelection()
        self.GetBitmap(input, 2)
        event.Skip()


    def OnComboSelectedExpanded(self, event):

        input = event.GetSelection()
        self.GetBitmap(input, 3)
        event.Skip()


    def OnOk(self, event):

        bitmaps = [-1, -1, -1, -1]
        normal = self.combonormal.GetSelection()
        selected = self.comboselected.GetSelection()
        expanded = self.comboexpanded.GetSelection()
        selexp = self.comboselectedexpanded.GetSelection()

        bitmaps = [(normal > 0 and normal or -1), (selected > 0 and selected or -1),
                   (expanded > 0 and expanded or -1), (selexp > 0 and selexp or -1)]

        newbitmaps = []

        for bmp in bitmaps:
            if bmp > 0:
                newbitmaps.append(bmp-1)
            else:
                newbitmaps.append(bmp)

        self.parent.SetNewIcons(newbitmaps)

        self.Destroy()
        event.Skip()


    def OnCancel(self, event):

        self.Destroy()
        event.Skip()


    def GetBitmap(self, input, which):

        if input == 0:
            bmp = wx.Bitmap(16,16)
            self.ClearBmp(bmp)
        elif input > 36:
            bmp = GetSmilesBitmap()
        else:
            bmp = wx.ArtProvider.GetBitmap(eval(ArtIDs[input]), wx.ART_OTHER, (16,16))
            if not bmp.Ok():
                bmp = wx.Bitmap(16,16)
                self.ClearBmp(bmp)

        self.bitmaps[which].SetBitmap(bmp)
        self.bitmaps[which].Refresh()


    def GetBitmaps(self, bitmaps):

        output = []

        for count, input in enumerate(bitmaps):
            if input < 0:
                bmp = wx.Bitmap(16,16)
                self.ClearBmp(bmp)
            elif input > 35:
                bmp = GetSmilesBitmap()
            else:
                bmp = wx.ArtProvider.GetBitmap(eval(ArtIDs[input+1]), wx.ART_OTHER, (16,16))
                if not bmp.Ok():
                    bmp = wx.Bitmap(16,16)
                    self.ClearBmp(bmp)

            self.bitmaps[count].SetBitmap(bmp)


    def ClearBmp(self, bmp):

        dc = wx.MemoryDC()
        dc.SelectObject(bmp)
        dc.SetBackground(wx.Brush("white"))
        dc.Clear()


#---------------------------------------------------------------------------
# Custom Renderer for the column headers
#---------------------------------------------------------------------------
class HyperTreeHeaderRenderer(object):
    """
    Draws the column headers as a solid color (self.color)
    """

    def __init__(self, parent):
        self.color = wx.Colour(150,150,150)

    def DrawTextFormatted(self, dc, text, rect):
        """
        Draws the item text, correctly formatted.

        :param `dc`: an instance of `wx.DC`;
        :param `text`: the item text;
        :param `rect`: the item client rectangle.
        """

        # determine if the string can fit inside the current width
        w, h, dummy = dc.GetFullMultiLineTextExtent(text)
        width = rect.width

        if w <= width:

            dc.DrawLabel(text, rect, wx.ALIGN_CENTER_VERTICAL)

        else:

            # determine the base width
            ellipsis = "..."
            base_w, h = dc.GetTextExtent(ellipsis)

            # continue until we have enough space or only one character left

            newText = text.split("\n")
            theText = ""

            for text in newText:

                lenText = len(text)
                drawntext = text
                w, dummy = dc.GetTextExtent(text)

                while lenText > 1:

                    if w + base_w <= width:
                        break

                    w_c, h_c = dc.GetTextExtent(drawntext[-1])
                    drawntext = drawntext[0:-1]
                    lenText -= 1
                    w -= w_c

                # if still not enough space, remove ellipsis characters
                while len(ellipsis) > 0 and w + base_w > width:
                    ellipsis = ellipsis[0:-1]
                    base_w, h = dc.GetTextExtent(ellipsis)

                theText += drawntext + ellipsis + "\n"

            theText = theText.rstrip()
            dc.DrawLabel(theText, rect, wx.ALIGN_CENTER_VERTICAL)



    def DrawHeaderButton(self, dc, rect, flags=0, params=None):

        if params != None:
            text_align = params.m_labelAlignment
            bitmap     = params.m_labelBitmap
            text_color = params.m_labelColour
            text_font  = params.m_labelFont
            text       = params.m_labelText

        color = self.color

        if flags & wx.CONTROL_DISABLED:
            color = wx.Colour(wx.WHITE)
        elif flags & wx.CONTROL_SELECTED:
            color = wx.Colour(wx.BLUE)
        if flags & wx.CONTROL_PRESSED:
            self._pressed = True
            color = cutils.AdjustColour(color,-30)
        elif flags & wx.CONTROL_CURRENT:
            self._hover = True
            color = cutils.AdjustColour(color,50)

        # Draw a solid background in self.color
        dc.SetBrush(wx.Brush(color, wx.BRUSHSTYLE_SOLID))
        dc.SetBackgroundMode(wx.SOLID)
        dc.SetPen(wx.TRANSPARENT_PEN)
        dc.DrawRectangleRect(rect)

        # Draw the column divider on the right
        x = rect.width + rect.x - 2
        dc.SetPen(wx.Pen(cutils.AdjustColour(color,-30)))
        dc.DrawLine(x,2,x,rect.height-2)
        x += 1
        dc.SetPen(wx.Pen(cutils.AdjustColour(color,30)))
        dc.DrawLine(x,2,x,rect.height-2)

        dc.SetBackgroundMode(wx.TRANSPARENT)

        if params == None:
            return

        # We need to draw the text and/or icon bitmap
        dc.SetFont(text_font)
        dc.SetTextForeground(text_color)

        # Determine the width of the text
        wLabel, hLabel, dummy = dc.GetFullMultiLineTextExtent(text)
        wLabel += 4  # 2 pixel margin either side

        # and the width of the icon, if any
        if bitmap:
            wLabel += bitmap.GetWidth() + 2  # 2 is a margin between the image and text

        # ALIGN_LEFT if the label is larger than the available space
        text_align = (wLabel < rect.width and [text_align] or [wx.ALIGN_LEFT])[0]

        x = rect.x + 2

        if text_align == wx.ALIGN_LEFT:
            xAligned = x

        elif text_align == wx.ALIGN_RIGHT:
            xAligned = x + rect.width - wLabel - 1

        elif text_align == wx.ALIGN_CENTER:
            xAligned = x + (rect.width - wLabel)/2

        if bitmap:
            dc.DrawBitmap(bitmap, xAligned + wLabel - bitmap.GetWidth() , 2, True)

        dc.SetClippingRegion(x, 1, rect.width-2, rect.height - 2)
        self.DrawTextFormatted(dc, text, wx.Rect(xAligned+2, 1, rect.width-2, rect.height-2))
        dc.DestroyClippingRegion()



#---------------------------------------------------------------------------
# HyperTreeList Implementation
#---------------------------------------------------------------------------
class BaseTreeList(HTL.HyperTreeList):

    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition,
                 size=wx.DefaultSize,
                 style=wx.SUNKEN_BORDER,
                agwStyle=wx.TR_HAS_BUTTONS | wx.TR_HAS_VARIABLE_ROW_HEIGHT | HTL.TR_AUTO_CHECK_CHILD | HTL.TR_AUTO_CHECK_PARENT | HTL.TR_AUTO_TOGGLE_CHILD,
#                  agwStyle= HTL.TR_ALIGN_WINDOWS | HTL.TR_AUTO_CHECK_CHILD | HTL.TR_AUTO_CHECK_PARENT | HTL.TR_AUTO_TOGGLE_CHILD | HTL.TR_COLUMN_LINES | wx.TR_DEFAULT_STYLE | wx.TR_EDIT_LABELS | HTL.TR_ELLIPSIZE_LONG_ITEMS | HTL.TR_EXTENDED | wx.TR_FULL_ROW_HIGHLIGHT | wx.TR_HAS_BUTTONS | wx.TR_HAS_VARIABLE_ROW_HEIGHT | wx.TR_HIDE_ROOT | wx.TR_LINES_AT_ROOT | wx.TR_MULTIPLE | wx.TR_NO_BUTTONS | HTL.TR_NO_HEADER | wx.TR_NO_LINES | wx.TR_ROW_LINES | wx.TR_SINGLE | wx.TR_TWIST_BUTTONS | HTL.TR_VIRTUAL,
                 log=None):

        HTL.HyperTreeList.__init__(self, parent, id, pos, size, style, agwStyle)

        alldata = dir(HTL)

        treestyles = []
        events = []
        for data in alldata:
            if data.startswith("TR_"):
                treestyles.append(data)
            elif data.startswith("EVT_"):
                events.append(data)

        events = events + [i for i in dir(wx) if i.startswith("EVT_TREE_")]
        for evt in ["EVT_TREE_GET_INFO", "EVT_TREE_SET_INFO", "EVT_TREE_ITEM_MIDDLE_CLICK",
                    "EVT_TREE_STATE_IMAGE_CLICK"]:
            events.remove(evt)

        treestyles = treestyles + [i for i in dir(wx) if i.startswith("TR_")]
        treeset = {}
        treestyles = [treeset.setdefault(e,e) for e in treestyles if e not in treeset]

        treestyles.sort()

        self.events = events
        self.styles = treestyles
        self.item = None

        il = wx.ImageList(16, 16)

        for items in ArtIDs[1:-1]:
            bmp = wx.ArtProvider.GetBitmap(eval(items), wx.ART_TOOLBAR, (16, 16))
            il.Add(bmp)

#         smileidx = il.Add(images.Smiles.GetBitmap())
#         numicons = il.GetImageCount()

        self.AssignImageList(il)
#         self.count = 0
        self.log = log

        # NOTE:  For some reason tree items have to have a data object in
        #        order to be sorted.  Since our compare just uses the labels
        #        we don't need any real data, so we'll just use None below for
        #        the item data.

        self.setup_list()
        
        self.GetMainWindow().Bind(wx.EVT_LEFT_DCLICK, self.OnLeftDClick)
        self.Bind(wx.EVT_IDLE, self.OnIdle)

        self.eventdict = {'EVT_TREE_BEGIN_DRAG': self.OnBeginDrag, 'EVT_TREE_BEGIN_LABEL_EDIT': self.OnBeginEdit,
                          'EVT_TREE_BEGIN_RDRAG': self.OnBeginRDrag, 'EVT_TREE_DELETE_ITEM': self.OnDeleteItem,
                          'EVT_TREE_END_DRAG': self.OnEndDrag, 'EVT_TREE_END_LABEL_EDIT': self.OnEndEdit,
                          'EVT_TREE_ITEM_ACTIVATED': self.OnActivate, 'EVT_TREE_ITEM_CHECKED': self.OnItemCheck,
                          'EVT_TREE_ITEM_CHECKING': self.OnItemChecking, 'EVT_TREE_ITEM_COLLAPSED': self.OnItemCollapsed,
                          'EVT_TREE_ITEM_COLLAPSING': self.OnItemCollapsing, 'EVT_TREE_ITEM_EXPANDED': self.OnItemExpanded,
                          'EVT_TREE_ITEM_EXPANDING': self.OnItemExpanding, 'EVT_TREE_ITEM_GETTOOLTIP': self.OnToolTip,
                          'EVT_TREE_ITEM_MENU': self.OnItemMenu, 'EVT_TREE_ITEM_RIGHT_CLICK': self.OnRightDown,
                          'EVT_TREE_KEY_DOWN': self.OnKey, 'EVT_TREE_SEL_CHANGED': self.OnSelChanged,
                          'EVT_TREE_SEL_CHANGING': self.OnSelChanging, "EVT_TREE_ITEM_HYPERLINK": self.OnHyperLink}

        if not(self.GetAGWWindowStyleFlag() & wx.TR_HIDE_ROOT):
            self.SelectItem(self.root)
            self.Expand(self.root)


    def setup_list(self):  pass
    
    def BindEvents(self, choice, recreate=False):

        value = choice.GetValue()
        text = choice.GetLabel()

        evt = "wx." + text
        binder = self.eventdict[text]

        if value == 1:
            if evt == "wx.EVT_TREE_BEGIN_RDRAG":
                self.GetMainWindow().Bind(wx.EVT_RIGHT_DOWN, None)
                self.GetMainWindow().Bind(wx.EVT_RIGHT_UP, None)
            try:
                self.Bind(eval(evt), binder)
            except:
                self.Bind(eval("HTL." + text), binder)
        else:
            try:
                self.Bind(eval(evt), None)
            except:
                self.Bind(eval("HTL." + text), None)

            if evt == "wx.EVT_TREE_BEGIN_RDRAG":
                self.GetMainWindow().Bind(wx.EVT_RIGHT_DOWN, self.OnRightDown)
                self.GetMainWindow().Bind(wx.EVT_RIGHT_UP, self.OnRightUp)


    def ChangeStyle(self, combos):

        style = 0
        for combo in combos:
            if combo.GetValue() == 1:
                if combo.GetLabel() == "TR_VIRTUAL":
                    style = style | HTL.TR_VIRTUAL
                else:
                    try:
                        style = style | eval("wx." + combo.GetLabel())
                    except:
                        style = style | eval("HTL." + combo.GetLabel())

        if self.GetAGWWindowStyleFlag() != style:
            self.SetAGWWindowStyleFlag(style)




    def NewSetStyle(self, lst):

        style = 0
        for itm in lst:

            if itm == "TR_VIRTUAL":
                style = style | HTL.TR_VIRTUAL
            else:
                try:
                    style = style | eval("wx." + itm)
                except:
                    style = style | eval("HTL." + itm)

        if self.GetAGWWindowStyleFlag() != style:
            self.SetAGWWindowStyleFlag(style)
            

    def OnCompareItems(self, item1, item2):

        t1 = self.GetItemText(item1)
        t2 = self.GetItemText(item2)

        self.log.write('compare: ' + t1 + ' <> ' + t2 + "\n")

        if t1 < t2:
            return -1
        if t1 == t2:
            return 0

        return 1


    def OnIdle(self, event):  pass

#         if self.gauge:
# 
#             try:
#                 if self.gauge.IsEnabled() and self.gauge.IsShown():
#                     self.count = self.count + 1
# 
#                     if self.count >= 50:
#                         self.count = 0
# 
#                     self.gauge.SetValue(self.count)
# 
#             except:
# 
#                 self.gauge = None
# 
#         event.Skip()


    def OnRightDown(self, event):

        pt = event.GetPosition()
        item, flags, column = self.HitTest(pt)

        if item:
            self.item = item
            self.log.write("OnRightClick: %s, %s, %s\n" % (self.GetItemText(item), type(item), item.__class__))
            self.SelectItem(item)


    def OnRightUp(self, event):

        item = self.item

        if not item:
            event.Skip()
            return

        if not self.IsItemEnabled(item):
            event.Skip()
            return

        # Item Text Appearance
        ishtml = self.IsItemHyperText(item)
        back = self.GetItemBackgroundColour(item)
        fore = self.GetItemTextColour(item)
        isbold = self.IsBold(item)
        font = self.GetItemFont(item)

        # Icons On Item
        normal = self.GetItemImage(item, wx.TreeItemIcon_Normal)
        selected = self.GetItemImage(item, wx.TreeItemIcon_Selected)
        expanded = self.GetItemImage(item, wx.TreeItemIcon_Expanded)
        selexp = self.GetItemImage(item, wx.TreeItemIcon_SelectedExpanded)

        # Enabling/Disabling Windows Associated To An Item
        haswin = self.GetItemWindow(item)

        # Enabling/Disabling Items
        enabled = self.IsItemEnabled(item)

        # Generic Item's Info
        children = self.GetChildrenCount(item)
        itemtype = self.GetItemType(item)
        text = self.GetItemText(item)
        pydata = self.GetPyData(item)

        self.current = item
        self.itemdict = {"ishtml": ishtml, "back": back, "fore": fore, "isbold": isbold,
                         "font": font, "normal": normal, "selected": selected, "expanded": expanded,
                         "selexp": selexp, "haswin": haswin, "children": children,
                         "itemtype": itemtype, "text": text, "pydata": pydata, "enabled": enabled}

        menu = wx.Menu()

        item2 = menu.Append(wx.ID_ANY, "Modify Item Text Colour")
        menu.AppendSeparator()
        if isbold:
            strs = "Make Item Text Not Bold"
        else:
            strs = "Make Item Text Bold"
        item3 = menu.Append(wx.ID_ANY, strs)
        item4 = menu.Append(wx.ID_ANY, "Change Item Font")
        item13 = menu.Append(wx.ID_ANY, "Change Item Background Colour")
        menu.AppendSeparator()
        if ishtml:
            strs = "Set Item As Non-Hyperlink"
        else:
            strs = "Set Item As Hyperlink"
        item5 = menu.Append(wx.ID_ANY, strs)
        menu.AppendSeparator()

        item7 = menu.Append(wx.ID_ANY, "Disable Item")

        menu.AppendSeparator()
        item8 = menu.Append(wx.ID_ANY, "Change Item Icons")
        menu.AppendSeparator()
        item9 = menu.Append(wx.ID_ANY, "Get Other Information For This Item")
        menu.AppendSeparator()

        item10 = menu.Append(wx.ID_ANY, "Delete Item")
        if item == self.GetRootItem():
            item10.Enable(False)
        item11 = menu.Append(wx.ID_ANY, "Prepend An Item")
        item12 = menu.Append(wx.ID_ANY, "Append An Item")

        self.Bind(wx.EVT_MENU, self.OnItemForeground, item2)
        self.Bind(wx.EVT_MENU, self.OnItemBold, item3)
        self.Bind(wx.EVT_MENU, self.OnItemFont, item4)
        self.Bind(wx.EVT_MENU, self.OnItemHyperText, item5)
        self.Bind(wx.EVT_MENU, self.OnDisableItem, item7)
        self.Bind(wx.EVT_MENU, self.OnItemIcons, item8)
        self.Bind(wx.EVT_MENU, self.OnItemInfo, item9)
        self.Bind(wx.EVT_MENU, self.OnItemDelete, item10)
        self.Bind(wx.EVT_MENU, self.OnItemPrepend, item11)
        self.Bind(wx.EVT_MENU, self.OnItemAppend, item12)
        self.Bind(wx.EVT_MENU, self.OnItemBackground, item13)

        self.PopupMenu(menu)
        menu.Destroy()
        event.Skip()


    def OnItemForeground(self, event):

        colourdata = wx.ColourData()
        colourdata.SetColour(self.itemdict["fore"])
        dlg = wx.ColourDialog(self, colourdata)

        dlg.GetColourData().SetChooseFull(True)

        if dlg.ShowModal() == wx.ID_OK:
            data = dlg.GetColourData()
            col1 = data.GetColour().Get()
            self.SetItemTextColour(self.current, col1)
        dlg.Destroy()
        event.Skip()


    def OnItemBold(self, event):

        self.SetItemBold(self.current, not self.itemdict["isbold"])
        event.Skip()


    def OnItemFont(self, event):

        data = wx.FontData()
        font = self.itemdict["font"]

        if font is None:
#             font = wx.SystemSettings_GetFont(wx.SYS_DEFAULT_GUI_FONT)
            font = wx.SystemSettings.GetFont(wx.SYS_DEFAULT_GUI_FONT)

        data.SetInitialFont(font)

        dlg = wx.FontDialog(self, data)

        if dlg.ShowModal() == wx.ID_OK:
            data = dlg.GetFontData()
            font = data.GetChosenFont()
            self.SetItemFont(self.current, font)

        dlg.Destroy()
        event.Skip()


    def OnItemHyperText(self, event):

        self.SetItemHyperText(self.current, not self.itemdict["ishtml"])
        event.Skip()


    def OnDisableItem(self, event):

        self.EnableItem(self.current, False)
        event.Skip()


    def OnItemIcons(self, event):

        bitmaps = [self.itemdict["normal"], self.itemdict["selected"],
                   self.itemdict["expanded"], self.itemdict["selexp"]]
 
        wx.BeginBusyCursor()
        dlg = TreeIcons(self, -1, bitmaps=bitmaps)
        wx.EndBusyCursor()
        dlg.ShowModal()
        event.Skip()


    def SetNewIcons(self, bitmaps):

        self.SetItemImage(self.current, bitmaps[0], which=wx.TreeItemIcon_Normal)
        self.SetItemImage(self.current, bitmaps[1], which=wx.TreeItemIcon_Selected)
        self.SetItemImage(self.current, bitmaps[2], which=wx.TreeItemIcon_Expanded)
        self.SetItemImage(self.current, bitmaps[3], which=wx.TreeItemIcon_SelectedExpanded)


    def OnItemInfo(self, event):

        itemtext = self.itemdict["text"]
        numchildren = str(self.itemdict["children"])
        itemtype = self.itemdict["itemtype"]
        pydata = repr(type(self.itemdict["pydata"]))

        if itemtype == 0:
            itemtype = "Normal"
        elif itemtype == 1:
            itemtype = "CheckBox"
        else:
            itemtype = "RadioButton"

        strs = "Information On Selected Item:\n\n" + "Text: " + itemtext + "\n" \
               "Number Of Children: " + numchildren + "\n" \
               "Item Type: " + itemtype + "\n" \
               "Item Data Type: " + pydata + "\n"

        dlg = wx.MessageDialog(self, strs, "HyperTreeListDemo Info", wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()

        event.Skip()


    def OnItemDelete(self, event):

        strs = "Are You Sure You Want To Delete Item " + self.GetItemText(self.current) + "?"
        dlg = wx.MessageDialog(None, strs, 'Deleting Item', wx.YES_NO | wx.NO_DEFAULT | wx.CANCEL | wx.ICON_QUESTION)

        if dlg.ShowModal() in [wx.ID_NO, wx.ID_CANCEL]:
            dlg.Destroy()
            return

        dlg.Destroy()

        self.DeleteChildren(self.current)
        self.Delete(self.current)
        self.current = None

        event.Skip()


    def OnItemPrepend(self, event):

        dlg = wx.TextEntryDialog(self, "Please Enter The New Item Name", 'Item Naming', 'Python')

        if dlg.ShowModal() == wx.ID_OK:
            newname = dlg.GetValue()
            newitem = self.PrependItem(self.current, newname)
            self.EnsureVisible(newitem)

        dlg.Destroy()
        event.Skip()


    def OnItemAppend(self, event):

        dlg = wx.TextEntryDialog(self, "Please Enter The New Item Name", 'Item Naming', 'Python')

        if dlg.ShowModal() == wx.ID_OK:
            newname = dlg.GetValue()
            newitem = self.AppendItem(self.current, newname)
            self.EnsureVisible(newitem)

        dlg.Destroy()
        event.Skip()


    def OnItemBackground(self, event):

        colourdata = wx.ColourData()
        colourdata.SetColour(self.itemdict["back"])
        dlg = wx.ColourDialog(self, colourdata)

        dlg.GetColourData().SetChooseFull(True)

        if dlg.ShowModal() == wx.ID_OK:
            data = dlg.GetColourData()
            col1 = data.GetColour().Get()
            self.SetItemBackgroundColour(self.current, col1)

        dlg.Destroy()
        event.Skip()


    def OnBeginEdit(self, event):

        self.log.write("OnBeginEdit\n")
        # show how to prevent edit...
        item = event.GetItem()
        if item and self.GetItemText(item) == "The Root Item":
            wx.Bell()
            self.log.write("You can't edit this one...\n")

            # Lets just see what's visible of its children
            cookie = 0
            root = event.GetItem()
            (child, cookie) = self.GetFirstChild(root)

            while child:
                self.log.write("Child [%s] visible = %d\n" % (self.GetItemText(child), self.IsVisible(child)))
                (child, cookie) = self.GetNextChild(root, cookie)

            event.Veto()


    def OnEndEdit(self, event):

        self.log.write("OnEndEdit: %s %s\n" %(event.IsEditCancelled(), event.GetLabel()))
        # show how to reject edit, we'll not allow any digits
        for x in event.GetLabel():
            if x in string.digits:
                self.log.write("You can't enter digits...\n")
                event.Veto()
                return


    def OnLeftDClick(self, event):

        pt = event.GetPosition()
        item, flags, column = self.HitTest(pt)
        if item and (flags & wx.TREE_HITTEST_ONITEMLABEL):
            if self.GetAGWWindowStyleFlag() & wx.TR_EDIT_LABELS:
                self.log.write("OnLeftDClick: %s (manually starting label edit)\n"% self.GetItemText(item))
                self.EditLabel(item)
            else:
                self.log.write("OnLeftDClick: Cannot Start Manual Editing, Missing Style TR_EDIT_LABELS\n")

        event.Skip()


    def OnItemExpanded(self, event):

        item = event.GetItem()
        if item:
            self.log.write("OnItemExpanded: %s\n" % self.GetItemText(item))


    def OnItemExpanding(self, event):

        item = event.GetItem()
        if item:
            self.log.write("OnItemExpanding: %s\n" % self.GetItemText(item))

        event.Skip()


    def OnItemCollapsed(self, event):

        item = event.GetItem()
        if item:
            self.log.write("OnItemCollapsed: %s" % self.GetItemText(item))


    def OnItemCollapsing(self, event):

        item = event.GetItem()
        if item:
            self.log.write("OnItemCollapsing: %s\n" % self.GetItemText(item))

        event.Skip()


    def OnSelChanged(self, event):

        self.item = event.GetItem()
        if self.item:
            self.log.write("OnSelChanged: %s" % self.GetItemText(self.item))
            if wx.Platform == '__WXMSW__':
                self.log.write(", BoundingRect: %s\n" % self.GetBoundingRect(self.item, True))
            else:
                self.log.write("\n")

        event.Skip()


    def OnSelChanging(self, event):

        item = event.GetItem()
        olditem = event.GetOldItem()

        if item:
            if not olditem:
                olditemtext = "None"
            else:
                olditemtext = self.GetItemText(olditem)
            self.log.write("OnSelChanging: From %s To %s\n" %(olditemtext, self.GetItemText(item)))

        event.Skip()


    def OnBeginDrag(self, event):

        self.item = event.GetItem()
        if self.item:
            self.log.write("Beginning Drag...\n")

            event.Allow()


    def OnBeginRDrag(self, event):

        self.item = event.GetItem()
        if self.item:
            self.log.write("Beginning Right Drag...\n")

            event.Allow()


    def OnEndDrag(self, event):

        self.item = event.GetItem()
        if self.item:
            self.log.write("Ending Drag!\n")

        event.Skip()


    def OnDeleteItem(self, event):

        item = event.GetItem()

        if not item:
            return

        self.log.write("Deleting Item: %s\n" % self.GetItemText(item))
        event.Skip()


    def OnItemCheck(self, event):

        item = event.GetItem()
        self.log.write("Item " + self.GetItemText(item) + " Has Been Cheched!\n")
        event.Skip()


    def OnItemChecking(self, event):

        item = event.GetItem()
        self.log.write("Item " + self.GetItemText(item) + " Is Being Checked...\n")
        event.Skip()


    def OnToolTip(self, event):

        item = event.GetItem()
        if item:
            event.SetToolTip(wx.ToolTip(self.GetItemText(item)))


    def OnItemMenu(self, event):

        item = event.GetItem()
        if item:
            self.log.write("OnItemMenu: %s\n" % self.GetItemText(item))

        event.Skip()


    def OnKey(self, event):

        keycode = event.GetKeyCode()
        keyname = keyMap.get(keycode, None)

        if keycode == wx.WXK_BACK:
            self.log.write("OnKeyDown: HAHAHAHA! I Vetoed Your Backspace! HAHAHAHA\n")
            return

        if keyname is None:
            if "unicode" in wx.PlatformInfo:
                keycode = event.GetUnicodeKey()
                if keycode <= 127:
                    keycode = event.GetKeyCode()
#                 keyname = "\"" + unichr(event.GetUnicodeKey()) + "\""
                keyname = "\"" + chr(event.GetUnicodeKey()) + "\""
                if keycode < 27:
                    keyname = "Ctrl-%s" % chr(ord('A') + keycode-1)

            elif keycode < 256:
                if keycode == 0:
                    keyname = "NUL"
                elif keycode < 27:
                    keyname = "Ctrl-%s" % chr(ord('A') + keycode-1)
                else:
                    keyname = "\"%s\"" % chr(keycode)
            else:
                keyname = "unknown (%s)" % keycode

        self.log.write("OnKeyDown: You Pressed '" + keyname + "'\n")

        event.Skip()


    def OnActivate(self, event):

        if self.item:
            self.log.write("OnActivate: %s\n" % self.GetItemText(self.item))

        event.Skip()


    def OnHyperLink(self, event):

        item = event.GetItem()
        if item:
            self.log.write("OnHyperLink: %s\n" % self.GetItemText(self.item))


    def OnTextCtrl(self, event):

        char = chr(event.GetKeyCode())
        self.log.write("EDITING THE TEXTCTRL: You Wrote '" + char + \
                       "' (KeyCode = " + str(event.GetKeyCode()) + ")\n")
        event.Skip()


    def OnComboBox(self, event):

        selection = event.GetEventObject().GetValue()
        self.log.write("CHOICE FROM COMBOBOX: You Chose '" + selection + "'\n")
        event.Skip()


#---------------------------------------------------------------------------


#----------------------------------------------------------------------
