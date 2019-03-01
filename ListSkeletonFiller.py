import sys
import wx
#import wx.lib.agw.ultimatelistctrl as ULC

class ListSkeletonFiller:
    def __init__(self, parent, rows):

        self.parent = parent
        self.rows = rows

    def insertRowIndex(self, rowindex):
            index = self.parent.elvisulc.InsertStringItem(sys.maxsize, self.rows[rowindex][0])
            self.parent.elvisulc.SetStringItem(index, 1, self.rows[rowindex][1])
            self.parent.elvisulc.SetStringItem(index, 2, self.rows[rowindex][2])
            identity = self.parent.elvisulc.GetItemText(index)
            self.parent.elvisulc.SetStringItem(index, 3, self.rows[rowindex][3])
            self.parent.elvisulc.SetStringItem(index, 4, self.rows[rowindex][4])
            self.parent.elvisulc.SetStringItem(index, 5, self.rows[rowindex][5])
            self.parent.elvisulc.SetStringItem(index, 6, self.rows[rowindex][6])
            editBtn = wx.Button(self.parent.elvisulc, wx.ID_ANY, u"Redigera", wx.DefaultPosition, wx.DefaultSize, 0)
            editBtn.course = identity
            self.parent.elvisulc.SetItemWindow(index, 7, editBtn, expand=False)
            editBtn.Bind(wx.EVT_BUTTON, self.parent.onClickCourse)

