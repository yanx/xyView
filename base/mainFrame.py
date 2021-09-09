#!/usr/bin/env python
import wx.html
import wx.grid
import datetime
import random

from xyTest.base.config_base import CONFIG_BASE
from xyTest.base.report_base import ReportBase
from xyTest.util.file_operation import OPERATION_FILE

from xyView.base.artImage import *
from xyView.base import images

# Define a translation function
_ = wx.GetTranslation

ID_CreateTree = wx.ID_HIGHEST + 1

ID_E = ID_CreateTree + 1
ID_A = ID_CreateTree + 2

ID_CreateHTML = ID_CreateTree + 3
ID_LogContent = ID_CreateTree + 6

ID_TextContent = ID_CreateTree + 7
ID_TreeContent = ID_CreateTree + 8
ID_HTMLContent = ID_CreateTree + 9
ID_NotebookContent = ID_CreateTree + 10
ID_SizeReportContent = ID_CreateTree + 11
ID_SwitchPane = ID_CreateTree + 12
ID_CreatePerspective = ID_CreateTree + 13
ID_CopyPerspectiveCode = ID_CreateTree + 14
ID_CreateNBPerspective = ID_CreateTree + 15
ID_CopyNBPerspectiveCode = ID_CreateTree + 16
ID_AllowFloating = ID_CreateTree + 17
ID_AllowActivePane = ID_CreateTree + 18
ID_TransparentHint = ID_CreateTree + 19
ID_VenetianBlindsHint = ID_CreateTree + 20
ID_RectangleHint = ID_CreateTree + 21
ID_NoHint = ID_CreateTree + 22
ID_HintFade = ID_CreateTree + 23
ID_NoVenetianFade = ID_CreateTree + 24
ID_TransparentDrag = ID_CreateTree + 25
ID_NoGradient = ID_CreateTree + 26
ID_VerticalGradient = ID_CreateTree + 27
ID_HorizontalGradient = ID_CreateTree + 28
ID_LiveUpdate = ID_CreateTree + 29
ID_AnimateFrames = ID_CreateTree + 30
ID_PaneIcons = ID_CreateTree + 31
ID_TransparentPane = ID_CreateTree + 32
ID_DefaultDockArt = ID_CreateTree + 33
ID_ModernDockArt = ID_CreateTree + 34
ID_SnapToScreen = ID_CreateTree + 35
ID_SnapPanes = ID_CreateTree + 36
ID_FlyOut = ID_CreateTree + 37
ID_CustomPaneButtons = ID_CreateTree + 38
ID_Settings = ID_CreateTree + 39
ID_CustomizeToolbar = ID_CreateTree + 40
ID_DropDownToolbarItem = ID_CreateTree + 41
ID_MinimizePosSmart = ID_CreateTree + 42
ID_MinimizePosTop = ID_CreateTree + 43
ID_MinimizePosLeft = ID_CreateTree + 44
ID_MinimizePosRight = ID_CreateTree + 45
ID_MinimizePosBottom = ID_CreateTree + 46
ID_MinimizeCaptSmart = ID_CreateTree + 47
ID_MinimizeCaptHorz = ID_CreateTree + 48
ID_MinimizeCaptHide = ID_CreateTree + 49

ID_NotebookNoCloseButton = ID_CreateTree + 50
ID_NotebookCloseButton = ID_CreateTree + 51
ID_NotebookCloseButtonAll = ID_CreateTree + 52
ID_NotebookCloseButtonActive = ID_CreateTree + 53
ID_NotebookCloseOnLeft = ID_CreateTree + 54
ID_NotebookAllowTabMove = ID_CreateTree + 55
ID_NotebookAllowTabExternalMove = ID_CreateTree + 56
ID_NotebookAllowTabSplit = ID_CreateTree + 57
ID_NotebookTabFloat = ID_CreateTree + 58
ID_NotebookTabDrawDnd = ID_CreateTree + 59
ID_NotebookDclickUnsplit = ID_CreateTree + 60
ID_NotebookWindowList = ID_CreateTree + 61
ID_NotebookScrollButtons = ID_CreateTree + 62
ID_NotebookTabFixedWidth = ID_CreateTree + 63
ID_NotebookArtGloss = ID_CreateTree + 64
ID_NotebookArtSimple = ID_CreateTree + 65
ID_NotebookArtVC71 = ID_CreateTree + 66
ID_NotebookArtFF2 = ID_CreateTree + 67
ID_NotebookArtVC8 = ID_CreateTree + 68
ID_NotebookArtChrome = ID_CreateTree + 69
ID_NotebookAlignTop = ID_CreateTree + 70
ID_NotebookAlignBottom = ID_CreateTree + 71
ID_NotebookHideSingle = ID_CreateTree + 72
ID_NotebookSmartTab = ID_CreateTree + 73
ID_NotebookUseImagesDropDown = ID_CreateTree + 74
ID_NotebookCustomButtons = ID_CreateTree + 75
ID_NotebookMinMaxWidth = ID_CreateTree + 76

ID_SampleItem = ID_CreateTree + 77
ID_StandardGuides = ID_CreateTree + 78
ID_AeroGuides = ID_CreateTree + 79
ID_WhidbeyGuides = ID_CreateTree + 80
ID_NotebookPreview = ID_CreateTree + 81
ID_PreviewMinimized = ID_CreateTree + 82

ID_SmoothDocking = ID_CreateTree + 83
ID_NativeMiniframes = ID_CreateTree + 84

ID_FirstPerspective = ID_CreatePerspective + 1000
ID_FirstNBPerspective = ID_CreateNBPerspective + 10000

ID_PaneBorderSize = ID_SampleItem + 100
ID_SashSize = ID_PaneBorderSize + 2
ID_CaptionSize = ID_PaneBorderSize + 3
ID_BackgroundColour = ID_PaneBorderSize + 4
ID_SashColour = ID_PaneBorderSize + 5
ID_InactiveCaptionColour = ID_PaneBorderSize + 6
ID_InactiveCaptionGradientColour = ID_PaneBorderSize + 7
ID_InactiveCaptionTextColour = ID_PaneBorderSize + 8
ID_ActiveCaptionColour = ID_PaneBorderSize + 9
ID_ActiveCaptionGradientColour = ID_PaneBorderSize + 10
ID_ActiveCaptionTextColour = ID_PaneBorderSize + 11
ID_BorderColour = ID_PaneBorderSize + 12
ID_GripperColour = ID_PaneBorderSize + 13
ID_SashGrip = ID_PaneBorderSize + 14
ID_HintColour = ID_PaneBorderSize + 15

ID_VetoTree = ID_PaneBorderSize + 16
ID_VetoText = ID_PaneBorderSize + 17
ID_NotebookMultiLine = ID_PaneBorderSize + 18


class SettingsPanel(wx.Panel):

    def __init__(self, parent, frame):

        wx.Panel.__init__(self, parent)
        self._frame = frame

        s1 = wx.BoxSizer(wx.HORIZONTAL)
        self._border_size = wx.SpinCtrl(self, ID_PaneBorderSize, "%d"%frame.GetDockArt().GetMetric(aui.AUI_DOCKART_PANE_BORDER_SIZE),
                                        wx.DefaultPosition, wx.Size(50, 20), wx.SP_ARROW_KEYS, 0, 100,
                                        frame.GetDockArt().GetMetric(aui.AUI_DOCKART_PANE_BORDER_SIZE))
        s1.Add((1, 1), 1, wx.EXPAND)
        s1.Add(wx.StaticText(self, -1, "Pane Border Size:"))
        s1.Add(self._border_size)
        s1.Add((1, 1), 1, wx.EXPAND)
        s1.SetItemMinSize(1, (180, 20))

        s2 = wx.BoxSizer(wx.HORIZONTAL)
        self._sash_size = wx.SpinCtrl(self, ID_SashSize, "%d"%frame.GetDockArt().GetMetric(aui.AUI_DOCKART_SASH_SIZE), wx.DefaultPosition,
                                      wx.Size(50, 20), wx.SP_ARROW_KEYS, 0, 100, frame.GetDockArt().GetMetric(aui.AUI_DOCKART_SASH_SIZE))
        s2.Add((1, 1), 1, wx.EXPAND)
        s2.Add(wx.StaticText(self, -1, "Sash Size:"))
        s2.Add(self._sash_size)
        s2.Add((1, 1), 1, wx.EXPAND)
        s2.SetItemMinSize(1, (180, 20))

        s3 = wx.BoxSizer(wx.HORIZONTAL)
        self._caption_size = wx.SpinCtrl(self, ID_CaptionSize, "%d"%frame.GetDockArt().GetMetric(aui.AUI_DOCKART_CAPTION_SIZE),
                                         wx.DefaultPosition, wx.Size(50, 20), wx.SP_ARROW_KEYS, 0, 100, frame.GetDockArt().GetMetric(aui.AUI_DOCKART_CAPTION_SIZE))
        s3.Add((1, 1), 1, wx.EXPAND)
        s3.Add(wx.StaticText(self, -1, "Caption Size:"))
        s3.Add(self._caption_size)
        s3.Add((1, 1), 1, wx.EXPAND)
        s3.SetItemMinSize(1, (180, 20))

        b = self.CreateColourBitmap(wx.BLACK)

        s4 = wx.BoxSizer(wx.HORIZONTAL)
        self._background_colour = wx.BitmapButton(self, ID_BackgroundColour, b, wx.DefaultPosition, wx.Size(50, 25))
        s4.Add((1, 1), 1, wx.EXPAND)
        s4.Add(wx.StaticText(self, -1, "Background Colour:"))
        s4.Add(self._background_colour)
        s4.Add((1, 1), 1, wx.EXPAND)
        s4.SetItemMinSize(1, (180, 20))

        s5 = wx.BoxSizer(wx.HORIZONTAL)
        self._sash_colour = wx.BitmapButton(self, ID_SashColour, b, wx.DefaultPosition, wx.Size(50, 25))
        s5.Add((1, 1), 1, wx.EXPAND)
        s5.Add(wx.StaticText(self, -1, "Sash Colour:"))
        s5.Add(self._sash_colour)
        s5.Add((1, 1), 1, wx.EXPAND)
        s5.SetItemMinSize(1, (180, 20))

        s6 = wx.BoxSizer(wx.HORIZONTAL)
        self._inactive_caption_colour = wx.BitmapButton(self, ID_InactiveCaptionColour, b, wx.DefaultPosition, wx.Size(50, 25))
        s6.Add((1, 1), 1, wx.EXPAND)
        s6.Add(wx.StaticText(self, -1, "Normal Caption:"))
        s6.Add(self._inactive_caption_colour)
        s6.Add((1, 1), 1, wx.EXPAND)
        s6.SetItemMinSize(1, (180, 20))

        s7 = wx.BoxSizer(wx.HORIZONTAL)
        self._inactive_caption_gradient_colour = wx.BitmapButton(self, ID_InactiveCaptionGradientColour, b, wx.DefaultPosition, wx.Size(50, 25))
        s7.Add((1, 1), 1, wx.EXPAND)
        s7.Add(wx.StaticText(self, -1, "Normal Caption Gradient:"))
        s7.Add(self._inactive_caption_gradient_colour)
        s7.Add((1, 1), 1, wx.EXPAND)
        s7.SetItemMinSize(1, (180, 20))

        s8 = wx.BoxSizer(wx.HORIZONTAL)
        self._inactive_caption_text_colour = wx.BitmapButton(self, ID_InactiveCaptionTextColour, b, wx.DefaultPosition, wx.Size(50, 25))
        s8.Add((1, 1), 1, wx.EXPAND)
        s8.Add(wx.StaticText(self, -1, "Normal Caption Text:"))
        s8.Add(self._inactive_caption_text_colour)
        s8.Add((1, 1), 1, wx.EXPAND)
        s8.SetItemMinSize(1, (180, 20))

        s9 = wx.BoxSizer(wx.HORIZONTAL)
        self._active_caption_colour = wx.BitmapButton(self, ID_ActiveCaptionColour, b, wx.DefaultPosition, wx.Size(50, 25))
        s9.Add((1, 1), 1, wx.EXPAND)
        s9.Add(wx.StaticText(self, -1, "Active Caption:"))
        s9.Add(self._active_caption_colour)
        s9.Add((1, 1), 1, wx.EXPAND)
        s9.SetItemMinSize(1, (180, 20))

        s10 = wx.BoxSizer(wx.HORIZONTAL)
        self._active_caption_gradient_colour = wx.BitmapButton(self, ID_ActiveCaptionGradientColour, b, wx.DefaultPosition, wx.Size(50, 25))
        s10.Add((1, 1), 1, wx.EXPAND)
        s10.Add(wx.StaticText(self, -1, "Active Caption Gradient:"))
        s10.Add(self._active_caption_gradient_colour)
        s10.Add((1, 1), 1, wx.EXPAND)
        s10.SetItemMinSize(1, (180, 20))

        s11 = wx.BoxSizer(wx.HORIZONTAL)
        self._active_caption_text_colour = wx.BitmapButton(self, ID_ActiveCaptionTextColour, b, wx.DefaultPosition, wx.Size(50, 25))
        s11.Add((1, 1), 1, wx.EXPAND)
        s11.Add(wx.StaticText(self, -1, "Active Caption Text:"))
        s11.Add(self._active_caption_text_colour)
        s11.Add((1, 1), 1, wx.EXPAND)
        s11.SetItemMinSize(1, (180, 20))

        s12 = wx.BoxSizer(wx.HORIZONTAL)
        self._border_colour = wx.BitmapButton(self, ID_BorderColour, b, wx.DefaultPosition, wx.Size(50, 25))
        s12.Add((1, 1), 1, wx.EXPAND)
        s12.Add(wx.StaticText(self, -1, "Border Colour:"))
        s12.Add(self._border_colour)
        s12.Add((1, 1), 1, wx.EXPAND)
        s12.SetItemMinSize(1, (180, 20))

        s13 = wx.BoxSizer(wx.HORIZONTAL)
        self._gripper_colour = wx.BitmapButton(self, ID_GripperColour, b, wx.DefaultPosition, wx.Size(50,25))
        s13.Add((1, 1), 1, wx.EXPAND)
        s13.Add(wx.StaticText(self, -1, "Gripper Colour:"))
        s13.Add(self._gripper_colour)
        s13.Add((1, 1), 1, wx.EXPAND)
        s13.SetItemMinSize(1, (180, 20))

        s14 = wx.BoxSizer(wx.HORIZONTAL)
        self._sash_grip = wx.CheckBox(self, ID_SashGrip, "", wx.DefaultPosition, wx.Size(50,20))
        s14.Add((1, 1), 1, wx.EXPAND)
        s14.Add(wx.StaticText(self, -1, "Draw Sash Grip:"))
        s14.Add(self._sash_grip)
        s14.Add((1, 1), 1, wx.EXPAND)
        s14.SetItemMinSize(1, (180, 20))

        s15 = wx.BoxSizer(wx.HORIZONTAL)
        self._hint_colour = wx.BitmapButton(self, ID_HintColour, b, wx.DefaultPosition, wx.Size(50,25))
        s15.Add((1, 1), 1, wx.EXPAND)
        s15.Add(wx.StaticText(self, -1, "Hint Window Colour:"))
        s15.Add(self._hint_colour)
        s15.Add((1, 1), 1, wx.EXPAND)
        s15.SetItemMinSize(1, (180, 20))

        grid_sizer = wx.GridSizer(rows=0, cols=2, vgap=5, hgap=5)
        grid_sizer.SetHGap(5)
        grid_sizer.Add(s1)
        grid_sizer.Add(s4)
        grid_sizer.Add(s2)
        grid_sizer.Add(s5)
        grid_sizer.Add(s3)
        grid_sizer.Add(s13)
        grid_sizer.Add(s14)
        grid_sizer.Add((1, 1))
        grid_sizer.Add(s12)
        grid_sizer.Add(s6)
        grid_sizer.Add(s9)
        grid_sizer.Add(s7)
        grid_sizer.Add(s10)
        grid_sizer.Add(s8)
        grid_sizer.Add(s11)
        grid_sizer.Add(s15)

        cont_sizer = wx.BoxSizer(wx.VERTICAL)
        cont_sizer.Add(grid_sizer, 1, wx.EXPAND | wx.ALL, 5)
        self.SetSizer(cont_sizer)
        self.GetSizer().SetSizeHints(self)

        self._border_size.SetValue(frame.GetDockArt().GetMetric(aui.AUI_DOCKART_PANE_BORDER_SIZE))
        self._sash_size.SetValue(frame.GetDockArt().GetMetric(aui.AUI_DOCKART_SASH_SIZE))
        self._caption_size.SetValue(frame.GetDockArt().GetMetric(aui.AUI_DOCKART_CAPTION_SIZE))
        self._sash_grip.SetValue(frame.GetDockArt().GetMetric(aui.AUI_DOCKART_DRAW_SASH_GRIP))

        self.UpdateColours()

        self.Bind(wx.EVT_SPINCTRL, self.OnPaneBorderSize, id=ID_PaneBorderSize)
        self.Bind(wx.EVT_SPINCTRL, self.OnSashSize, id=ID_SashSize)
        self.Bind(wx.EVT_SPINCTRL, self.OnCaptionSize, id=ID_CaptionSize)
        self.Bind(wx.EVT_CHECKBOX, self.OnDrawSashGrip, id=ID_SashGrip)
        self.Bind(wx.EVT_BUTTON, self.OnSetColour, id=ID_BackgroundColour)
        self.Bind(wx.EVT_BUTTON, self.OnSetColour, id=ID_SashColour)
        self.Bind(wx.EVT_BUTTON, self.OnSetColour, id=ID_InactiveCaptionColour)
        self.Bind(wx.EVT_BUTTON, self.OnSetColour, id=ID_InactiveCaptionGradientColour)
        self.Bind(wx.EVT_BUTTON, self.OnSetColour, id=ID_InactiveCaptionTextColour)
        self.Bind(wx.EVT_BUTTON, self.OnSetColour, id=ID_ActiveCaptionColour)
        self.Bind(wx.EVT_BUTTON, self.OnSetColour, id=ID_ActiveCaptionGradientColour)
        self.Bind(wx.EVT_BUTTON, self.OnSetColour, id=ID_ActiveCaptionTextColour)
        self.Bind(wx.EVT_BUTTON, self.OnSetColour, id=ID_BorderColour)
        self.Bind(wx.EVT_BUTTON, self.OnSetColour, id=ID_GripperColour)
        self.Bind(wx.EVT_BUTTON, self.OnSetColour, id=ID_HintColour)


    def CreateColourBitmap(self, c):

        image = wx.Image(25, 14)
        for x in range(25):
            for y in range(14):
                pixcol = c
                if x == 0 or x == 24 or y == 0 or y == 13:
                    pixcol = wx.BLACK

                image.SetRGB(wx.Rect(wx.Size(25, 14)), pixcol.Red(), pixcol.Green(), pixcol.Blue())

        return image.ConvertToBitmap()


    def UpdateColours(self):

        bk = self._frame.GetDockArt().GetColour(aui.AUI_DOCKART_BACKGROUND_COLOUR)
        self._background_colour.SetBitmapLabel(self.CreateColourBitmap(bk))

        cap = self._frame.GetDockArt().GetColour(aui.AUI_DOCKART_INACTIVE_CAPTION_COLOUR)
        self._inactive_caption_colour.SetBitmapLabel(self.CreateColourBitmap(cap))

        capgrad = self._frame.GetDockArt().GetColour(aui.AUI_DOCKART_INACTIVE_CAPTION_GRADIENT_COLOUR)
        self._inactive_caption_gradient_colour.SetBitmapLabel(self.CreateColourBitmap(capgrad))

        captxt = self._frame.GetDockArt().GetColour(aui.AUI_DOCKART_INACTIVE_CAPTION_TEXT_COLOUR)
        self._inactive_caption_text_colour.SetBitmapLabel(self.CreateColourBitmap(captxt))

        acap = self._frame.GetDockArt().GetColour(aui.AUI_DOCKART_ACTIVE_CAPTION_COLOUR)
        self._active_caption_colour.SetBitmapLabel(self.CreateColourBitmap(acap))

        acapgrad = self._frame.GetDockArt().GetColour(aui.AUI_DOCKART_ACTIVE_CAPTION_GRADIENT_COLOUR)
        self._active_caption_gradient_colour.SetBitmapLabel(self.CreateColourBitmap(acapgrad))

        acaptxt = self._frame.GetDockArt().GetColour(aui.AUI_DOCKART_ACTIVE_CAPTION_TEXT_COLOUR)
        self._active_caption_text_colour.SetBitmapLabel(self.CreateColourBitmap(acaptxt))

        sash = self._frame.GetDockArt().GetColour(aui.AUI_DOCKART_SASH_COLOUR)
        self._sash_colour.SetBitmapLabel(self.CreateColourBitmap(sash))

        border = self._frame.GetDockArt().GetColour(aui.AUI_DOCKART_BORDER_COLOUR)
        self._border_colour.SetBitmapLabel(self.CreateColourBitmap(border))

        gripper = self._frame.GetDockArt().GetColour(aui.AUI_DOCKART_GRIPPER_COLOUR)
        self._gripper_colour.SetBitmapLabel(self.CreateColourBitmap(gripper))

        hint = self._frame.GetDockArt().GetColour(aui.AUI_DOCKART_HINT_WINDOW_COLOUR)
        self._hint_colour.SetBitmapLabel(self.CreateColourBitmap(hint))


    def OnPaneBorderSize(self, event):

        self._frame.GetDockArt().SetMetric(aui.AUI_DOCKART_PANE_BORDER_SIZE,
                                           event.GetInt())
        self._frame.DoUpdate()


    def OnSashSize(self, event):

        self._frame.GetDockArt().SetMetric(aui.AUI_DOCKART_SASH_SIZE,
                                           event.GetInt())
        self._frame.DoUpdate()


    def OnCaptionSize(self, event):

        self._frame.GetDockArt().SetMetric(aui.AUI_DOCKART_CAPTION_SIZE,
                                           event.GetInt())
        self._frame.DoUpdate()


    def OnDrawSashGrip(self, event):

        self._frame.GetDockArt().SetMetric(aui.AUI_DOCKART_DRAW_SASH_GRIP,
                                           event.GetInt())
        self._frame.DoUpdate()


    def OnSetColour(self, event):

        dlg = wx.ColourDialog(self._frame)
        dlg.SetTitle("Colour Picker")

        if dlg.ShowModal() != wx.ID_OK:
            return

        evId = event.GetId()
        if evId == ID_BackgroundColour:
            var = aui.AUI_DOCKART_BACKGROUND_COLOUR
        elif evId == ID_SashColour:
            var = aui.AUI_DOCKART_SASH_COLOUR
        elif evId == ID_InactiveCaptionColour:
            var = aui.AUI_DOCKART_INACTIVE_CAPTION_COLOUR
        elif evId == ID_InactiveCaptionGradientColour:
            var = aui.AUI_DOCKART_INACTIVE_CAPTION_GRADIENT_COLOUR
        elif evId == ID_InactiveCaptionTextColour:
            var = aui.AUI_DOCKART_INACTIVE_CAPTION_TEXT_COLOUR
        elif evId == ID_ActiveCaptionColour:
            var = aui.AUI_DOCKART_ACTIVE_CAPTION_COLOUR
        elif evId == ID_ActiveCaptionGradientColour:
            var = aui.AUI_DOCKART_ACTIVE_CAPTION_GRADIENT_COLOUR
        elif evId == ID_ActiveCaptionTextColour:
            var = aui.AUI_DOCKART_ACTIVE_CAPTION_TEXT_COLOUR
        elif evId == ID_BorderColour:
            var = aui.AUI_DOCKART_BORDER_COLOUR
        elif evId == ID_GripperColour:
            var = aui.AUI_DOCKART_GRIPPER_COLOUR
        elif evId == ID_HintColour:
            var = aui.AUI_DOCKART_HINT_WINDOW_COLOUR
        else:
            return

        self._frame.GetDockArt().SetColour(var, dlg.GetColourData().GetColour())
        self._frame.DoUpdate()
        self.UpdateColours()


class AdminFrame(wx.Frame):

    def __init__(self, parent, id=wx.ID_ANY, title="", pos= wx.DefaultPosition,
                 size=wx.DefaultSize, style=wx.DEFAULT_FRAME_STYLE|wx.SUNKEN_BORDER, log=None):

        wx.Frame.__init__(self, parent, id, title, pos, size, style)
        
        self._mgr = aui.AuiManager()
        # tell AuiManager to manage this frame
        self._mgr.SetManagedWindow(self)

        # set frame icon
        self.SetIcon(images.Mondrian.GetIcon())

        # set up default notebook style
        self._notebook_style = aui.AUI_NB_DEFAULT_STYLE | aui.AUI_NB_TAB_EXTERNAL_MOVE | wx.NO_BORDER
        self._notebook_theme = 0
        # Attributes
        self._textCount = 1
        self._transparency = 255
        self._snapped = False
        self._custom_pane_buttons = False
        self._custom_tab_buttons = False
        self._pane_icons = False
        self._veto_tree = self._veto_text = False

        self.log = log

        self.CreateStatusBar()
        self.GetStatusBar().SetStatusText("Ready")

        self.BuildPanes()
        self.CreateMenuBar()
        self.BindEvents()
        self.log.write("In log page")


    def CreateMenuBar(self):

        # create menu
        mb = wx.MenuBar()

        file_menu = wx.Menu()
        file_menu.Append(ID_E, "Exit")

        view_menu = wx.Menu()
        
        view_menu.AppendSeparator()
        view_menu.Append(ID_LogContent, "Show Log Content Pane")
        view_menu.Append(ID_NotebookContent, "Show Config Content Pane")
        view_menu.AppendSeparator()
        view_menu.Append(ID_Settings, "Settings Pane")


        help_menu = wx.Menu()
        help_menu.Append(ID_A, "About...")

        mb.Append(file_menu, "&File")
        mb.Append(view_menu, "&View")
#         mb.Append(notebook_menu, "&Notebook")
        mb.Append(help_menu, "&Help")

        self.SetMenuBar(mb)

    def own_tool_bar(self, tb, tbmp): pass
    def BuildPanes(self):

        # min size for the frame itself isn't completely done.
        # see the end up AuiManager.Update() for the test
        # code. For now, just hard code a frame minimum size
        self.SetMinSize(wx.Size(400, 300))

        # create a toolbars

        tb4 = aui.AuiToolBar(self, -1, wx.DefaultPosition, wx.DefaultSize,
                             agwStyle=aui.AUI_TB_OVERFLOW | aui.AUI_TB_TEXT | aui.AUI_TB_HORZ_TEXT)
        tb4.SetToolBitmapSize(wx.Size(16, 16))
        tb4_bmp1 = wx.ArtProvider.GetBitmap(wx.ART_NORMAL_FILE, wx.ART_OTHER, wx.Size(16, 16))
#         tb4.AddSimpleTool(ID_DropDownToolbarItem, "Item 1", tb4_bmp1)
        
        self.own_tool_bar(tb4, tb4_bmp1)
#         tb4.AddSimpleTool(ID_SampleItem+23, "Run Test", tb4_bmp1)
#         tb4.AddSimpleTool(ID_SampleItem+24, "Show Log", tb4_bmp1)
#         tb4.AddSimpleTool(ID_SampleItem+25, "Show Config", tb4_bmp1)
#         tb4.AddSeparator()
# #         tb4.AddSimpleTool(ID_SampleItem+26, "Item 5", tb4_bmp1)
# #         tb4.AddSimpleTool(ID_SampleItem+27, "Item 6", tb4_bmp1)
# 
#         self.l_env = wx.Choice(tb4, -1, choices=self.lst_all_env)
#         tb4.AddControl(self.l_env, "env")
#         tb4.AddSeparator()
#         self.l_report = wx.Choice(tb4, -1, choices=["show report", "send report", "send + show", "nothing"])
#         tb4.AddControl(self.l_report, "report")
#         tb4.AddSeparator()
#         self.l_browser = wx.Choice(tb4, -1, choices=["chrome", "firefox", "safari"])
#         tb4.AddControl(self.l_browser, "browser")
#         tb4.AddSeparator()
#         self.l_view = wx.Choice(tb4, -1, choices=["view", "headless"])
#         tb4.AddControl(self.l_view, "view")
#         
#         
# #         tb4.SetToolDropDown(ID_DropDownToolbarItem, True)
#         tb4.Realize()
# 
# 
#         # add a bunch of panes
#         self.panel_tree = VicunaTreeList(self, self.dic_session, -1, log=self.log)
#         
#         self._mgr.AddPane(self.panel_tree, aui.AuiPaneInfo().Name("casetree").Caption("Case-Tree").
#                           Left().Layer(1).Position(1).MinSize((240, -1)).CloseButton(True).MaximizeButton(True).
#                           MinimizeButton(True))
#         
#         self._mgr.AddPane(self.CreateTextCtrl(self.text_root_readme()), aui.AuiPaneInfo().
#                           Name("autonotebook").Caption("Readme").
#                           Bottom().Layer(1).Position(1).MinimizeButton(True))
# 
# #         print ('CONFIG_BASE.dic_lib_category = ', CONFIG_BASE.dic_lib_category)
#         for k, v in CONFIG_BASE.dic_lib_category.items():
#             if (k in self.lst_current_category) and v['readme']:
# #             if v['readme']:
#                 newpage = self.CreateTextCtrl(v['readme'])
#                 new_name = k+"-readme"
#                 self._mgr.AddPane(newpage, aui.AuiPaneInfo().
#                                   Name(new_name).Caption(new_name).
#                                   Bottom().MinimizeButton(True), target=self._mgr.GetPane("autonotebook"))


        self._mgr.AddPane(SettingsPanel(self,self), aui.AuiPaneInfo().
                          Name("settings").Caption("Dock Manager Settings").
                          Dockable(False).Float().Hide().MinimizeButton(True))

        # create some center panes

        # Set up a log window
        self.panel_log = wx.TextCtrl(self, -1,
                              style = wx.TE_MULTILINE|wx.TE_READONLY|wx.HSCROLL)
        if wx.Platform == "__WXMAC__":
            self.panel_log.MacCheckSpelling(False)

        # Set the wxWindows log target to be this textctrl
        wx.Log.SetActiveTarget(wx.LogTextCtrl(self.panel_log))
        self._mgr.AddPane(self.panel_log, aui.AuiPaneInfo().Name("log_content").
                          CenterPane().Hide().MinimizeButton(True))
        
        print ("self._mgr.AddPane(self.CreateNotebook()," * 20)

        self._mgr.AddPane(self.CreateNotebook(), aui.AuiPaneInfo().Name("config_content").
                          CenterPane().PaneBorder(False))

        # add the toolbars to the manager


        self._mgr.AddPane(tb4, aui.AuiPaneInfo().Name("tb4").Caption("Toolbar").
                          ToolbarPane().Top().Row(2))
        
        # Show how to add a control inside a tab
        notebook = self._mgr.GetPane("config_content").window
#         self.gauge = ProgressGauge(notebook, size=(55, 15))
#         notebook.AddControlToPage(4, self.gauge)

        self._main_notebook = notebook

        # make some default perspectives
        perspective_all = self._mgr.SavePerspective()

        all_panes = self._mgr.GetAllPanes()
        for pane in all_panes:
            if not pane.IsToolbar():
                pane.Hide()


        self._mgr.GetPane("casetree").Show().Left().Layer(0).Row(0).Position(0)
        self._mgr.GetPane("__notebook_%d"%self._mgr.GetPane("whimmade-readme").notebook_id).Show().Bottom().Layer(0).Row(0).Position(0)
        self._mgr.GetPane("autonotebook").Show()
#         self._mgr.GetPane("thirdauto").Show()
        self._mgr.GetPane("whimmade-readme").Show()
#         self._mgr.GetPane("config_content").Show()
        self._mgr.GetPane("log_content").Show()
        
#         self._mgr.GetPane("settings").Show()
#         

        perspective_default = self._mgr.SavePerspective()

        self._perspectives = []
        self._perspectives.append(perspective_default)
        self._perspectives.append(perspective_all)

        self._nb_perspectives = []
        auibook = self._mgr.GetPane("config_content").window
        print ("auibook = ", auibook)
        nb_perspective_default = auibook.SavePerspective()
        self._nb_perspectives.append(nb_perspective_default)

        self._mgr.LoadPerspective(perspective_default)

        # Show how to get a custom minimizing behaviour, i.e., to minimize a pane
        # inside an existing AuiToolBar
        tree = self._mgr.GetPane("casetree")
        tree.MinimizeMode(aui.AUI_MINIMIZE_POS_TOOLBAR)
        toolbarPane = self._mgr.GetPane(tb4)
        tree.MinimizeTarget(toolbarPane)

        # "commit" all changes made to AuiManager
        self._mgr.Update()

# 
#         for i in range (100):
#             self.log.write("dooooooooooooooooo - /n"*100)


    def own_bind_events(self): pass
    def BindEvents(self):

        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
        self.Bind(wx.EVT_SIZE, self.OnSize)

#         self.Bind(wx.EVT_MENU, self.OnCreateHTML, id=ID_CreateHTML)

        self.own_bind_events()
#         self.Bind(wx.EVT_MENU, self.OnRunTest, id=ID_SampleItem+23)
#         self.Bind(wx.EVT_MENU, self.OnChangeContentPane, id=ID_SampleItem+24)
#         self.Bind(wx.EVT_MENU, self.OnChangeContentPane, id=ID_SampleItem+25)
# #         self.Bind(wx.EVT_MENU, self.OntopTool, id=ID_SampleItem+26)
# #         self.Bind(wx.EVT_MENU, self.OntopTool, id=ID_SampleItem+27)
        
        self.Bind(wx.EVT_MENU, self.OnNotebookFlag, id=ID_NotebookTabFixedWidth)
        self.Bind(wx.EVT_MENU, self.OnNotebookFlag, id=ID_NotebookNoCloseButton)
        self.Bind(wx.EVT_MENU, self.OnNotebookFlag, id=ID_NotebookCloseButton)
        self.Bind(wx.EVT_MENU, self.OnNotebookFlag, id=ID_NotebookCloseButtonAll)
        self.Bind(wx.EVT_MENU, self.OnNotebookFlag, id=ID_NotebookCloseButtonActive)
        self.Bind(wx.EVT_MENU, self.OnNotebookFlag, id=ID_NotebookAllowTabMove)
        self.Bind(wx.EVT_MENU, self.OnNotebookFlag, id=ID_NotebookAllowTabExternalMove)
        self.Bind(wx.EVT_MENU, self.OnNotebookFlag, id=ID_NotebookAllowTabSplit)
        self.Bind(wx.EVT_MENU, self.OnNotebookFlag, id=ID_NotebookTabFloat)
        self.Bind(wx.EVT_MENU, self.OnNotebookFlag, id=ID_NotebookDclickUnsplit)
        self.Bind(wx.EVT_MENU, self.OnNotebookFlag, id=ID_NotebookTabDrawDnd)
        self.Bind(wx.EVT_MENU, self.OnNotebookFlag, id=ID_NotebookScrollButtons)
        self.Bind(wx.EVT_MENU, self.OnNotebookFlag, id=ID_NotebookWindowList)
        self.Bind(wx.EVT_MENU, self.OnNotebookFlag, id=ID_NotebookArtGloss)
        self.Bind(wx.EVT_MENU, self.OnNotebookFlag, id=ID_NotebookArtSimple)
        self.Bind(wx.EVT_MENU, self.OnNotebookFlag, id=ID_NotebookArtVC71)
        self.Bind(wx.EVT_MENU, self.OnNotebookFlag, id=ID_NotebookArtFF2)
        self.Bind(wx.EVT_MENU, self.OnNotebookFlag, id=ID_NotebookArtVC8)
        self.Bind(wx.EVT_MENU, self.OnNotebookFlag, id=ID_NotebookArtChrome)
        self.Bind(wx.EVT_MENU, self.OnNotebookFlag, id=ID_NotebookHideSingle)
        self.Bind(wx.EVT_MENU, self.OnNotebookFlag, id=ID_NotebookSmartTab)
        self.Bind(wx.EVT_MENU, self.OnNotebookFlag, id=ID_NotebookUseImagesDropDown)
        self.Bind(wx.EVT_MENU, self.OnNotebookFlag, id=ID_NotebookCloseOnLeft)
        self.Bind(wx.EVT_MENU, self.OnTabAlignment, id=ID_NotebookAlignTop)
        self.Bind(wx.EVT_MENU, self.OnTabAlignment, id=ID_NotebookAlignBottom)
        self.Bind(wx.EVT_MENU, self.OnCustomTabButtons, id=ID_NotebookCustomButtons)
        self.Bind(wx.EVT_MENU, self.OnMinMaxTabWidth, id=ID_NotebookMinMaxWidth)
        self.Bind(wx.EVT_MENU, self.OnPreview, id=ID_NotebookPreview)
        self.Bind(wx.EVT_MENU, self.OnAddMultiLine, id=ID_NotebookMultiLine)

        self.Bind(wx.EVT_MENU, self.OnSettings, id=ID_Settings)
        self.Bind(wx.EVT_MENU, self.OnChangeContentPane, id=ID_LogContent)
        self.Bind(wx.EVT_MENU, self.OnChangeContentPane, id=ID_NotebookContent)


        self.Bind(wx.EVT_MENU, self.OnExit, id=ID_E)
        self.Bind(wx.EVT_MENU, self.OnAbout, id=ID_A)

        self.Bind(wx.EVT_MENU_RANGE, self.OnRestorePerspective, id=ID_FirstPerspective,
                  id2=ID_FirstPerspective+1000)
        self.Bind(wx.EVT_MENU_RANGE, self.OnRestoreNBPerspective, id=ID_FirstNBPerspective,
                  id2=ID_FirstNBPerspective+1000)

        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_AllowFloating)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_TransparentHint)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_HintFade)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_TransparentDrag)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_NoGradient)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_VerticalGradient)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_HorizontalGradient)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_VenetianBlindsHint)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_RectangleHint)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_NoHint)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_NoVenetianFade)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_LiveUpdate)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_PaneIcons)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_AnimateFrames)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_DefaultDockArt)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_ModernDockArt)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_SnapPanes)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_FlyOut)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_CustomPaneButtons)

        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_NotebookTabFixedWidth)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_NotebookNoCloseButton)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_NotebookCloseButton)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_NotebookCloseButtonAll)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_NotebookCloseButtonActive)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_NotebookAllowTabMove)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_NotebookAllowTabExternalMove)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_NotebookAllowTabSplit)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_NotebookTabFloat)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_NotebookDclickUnsplit)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_NotebookTabDrawDnd)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_NotebookScrollButtons)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_NotebookWindowList)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_NotebookHideSingle)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_NotebookSmartTab)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_NotebookUseImagesDropDown)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_NotebookCustomButtons)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_VetoTree)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_VetoText)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_StandardGuides)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_AeroGuides)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_WhidbeyGuides)


        self.Bind(aui.EVT_AUITOOLBAR_TOOL_DROPDOWN, self.OnDropDownToolbarItem, id=ID_DropDownToolbarItem)
        self.Bind(aui.EVT_AUI_PANE_CLOSE, self.OnPaneClose)
        self.Bind(aui.EVT_AUINOTEBOOK_ALLOW_DND, self.OnAllowNotebookDnD)
        self.Bind(aui.EVT_AUINOTEBOOK_PAGE_CLOSE, self.OnNotebookPageClose)

        self.Bind(aui.EVT_AUI_PANE_FLOATING, self.OnFloatDock)
        self.Bind(aui.EVT_AUI_PANE_FLOATED, self.OnFloatDock)
        self.Bind(aui.EVT_AUI_PANE_DOCKING, self.OnFloatDock)
        self.Bind(aui.EVT_AUI_PANE_DOCKED, self.OnFloatDock)

        self.Bind(wx.EVT_CLOSE, self.OnClose)

#         self.Bind(wx.EVT_TIMER, self.TimerHandler)
        self.timer = wx.Timer(self)
        self.timer.Start(100)


    def __del__(self):

        self.timer.Stop()



    def SetTest(self): pass
    def get_string_choice(self, obj): pass
    def set_test_option(self): pass
    def OnRunTest(self, event): pass
         
         
    def CreateHTMLReport(self, msg, name):

        ctrl = wx.html.HtmlWindow(self, -1, wx.DefaultPosition, wx.Size(600, 500))
        ctrl.SetPage(msg)
        self._mgr.AddPane(ctrl, aui.AuiPaneInfo().
                          Caption(name).
                          Float().FloatingPosition(self.GetStartPosition()).
                          FloatingSize(wx.Size(600, 500)).MinimizeButton(True))
        self._mgr.Update()

         
         
         
    def message_command(self, level, msg=' -No Message-', e=None):
        OPERATION_FILE.message_command(self, level, msg, e)
        self.log.write('%s - %s ' % (level, msg))
#         print msg


    def OnClose(self, event):

        self.timer.Stop()
        self._mgr.UnInit()
        event.Skip()


#     def TimerHandler(self, event):
# 
#         try:
#             self.gauge.Pulse()
#         except:
#             self.timer.Stop()


    def GetDockArt(self):

        return self._mgr.GetArtProvider()


    def DoUpdate(self):

        self._mgr.Update()
        self.Refresh()


    def OnEraseBackground(self, event):

        event.Skip()


    def OnSize(self, event):

        event.Skip()


    def OnSettings(self, event):

        # show the settings pane, and float it
        floating_pane = self._mgr.GetPane("settings").Float().Show()

        if floating_pane.floating_pos == wx.DefaultPosition:
            floating_pane.FloatingPosition(self.GetStartPosition())

        self._mgr.Update()


    def OnPreviewMinimized(self, event):

        checked = event.IsChecked()
        agwFlags = self._mgr.GetAGWFlags()

        if event.IsChecked():
            agwFlags ^= aui.AUI_MGR_PREVIEW_MINIMIZED_PANES
        else:
            agwFlags &= ~aui.AUI_MGR_PREVIEW_MINIMIZED_PANES

        self._mgr.SetAGWFlags(agwFlags)


    def OnSetIconsOnPanes(self, event):

        panes = self._mgr.GetAllPanes()
        checked = event.IsChecked()
        self._pane_icons = checked

        for pane in panes:
            if checked:
                randimage = random.randint(0, len(ArtIDs) - 1)
                bmp = wx.ArtProvider.GetBitmap(eval(ArtIDs[randimage]), wx.ART_OTHER, (16, 16))
            else:
                bmp = None

            pane.Icon(bmp)

        self._mgr.Update()


    def OnTransparentPane(self, event):

        dlg = wx.TextEntryDialog(self, "Enter a transparency value (0-255):", "Pane transparency")

        dlg.SetValue("%d"%self._transparency)
        if dlg.ShowModal() != wx.ID_OK:
            return

        transparency = int(dlg.GetValue())
        dlg.Destroy()
        try:
            transparency = int(transparency)
        except:
            dlg = wx.MessageDialog(self, 'Invalid transparency value. Transparency' \
                                   ' should be an integer between 0 and 255.',
                                   'Error',
                                   wx.OK | wx.ICON_ERROR)
            dlg.ShowModal()
            dlg.Destroy()
            return

        if transparency < 0 or transparency > 255:
            dlg = wx.MessageDialog(self, 'Invalid transparency value. Transparency' \
                                   ' should be an integer between 0 and 255.',
                                   'Error',
                                   wx.OK | wx.ICON_ERROR)
            dlg.ShowModal()
            dlg.Destroy()
            return

        self._transparency = transparency
        panes = self._mgr.GetAllPanes()
        for pane in panes:
            pane.Transparent(self._transparency)

        self._mgr.Update()


    def OnDockArt(self, event):

        if event.GetId() == ID_DefaultDockArt:
            self._mgr.SetArtProvider(aui.AuiDefaultDockArt())
        else:
            if self._mgr.CanUseModernDockArt():
                self._mgr.SetArtProvider(aui.ModernDockArt(self))

        self._mgr.Update()
        self.Refresh()


    def OnSnapToScreen(self, event):

        self._mgr.SnapToScreen(True, monitor=0, hAlign=wx.RIGHT, vAlign=wx.TOP)


    def OnSnapPanes(self, event):

        allPanes = self._mgr.GetAllPanes()

        if not self._snapped:
            self._captions = {}
            for pane in allPanes:
                self._captions[pane.name] = pane.caption

        toSnap = not self._snapped

        if toSnap:
            for pane in allPanes:
                if pane.IsToolbar() or isinstance(pane.window, aui.AuiNotebook):
                    continue

                snap = random.randint(0, 4)
                if snap == 0:
                    # Snap everywhere
                    pane.Caption(pane.caption + " (Snap Everywhere)")
                    pane.Snappable(True)
                elif snap == 1:
                    # Snap left
                    pane.Caption(pane.caption + " (Snap Left)")
                    pane.LeftSnappable(True)
                elif snap == 2:
                    # Snap right
                    pane.Caption(pane.caption + " (Snap Right)")
                    pane.RightSnappable(True)
                elif snap == 3:
                    # Snap top
                    pane.Caption(pane.caption + " (Snap Top)")
                    pane.TopSnappable(True)
                elif snap == 4:
                    # Snap bottom
                    pane.Caption(pane.caption + " (Snap Bottom)")
                    pane.BottomSnappable(True)

        else:

            for pane in allPanes:
                if pane.IsToolbar() or isinstance(pane.window, aui.AuiNotebook):
                    continue

                pane.Caption(self._captions[pane.name])
                pane.Snappable(False)

        self._snapped = toSnap
        self._mgr.Update()
        self.Refresh()


    def OnFlyOut(self, event):

        checked = event.IsChecked()
        pane = self._mgr.GetPane("casetree")

        if checked:
            dlg = wx.MessageDialog(self, 'The tree pane will have fly-out' \
                                   ' behaviour when floating.',
                                   'Message',
                                   wx.OK | wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()
            pane.FlyOut(True)
        else:
            pane.FlyOut(False)

        self._mgr.Update()


    def OnCustomPaneButtons(self, event):

        self._custom_pane_buttons = checked = event.IsChecked()
        art = self._mgr.GetArtProvider()

        if not checked:
            art.SetDefaultPaneBitmaps(wx.Platform == "__WXMAC__")
        else:
            for bmp, button, active, maximize in CUSTOM_PANE_BITMAPS:
                art.SetCustomPaneBitmap(bmp.GetBitmap(), button, active, maximize)

        self._mgr.Update()
        self.Refresh()


    def OnCustomizeToolbar(self, event):

        wx.MessageBox("Customize Toolbar clicked", "AUI Test")


    def OnGradient(self, event):

        evId = event.GetId()
        if evId == ID_NoGradient:
            gradient = aui.AUI_GRADIENT_NONE
        elif evId == ID_VerticalGradient:
            gradient = aui.AUI_GRADIENT_VERTICAL
        elif evId == ID_HorizontalGradient:
            gradient = aui.AUI_GRADIENT_HORIZONTAL

        self._mgr.GetArtProvider().SetMetric(aui.AUI_DOCKART_GRADIENT_TYPE, gradient)
        self._mgr.Update()

# 
#     def OnManagerFlag(self, event):
# 
#         flag = 0
#         evId = event.GetId()
# 
#         if evId in [ID_TransparentHint, ID_VenetianBlindsHint, ID_RectangleHint, ID_NoHint]:
# 
#             agwFlags = self._mgr.GetAGWFlags()
#             agwFlags &= ~aui.AUI_MGR_TRANSPARENT_HINT
#             agwFlags &= ~aui.AUI_MGR_VENETIAN_BLINDS_HINT
#             agwFlags &= ~aui.AUI_MGR_RECTANGLE_HINT
#             self._mgr.SetAGWFlags(agwFlags)
# 
#         if evId == ID_AllowFloating:
#             flag = aui.AUI_MGR_ALLOW_FLOATING
#         elif evId == ID_TransparentDrag:
#             flag = aui.AUI_MGR_TRANSPARENT_DRAG
#         elif evId == ID_HintFade:
#             flag = aui.AUI_MGR_HINT_FADE
#         elif evId == ID_NoVenetianFade:
#             flag = aui.AUI_MGR_NO_VENETIAN_BLINDS_FADE
#         elif evId == ID_AllowActivePane:
#             flag = aui.AUI_MGR_ALLOW_ACTIVE_PANE
#         elif evId == ID_TransparentHint:
#             flag = aui.AUI_MGR_TRANSPARENT_HINT
#         elif evId == ID_VenetianBlindsHint:
#             flag = aui.AUI_MGR_VENETIAN_BLINDS_HINT
#         elif evId == ID_RectangleHint:
#             flag = aui.AUI_MGR_RECTANGLE_HINT
#         elif evId == ID_LiveUpdate:
#             flag = aui.AUI_MGR_LIVE_RESIZE
#         elif evId == ID_AnimateFrames:
#             flag = aui.AUI_MGR_ANIMATE_FRAMES
#         elif evId == ID_SmoothDocking:
#             flag = aui.AUI_MGR_SMOOTH_DOCKING
#         elif evId == ID_NativeMiniframes:
#             flag = aui.AUI_MGR_USE_NATIVE_MINIFRAMES
# 
#         if flag:
#             self._mgr.SetAGWFlags(self._mgr.GetAGWFlags() ^ flag)
# 
#         self._mgr.Update()
# 
# 
#     def OnMinimizePosition(self, event):
# 
#         minize_mode = 0
#         evId = event.GetId()
# 
#         if evId == ID_MinimizePosSmart:
#             minize_mode |= aui.AUI_MINIMIZE_POS_SMART
#         elif evId == ID_MinimizePosTop:
#             minize_mode |= aui.AUI_MINIMIZE_POS_TOP
#         elif evId == ID_MinimizePosLeft:
#             minize_mode |= aui.AUI_MINIMIZE_POS_LEFT
#         elif evId == ID_MinimizePosRight:
#             minize_mode |= aui.AUI_MINIMIZE_POS_RIGHT
#         elif evId == ID_MinimizePosBottom:
#             minize_mode |= aui.AUI_MINIMIZE_POS_BOTTOM
# 
#         all_panes = self._mgr.GetAllPanes()
#         for pane in all_panes:
#             if pane.name != "casetree":
#                 pane.MinimizeMode(minize_mode | (pane.GetMinimizeMode() & aui.AUI_MINIMIZE_CAPT_MASK))
# 
# 
#     def OnMinimizeCaption(self, event):
# 
#         minize_mode = 0
#         evId = event.GetId()
# 
#         if evId == ID_MinimizeCaptSmart:
#             minize_mode |= aui.AUI_MINIMIZE_CAPT_SMART
#         elif evId == ID_MinimizeCaptHorz:
#             minize_mode |= aui.AUI_MINIMIZE_CAPT_HORZ
#         elif evId == ID_MinimizeCaptHide:
#             minize_mode |= aui.AUI_MINIMIZE_CAPT_HIDE
# 
#         all_panes = self._mgr.GetAllPanes()
#         for pane in all_panes:
#             pane.MinimizeMode(minize_mode | (pane.GetMinimizeMode() & aui.AUI_MINIMIZE_POS_MASK))


    def OnNotebookFlag(self, event):

        evId = event.GetId()
        unsplit = None

        if evId in [ID_NotebookNoCloseButton, ID_NotebookCloseButton, ID_NotebookCloseButtonAll, \
                    ID_NotebookCloseButtonActive]:

            self._notebook_style &= ~(aui.AUI_NB_CLOSE_BUTTON |
                                      aui.AUI_NB_CLOSE_ON_ACTIVE_TAB |
                                      aui.AUI_NB_CLOSE_ON_ALL_TABS)

            if evId == ID_NotebookCloseButton:
                self._notebook_style ^= aui.AUI_NB_CLOSE_BUTTON
            elif evId == ID_NotebookCloseButtonAll:
                self._notebook_style ^= aui.AUI_NB_CLOSE_ON_ALL_TABS
            elif evId == ID_NotebookCloseButtonActive:
                self._notebook_style ^= aui.AUI_NB_CLOSE_ON_ACTIVE_TAB

        if evId == ID_NotebookAllowTabMove:
            self._notebook_style ^= aui.AUI_NB_TAB_MOVE

        if evId == ID_NotebookAllowTabExternalMove:
            self._notebook_style ^= aui.AUI_NB_TAB_EXTERNAL_MOVE

        elif evId == ID_NotebookAllowTabSplit:
            self._notebook_style ^= aui.AUI_NB_TAB_SPLIT

        elif evId == ID_NotebookTabFloat:
            self._notebook_style ^= aui.AUI_NB_TAB_FLOAT

        elif evId == ID_NotebookTabDrawDnd:
            self._notebook_style ^= aui.AUI_NB_DRAW_DND_TAB

        elif evId == ID_NotebookWindowList:
            self._notebook_style ^= aui.AUI_NB_WINDOWLIST_BUTTON

        elif evId == ID_NotebookScrollButtons:
            self._notebook_style ^= aui.AUI_NB_SCROLL_BUTTONS

        elif evId == ID_NotebookTabFixedWidth:
            self._notebook_style ^= aui.AUI_NB_TAB_FIXED_WIDTH

        elif evId == ID_NotebookHideSingle:
            self._notebook_style ^= aui.AUI_NB_HIDE_ON_SINGLE_TAB

        elif evId == ID_NotebookSmartTab:
            self._notebook_style ^= aui.AUI_NB_SMART_TABS

        elif evId == ID_NotebookUseImagesDropDown:
            self._notebook_style ^= aui.AUI_NB_USE_IMAGES_DROPDOWN

        elif evId == ID_NotebookCloseOnLeft:
            self._notebook_style ^= aui.AUI_NB_CLOSE_ON_TAB_LEFT

        all_panes = self._mgr.GetAllPanes()

        for pane in all_panes:

            if isinstance(pane.window, aui.AuiNotebook):
                nb = pane.window

                if evId == ID_NotebookArtGloss:

                    nb.SetArtProvider(aui.AuiDefaultTabArt())
                    self._notebook_theme = 0

                elif evId == ID_NotebookArtSimple:
                    nb.SetArtProvider(aui.AuiSimpleTabArt())
                    self._notebook_theme = 1

                elif evId == ID_NotebookArtVC71:
                    nb.SetArtProvider(aui.VC71TabArt())
                    self._notebook_theme = 2

                elif evId == ID_NotebookArtFF2:
                    nb.SetArtProvider(aui.FF2TabArt())
                    self._notebook_theme = 3

                elif evId == ID_NotebookArtVC8:
                    nb.SetArtProvider(aui.VC8TabArt())
                    self._notebook_theme = 4

                elif evId == ID_NotebookArtChrome:
                    nb.SetArtProvider(aui.ChromeTabArt())
                    self._notebook_theme = 5

                if nb.GetAGWWindowStyleFlag() & aui.AUI_NB_BOTTOM == 0:
                    nb.SetAGWWindowStyleFlag(self._notebook_style)

                if evId == ID_NotebookCloseButtonAll:
                    # Demonstrate how to remove a close button from a tab
                    nb.SetCloseButton(2, False)
                elif evId == ID_NotebookDclickUnsplit:
                    nb.SetSashDClickUnsplit(event.IsChecked())

                nb.Refresh()
                nb.Update()


    def OnUpdateUI(self, event):

        agwFlags = self._mgr.GetAGWFlags()
        evId = event.GetId()

        if evId == ID_NoGradient:
            event.Check(self._mgr.GetArtProvider().GetMetric(aui.AUI_DOCKART_GRADIENT_TYPE) == aui.AUI_GRADIENT_NONE)

        elif evId == ID_VerticalGradient:
            event.Check(self._mgr.GetArtProvider().GetMetric(aui.AUI_DOCKART_GRADIENT_TYPE) == aui.AUI_GRADIENT_VERTICAL)

        elif evId == ID_HorizontalGradient:
            event.Check(self._mgr.GetArtProvider().GetMetric(aui.AUI_DOCKART_GRADIENT_TYPE) == aui.AUI_GRADIENT_HORIZONTAL)

        elif evId == ID_AllowFloating:
            event.Check((agwFlags & aui.AUI_MGR_ALLOW_FLOATING) != 0)

        elif evId == ID_TransparentDrag:
            event.Check((agwFlags & aui.AUI_MGR_TRANSPARENT_DRAG) != 0)

        elif evId == ID_TransparentHint:
            event.Check((agwFlags & aui.AUI_MGR_TRANSPARENT_HINT) != 0)

        elif evId == ID_LiveUpdate:
            event.Check(aui.AuiManager_HasLiveResize(self._mgr))

        elif evId == ID_VenetianBlindsHint:
            event.Check((agwFlags & aui.AUI_MGR_VENETIAN_BLINDS_HINT) != 0)

        elif evId == ID_RectangleHint:
            event.Check((agwFlags & aui.AUI_MGR_RECTANGLE_HINT) != 0)

        elif evId == ID_NoHint:
            event.Check(((aui.AUI_MGR_TRANSPARENT_HINT |
                              aui.AUI_MGR_VENETIAN_BLINDS_HINT |
                              aui.AUI_MGR_RECTANGLE_HINT) & agwFlags) == 0)

        elif evId == ID_HintFade:
            event.Check((agwFlags & aui.AUI_MGR_HINT_FADE) != 0)

        elif evId == ID_NoVenetianFade:
            event.Check((agwFlags & aui.AUI_MGR_NO_VENETIAN_BLINDS_FADE) != 0)

        elif evId == ID_NativeMiniframes:
            event.Check(aui.AuiManager_UseNativeMiniframes(self._mgr))

        elif evId == ID_PaneIcons:
            event.Check(self._pane_icons)

        elif evId == ID_SmoothDocking:
            event.Check((agwFlags & aui.AUI_MGR_SMOOTH_DOCKING) != 0)

        elif evId == ID_AnimateFrames:
            event.Check((agwFlags & aui.AUI_MGR_ANIMATE_FRAMES) != 0)

        elif evId == ID_DefaultDockArt:
            event.Check(isinstance(self._mgr.GetArtProvider(), aui.AuiDefaultDockArt))

        elif evId == ID_ModernDockArt:
            event.Check(isinstance(self._mgr.GetArtProvider(), aui.ModernDockArt))

        elif evId == ID_SnapPanes:
            event.Check(self._snapped)

        elif evId == ID_FlyOut:
            pane = self._mgr.GetPane("casetree")
            event.Check(pane.IsFlyOut())

        elif evId == ID_AeroGuides:
            event.Check(agwFlags & aui.AUI_MGR_AERO_DOCKING_GUIDES != 0)

        elif evId == ID_WhidbeyGuides:
            event.Check(agwFlags & aui.AUI_MGR_WHIDBEY_DOCKING_GUIDES != 0)

        elif evId == ID_StandardGuides:
            event.Check((agwFlags & aui.AUI_MGR_AERO_DOCKING_GUIDES == 0) and (agwFlags & aui.AUI_MGR_WHIDBEY_DOCKING_GUIDES == 0))

        elif evId == ID_CustomPaneButtons:
            event.Check(self._custom_pane_buttons)

        elif evId == ID_PreviewMinimized:
            event.Check(agwFlags & aui.AUI_MGR_PREVIEW_MINIMIZED_PANES)

        elif evId == ID_NotebookNoCloseButton:
            event.Check((self._notebook_style & (aui.AUI_NB_CLOSE_BUTTON|aui.AUI_NB_CLOSE_ON_ALL_TABS|aui.AUI_NB_CLOSE_ON_ACTIVE_TAB)) != 0)

        elif evId == ID_NotebookCloseButton:
            event.Check((self._notebook_style & aui.AUI_NB_CLOSE_BUTTON) != 0)

        elif evId == ID_NotebookCloseButtonAll:
            event.Check((self._notebook_style & aui.AUI_NB_CLOSE_ON_ALL_TABS) != 0)

        elif evId == ID_NotebookCloseButtonActive:
            event.Check((self._notebook_style & aui.AUI_NB_CLOSE_ON_ACTIVE_TAB) != 0)

        elif evId == ID_NotebookAllowTabSplit:
            event.Check((self._notebook_style & aui.AUI_NB_TAB_SPLIT) != 0)

        elif evId == ID_NotebookTabFloat:
            event.Check((self._notebook_style & aui.AUI_NB_TAB_FLOAT) != 0)

        elif evId == ID_NotebookDclickUnsplit:
            event.Check(self._main_notebook.GetSashDClickUnsplit())

        elif evId == ID_NotebookTabDrawDnd:
            event.Check((self._notebook_style & aui.AUI_NB_DRAW_DND_TAB) != 0)

        elif evId == ID_NotebookAllowTabMove:
            event.Check((self._notebook_style & aui.AUI_NB_TAB_MOVE) != 0)

        elif evId == ID_NotebookAllowTabExternalMove:
            event.Check((self._notebook_style & aui.AUI_NB_TAB_EXTERNAL_MOVE) != 0)

        elif evId == ID_NotebookScrollButtons:
            event.Check((self._notebook_style & aui.AUI_NB_SCROLL_BUTTONS) != 0)

        elif evId == ID_NotebookWindowList:
            event.Check((self._notebook_style & aui.AUI_NB_WINDOWLIST_BUTTON) != 0)

        elif evId == ID_NotebookTabFixedWidth:
            event.Check((self._notebook_style & aui.AUI_NB_TAB_FIXED_WIDTH) != 0)

        elif evId == ID_NotebookHideSingle:
            event.Check((self._notebook_style & aui.AUI_NB_HIDE_ON_SINGLE_TAB) != 0)

        elif evId == ID_NotebookSmartTab:
            event.Check((self._notebook_style & aui.AUI_NB_SMART_TABS) != 0)

        elif evId == ID_NotebookUseImagesDropDown:
            event.Check((self._notebook_style & aui.AUI_NB_USE_IMAGES_DROPDOWN) != 0)

        elif evId == ID_NotebookCloseOnLeft:
            event.Check((self._notebook_style & aui.AUI_NB_CLOSE_ON_TAB_LEFT) != 0)

        elif evId == ID_NotebookCustomButtons:
            event.Check(self._custom_tab_buttons)

        elif evId == ID_NotebookArtGloss:
            event.Check(self._notebook_theme == 0)

        elif evId == ID_NotebookArtSimple:
            event.Check(self._notebook_theme == 1)

        elif evId == ID_NotebookArtVC71:
            event.Check(self._notebook_theme == 2)

        elif evId == ID_NotebookArtFF2:
            event.Check(self._notebook_theme == 3)

        elif evId == ID_NotebookArtVC8:
            event.Check(self._notebook_theme == 4)

        elif evId == ID_NotebookArtChrome:
            event.Check(self._notebook_theme == 5)

        elif evId == ID_VetoTree:
            event.Check(self._veto_tree)

        elif evId == ID_VetoText:
            event.Check(self._veto_text)

        else:
            for ids in self._requestPanes:
                if evId == ids:
                    paneName = self._requestPanes[ids]
                    pane = self._mgr.GetPane(paneName)
                    event.Enable(pane.IsShown())


    def OnPaneClose(self, event):

        if event.pane.name == "test10":

            msg = "Are you sure you want to "
            if event.GetEventType() == aui.wxEVT_AUI_PANE_MINIMIZE:
                msg += "minimize "
            else:
                msg += "close/hide "

            res = wx.MessageBox(msg + "this pane?", "AUI", wx.YES_NO, self)
            if res != wx.YES:
                event.Veto()

# 
#     def OnCreatePerspective(self, event):
# 
#         dlg = wx.TextEntryDialog(self, "Enter a name for the new perspective:", "AUI Test")
# 
#         dlg.SetValue("Perspective %u"%(len(self._perspectives) + 1))
#         if dlg.ShowModal() != wx.ID_OK:
#             return
# 
#         if len(self._perspectives) == 0:
#             self._perspectives_menu.AppendSeparator()
# 
#         self._perspectives_menu.Append(ID_FirstPerspective + len(self._perspectives), dlg.GetValue())
#         self._perspectives.append(self._mgr.SavePerspective())
# 
# 
#     def OnCopyPerspectiveCode(self, event):
# 
#         s = self._mgr.SavePerspective()
# 
#         if wx.TheClipboard.Open():
# 
#             wx.TheClipboard.SetData(wx.TextDataObject(s))
#             wx.TheClipboard.Close()


    def OnRestorePerspective(self, event):

        self._mgr.LoadPerspective(self._perspectives[event.GetId() - ID_FirstPerspective])


#     def OnCreateNBPerspective(self, event):
# 
#         dlg = wx.TextEntryDialog(self, "Enter a name for the new perspective:", "AUI Test")
# 
#         dlg.SetValue("Perspective %u"%(len(self._nb_perspectives) + 1))
#         if dlg.ShowModal() != wx.ID_OK:
#             return
# 
#         if len(self._nb_perspectives) == 0:
#             self._nb_perspectives_menu.AppendSeparator()
# 
#         auibook = self._mgr.GetPane("config_content").window
#         self._nb_perspectives_menu.Append(ID_FirstNBPerspective + len(self._nb_perspectives), dlg.GetValue())
#         self._nb_perspectives.append(auibook.SavePerspective())
# 
# 
#     def OnCopyNBPerspectiveCode(self, event):
# 
#         auibook = self._mgr.GetPane("config_content").window
#         s = auibook.SavePerspective()
# 
#         if wx.TheClipboard.Open():
# 
#             wx.TheClipboard.SetData(wx.TextDataObject(s))
#             wx.TheClipboard.Close()


    def OnRestoreNBPerspective(self, event):

        auibook = self._mgr.GetPane("config_content").window
        auibook.LoadPerspective(self._nb_perspectives[event.GetId() - ID_FirstNBPerspective])


    def OnGuides(self, event):

        useAero = event.GetId() == ID_AeroGuides
        useWhidbey = event.GetId() == ID_WhidbeyGuides
        agwFlags = self._mgr.GetAGWFlags()

        if useAero:
            agwFlags ^= aui.AUI_MGR_AERO_DOCKING_GUIDES
            agwFlags &= ~aui.AUI_MGR_WHIDBEY_DOCKING_GUIDES
        elif useWhidbey:
            agwFlags ^= aui.AUI_MGR_WHIDBEY_DOCKING_GUIDES
            agwFlags &= ~aui.AUI_MGR_AERO_DOCKING_GUIDES
        else:
            agwFlags &= ~aui.AUI_MGR_AERO_DOCKING_GUIDES
            agwFlags &= ~aui.AUI_MGR_WHIDBEY_DOCKING_GUIDES

        self._mgr.SetAGWFlags(agwFlags)


    def OnNotebookPageClose(self, event):

        ctrl = event.GetEventObject()
        if isinstance(ctrl.GetPage(event.GetSelection()), wx.html.HtmlWindow):

            res = wx.MessageBox("Are you sure you want to close/hide this notebook page?",
                                "AUI", wx.YES_NO, self)
            if res != wx.YES:
                event.Veto()


    def OnAllowNotebookDnD(self, event):

        # for the purpose of this test application, explicitly
        # allow all noteboko drag and drop events
        event.Allow()


    def GetStartPosition(self):

        x = 20
        pt = self.ClientToScreen(wx.Point(0, 0))
        return wx.Point(pt.x + x, pt.y + x)



    def OnChangeContentPane(self, event):
        self._mgr.GetPane("log_content").Show(event.GetId() in   [ID_LogContent, ID_SampleItem+24])
        self._mgr.GetPane("config_content").Show(event.GetId() in [ID_NotebookContent, ID_SampleItem+25])

#         self._mgr.GetPane("log_content").Show(event.GetId() == ID_LogContent)
#         self._mgr.GetPane("config_content").Show(event.GetId() == ID_NotebookContent)
        self._mgr.Update()


    def OnVetoTree(self, event):

        self._veto_tree = event.IsChecked()


    def OnVetoText(self, event):

        self._veto_text = event.IsChecked()


    def OnRequestUserAttention(self, event):

        ids = event.GetId()
        if ids not in self._requestPanes:
            return

        paneName = self._requestPanes[ids]
        pane = self._mgr.GetPane(paneName)
        self._mgr.RequestUserAttention(pane.window)


    def OnDropDownToolbarItem(self, event):

        if event.IsDropDownClicked():

            tb = event.GetEventObject()
            tb.SetToolSticky(event.GetId(), True)

            # create the popup menu
            menuPopup = wx.Menu()
            bmp = wx.ArtProvider.GetBitmap(wx.ART_QUESTION, wx.ART_OTHER, wx.Size(16, 16))

            m1 =  wx.MenuItem(menuPopup, 10001, "Drop Down Item 1")
            m1.SetBitmap(bmp)
            menuPopup.Append(m1)

            m2 =  wx.MenuItem(menuPopup, 10002, "Drop Down Item 2")
            m2.SetBitmap(bmp)
            menuPopup.Append(m2)

            m3 =  wx.MenuItem(menuPopup, 10003, "Drop Down Item 3")
            m3.SetBitmap(bmp)
            menuPopup.Append(m3)

            m4 =  wx.MenuItem(menuPopup, 10004, "Drop Down Item 4")
            m4.SetBitmap(bmp)
            menuPopup.Append(m4)

            # line up our menu with the button
            rect = tb.GetToolRect(event.GetId())
            pt = tb.ClientToScreen(rect.GetBottomLeft())
            pt = self.ScreenToClient(pt)

            self.PopupMenu(menuPopup, pt)

            # make sure the button is "un-stuck"
            tb.SetToolSticky(event.GetId(), False)


    def OnTabAlignment(self, event):

        for pane in self._mgr.GetAllPanes():

            if isinstance(pane.window, aui.AuiNotebook):

                nb = pane.window
                style = nb.GetAGWWindowStyleFlag()

                if event.GetId() == ID_NotebookAlignTop:
                    style &= ~aui.AUI_NB_BOTTOM
                    style ^= aui.AUI_NB_TOP
                    nb.SetAGWWindowStyleFlag(style)
                elif event.GetId() == ID_NotebookAlignBottom:
                    style &= ~aui.AUI_NB_TOP
                    style ^= aui.AUI_NB_BOTTOM
                    nb.SetAGWWindowStyleFlag(style)

                self._notebook_style = style
                nb.Update()
                nb.Refresh()


    def OnCustomTabButtons(self, event):

        checked = event.IsChecked()
        self._custom_tab_buttons = checked
        auibook = self._mgr.GetPane("config_content").window

        left = CUSTOM_TAB_BUTTONS["Left"]
        for btn, ids in left:
            if checked:
                auibook.AddTabAreaButton(ids, wx.LEFT, btn.GetBitmap())
            else:
                auibook.RemoveTabAreaButton(ids)

        right = CUSTOM_TAB_BUTTONS["Right"]
        for btn, ids in right:
            if checked:
                auibook.AddTabAreaButton(ids, wx.RIGHT, btn.GetBitmap())
            else:
                auibook.RemoveTabAreaButton(ids)

        auibook.Refresh()
        auibook.Update()


    def OnMinMaxTabWidth(self, event):

        auibook = self._mgr.GetPane("config_content").window
        minTabWidth, maxTabWidth = auibook.GetMinMaxTabWidth()

        dlg = wx.TextEntryDialog(self, "Enter the minimum and maximum tab widths, separated by a comma:",
                                 "AuiNotebook Tab Widths")

        dlg.SetValue("%d,%d"%(minTabWidth, maxTabWidth))
        if dlg.ShowModal() != wx.ID_OK:
            return

        value = dlg.GetValue()
        dlg.Destroy()

        try:
            minTabWidth, maxTabWidth = value.split(",")
            minTabWidth, maxTabWidth = int(minTabWidth), int(maxTabWidth)
        except:
            dlg = wx.MessageDialog(self, 'Invalid minimum/maximum tab width. Tab widths should be' \
                                   ' 2 integers separated by a comma.',
                                   'Error',
                                   wx.OK | wx.ICON_ERROR)
            dlg.ShowModal()
            dlg.Destroy()
            return

        if minTabWidth > maxTabWidth:
            dlg = wx.MessageDialog(self, 'Invalid minimum/maximum tab width. Minimum tab width' \
                                   ' should be less of equal than maximum tab width.',
                                   'Error',
                                   wx.OK | wx.ICON_ERROR)
            dlg.ShowModal()
            dlg.Destroy()
            return

        auibook.SetMinMaxTabWidth(minTabWidth, maxTabWidth)
        auibook.Refresh()
        auibook.Update()


    def OnPreview(self, event):

        auibook = self._mgr.GetPane("config_content").window
        auibook.NotebookPreview()


    def OnAddMultiLine(self, event):

        auibook = self._mgr.GetPane("config_content").window

        auibook.InsertPage(1, wx.TextCtrl(auibook, -1, "Some more text", wx.DefaultPosition, wx.DefaultSize,
                                          wx.TE_MULTILINE|wx.NO_BORDER), "Multi-Line\nTab Labels", True)

        auibook.SetPageTextColour(1, wx.BLUE)


    def OnFloatDock(self, event):

        paneLabel = event.pane.caption
        etype = event.GetEventType()

        strs = "Pane %s "%paneLabel
        if etype == aui.wxEVT_AUI_PANE_FLOATING:
            strs += "is about to be floated"

            if event.pane.name == "casetree" and self._veto_tree:
                event.Veto()
                strs += "... Event vetoed by user selection!"
                self.log.write(strs + "\n")
                return

        elif etype == aui.wxEVT_AUI_PANE_FLOATED:
            strs += "has been floated"
        elif etype == aui.wxEVT_AUI_PANE_DOCKING:
            strs += "is about to be docked"

            if event.pane.name == "test11" and self._veto_text:
                event.Veto()
                strs += "... Event vetoed by user selection!"
                self.log.write(strs + "\n")
                return

        elif etype == aui.wxEVT_AUI_PANE_DOCKED:
            strs += "has been docked"

        self.log.write(strs + "\n")


    def OnExit(self, event):

        self.Close(True)


    def OnAbout(self, event):

        msg = "This Is The About Dialog Of The Pure Python Version Of AUI.\n\n" + \
              "Author: Andrea Gavana @ 23 Dec 2005\n\n" + \
              "Please Report Any Bug/Requests Of Improvements\n" + \
              "To Me At The Following Adresses:\n\n" + \
              "andrea.gavana@maerskoil.com\n" + "andrea.gavana@gmail.com\n\n" + \
              "Welcome To wxPython " + wx.VERSION_STRING + "!!"

        dlg = wx.MessageDialog(self, msg, "AUI Demo",
                               wx.OK | wx.ICON_INFORMATION)

        if wx.Platform != '__WXMAC__':
            dlg.SetFont(wx.Font(8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL,
                                False, '', wx.FONTENCODING_DEFAULT))

        dlg.ShowModal()
        dlg.Destroy()

### -----------------------------------------------------
### data function
### -----------------------------------------------------

    def text_lib_readme(self):
#         print ("CONFIG_BASE.dic_root_lib = ", CONFIG_BASE.dic_root_lib)
        if CONFIG_BASE.dic_root_lib['readme']:
            return CONFIG_BASE.dic_root_lib['readme']
        else:
            return "No README FILE"


    def text_root_readme(self):
#         print ("CONFIG_BASE.dic_root_lib = ", CONFIG_BASE.dic_root_lib)
        if CONFIG_BASE.dic_root_lib['readme']:
            return CONFIG_BASE.dic_root_lib['root_readme']
        else:
            return "No README FILE"
        
        
    def CreateTextCtrl(self, ctrl_text=""):

        if ctrl_text.strip():
            text = ctrl_text
        else:
            text = "This is text box %d"%self._textCount
            self._textCount += 1

        return wx.TextCtrl(self,-1, text, wx.Point(0, 0), wx.Size(150, 90),
                           wx.NO_BORDER | wx.TE_MULTILINE)



    def CreateNotebook(self):
        print ("CreateNotebook"*30)
        # create the notebook off-window to avoid flicker
        client_size = self.GetClientSize()
        ctrl = aui.AuiNotebook(self, -1, wx.Point(client_size.x, client_size.y),
                              wx.Size(430, 200), agwStyle=self._notebook_style)

        arts = [aui.AuiDefaultTabArt, aui.AuiSimpleTabArt, aui.VC71TabArt, aui.FF2TabArt,
                aui.VC8TabArt, aui.ChromeTabArt]

        art = arts[self._notebook_theme]()
        ctrl.SetArtProvider(art)

        page_bmp = wx.ArtProvider.GetBitmap(wx.ART_NORMAL_FILE, wx.ART_OTHER, wx.Size(16, 16))

        ctrl.AddPage(self.CreateTextCtrl(self.text_lib_readme()), "Usage", False, page_bmp)



        for k, v in CONFIG_BASE.dic_lib_category.items():
            if (k in self.lst_current_category) and v['text']:
#             if v['text']:
                newpage = wx.TextCtrl(ctrl, -1, v['text'], wx.DefaultPosition, wx.DefaultSize,
                                 wx.TE_MULTILINE|wx.NO_BORDER)
                ctrl.AddPage(newpage, k+"-config")#, False, page_bmp)
                
#         ctrl.AddPage(wx.TextCtrl(ctrl, -1, "Some text", wx.DefaultPosition, wx.DefaultSize,
#                                  wx.TE_MULTILINE|wx.NO_BORDER), "DClick Edit!", False, page_bmp)
# 
#         ctrl.AddPage(wx.TextCtrl(ctrl, -1, "Some more text", wx.DefaultPosition, wx.DefaultSize,
#                                  wx.TE_MULTILINE|wx.NO_BORDER), "Blue Tab")
# 
#         ctrl.AddPage(wx.TextCtrl(ctrl, -1, "Some more text", wx.DefaultPosition, wx.DefaultSize,
#                                  wx.TE_MULTILINE|wx.NO_BORDER), "A Control")
# 
#         ctrl.AddPage(wx.TextCtrl(ctrl, -1, "Some more text", wx.DefaultPosition, wx.DefaultSize,
#                                  wx.TE_MULTILINE|wx.NO_BORDER), "wxTextCtrl 4")
# 
#         ctrl.AddPage(wx.TextCtrl(ctrl, -1, "Some more text", wx.DefaultPosition, wx.DefaultSize,
#                                  wx.TE_MULTILINE|wx.NO_BORDER), "wxTextCtrl 5")
# 
#         ctrl.AddPage(wx.TextCtrl(ctrl, -1, "Some more text", wx.DefaultPosition, wx.DefaultSize,
#                                  wx.TE_MULTILINE|wx.NO_BORDER), "wxTextCtrl 6")
# 
#         ctrl.AddPage(wx.TextCtrl(ctrl, -1, "Some more text", wx.DefaultPosition, wx.DefaultSize,
#                                  wx.TE_MULTILINE|wx.NO_BORDER), "wxTextCtrl 7 (longer title)")
# 
#         ctrl.AddPage(wx.TextCtrl(ctrl, -1, "Some more text", wx.DefaultPosition, wx.DefaultSize,
#                                  wx.TE_MULTILINE|wx.NO_BORDER), "wxTextCtrl 8")
#
#         # Demonstrate how to disable a tab
#         ctrl.EnableTab(1, False)
#
#         ctrl.SetPageTextColour(2, wx.RED)
#         ctrl.SetRenamable(2, True)

        return ctrl


    def OnSwitchPane(self, event):

        items = ASD.SwitcherItems()
        items.SetRowCount(12)

        # Add the main windows and toolbars, in two separate columns
        # We'll use the item 'id' to store the notebook selection, or -1 if not a page

        for k in range(2):
            if k == 0:
                items.AddGroup(_("Main Windows"), "mainwindows")
            else:
                items.AddGroup(_("Toolbars"), "toolbars").BreakColumn()

            for pane in self._mgr.GetAllPanes():
                name = pane.name
                caption = pane.caption
                if not caption:
                    continue

                toolBar = isinstance(pane.window, wx.ToolBar) or isinstance(pane.window, aui.AuiToolBar)
                bitmap = (pane.icon.IsOk() and [pane.icon] or [wx.NullBitmap])[0]

                if (toolBar and k == 1) or (not toolBar and k == 0):
                    items.AddItem(caption, name, -1, bitmap).SetWindow(pane.window)

        # Now add the wxAuiNotebook pages
        items.AddGroup(_("Notebook Pages"), "pages").BreakColumn()

        for pane in self._mgr.GetAllPanes():
            nb = pane.window
            if isinstance(nb, aui.AuiNotebook):
                for j in range(nb.GetPageCount()):

                    name = nb.GetPageText(j)
                    win = nb.GetPage(j)

                    items.AddItem(name, name, j, nb.GetPageBitmap(j)).SetWindow(win)

        # Select the focused window

        idx = items.GetIndexForFocus()
        if idx != wx.NOT_FOUND:
            items.SetSelection(idx)

        if wx.Platform == "__WXMAC__":
            items.SetBackgroundColour(wx.WHITE)

        # Show the switcher dialog

        dlg = ASD.SwitcherDialog(items, self, self._mgr)

        # In GTK+ we can't use Ctrl+Tab; we use Ctrl+/ instead and tell the switcher
        # to treat / in the same was as tab (i.e. cycle through the names)

        if wx.Platform == "__WXGTK__":
            dlg.SetExtraNavigationKey('/')

        if wx.Platform == "__WXMAC__":
            dlg.SetBackgroundColour(wx.WHITE)
            dlg.SetModifierKey(wx.WXK_ALT)

        ans = dlg.ShowModal()

        if ans == wx.ID_OK and dlg.GetSelection() != -1:
            item = items.GetItem(dlg.GetSelection())

            if item.GetId() == -1:
                info = self._mgr.GetPane(item.GetName())
                info.Show()
                self._mgr.Update()
                info.window.SetFocus()

            else:
                nb = item.GetWindow().GetParent()
                win = item.GetWindow()
                if isinstance(nb, aui.AuiNotebook):
                    nb.SetSelection(item.GetId())
                    win.SetFocus()

