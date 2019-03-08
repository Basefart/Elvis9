# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Mar 23 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.aui
from ElvisUltimateCourseList1e import ElvisUltimateCourseList
from ElvisTemplates import ElvisTmplPanel
from ExemElvis import ExemElvis
from ElvisFeedPanel import ElvisFeedPanel
import wx.locale
import locale
import wx.adv
import subprocess

import gettext

_ = gettext.gettext

locale.setlocale(locale.LC_ALL, '')
locale.setlocale(locale.LC_ALL, 'swedish')

###########################################################################
## Class ElvisFrame
###########################################################################

class ElvisFrame(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=_(u"Älvis - en robot för Alvis"), pos=wx.DefaultPosition,
                          size=wx.Size(1100, 800), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL | wx.EXPAND)

        self.oldcust = ""
        self.firstrun = 1

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetBackgroundStyle(wx.BG_STYLE_ERASE)
        self.locale = wx.Locale(wx.LANGUAGE_SWEDISH)
        self.elvisbSizer1 = wx.BoxSizer(wx.VERTICAL)

        self.ElvisToolbar = wx.aui.AuiToolBar(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1, 60),
                                               wx.aui.AUI_TB_HORZ_LAYOUT | wx.EXPAND | wx.TAB_TRAVERSAL)
        self.ElvisToolbar.SetToolSeparation(8)
        self.ElvisToolbar.SetMargins(wx.Size(6, 4))
        self.ElvisToolbar.SetToolPacking(8)
        self.ElvisToolbar.SetMinSize(wx.Size(-1, 60))
        self.ElvisToolbar.SetMaxSize(wx.Size(-1, 60))
        self.ElvisToolbar.SetToolBitmapSize(wx.Size(15, 60))
        self.ElvisToolbar.SetFont(
            wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))

        self.ElvisToolbar2 = wx.aui.AuiToolBar(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1, 60),
                                               wx.aui.AUI_TB_HORZ_LAYOUT | wx.EXPAND | wx.TAB_TRAVERSAL)
        self.ElvisToolbar2.SetToolSeparation(8)
        self.ElvisToolbar2.SetMargins(wx.Size(6, 4))
        self.ElvisToolbar2.SetToolPacking(8)
        self.ElvisToolbar2.SetMinSize(wx.Size(-1, 60))
        self.ElvisToolbar2.SetMaxSize(wx.Size(-1, 60))
        self.ElvisToolbar2.SetToolBitmapSize(wx.Size(15, 60))
        self.ElvisToolbar2.SetFont(
            wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))
        ElvisComboChoices = [u"Välj kund", u"Södertälje", u"Freja", u"Huddinge", u"Norrtälje", u"Salem", u"Järfälla"]
        self.ElvisCombo = wx.ComboBox(self.ElvisToolbar, wx.ID_ANY, u"Välj kund", wx.DefaultPosition, wx.DefaultSize,
                                      ElvisComboChoices, 0)
        self.ElvisCombo.SetToolTip(u"Här väljer du kund")
        self.ElvisToolbar.AddControl(self.ElvisCombo)
        self.ElvisApplicationStart = wx.adv.DatePickerCtrl(self.ElvisToolbar, wx.ID_ANY, wx.DefaultDateTime,
                                                   wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DROPDOWN)
        self.ElvisApplicationStart.SetToolTip(u"Ansökningstiden börjar")
        self.ElvisToolbar.AddControl(self.ElvisApplicationStart)
        self.ElvisApplicationFinish = wx.adv.DatePickerCtrl(self.ElvisToolbar, wx.ID_ANY, wx.DefaultDateTime,
                                                   wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DROPDOWN)
        self.ElvisApplicationFinish.SetToolTip(u"Ansökningstiden slutar")
        self.ElvisToolbar.AddControl(self.ElvisApplicationFinish)
        self.ElvisCourseStart = wx.adv.DatePickerCtrl(self.ElvisToolbar, wx.ID_ANY, wx.DefaultDateTime, wx.Point(-1, -1),
                                                   wx.DefaultSize, wx.adv.DP_DROPDOWN)
        self.ElvisCourseStart.SetToolTip(u"Kursen börjar")
        self.ElvisToolbar.AddControl(self.ElvisCourseStart)
        self.ElvisFeedName = wx.TextCtrl(self.ElvisToolbar, wx.ID_ANY, u"Inmatningens namn", wx.DefaultPosition,
                                         wx.Size(220, -1), 0)
        self.ElvisFeedName.SetMaxLength(10)
        self.ElvisFeedName.SetToolTip(u"Inmatningens namn. Används för mallar.")
        self.ElvisFeedName.Bind(wx.EVT_LEFT_DOWN, self.clearTC)

        self.ElvisToolbar.AddControl(self.ElvisFeedName)

        self.ElvisPeriod = wx.TextCtrl(self.ElvisToolbar, wx.ID_ANY, u"Period", wx.DefaultPosition,
                                         wx.Size(100, -1), 0)
        self.ElvisPeriod.SetToolTip(u"Inmatningens period. Används för mallar.")
        self.ElvisPeriod.Bind(wx.EVT_LEFT_DOWN, self.clearTC)

        self.ElvisToolbar.AddControl(self.ElvisPeriod)

        self.ElvisComment = wx.TextCtrl(self.ElvisToolbar2, wx.ID_ANY, u"Generell kursbeskrivning. Skriv heltid.", wx.DefaultPosition,
                                       wx.Size(400, 60), wx.TE_MULTILINE)
        self.ElvisComment.SetToolTip(u"Generell kursbeskrivning. Skriv som vid heltid.")
        self.ElvisComment.Bind(wx.EVT_LEFT_DOWN, self.clearTC)
        self.ElvisToolbar2.AddControl(self.ElvisComment)

        self.oneTmpl = wx.CheckBox(self.ElvisToolbar2, wx.ID_ANY, u"Bara en mall", wx.DefaultPosition, wx.DefaultSize,
                                   wx.TRANSPARENT_WINDOW)

        self.oneTmpl.SetFont(
            wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))

        self.ElvisToolbar2.AddControl(self.oneTmpl)
        self.tmplFiller = wx.Button(self.ElvisToolbar2, wx.ID_ANY, u"Skapa mallunderlag", wx.DefaultPosition,
                                    wx.DefaultSize, 0)
        self.tmplFiller.SetFont(
            wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))

        self.ElvisToolbar2.AddControl(self.tmplFiller)
        self.saveTemplates = wx.Button(self.ElvisToolbar2, wx.ID_ANY, u"Spara mallar", wx.DefaultPosition,
                                    wx.DefaultSize, 0)
        self.saveTemplates.SetFont(
            wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))

        self.ElvisToolbar2.AddControl(self.saveTemplates)

        self.ElvisToolbar.Realize()
        self.ElvisToolbar2.Realize()

        self.elvisbSizer1.Add(self.ElvisToolbar, 1, wx.EXPAND)
        self.elvisbSizer1.Add(self.ElvisToolbar2, 1, wx.EXPAND)

        self.ElvisStatus = self.CreateStatusBar(1, wx.STB_SIZEGRIP, wx.ID_ANY)
        self.ElvisStatus.SetFont(
            wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))

        self.ElvisMenuBar = wx.MenuBar(0)
        self.ElvisMenuBar.SetFont(
            wx.Font(11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))

        self.ElvisMenu = wx.Menu()
        self.ElvisHelp = wx.MenuItem(self.ElvisMenu, wx.ID_ANY, u"&Hjälp", u"Hjälpfil", wx.ITEM_NORMAL)
        self.ElvisMenu.Append(self.ElvisHelp)

        self.QLSodert = wx.MenuItem(self.ElvisMenu, wx.ID_ANY, u"Redigera S&ödertäljekurser", u"Södertäljekurser", wx.ITEM_NORMAL)
        self.ElvisMenu.Append(self.QLSodert)
        self.QLFreja = wx.MenuItem(self.ElvisMenu, wx.ID_ANY, u"Redigera Fre&jakurser", u"Frejakurser", wx.ITEM_NORMAL)
        self.ElvisMenu.Append(self.QLFreja)
        self.QLHudd = wx.MenuItem(self.ElvisMenu, wx.ID_ANY, u"Redigera Hudd&ingekurser", u"Huddingekurser", wx.ITEM_NORMAL)
        self.ElvisMenu.Append(self.QLHudd)
        self.QLNorrt = wx.MenuItem(self.ElvisMenu, wx.ID_ANY, u"Redigera Norrt&äljekurser", u"Norrtäljekurser", wx.ITEM_NORMAL)
        self.ElvisMenu.Append(self.QLNorrt)
        self.QLSalem = wx.MenuItem(self.ElvisMenu, wx.ID_ANY, u"Redigera Sale&mkurser", u"Salemkurser", wx.ITEM_NORMAL)
        self.ElvisMenu.Append(self.QLSalem)
        self.QLJarf = wx.MenuItem(self.ElvisMenu, wx.ID_ANY, u"Redigera Järfä&llakurser", u"Järfällakurser", wx.ITEM_NORMAL)
        self.ElvisMenu.Append(self.QLJarf)

        self.ElvisClose = wx.MenuItem(self.ElvisMenu, wx.ID_ANY, u"Avsl&uta", u"Stäng programmet", wx.ITEM_NORMAL)
        self.ElvisMenu.Append(self.ElvisClose)

        self.ElvisMenuBar.Append(self.ElvisMenu, u"&Arkiv")

        self.SetMenuBar(self.ElvisMenuBar)

        self.Centre(wx.BOTH)
        self.Layout()
        self.onChangeCustomer(wx.EVT_COMBOBOX)

        # Connect Events
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.onEraseBackground)
        self.ElvisCombo.Bind(wx.EVT_COMBOBOX, self.onChangeCustomer)
        self.ElvisCombo.Bind(wx.EVT_COMBOBOX_DROPDOWN, self.setOldCustomer)
        self.Bind(wx.EVT_MENU, self.onClose, self.ElvisClose)
        self.Bind(wx.EVT_MENU, self.editSodert, self.QLSodert)
        self.Bind(wx.EVT_MENU, self.editFreja, self.QLFreja)
        self.Bind(wx.EVT_MENU, self.editHudd, self.QLHudd)
        self.Bind(wx.EVT_MENU, self.editNorrt, self.QLNorrt)
        self.Bind(wx.EVT_MENU, self.editSalem, self.QLSalem)
        self.Bind(wx.EVT_MENU, self.editJarf, self.QLJarf)
        self.tmplFiller.Bind(wx.EVT_BUTTON, self.fillTemplates)
        self.saveTemplates.Bind(wx.EVT_BUTTON, self.saveTmpls2xml)
        self.oneTmpl.Bind(wx.EVT_CHECKBOX, self.setActiveState)

        self.Show(True)
        if hasattr(self, 'courselist') and isinstance(self.courselist, ElvisUltimateCourseList):
            self.courselist.SetFocus()

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def onEraseBackground(self, evt):
        dc = evt.GetDC()
        if not dc:
            dc = wx.ClientDC(self)
            rect = self.GetUpdateRegion().GetBox()
            dc.SetClippingRegion(rect)

        dc.Clear()
        width, height = wx.GetDisplaySize()
        x = 0
        y = 30
        bmp = wx.Bitmap("elvis.jpg")
        dc.DrawBitmap(bmp, x, y)

    def makeWorkTabs(self, custsel):
        if hasattr(self, 'ElvisWorktabs'):
            self.ElvisWorktabs.Destroy()
        self.ElvisWorktabs = wx.Notebook(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        self.ElvisWorktabs.Hide()
        self.ElvisWorktabs.SetFont(
            wx.Font(11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))
        elvisP1 = wx.Panel(self.ElvisWorktabs, wx.ID_ANY, wx.DefaultPosition, wx.Size(1050, 800),
                                wx.TAB_TRAVERSAL | wx.ALL)


        # Kurslista
        self.courselist = ElvisUltimateCourseList(self.ElvisWorktabs, custsel)
        self.courselist.SetBackgroundColour(wx.Colour(255, 255, 255, 120))
        self.ElvisWorktabs.AddPage(self.courselist, _(u"Redigera kurslista"), True)
        elvisbSizer2 = wx.BoxSizer(wx.HORIZONTAL)

        # Mallar
        self.templates = ElvisTmplPanel(self.ElvisWorktabs)
        self.ElvisWorktabs.AddPage(self.templates, _(u"Mallhantering"), False)
        self.ElvisWorktabs.AddPage(elvisP1, _(u"Inmatning"), False)

        elvisP1.SetSizer(elvisbSizer2)
        self.feedpanel = ElvisFeedPanel(elvisP1)
        elvisbSizer2.Add(self.feedpanel, 1, wx.EXPAND)
        elvisP1.Layout()
        self.elvisbSizer1.Fit(elvisP1)


        self.elvisbSizer1.Add(self.ElvisWorktabs, 1, wx.ALL, 10)

        self.SetSizer(self.elvisbSizer1)
        if hasattr(self, 'courselist') and isinstance(self.courselist, ElvisUltimateCourseList):
            self.courselist.Bind(wx.EVT_ENTER_WINDOW, self.onEnterWindow)
        if custsel != 'Välj kund':
            self.ElvisWorktabs.Show()

    def editSodert(self, evt):
        subprocess.Popen('QuickList.exe Södertälje')

    def editFreja(self, evt):
        subprocess.Popen('QuickList.exe Freja')

    def editHudd(self, evt):
        subprocess.Popen('QuickList.exe Huddinge')

    def editNorrt(self, evt):
        subprocess.Popen('QuickList.exe Norrtälje')

    def editSalem(self, evt):
        subprocess.Popen('QuickList.exe Salem')

    def editJarf(self, evt):
        subprocess.Popen('QuickList.exe Järfälla')

    def halfpaceadjust(self, string):
        halfdict = {'Heltid': 'Halvtid', 'heltid': 'halvtid', '100%': '50%', '100 %': '50 %'}
        for k, v in halfdict.items():
            string = string.replace(k, v)
        return string

    def quartpaceadjust(self, string):
        quartdict = {'Heltid': 'Kvartstid', 'heltid': 'kvartstid', '100%': '25%', '100 %': '25 %'}
        for k, v in quartdict.items():
            string = string.replace(k, v)
        return string

    def convertAndDistribute(self, values):
        weekdict = {'five': 5, 'seven': 7, 'ten': 10, 'fifteen': 15, 'twenty': 20, 'thirty': 30, 'forty': 40}
        fulltime100 = 7 * weekdict['five'] - 3
        halftime100 = 7 * weekdict['ten'] - 3
        quarttime100 = 7 * weekdict['twenty'] - 3
        fulltime200 = 7 * weekdict['ten'] - 3
        halftime200 = 7 * weekdict['twenty'] - 3
        quarttime200 = 7 * weekdict['forty'] - 3
        fulltime150 = 7 * weekdict['seven'] - 3
        halftime150 = 7 * weekdict['fifteen'] - 3
        quarttime150 = 7 * weekdict['thirty'] - 3
        halftime50 = 7 * weekdict['five'] - 3
        quarttime50 = 7 * weekdict['ten'] - 3
        suffixdict = {'full100': '_100_100', 'half100': '_100_50', 'quart100': '_100_25',
                      'full200': '_200_100', 'half200': '_200_50', 'quart200': '_200_25',
                      'full150': '_150_100', 'half150': '_150_50', 'quart150': '_150_25',
                      'half50': '_50_50', 'quart50': '_50_25'}
        # 100 100%
        enddate100Full = values['coursestart'] + wx.DateSpan(days=fulltime100)
        self.templates.courseEnd100Full.SetValue(enddate100Full)
        self.templates.weeks100Full.SetValue(str(weekdict['five']))
        self.templates.tmplNm100Full.SetValue(values['feedname']+suffixdict['full100'])
        self.templates.descr100Full.SetValue(values['comment'])

        # 100 50%
        enddate100Half = values['coursestart'] + wx.DateSpan(days=halftime100)
        self.templates.courseEnd100Half.SetValue(enddate100Half)
        self.templates.weeks100Half.SetValue(str(weekdict['ten']))
        self.templates.tmplNm100Half.SetValue(values['feedname']+suffixdict['half100'])
        self.templates.descr100Half.SetValue(self.halfpaceadjust(values['comment']))

        # 100 25%
        enddate100Quart = values['coursestart'] + wx.DateSpan(days=quarttime100)
        self.templates.courseEnd100Quart.SetValue(enddate100Quart)
        self.templates.weeks100Quart.SetValue(str(weekdict['twenty']))
        self.templates.tmplNm100Quart.SetValue(values['feedname']+suffixdict['quart100'])
        self.templates.descr100Quart.SetValue(self.quartpaceadjust(values['comment']))

        # 200 100%
        enddate200Full = values['coursestart'] + wx.DateSpan(days=fulltime200)
        self.templates.courseEnd200Full.SetValue(enddate200Full)
        self.templates.weeks200Full.SetValue(str(weekdict['ten']))
        self.templates.tmplNm200Full.SetValue(values['feedname']+suffixdict['full200'])
        self.templates.descr200Full.SetValue(values['comment'])

        # 200 50%
        enddate200Half = values['coursestart'] + wx.DateSpan(days=halftime200)
        self.templates.courseEnd200Half.SetValue(enddate200Half)
        self.templates.weeks200Half.SetValue(str(weekdict['twenty']))
        self.templates.tmplNm200Half.SetValue(values['feedname']+suffixdict['half200'])
        self.templates.descr200Half.SetValue(self.halfpaceadjust(values['comment']))

        # 200 25%
        enddate200Quart = values['coursestart'] + wx.DateSpan(days=quarttime200)
        self.templates.courseEnd200Quart.SetValue(enddate200Quart)
        self.templates.weeks200Quart.SetValue(str(weekdict['forty']))
        self.templates.tmplNm200Quart.SetValue(values['feedname']+suffixdict['quart200'])
        self.templates.descr200Quart.SetValue(self.quartpaceadjust(values['comment']))

        # 150 100%
        enddate150Full = values['coursestart'] + wx.DateSpan(days=fulltime150)
        self.templates.courseEnd150Full.SetValue(enddate150Full)
        self.templates.weeks150Full.SetValue(str(weekdict['seven']))
        self.templates.tmplNm150Full.SetValue(values['feedname']+suffixdict['full150'])
        self.templates.descr150Full.SetValue(values['comment'])

        # 150 50%
        enddate150Half = values['coursestart'] + wx.DateSpan(days=halftime150)
        self.templates.courseEnd150Half.SetValue(enddate150Half)
        self.templates.weeks150Half.SetValue(str(weekdict['fifteen']))
        self.templates.tmplNm150Half.SetValue(values['feedname']+suffixdict['half150'])
        self.templates.descr150Half.SetValue(self.halfpaceadjust(values['comment']))

        # 150 25%
        enddate150Quart = values['coursestart'] + wx.DateSpan(days=quarttime150)
        self.templates.courseEnd150Quart.SetValue(enddate150Quart)
        self.templates.weeks150Quart.SetValue(str(weekdict['thirty']))
        self.templates.tmplNm150Quart.SetValue(values['feedname']+suffixdict['quart150'])
        self.templates.descr150Quart.SetValue(self.quartpaceadjust(values['comment']))

        # 50 50%
        enddate50Half = values['coursestart'] + wx.DateSpan(days=halftime50)
        self.templates.courseEnd50Half.SetValue(enddate50Half)
        self.templates.weeks50Half.SetValue(str(weekdict['five']))
        self.templates.tmplNm50Half.SetValue(values['feedname']+suffixdict['half50'])
        self.templates.descr50Half.SetValue(self.halfpaceadjust(values['comment']))

        # 50 25%
        enddate50Quart = values['coursestart'] + wx.DateSpan(days=quarttime50)
        self.templates.courseEnd50Quart.SetValue(enddate50Quart)
        self.templates.weeks50Quart.SetValue(str(weekdict['ten']))
        self.templates.tmplNm50Quart.SetValue(values['feedname']+suffixdict['quart50'])
        self.templates.descr50Quart.SetValue(self.quartpaceadjust(values['comment']))

        # aktiva mallar
    def setActiveState(self, evt):
        one = self.oneTmpl.GetValue()
        if one:
            self.templates.state100Full.SetValue(True)
            self.templates.state100Half.SetValue(False)
            self.templates.state100Quart.SetValue(False)
            self.templates.state200Full.SetValue(False)
            self.templates.state200Half.SetValue(False)
            self.templates.state200Quart.SetValue(False)
            self.templates.state150Full.SetValue(False)
            self.templates.state150Half.SetValue(False)
            self.templates.state150Quart.SetValue(False)
            self.templates.state50Half.SetValue(False)
            self.templates.state50Quart.SetValue(False)
        else:
            self.templates.state100Full.SetValue(True)
            self.templates.state100Half.SetValue(True)
            self.templates.state100Quart.SetValue(True)
            self.templates.state200Full.SetValue(True)
            self.templates.state200Half.SetValue(True)
            self.templates.state200Quart.SetValue(True)
            self.templates.state150Full.SetValue(True)
            self.templates.state150Half.SetValue(True)
            self.templates.state150Quart.SetValue(True)
            self.templates.state50Half.SetValue(True)
            self.templates.state50Quart.SetValue(True)

    def getFormValues(self):
        tmplDict = {'feedname': self.ElvisFeedName.GetValue()}
        tmplDict.update({'period': self.ElvisPeriod.GetValue()})
        tmplDict.update({'applicationstart': self.ElvisApplicationStart.GetValue().FormatDate()})
        tmplDict.update({'applicationend': self.ElvisApplicationFinish.GetValue().FormatDate()})
        tmplDict.update({'coursestart': self.ElvisCourseStart.GetValue().FormatDate()})
        if self.templates.state100Full.GetValue():
            tmplDict.update({'tmplNm100Full': self.templates.tmplNm100Full.GetValue()})
            tmplDict.update({'courseEnd100Full': self.templates.courseEnd100Full.GetValue().FormatDate()})
            tmplDict.update({'weeks100Full': self.templates.weeks100Full.GetValue()})
            tmplDict.update({'descr100Full': self.templates.descr100Full.GetValue()})
        if self.templates.state100Half.GetValue():
            tmplDict.update({'tmplNm100Half': self.templates.tmplNm100Half.GetValue()})
            tmplDict.update({'courseEnd100Half': self.templates.courseEnd100Half.GetValue().FormatDate()})
            tmplDict.update({'weeks100Half': self.templates.weeks100Half.GetValue()})
            tmplDict.update({'descr100Half': self.templates.descr100Half.GetValue()})
        if self.templates.state100Quart.GetValue():
            tmplDict.update({'tmplNm100Quart': self.templates.tmplNm100Quart.GetValue()})
            tmplDict.update({'courseEnd100Quart': self.templates.courseEnd100Quart.GetValue().FormatDate()})
            tmplDict.update({'weeks100Quart': self.templates.weeks100Quart.GetValue()})
            tmplDict.update({'descr100Quart': self.templates.descr100Quart.GetValue()})
        if self.templates.state200Full.GetValue():
            tmplDict.update({'tmplNm200Full': self.templates.tmplNm200Full.GetValue()})
            tmplDict.update({'courseEnd200Full': self.templates.courseEnd200Full.GetValue().FormatDate()})
            tmplDict.update({'weeks200Full': self.templates.weeks200Full.GetValue()})
            tmplDict.update({'descr200Full': self.templates.descr200Full.GetValue()})
        if self.templates.state200Half.GetValue():
            tmplDict.update({'tmplNm200Half': self.templates.tmplNm200Half.GetValue()})
            tmplDict.update({'courseEnd200Half': self.templates.courseEnd200Half.GetValue().FormatDate()})
            tmplDict.update({'weeks200Half': self.templates.weeks200Half.GetValue()})
            tmplDict.update({'descr200Half': self.templates.descr200Half.GetValue()})
        if self.templates.state200Quart.GetValue():
            tmplDict.update({'tmplNm200Quart': self.templates.tmplNm200Quart.GetValue()})
            tmplDict.update({'courseEnd200Quart': self.templates.courseEnd200Quart.GetValue().FormatDate()})
            tmplDict.update({'weeks200Quart': self.templates.weeks200Quart.GetValue()})
            tmplDict.update({'descr200Quart': self.templates.descr200Quart.GetValue()})
        if self.templates.state150Full.GetValue():
            tmplDict.update({'tmplNm150Full': self.templates.tmplNm150Full.GetValue()})
            tmplDict.update({'courseEnd150Full': self.templates.courseEnd150Full.GetValue().FormatDate()})
            tmplDict.update({'weeks150Full': self.templates.weeks150Full.GetValue()})
            tmplDict.update({'descr150Full': self.templates.descr150Full.GetValue()})
        if self.templates.state150Half.GetValue():
            tmplDict.update({'tmplNm150Half': self.templates.tmplNm150Half.GetValue()})
            tmplDict.update({'courseEnd150Half': self.templates.courseEnd150Half.GetValue().FormatDate()})
            tmplDict.update({'weeks150Half': self.templates.weeks150Half.GetValue()})
            tmplDict.update({'descr150Half': self.templates.descr150Half.GetValue()})
        if self.templates.state150Quart.GetValue():
            tmplDict.update({'tmplNm150Quart': self.templates.tmplNm150Quart.GetValue()})
            tmplDict.update({'courseEnd150Quart': self.templates.courseEnd150Quart.GetValue().FormatDate()})
            tmplDict.update({'weeks150Quart': self.templates.weeks150Quart.GetValue()})
            tmplDict.update({'descr150Quart': self.templates.descr150Quart.GetValue()})
        if self.templates.state50Half.GetValue():
            tmplDict.update({'tmplNm50Half': self.templates.tmplNm50Half.GetValue()})
            tmplDict.update({'courseEnd50Half': self.templates.courseEnd50Half.GetValue().FormatDate()})
            tmplDict.update({'weeks50Half': self.templates.weeks50Half.GetValue()})
            tmplDict.update({'descr50Half': self.templates.descr50Half.GetValue()})
        if self.templates.state50Quart.GetValue():
            tmplDict.update({'tmplNm50Quart': self.templates.tmplNm50Quart.GetValue()})
            tmplDict.update({'courseEnd50Quart': self.templates.courseEnd50Quart.GetValue().FormatDate()})
            tmplDict.update({'weeks50Quart': self.templates.weeks50Quart.GetValue()})
            tmplDict.update({'descr50Quart': self.templates.descr50Quart.GetValue()})
        self.path = ''
        with wx.DirDialog(self, message="Var ska XML-mallfilen sparas?", defaultPath="",
                          style=wx.DD_DEFAULT_STYLE, pos=wx.DefaultPosition, size=wx.DefaultSize) as dirDialog:
            if dirDialog.ShowModal() == wx.ID_CANCEL:
                return
            self.path = dirDialog.GetPath()
        xmelv = ExemElvis(self, tmplDict, self.path)
        xmelv.saveTemplates2xml()

    def onEnterWindow(self, evt):
        if hasattr(self, 'courselist') and isinstance(self.courselist, ElvisUltimateCourseList):
            self.giveCourseListFocus()

    def giveCourseListFocus(self):
        self.courselist.SetFocus()

    def setOldCustomer(self, evt):
        self.oldcust = self.ElvisCombo.GetValue()

    def onChangeCustomer(self, evt):
        if self.firstrun == 1:
            self.onChangeCustomerFirst()
        else:
            self.onChangeCustomerRun()

    def onChangeCustomerFirst(self):
        custsel = self.ElvisCombo.GetValue()
        self.makeWorkTabs(custsel)
        self.Layout()
        self.Update()
        self.firstrun = 0

    def onChangeCustomerRun(self):
        if self.oldcust != 'Välj kund':
            confirmtext= """
            När du byter kund försvinner allt som du skrivit
            i gränssnittet. Så om du inte är klar ännu,
            svara Nej.
            """
            confirm = wx.MessageDialog(None, confirmtext, 'Har du sparat?', wx.YES_NO | wx.NO_DEFAULT)
            confirmanswer = confirm.ShowModal()
            if confirmanswer == wx.ID_YES:
                custsel = self.ElvisCombo.GetValue()
                self.makeWorkTabs(custsel)
                if custsel != 'Välj kund':
                    self.ElvisWorktabs.Show()
                self.Layout()
                self.Update()
                self.firstrun = 0
                confirm.Destroy()
            else:
                return
        else:
            custsel = self.ElvisCombo.GetValue()
            self.ElvisCombo.Dismiss()
            self.makeWorkTabs(custsel)
            self.Layout()
            self.Update()
            self.firstrun = 0

    def fillTemplates(self, evt):
        tbCtrlDict = {}
        tbCtrlDict.update({"coursestart": self.ElvisCourseStart.GetValue()})
        tbCtrlDict.update({"feedname": self.ElvisFeedName.GetValue()})
        tbCtrlDict.update({"comment": self.ElvisComment.GetValue()})
        self.convertAndDistribute(tbCtrlDict)

    def saveTmpls2xml(self, evt):
        self.getFormValues()

    def onClose(self, e):
        if hasattr(self, 'courselist') and isinstance(self.courselist, ElvisUltimateCourseList):
            self.courselist.Destroy()
        self.templates.Destroy()
        self.feedpanel.Destroy()
        self.Close()

    def clearTC(self, evt):
        tc = evt.GetEventObject()
        val = tc.GetValue()
        if val == "Inmatningens namn" or val == "Period" or val == "Generell kursbeskrivning. Skriv heltid.":
            tc.SetValue('')
        tc.SetFocus()



def main():
    ex = wx.App()
    ElvisFrame(None)
    ex.MainLoop()

if __name__ == '__main__':
    main()