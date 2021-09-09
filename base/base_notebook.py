#!/usr/bin/env python

import sys
import wx
# from xyView.base import images

#----------------------------------------------------------------------------

class TestNB(wx.Notebook):
    def __init__(self, parent, id, log):
        wx.Notebook.__init__(self, parent, id, size=(21,21), style=
                             wx.BK_DEFAULT
                             #wx.BK_TOP
                             #wx.BK_BOTTOM
                             #wx.BK_LEFT
                             #wx.BK_RIGHT
                             # | wx.NB_MULTILINE
                             )
        self.log = log

        # Show how to put an image on one of the notebook tabs,
        # first make the image list:
        il = wx.ImageList(16, 16)
#         idx1 = il.Add(images.Smiles.GetBitmap())
        self.AssignImageList(il)

        # now put an image on the first tab we just created:
#         self.SetPageImage(0, idx1)


        self.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGED, self.OnPageChanged)
        self.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGING, self.OnPageChanging)


    def OnPageChanged(self, event):  pass
#         if self:
#             old = event.GetOldSelection()
#             new = event.GetSelection()
#             sel = self.GetSelection()
#             self.log.write('OnPageChanged,  old:%d, new:%d, sel:%d\n' % (old, new, sel))
#         event.Skip()

    def OnPageChanging(self, event):  pass
#         if self:
#             old = event.GetOldSelection()
#             new = event.GetSelection()
#             sel = self.GetSelection()
#             self.log.write('OnPageChanging, old:%d, new:%d, sel:%d\n' % (old, new, sel))
#         event.Skip()

#----------------------------------------------------------------------------

#----------------------------------------------------------------------------



