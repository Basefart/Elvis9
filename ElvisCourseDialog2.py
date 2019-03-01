# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Dec 17 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc


###########################################################################
## Class elvisNewCourseDlg
###########################################################################

class ElvisCourseDlg(wx.Dialog):

    def __init__(self, parent, kod):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"Skapa ny kurs", pos=wx.DefaultPosition,
                           size=wx.Size(500, 500), style=wx.DEFAULT_DIALOG_STYLE | wx.STAY_ON_TOP)
        self.anmkod = kod
        self.hel = True
        self.halv = True
        self.kvart = True
        self.dlgValues = {'anmkod':'', 'name':'', 'points':'', 'heltid': self.hel, 'halvtid': self.halv, 'kvartstid': self.kvart, 'kurstyp': 'Normal'}
        if self.anmkod is not 'Ny':
            self.SetTitle(u"Redigera kurs")
            self.dlgValues = self.GetParent().getDlgValues(self.anmkod)
            self.hel = eval(self.dlgValues['heltid'])
            self.halv = eval(self.dlgValues['halvtid'])
            self.kvart = eval(self.dlgValues['kvartstid'])
        self.greatgrandparentRel = False
        self.boldfont = wx.SystemSettings.GetFont(wx.SYS_DEFAULT_GUI_FONT)
        self.boldfont.SetWeight(wx.FONTWEIGHT_BOLD)
        self.boldfont.SetPointSize(12)

        self.SetSizeHints(wx.Size(500, 500), wx.Size(500, 500))
        self.SetFont(
            wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))

        dlgBSizer = wx.BoxSizer(wx.VERTICAL)

        bSizer17 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer17.SetMinSize(wx.Size(450, 30))
        sbSizer2 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, wx.EmptyString), wx.VERTICAL)

        fgSizer2 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer2.SetFlexibleDirection(wx.BOTH)
        fgSizer2.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText10 = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Anmälningskod: ", wx.DefaultPosition,
                                            wx.Size(150, -1), wx.ALIGN_RIGHT)
        self.m_staticText10.Wrap(-1)

        self.m_staticText10.SetFont(
            wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))

        fgSizer2.Add(self.m_staticText10, 0, wx.ALL, 5)

        self.anmkodTxt = wx.TextCtrl(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                     wx.Size(250, 30), 0)
        self.anmkodTxt.SetFont(
            wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))
        self.anmkodTxt.SetValue(self.dlgValues['anmkod'])
        fgSizer2.Add(self.anmkodTxt, 0, wx.ALL, 5)

        sbSizer2.Add(fgSizer2, 1, wx.EXPAND, 5)



        bSizer17.Add(sbSizer2, 1, wx.FIXED_MINSIZE, 5)

        dlgBSizer.Add(bSizer17, 1, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL | wx.FIXED_MINSIZE, 3)

        bSizer171 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer171.SetMinSize(wx.Size(450, 30))
        sbSizer21 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, wx.EmptyString), wx.VERTICAL)

        fgSizer21 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer21.SetFlexibleDirection(wx.BOTH)
        fgSizer21.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText101 = wx.StaticText(sbSizer21.GetStaticBox(), wx.ID_ANY, u"Namn: ", wx.DefaultPosition,
                                             wx.Size(150, -1), wx.ALIGN_RIGHT)
        self.m_staticText101.Wrap(-1)

        self.m_staticText101.SetFont(
            wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))

        fgSizer21.Add(self.m_staticText101, 0, wx.ALL, 5)

        self.nameTxt = wx.TextCtrl(sbSizer21.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                   wx.Size(250, 30), 0)
        self.nameTxt.SetFont(
            wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))
        self.nameTxt.SetValue(self.dlgValues['name'])

        fgSizer21.Add(self.nameTxt, 0, wx.ALL, 5)

        sbSizer21.Add(fgSizer21, 1, wx.EXPAND, 5)

        bSizer171.Add(sbSizer21, 1, wx.FIXED_MINSIZE, 5)

        dlgBSizer.Add(bSizer171, 1, wx.ALIGN_CENTER_HORIZONTAL | wx.FIXED_MINSIZE, 3)

        bSizer1711 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer1711.SetMinSize(wx.Size(450, 30))
        sbSizer211 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, wx.EmptyString), wx.VERTICAL)

        fgSizer211 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer211.SetFlexibleDirection(wx.BOTH)
        fgSizer211.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText1011 = wx.StaticText(sbSizer211.GetStaticBox(), wx.ID_ANY, u"Poäng: ", wx.DefaultPosition,
                                              wx.Size(150, -1), wx.ALIGN_RIGHT)
        self.m_staticText1011.Wrap(-1)

        self.m_staticText1011.SetFont(
            wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))

        fgSizer211.Add(self.m_staticText1011, 0, wx.ALL, 5)

        self.pointsTxt = wx.TextCtrl(sbSizer211.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                     wx.Size(80, 30), 0)
        self.pointsTxt.SetFont(
            wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))
        self.pointsTxt.SetValue(self.dlgValues['points'])
        fgSizer211.Add(self.pointsTxt, 0, wx.ALL, 5)

        sbSizer211.Add(fgSizer211, 1, wx.EXPAND, 5)

        bSizer1711.Add(sbSizer211, 1, wx.FIXED_MINSIZE, 5)

        dlgBSizer.Add(bSizer1711, 1, wx.ALIGN_CENTER_HORIZONTAL | wx.FIXED_MINSIZE, 3)

        bSizer17111 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer17111.SetMinSize(wx.Size(450, 30))
        sbSizer2111 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, wx.EmptyString), wx.VERTICAL)

        fgSizer2111 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer2111.SetFlexibleDirection(wx.BOTH)
        fgSizer2111.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText17 = wx.StaticText(sbSizer2111.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                            wx.Size(150, -1), 0)
        self.m_staticText17.Wrap(-1)

        fgSizer2111.Add(self.m_staticText17, 0, wx.ALL, 5)

        self.heltidChk = wx.CheckBox(sbSizer2111.GetStaticBox(), wx.ID_ANY, u"Heltid", wx.DefaultPosition,
                                     wx.Size(200, 30), 0)
        self.heltidChk.SetFont(
            wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))
        self.heltidChk.SetValue(self.hel)


        fgSizer2111.Add(self.heltidChk, 0, wx.ALL, 5)

        sbSizer2111.Add(fgSizer2111, 1, wx.EXPAND, 5)

        bSizer17111.Add(sbSizer2111, 1, wx.FIXED_MINSIZE, 5)

        dlgBSizer.Add(bSizer17111, 1, wx.ALIGN_CENTER_HORIZONTAL | wx.FIXED_MINSIZE, 3)

        bSizer171111 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer171111.SetMinSize(wx.Size(450, 30))
        sbSizer21111 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, wx.EmptyString), wx.VERTICAL)

        fgSizer21111 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer21111.SetFlexibleDirection(wx.BOTH)
        fgSizer21111.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText171 = wx.StaticText(sbSizer21111.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                             wx.Size(150, -1), 0)
        self.m_staticText171.Wrap(-1)

        fgSizer21111.Add(self.m_staticText171, 0, wx.ALL, 5)

        self.halvtidChk = wx.CheckBox(sbSizer21111.GetStaticBox(), wx.ID_ANY, u"Halvtid", wx.DefaultPosition,
                                      wx.Size(200, 30), 0)
        self.halvtidChk.SetFont(
            wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))
        self.halvtidChk.SetValue(self.halv)

        fgSizer21111.Add(self.halvtidChk, 0, wx.ALL, 5)

        sbSizer21111.Add(fgSizer21111, 1, wx.EXPAND, 5)

        bSizer171111.Add(sbSizer21111, 1, wx.FIXED_MINSIZE, 5)

        dlgBSizer.Add(bSizer171111, 1, wx.ALIGN_CENTER_HORIZONTAL | wx.FIXED_MINSIZE, 3)

        bSizer1711111 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer1711111.SetMinSize(wx.Size(450, 30))
        sbSizer211111 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, wx.EmptyString), wx.VERTICAL)

        fgSizer211111 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer211111.SetFlexibleDirection(wx.BOTH)
        fgSizer211111.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText1711 = wx.StaticText(sbSizer211111.GetStaticBox(), wx.ID_ANY, wx.EmptyString,
                                              wx.DefaultPosition, wx.Size(150, -1), 0)
        self.m_staticText1711.Wrap(-1)

        fgSizer211111.Add(self.m_staticText1711, 0, wx.ALL, 5)

        self.kvartstidChk = wx.CheckBox(sbSizer211111.GetStaticBox(), wx.ID_ANY, u"Kvartstid", wx.DefaultPosition,
                                        wx.Size(200, 30), 0)
        self.kvartstidChk.SetFont(
            wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))
        self.kvartstidChk.SetValue(self.kvart)

        fgSizer211111.Add(self.kvartstidChk, 0, wx.ALL, 5)

        sbSizer211111.Add(fgSizer211111, 1, wx.EXPAND, 5)

        bSizer1711111.Add(sbSizer211111, 1, wx.FIXED_MINSIZE, 5)

        dlgBSizer.Add(bSizer1711111, 1, wx.ALIGN_CENTER_HORIZONTAL | wx.FIXED_MINSIZE, 3)

        bSizer17112 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer17112.SetMinSize(wx.Size(450, 30))
        sbSizer2112 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, wx.EmptyString), wx.VERTICAL)

        fgSizer2112 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer2112.SetFlexibleDirection(wx.BOTH)
        fgSizer2112.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText10111 = wx.StaticText(sbSizer2112.GetStaticBox(), wx.ID_ANY, u"Kurstyp: ", wx.DefaultPosition,
                                               wx.Size(150, -1), wx.ALIGN_RIGHT)
        self.m_staticText10111.Wrap(-1)

        self.m_staticText10111.SetFont(
            wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))

        fgSizer2112.Add(self.m_staticText10111, 0, wx.ALL, 5)

        kurstypComboChoices = [u"Välj kurstyp", u"Normal", u"APL", u"HLR", u"Laboration"]
        self.kurstypCombo = wx.ComboBox(sbSizer2112.GetStaticBox(), wx.ID_ANY, u"Välj kurstyp", wx.DefaultPosition,
                                        wx.Size(180, 30), kurstypComboChoices, 0)
        self.kurstypCombo.SetFont(
            wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))
        self.kurstypCombo.SetMinSize(wx.Size(180, 30))
        self.kurstypCombo.SetMaxSize(wx.Size(180, -1))
        self.kurstypCombo.SetValue(self.dlgValues['kurstyp'])

        fgSizer2112.Add(self.kurstypCombo, 0, wx.ALL, 5)

        sbSizer2112.Add(fgSizer2112, 1, wx.EXPAND, 5)

        bSizer17112.Add(sbSizer2112, 1, wx.FIXED_MINSIZE, 5)

        dlgBSizer.Add(bSizer17112, 1, wx.ALIGN_CENTER_HORIZONTAL | wx.FIXED_MINSIZE, 3)

        bSizer17111111 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer17111111.SetMinSize(wx.Size(450, 30))
        fgSizer2111111 = wx.FlexGridSizer(0, 2, 0, 100)
        fgSizer2111111.SetFlexibleDirection(wx.BOTH)
        fgSizer2111111.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        fgSizer2111111.Add((20, 0), 1, wx.EXPAND, 5)
        bSizer13 = wx.BoxSizer(wx.HORIZONTAL)

        self.dlgSaveBtn = wx.Button(self, wx.ID_ANY, u"Spara", wx.DefaultPosition, wx.DefaultSize, 0)
        self.dlgSaveBtn.SetFont(
            wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))

        bSizer13.Add(self.dlgSaveBtn, 0, wx.ALL |wx.EXPAND, 5)

        if self.anmkod is not 'Ny':
            self.dlgRemoveBtn = wx.Button(self, wx.ID_ANY, u"Ta bort", wx.DefaultPosition, wx.DefaultSize, 0)
            self.dlgRemoveBtn.SetFont(wx.Font(self.boldfont))

            self.dlgRemoveBtn.SetBackgroundColour(wx.Colour(240, 0, 0))
            self.dlgRemoveBtn.SetForegroundColour(wx.Colour(255, 255, 255))
            bSizer13.Add(self.dlgRemoveBtn, 0, wx.ALL | wx.EXPAND, 5)

            self.dlgCloseBtn = wx.Button(self, wx.ID_ANY, u"Stäng", wx.DefaultPosition, wx.DefaultSize, 0)
            self.dlgCloseBtn.SetFont(
                wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))

            bSizer13.Add(self.dlgCloseBtn, 0, wx.ALL | wx.EXPAND, 5)
        else:
            self.dlgCloseBtn = wx.Button(self, wx.ID_ANY, u"Stäng", wx.DefaultPosition, wx.DefaultSize, 0)
            self.dlgCloseBtn.SetFont(
                wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))

            bSizer13.Add(self.dlgCloseBtn, 0, wx.ALL | wx.EXPAND, 5)

        fgSizer2111111.Add(bSizer13, 1, wx.ALL | wx.EXPAND, 8)

        bSizer17111111.Add(fgSizer2111111, 1, wx.EXPAND, 5)

        dlgBSizer.Add(bSizer17111111, 1, wx.EXPAND, 5)

        self.SetSizer(dlgBSizer)



        self.Layout()

        self.Centre(wx.BOTH)



        # Connect Events
        self.dlgSaveBtn.Bind(wx.EVT_BUTTON, self.saveDlgValues)
        self.dlgCloseBtn.Bind(wx.EVT_BUTTON, self.onClose)
        if self.anmkod is not 'Ny':
            self.dlgRemoveBtn.Bind(wx.EVT_BUTTON, self.onRemove)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def saveDlgValues(self, event):
        values = {'id': self.anmkod, 'anmkod': self.anmkodTxt.GetValue(), 'name': self.nameTxt.GetValue(),
                  'points': self.pointsTxt.GetValue(), 'heltid': str(self.heltidChk.GetValue()),
                  'halvtid': str(self.halvtidChk.GetValue()), 'kvartstid': str(self.kvartstidChk.GetValue()),
                  'kurstyp': self.kurstypCombo.GetValue()}
        self.GetParent().processDlgResponse(values)

    def courseToEdit(self):
        dlgValues = self.GetParent().getDlgValues(self.anmkod)
        self.anmkodTxt.SetValue(dlgValues['anmkod'])
        self.nameTxt.SetValue(dlgValues['name'])
        self.pointsTxt.SetValue(dlgValues['points'])
        self.heltidChk.SetValue(bool(dlgValues['heltid']))
        self.halvtidChk.SetValue(bool(dlgValues['halvtid']))
        self.kvartstidChk.SetValue(bool(dlgValues['kvartstid']))
        self.kurstypCombo.SetValue(dlgValues['kurstyp'])

    def onRemove(self, evt):
        self.GetParent().removeCourse(self.anmkod)

    def prepReload(self):
        self.dlgCloseBtn.SetLabelText(u"Stäng ↻")
        self.dlgCloseBtn.SetFont(self.boldfont)
        self.greatgrandparentRel = True

    def onClose(self, event):
        event.Skip()
        if self.greatgrandparentRel:
            self.GetParent().resurrectMyGrandfather()
        self.Destroy()
