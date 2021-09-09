import os
import wx
try:
    from agw import aui
    from agw.aui import aui_switcherdialog as ASD
except ImportError: # if it's not there locally, try the wxPython lib.
    import wx.lib.agw.aui as aui
    from wx.lib.agw.aui import aui_switcherdialog as ASD

XYVIEW_LIB_PATH = os.path.dirname(os.path.abspath(__file__))
XYVIEW_ICON_PATH = os.path.join(XYVIEW_LIB_PATH, "icon")
XYVIEW_BASE_PATH = os.path.join(XYVIEW_LIB_PATH, "base")

########################################################
# Default Color                                        #
########################################################
#DEFAULT_BACKGROUND_COLOR = wx.Colour(195,195,195)
DEFAULT_BACKGROUND_COLOR = wx.Colour(245,245,245)
DEFAULT_NOTICE_COLOR = wx.Colour(255,155,155)

########################################################
# Default Size                                        #
########################################################

DEFAULT_BUTTON_SIZE = wx.Size(75, 25)
DEFAULT_MINIFRAME_SIZE = wx.Size(650, 500)