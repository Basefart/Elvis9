# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Mar 23 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.adv


###########################################################################
## Class elvistmplframe
###########################################################################

class ElvisTmplPanel(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition,
                          size=wx.Size(900, -1), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.Size(900, 900), wx.Size(900, 900))
        self.SetFont(
            wx.Font(11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))

        elvisTopbSizer = wx.BoxSizer(wx.VERTICAL)

        elvisTopbSizer.SetMinSize(wx.Size(900, 900))
        self.scrolledTmplWindow = wx.ScrolledWindow(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(900, 1300),
                                                    wx.FULL_REPAINT_ON_RESIZE | wx.HSCROLL | wx.VSCROLL)
        self.scrolledTmplWindow.SetScrollRate(5, 5)
        self.scrolledTmplWindow.SetFont(
            wx.Font(11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))
        self.scrolledTmplWindow.SetMinSize(wx.Size(900, 1300))

        elvisGSizerAll = wx.GridSizer(4, 0, 0, 0)

        sbSizer100 = wx.StaticBoxSizer(wx.StaticBox(self.scrolledTmplWindow, wx.ID_ANY, u"100 poäng"), wx.VERTICAL)

        sbSizer100.SetMinSize(wx.Size(840, 300))
        gSizer100 = wx.GridSizer(0, 3, 0, 0)

        gSizer100.SetMinSize(wx.Size(840, 300))

        sbSizer100Full = wx.StaticBoxSizer(wx.StaticBox(sbSizer100.GetStaticBox(), wx.ID_ANY, u"Heltid"), wx.VERTICAL)

        wSiz100Full = wx.WrapSizer(wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS)

        self.tmplNm100Full = wx.TextCtrl(sbSizer100Full.GetStaticBox(), wx.ID_ANY, u"Mallnamn", wx.DefaultPosition,
                                         wx.Size(180, -1), 0)
        self.tmplNm100Full.Bind(wx.EVT_LEFT_DOWN, self.clearTC)
        wSiz100Full.Add(self.tmplNm100Full, 0, wx.ALL, 5)

        self.state100Full = wx.CheckBox(sbSizer100Full.GetStaticBox(), wx.ID_ANY, u"Aktiv", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.state100Full.SetValue(True)
        wSiz100Full.Add(self.state100Full, 0, wx.ALL, 5)

        self.courseEnd100Full = wx.adv.DatePickerCtrl(sbSizer100Full.GetStaticBox(), wx.ID_ANY, wx.DefaultDateTime,
                                                      wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DROPDOWN)
        self.courseEnd100Full.SetToolTip(u"Kursslut")
        wSiz100Full.Add(self.courseEnd100Full, 0, wx.ALL, 5)
        self.weekLbl100Full = wx.StaticText(sbSizer100Full.GetStaticBox(), wx.ID_ANY, u"veckor:", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.weekLbl100Full.Wrap(-1)

        self.weekLbl100Full.SetFont(
            wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))

        wSiz100Full.Add(self.weekLbl100Full, 0, wx.ALL, 5)

        self.weeks100Full = wx.TextCtrl(sbSizer100Full.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                        wx.Size(50, -1), 0)
        wSiz100Full.Add(self.weeks100Full, 0, wx.ALL, 5)

        self.descr100Full = wx.TextCtrl(sbSizer100Full.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                        wx.Size(250, 200), wx.TE_MULTILINE)
        self.descr100Full.SetFont(
            wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))
        self.descr100Full.SetMinSize(wx.Size(250, 200))
        self.descr100Full.SetMaxSize(wx.Size(250, 200))

        wSiz100Full.Add(self.descr100Full, 0, wx.ALL, 5)

        sbSizer100Full.Add(wSiz100Full, 1, wx.EXPAND, 5)

        gSizer100.Add(sbSizer100Full, 1, wx.ALL | wx.EXPAND, 2)

        sbSizer100Half = wx.StaticBoxSizer(wx.StaticBox(sbSizer100.GetStaticBox(), wx.ID_ANY, u"Halvtid"), wx.VERTICAL)
        wSiz100Half = wx.WrapSizer(wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS)

        self.tmplNm100Half = wx.TextCtrl(sbSizer100Half.GetStaticBox(), wx.ID_ANY, u"Mallnamn", wx.DefaultPosition,
                                         wx.Size(180, -1), 0)
        self.tmplNm100Half.Bind(wx.EVT_LEFT_DOWN, self.clearTC)
        wSiz100Half.Add(self.tmplNm100Half, 0, wx.ALL, 5)

        self.state100Half = wx.CheckBox(sbSizer100Half.GetStaticBox(), wx.ID_ANY, u"Aktiv", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.state100Half.SetValue(True)
        wSiz100Half.Add(self.state100Half, 0, wx.ALL, 5)

        self.courseEnd100Half = wx.adv.DatePickerCtrl(sbSizer100Half.GetStaticBox(), wx.ID_ANY, wx.DefaultDateTime,
                                                      wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DROPDOWN)
        self.courseEnd100Half.SetToolTip(u"Kursslut")
        wSiz100Half.Add(self.courseEnd100Half, 0, wx.ALL, 5)
        self.weekLbl100Half = wx.StaticText(sbSizer100Half.GetStaticBox(), wx.ID_ANY, u"veckor:", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.weekLbl100Half.Wrap(-1)

        self.weekLbl100Half.SetFont(
            wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))

        wSiz100Half.Add(self.weekLbl100Half, 0, wx.ALL, 5)


        self.weeks100Half = wx.TextCtrl(sbSizer100Half.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                        wx.Size(50, -1), 0)
        wSiz100Half.Add(self.weeks100Half, 0, wx.ALL, 5)

        self.descr100Half = wx.TextCtrl(sbSizer100Half.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                        wx.Size(250, 200), wx.TE_MULTILINE)
        self.descr100Half.SetFont(
            wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))
        self.descr100Half.SetMinSize(wx.Size(250, 200))
        self.descr100Half.SetMaxSize(wx.Size(250, 200))

        wSiz100Half.Add(self.descr100Half, 0, wx.ALL, 5)
        sbSizer100Half.Add(wSiz100Half, 1, wx.EXPAND, 5)

        gSizer100.Add(sbSizer100Half, 1, wx.ALL | wx.EXPAND, 2)

        sbSizer100Quart = wx.StaticBoxSizer(wx.StaticBox(sbSizer100.GetStaticBox(), wx.ID_ANY, u"Kvartstid"),
                                            wx.VERTICAL)
        wSiz100Quart = wx.WrapSizer(wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS)

        self.tmplNm100Quart = wx.TextCtrl(sbSizer100Quart.GetStaticBox(), wx.ID_ANY, u"Mallnamn", wx.DefaultPosition,
                                         wx.Size(180, -1), 0)
        self.tmplNm100Quart.Bind(wx.EVT_LEFT_DOWN, self.clearTC)
        wSiz100Quart.Add(self.tmplNm100Quart, 0, wx.ALL, 5)

        self.state100Quart = wx.CheckBox(sbSizer100Quart.GetStaticBox(), wx.ID_ANY, u"Aktiv", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.state100Quart.SetValue(True)
        wSiz100Quart.Add(self.state100Quart, 0, wx.ALL, 5)

        self.courseEnd100Quart = wx.adv.DatePickerCtrl(sbSizer100Quart.GetStaticBox(), wx.ID_ANY, wx.DefaultDateTime,
                                                      wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DROPDOWN)
        self.courseEnd100Quart.SetToolTip(u"Kursslut")
        wSiz100Quart.Add(self.courseEnd100Quart, 0, wx.ALL, 5)
        self.weekLbl100Quart = wx.StaticText(sbSizer100Quart.GetStaticBox(), wx.ID_ANY, u"veckor:", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.weekLbl100Quart.Wrap(-1)

        self.weekLbl100Quart.SetFont(
            wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))

        wSiz100Quart.Add(self.weekLbl100Quart, 0, wx.ALL, 5)

        self.weeks100Quart = wx.TextCtrl(sbSizer100Quart.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                        wx.Size(50, -1), 0)
        wSiz100Quart.Add(self.weeks100Quart, 0, wx.ALL, 5)

        self.descr100Quart = wx.TextCtrl(sbSizer100Quart.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                        wx.Size(250, 200), wx.TE_MULTILINE)
        self.descr100Quart.SetFont(
            wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))
        self.descr100Quart.SetMinSize(wx.Size(250, 200))
        self.descr100Quart.SetMaxSize(wx.Size(250, 200))

        wSiz100Quart.Add(self.descr100Quart, 0, wx.ALL, 5)
        sbSizer100Quart.Add(wSiz100Quart, 1, wx.EXPAND, 5)

        gSizer100.Add(sbSizer100Quart, 1, wx.ALL | wx.EXPAND, 2)

        sbSizer100.Add(gSizer100, 1, wx.ALL | wx.EXPAND, 2)

        elvisGSizerAll.Add(sbSizer100, 1, wx.ALL | wx.EXPAND | wx.FIXED_MINSIZE, 4)

        sbSizer200 = wx.StaticBoxSizer(wx.StaticBox(self.scrolledTmplWindow, wx.ID_ANY, u"200 poäng"), wx.VERTICAL)

        sbSizer200.SetMinSize(wx.Size(840, 300))
        gSizer200 = wx.GridSizer(0, 3, 0, 0)

        gSizer200.SetMinSize(wx.Size(840, 300))
        sbSizer200Full = wx.StaticBoxSizer(wx.StaticBox(sbSizer200.GetStaticBox(), wx.ID_ANY, u"Heltid"), wx.VERTICAL)

        wSiz200Full = wx.WrapSizer(wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS)

        self.tmplNm200Full = wx.TextCtrl(sbSizer200Full.GetStaticBox(), wx.ID_ANY, u"Mallnamn", wx.DefaultPosition,
                                         wx.Size(180, -1), 0)
        self.tmplNm200Full.Bind(wx.EVT_LEFT_DOWN, self.clearTC)
        wSiz200Full.Add(self.tmplNm200Full, 0, wx.ALL, 5)

        self.state200Full = wx.CheckBox(sbSizer200Full.GetStaticBox(), wx.ID_ANY, u"Aktiv", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.state200Full.SetValue(True)
        wSiz200Full.Add(self.state200Full, 0, wx.ALL, 5)

        self.courseEnd200Full = wx.adv.DatePickerCtrl(sbSizer200Full.GetStaticBox(), wx.ID_ANY, wx.DefaultDateTime,
                                                      wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DROPDOWN)
        self.courseEnd200Full.SetToolTip(u"Kursslut")
        wSiz200Full.Add(self.courseEnd200Full, 0, wx.ALL, 5)
        self.weekLbl200Full = wx.StaticText(sbSizer200Full.GetStaticBox(), wx.ID_ANY, u"veckor:", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.weekLbl200Full.Wrap(-1)

        self.weekLbl200Full.SetFont(
            wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))

        wSiz200Full.Add(self.weekLbl200Full, 0, wx.ALL, 5)


        self.weeks200Full = wx.TextCtrl(sbSizer200Full.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                        wx.Size(50, -1), 0)
        wSiz200Full.Add(self.weeks200Full, 0, wx.ALL, 5)

        self.descr200Full = wx.TextCtrl(sbSizer200Full.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                        wx.Size(250, 200), wx.TE_MULTILINE)
        self.descr200Full.SetFont(
            wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))
        self.descr200Full.SetMinSize(wx.Size(250, 200))
        self.descr200Full.SetMaxSize(wx.Size(250, 200))

        wSiz200Full.Add(self.descr200Full, 0, wx.ALL, 5)

        sbSizer200Full.Add(wSiz200Full, 1, wx.EXPAND, 5)


        gSizer200.Add(sbSizer200Full, 1, wx.ALL | wx.EXPAND, 2)

        sbSizer200Half = wx.StaticBoxSizer(wx.StaticBox(sbSizer200.GetStaticBox(), wx.ID_ANY, u"Halvtid"), wx.VERTICAL)
        wSiz200Half = wx.WrapSizer(wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS)

        self.tmplNm200Half = wx.TextCtrl(sbSizer200Half.GetStaticBox(), wx.ID_ANY, u"Mallnamn", wx.DefaultPosition,
                                         wx.Size(180, -1), 0)
        self.tmplNm200Half.Bind(wx.EVT_LEFT_DOWN, self.clearTC)
        wSiz200Half.Add(self.tmplNm200Half, 0, wx.ALL, 5)

        self.state200Half = wx.CheckBox(sbSizer200Half.GetStaticBox(), wx.ID_ANY, u"Aktiv", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.state200Half.SetValue(True)
        wSiz200Half.Add(self.state200Half, 0, wx.ALL, 5)

        self.courseEnd200Half = wx.adv.DatePickerCtrl(sbSizer200Half.GetStaticBox(), wx.ID_ANY, wx.DefaultDateTime,
                                                      wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DROPDOWN)
        self.courseEnd200Half.SetToolTip(u"Kursslut")
        wSiz200Half.Add(self.courseEnd200Half, 0, wx.ALL, 5)
        self.weekLbl200Half = wx.StaticText(sbSizer200Half.GetStaticBox(), wx.ID_ANY, u"veckor:", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.weekLbl200Half.Wrap(-1)

        self.weekLbl200Half.SetFont(
            wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))

        wSiz200Half.Add(self.weekLbl200Half, 0, wx.ALL, 5)

        self.weeks200Half = wx.TextCtrl(sbSizer200Half.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                        wx.Size(50, -1), 0)
        wSiz200Half.Add(self.weeks200Half, 0, wx.ALL, 5)

        self.descr200Half = wx.TextCtrl(sbSizer200Half.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                        wx.Size(250, 200), wx.TE_MULTILINE)
        self.descr200Half.SetFont(
            wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))
        self.descr200Half.SetMinSize(wx.Size(250, 200))
        self.descr200Half.SetMaxSize(wx.Size(250, 200))

        wSiz200Half.Add(self.descr200Half, 0, wx.ALL, 5)

        sbSizer200Half.Add(wSiz200Half, 1, wx.EXPAND, 5)

        gSizer200.Add(sbSizer200Half, 1, wx.ALL | wx.EXPAND, 2)

        sbSizer200Quart = wx.StaticBoxSizer(wx.StaticBox(sbSizer200.GetStaticBox(), wx.ID_ANY, u"Kvartstid"),
                                            wx.VERTICAL)
        wSiz200Quart = wx.WrapSizer(wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS)

        self.tmplNm200Quart = wx.TextCtrl(sbSizer200Quart.GetStaticBox(), wx.ID_ANY, u"Mallnamn", wx.DefaultPosition,
                                         wx.Size(180, -1), 0)
        self.tmplNm200Quart.Bind(wx.EVT_LEFT_DOWN, self.clearTC)
        wSiz200Quart.Add(self.tmplNm200Quart, 0, wx.ALL, 5)

        self.state200Quart = wx.CheckBox(sbSizer200Quart.GetStaticBox(), wx.ID_ANY, u"Aktiv", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.state200Quart.SetValue(True)
        wSiz200Quart.Add(self.state200Quart, 0, wx.ALL, 5)

        self.courseEnd200Quart = wx.adv.DatePickerCtrl(sbSizer200Quart.GetStaticBox(), wx.ID_ANY, wx.DefaultDateTime,
                                                      wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DROPDOWN)
        self.courseEnd200Quart.SetToolTip(u"Kursslut")
        wSiz200Quart.Add(self.courseEnd200Quart, 0, wx.ALL, 5)
        self.weekLbl200Quart = wx.StaticText(sbSizer200Quart.GetStaticBox(), wx.ID_ANY, u"veckor:", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.weekLbl200Quart.Wrap(-1)

        self.weekLbl200Quart.SetFont(
            wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))

        wSiz200Quart.Add(self.weekLbl200Quart, 0, wx.ALL, 5)

        self.weeks200Quart = wx.TextCtrl(sbSizer200Quart.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                        wx.Size(50, -1), 0)
        wSiz200Quart.Add(self.weeks200Quart, 0, wx.ALL, 5)

        self.descr200Quart = wx.TextCtrl(sbSizer200Quart.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                        wx.Size(250, 200), wx.TE_MULTILINE)
        self.descr200Quart.SetFont(
            wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))
        self.descr200Quart.SetMinSize(wx.Size(250, 200))
        self.descr200Quart.SetMaxSize(wx.Size(250, 200))

        wSiz200Quart.Add(self.descr200Quart, 0, wx.ALL, 5)

        sbSizer200Quart.Add(wSiz200Quart, 1, wx.EXPAND, 5)

        gSizer200.Add(sbSizer200Quart, 1, wx.ALL | wx.EXPAND, 2)

        sbSizer200.Add(gSizer200, 1, wx.ALL | wx.EXPAND, 2)

        elvisGSizerAll.Add(sbSizer200, 1, wx.ALL | wx.EXPAND, 4)

        sbSizer150 = wx.StaticBoxSizer(wx.StaticBox(self.scrolledTmplWindow, wx.ID_ANY, u"150 poäng"), wx.VERTICAL)

        sbSizer150.SetMinSize(wx.Size(840, 300))
        gSizer150 = wx.GridSizer(0, 3, 0, 0)

        gSizer150.SetMinSize(wx.Size(840, 300))
        sbSizer150Full = wx.StaticBoxSizer(wx.StaticBox(sbSizer150.GetStaticBox(), wx.ID_ANY, u"Heltid"), wx.VERTICAL)
        wSiz150Full = wx.WrapSizer(wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS)

        self.tmplNm150Full = wx.TextCtrl(sbSizer150Full.GetStaticBox(), wx.ID_ANY, u"Mallnamn", wx.DefaultPosition,
                                         wx.Size(180, -1), 0)
        self.tmplNm150Full.Bind(wx.EVT_LEFT_DOWN, self.clearTC)
        wSiz150Full.Add(self.tmplNm150Full, 0, wx.ALL, 5)

        self.state150Full = wx.CheckBox(sbSizer150Full.GetStaticBox(), wx.ID_ANY, u"Aktiv", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.state150Full.SetValue(True)
        wSiz150Full.Add(self.state150Full, 0, wx.ALL, 5)

        self.courseEnd150Full = wx.adv.DatePickerCtrl(sbSizer150Full.GetStaticBox(), wx.ID_ANY, wx.DefaultDateTime,
                                                      wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DROPDOWN)
        self.courseEnd150Full.SetToolTip(u"Kursslut")
        wSiz150Full.Add(self.courseEnd150Full, 0, wx.ALL, 5)
        self.weekLbl150Full = wx.StaticText(sbSizer150Full.GetStaticBox(), wx.ID_ANY, u"veckor:", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.weekLbl150Full.Wrap(-1)

        self.weekLbl150Full.SetFont(
            wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))

        wSiz150Full.Add(self.weekLbl150Full, 0, wx.ALL, 5)


        self.weeks150Full = wx.TextCtrl(sbSizer150Full.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                        wx.Size(50, -1), 0)
        wSiz150Full.Add(self.weeks150Full, 0, wx.ALL, 5)

        self.descr150Full = wx.TextCtrl(sbSizer150Full.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                        wx.Size(250, 200), wx.TE_MULTILINE)
        self.descr150Full.SetFont(
            wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))
        self.descr150Full.SetMinSize(wx.Size(250, 200))
        self.descr150Full.SetMaxSize(wx.Size(250, 200))

        wSiz150Full.Add(self.descr150Full, 0, wx.ALL, 5)

        sbSizer150Full.Add(wSiz150Full, 1, wx.EXPAND, 5)

        gSizer150.Add(sbSizer150Full, 1, wx.ALL | wx.EXPAND, 2)

        sbSizer150Half = wx.StaticBoxSizer(wx.StaticBox(sbSizer150.GetStaticBox(), wx.ID_ANY, u"Halvtid"), wx.VERTICAL)
        wSiz150Half = wx.WrapSizer(wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS)

        self.tmplNm150Half = wx.TextCtrl(sbSizer150Half.GetStaticBox(), wx.ID_ANY, u"Mallnamn", wx.DefaultPosition,
                                         wx.Size(180, -1), 0)
        self.tmplNm150Half.Bind(wx.EVT_LEFT_DOWN, self.clearTC)
        wSiz150Half.Add(self.tmplNm150Half, 0, wx.ALL, 5)

        self.state150Half = wx.CheckBox(sbSizer150Half.GetStaticBox(), wx.ID_ANY, u"Aktiv", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.state150Half.SetValue(True)
        wSiz150Half.Add(self.state150Half, 0, wx.ALL, 5)

        self.courseEnd150Half = wx.adv.DatePickerCtrl(sbSizer150Half.GetStaticBox(), wx.ID_ANY, wx.DefaultDateTime,
                                                      wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DROPDOWN)
        self.courseEnd150Half.SetToolTip(u"Kursslut")
        wSiz150Half.Add(self.courseEnd150Half, 0, wx.ALL, 5)
        self.weekLbl150Half = wx.StaticText(sbSizer150Half.GetStaticBox(), wx.ID_ANY, u"veckor:", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.weekLbl150Half.Wrap(-1)

        self.weekLbl150Half.SetFont(
            wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))

        wSiz150Half.Add(self.weekLbl150Half, 0, wx.ALL, 5)

        self.weeks150Half = wx.TextCtrl(sbSizer150Half.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                        wx.Size(50, -1), 0)
        wSiz150Half.Add(self.weeks150Half, 0, wx.ALL, 5)

        self.descr150Half = wx.TextCtrl(sbSizer150Half.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                        wx.Size(250, 200), wx.TE_MULTILINE)
        self.descr150Half.SetFont(
            wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))
        self.descr150Half.SetMinSize(wx.Size(250, 200))
        self.descr150Half.SetMaxSize(wx.Size(250, 200))

        wSiz150Half.Add(self.descr150Half, 0, wx.ALL, 5)

        sbSizer150Half.Add(wSiz150Half, 1, wx.EXPAND, 5)

        gSizer150.Add(sbSizer150Half, 1, wx.ALL | wx.EXPAND, 2)

        sbSizer150Quart = wx.StaticBoxSizer(wx.StaticBox(sbSizer150.GetStaticBox(), wx.ID_ANY, u"Kvartstid"),
                                            wx.VERTICAL)
        wSiz150Quart = wx.WrapSizer(wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS)

        self.tmplNm150Quart = wx.TextCtrl(sbSizer150Quart.GetStaticBox(), wx.ID_ANY, u"Mallnamn", wx.DefaultPosition,
                                         wx.Size(180, -1), 0)
        self.tmplNm150Quart.Bind(wx.EVT_LEFT_DOWN, self.clearTC)
        wSiz150Quart.Add(self.tmplNm150Quart, 0, wx.ALL, 5)

        self.state150Quart = wx.CheckBox(sbSizer150Quart.GetStaticBox(), wx.ID_ANY, u"Aktiv", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.state150Quart.SetValue(True)
        wSiz150Quart.Add(self.state150Quart, 0, wx.ALL, 5)

        self.courseEnd150Quart = wx.adv.DatePickerCtrl(sbSizer150Quart.GetStaticBox(), wx.ID_ANY, wx.DefaultDateTime,
                                                      wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DROPDOWN)
        self.courseEnd150Quart.SetToolTip(u"Kursslut")
        wSiz150Quart.Add(self.courseEnd150Quart, 0, wx.ALL, 5)
        self.weekLbl150Quart = wx.StaticText(sbSizer150Quart.GetStaticBox(), wx.ID_ANY, u"veckor:", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.weekLbl150Quart.Wrap(-1)

        self.weekLbl150Quart.SetFont(
            wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))

        wSiz150Quart.Add(self.weekLbl150Quart, 0, wx.ALL, 5)

        self.weeks150Quart = wx.TextCtrl(sbSizer150Quart.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                        wx.Size(50, -1), 0)
        wSiz150Quart.Add(self.weeks150Quart, 0, wx.ALL, 5)

        self.descr150Quart = wx.TextCtrl(sbSizer150Quart.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                        wx.Size(250, 200), wx.TE_MULTILINE)
        self.descr150Quart.SetFont(
            wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))
        self.descr150Quart.SetMinSize(wx.Size(250, 200))
        self.descr150Quart.SetMaxSize(wx.Size(250, 200))

        wSiz150Quart.Add(self.descr150Quart, 0, wx.ALL, 5)

        sbSizer150Quart.Add(wSiz150Quart, 1, wx.EXPAND, 5)

        gSizer150.Add(sbSizer150Quart, 1, wx.ALL | wx.EXPAND, 2)

        sbSizer150.Add(gSizer150, 1, wx.ALL | wx.EXPAND, 2)

        elvisGSizerAll.Add(sbSizer150, 1, wx.ALL | wx.EXPAND, 4)

        sbSizer50 = wx.StaticBoxSizer(wx.StaticBox(self.scrolledTmplWindow, wx.ID_ANY, u"50 poäng"), wx.VERTICAL)

        sbSizer50.SetMinSize(wx.Size(840, 300))
        gSizer50 = wx.GridSizer(0, 3, 0, 0)

        gSizer50.SetMinSize(wx.Size(840, 300))

        gSizer50.Add((0, 0), 1, wx.EXPAND, 5)

        sbSizer50Half = wx.StaticBoxSizer(wx.StaticBox(sbSizer50.GetStaticBox(), wx.ID_ANY, u"Halvtid"), wx.VERTICAL)
        wSiz50Half = wx.WrapSizer(wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS)

        self.tmplNm50Half = wx.TextCtrl(sbSizer50Half.GetStaticBox(), wx.ID_ANY, u"Mallnamn", wx.DefaultPosition,
                                         wx.Size(180, -1), 0)
        self.tmplNm50Half.Bind(wx.EVT_LEFT_DOWN, self.clearTC)
        wSiz50Half.Add(self.tmplNm50Half, 0, wx.ALL, 5)

        self.state50Half = wx.CheckBox(sbSizer50Half.GetStaticBox(), wx.ID_ANY, u"Aktiv", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.state50Half.SetValue(True)
        wSiz50Half.Add(self.state50Half, 0, wx.ALL, 5)

        self.courseEnd50Half = wx.adv.DatePickerCtrl(sbSizer50Half.GetStaticBox(), wx.ID_ANY, wx.DefaultDateTime,
                                                      wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DROPDOWN)
        self.courseEnd50Half.SetToolTip(u"Kursslut")
        wSiz50Half.Add(self.courseEnd50Half, 0, wx.ALL, 5)
        self.weekLbl50Half = wx.StaticText(sbSizer50Half.GetStaticBox(), wx.ID_ANY, u"veckor:", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.weekLbl50Half.Wrap(-1)

        self.weekLbl50Half.SetFont(
            wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))

        wSiz50Half.Add(self.weekLbl50Half, 0, wx.ALL, 5)

        self.weeks50Half = wx.TextCtrl(sbSizer50Half.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                        wx.Size(50, -1), 0)
        wSiz50Half.Add(self.weeks50Half, 0, wx.ALL, 5)

        self.descr50Half = wx.TextCtrl(sbSizer50Half.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                        wx.Size(250, 200), wx.TE_MULTILINE)
        self.descr50Half.SetFont(
            wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))
        self.descr50Half.SetMinSize(wx.Size(250, 200))
        self.descr50Half.SetMaxSize(wx.Size(250, 200))

        wSiz50Half.Add(self.descr50Half, 0, wx.ALL, 5)

        sbSizer50Half.Add(wSiz50Half, 1, wx.EXPAND, 5)

        gSizer50.Add(sbSizer50Half, 1, wx.ALL | wx.EXPAND, 2)

        sbSizer50Quart = wx.StaticBoxSizer(wx.StaticBox(sbSizer50.GetStaticBox(), wx.ID_ANY, u"Kvartstid"), wx.VERTICAL)
        wSiz50Quart = wx.WrapSizer(wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS)

        self.tmplNm50Quart = wx.TextCtrl(sbSizer50Quart.GetStaticBox(), wx.ID_ANY, u"Mallnamn", wx.DefaultPosition,
                                         wx.Size(180, -1), 0)
        self.tmplNm50Quart.Bind(wx.EVT_LEFT_DOWN, self.clearTC)
        wSiz50Quart.Add(self.tmplNm50Quart, 0, wx.ALL, 5)

        self.state50Quart = wx.CheckBox(sbSizer50Quart.GetStaticBox(), wx.ID_ANY, u"Aktiv", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.state50Quart.SetValue(True)
        wSiz50Quart.Add(self.state50Quart, 0, wx.ALL, 5)

        self.courseEnd50Quart = wx.adv.DatePickerCtrl(sbSizer50Quart.GetStaticBox(), wx.ID_ANY, wx.DefaultDateTime,
                                                      wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DROPDOWN)
        self.courseEnd50Quart.SetToolTip(u"Kursslut")
        wSiz50Quart.Add(self.courseEnd50Quart, 0, wx.ALL, 5)
        self.weekLbl50Quart = wx.StaticText(sbSizer50Quart.GetStaticBox(), wx.ID_ANY, u"veckor:", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.weekLbl50Quart.Wrap(-1)

        self.weekLbl50Quart.SetFont(
            wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))

        wSiz50Quart.Add(self.weekLbl50Quart, 0, wx.ALL, 5)

        self.weeks50Quart = wx.TextCtrl(sbSizer50Quart.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                        wx.Size(50, -1), 0)
        wSiz50Quart.Add(self.weeks50Quart, 0, wx.ALL, 5)

        self.descr50Quart = wx.TextCtrl(sbSizer50Quart.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                        wx.Size(250, 200), wx.TE_MULTILINE)
        self.descr50Quart.SetFont(
            wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))
        self.descr50Quart.SetMinSize(wx.Size(250, 200))
        self.descr50Quart.SetMaxSize(wx.Size(250, 200))

        wSiz50Quart.Add(self.descr50Quart, 0, wx.ALL, 5)

        sbSizer50Quart.Add(wSiz50Quart, 1, wx.EXPAND, 5)

        gSizer50.Add(sbSizer50Quart, 1, wx.ALL | wx.EXPAND, 2)

        sbSizer50.Add(gSizer50, 1, wx.ALL | wx.EXPAND, 2)

        elvisGSizerAll.Add(sbSizer50, 1, wx.EXPAND, 5)

        self.scrolledTmplWindow.SetSizer(elvisGSizerAll)
        self.scrolledTmplWindow.Layout()
        elvisTopbSizer.Add(self.scrolledTmplWindow, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(elvisTopbSizer)


        self.Layout()

        self.Centre(wx.BOTH)
        self.Show(True)

    def __del__(self):
        pass

    def clearTC(self, evt):
        tc = evt.GetEventObject()
        val = tc.GetValue()
        if val == "Mallnamn":
            tc.SetValue('')
