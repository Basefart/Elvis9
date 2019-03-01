# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Dec 17 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
from ElvisFeeder import ElvisFeeder
import os
import threading
import time
from xml.etree import ElementTree as ET
from xml.etree.ElementTree import ParseError
import re

###########################################################################
## Class ElvisFeedPanel
###########################################################################

# Define notification event for thread completion
EVT_RESULT_ID = wx.NewId()


def EVT_RESULT(win, func):
    """Define Result Event."""
    win.Connect(-1, -1, EVT_RESULT_ID, func)


class ResultEvent(wx.PyEvent):
    """Simple event to carry arbitrary result data."""

    def __init__(self, data):
        """Init Result Event."""
        wx.PyEvent.__init__(self)
        self.SetEventType(EVT_RESULT_ID)
        self.data = data

class feedTemplatesThread(threading.Thread):
    def __init__(self, parent):
        threading.Thread.__init__(self)
        self.parent = parent
        self.child = threading.Thread(target=self.parent.ef.feedTmplWaitress)

    def run(self):
        self.child.start()
        self.parent.ElvisTemplFeedStart.Enable(False)
        i = 0
        while self.child.isAlive():
            time.sleep(0.6)
            self.parent.ElvisTemplProgress.SetValue(i)
            i += 1
        if i < 300:
            while i <= 300:
                time.sleep(0.0001)
                self.parent.ElvisTemplProgress.SetValue(i)
                i += 1
        wx.PostEvent(self.parent, ResultEvent("Thread finished!"))
        self.child.join(0.2)

class feedCoursesThread(threading.Thread):
    def __init__(self, parent, points, pace, type, templ):
        threading.Thread.__init__(self)
        self.parent = parent
        self.points = points
        self.pace = pace
        self.type = type
        self.templ = templ
        arglist = [self.points, self.pace, self.type, self.templ]
        self.child = threading.Thread(target=self.parent.ef.listCourses, args=arglist)

    def run(self):
        self.child.start()
        eval("self.parent.Elvis" + self.points + "_" + self.pace + "Btn").Enable(False)
        if eval("self.parent.Elvis" + self.points + "_" + self.pace + "Progress").GetValue() != 0:
            eval("self.parent.Elvis" + self.points + "_" + self.pace + "Progress").SetValue(0)
        i = 0
        while self.child.isAlive():
            time.sleep(0.6)
            eval("self.parent.Elvis" + self.points + "_" + self.pace + "Progress").SetValue(i)
            i += 1
        if i < 300:
            while i <= 300:
                time.sleep(0.0001)
                eval("self.parent.Elvis" + self.points + "_" + self.pace + "Progress").SetValue(i)
                i += 1
        wx.PostEvent(self.parent, ResultEvent("Thread finished!"))
        self.child.join(0.2)

class feedAltCoursesThread(threading.Thread):
    def __init__(self, parent, points, pace, type, templ):
        threading.Thread.__init__(self)
        self.parent = parent
        self.points = points
        self.pace = pace
        self.type = type
        self.templ = templ
        arglist = [self.points, self.pace, self.type, self.templ]
        self.child = threading.Thread(target=self.parent.ef.listCourses, args=arglist)

    def run(self):
        self.child.start()
        eval("self.parent.Elvis" + self.type + self.points + "_" + self.pace + "Btn").Enable(False)
        if eval("self.parent.Elvis" + self.points + "_" + self.pace + "Progress").GetValue() != 0:
            eval("self.parent.Elvis" + self.points + "_" + self.pace + "Progress").SetValue(0)
        i = 0
        while self.child.isAlive():
            time.sleep(0.6)
            eval("self.parent.Elvis" + self.points + "_" + self.pace + "Progress").SetValue(i)
            i += 1
        if i < 300:
            while i <= 300:
                time.sleep(0.02)
                eval("self.parent.Elvis" + self.points + "_" + self.pace + "Progress").SetValue(i)
                i += 1
        self.child.join(0.2)


class ElvisFeedPanel(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition,
                          size=wx.Size(1045, -1), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
        self.tmplfile = ''
        self.custsel = self.GetParent().GetParent().GetParent().ElvisCombo.GetValue()
        self.url = ''
        self.cfile = ''
        self.sharpcfile = ''
        self.testcfile = ''
        self.chaingang = []
        self.ef = ElvisFeeder(self)
        if self.custsel == 'Södertälje':
            self.url = 'https://sodertalje.alvis.gotit.se'
            self.cfile = './sodert_courses.xml'
        elif self.custsel == 'Freja':
            self.url = 'https://freja.alvis.gotit.se/'
            self.cfile = './freja_courses.xml'
        elif self.custsel == 'Huddinge':
            self.url = 'https://huddinge.alvis.gotit.se/'
            self.cfile = './hudd_courses.xml'
        elif self.custsel == 'Norrtälje':
            self.url = 'https://norrtalje.alvis.gotit.se/'
            self.cfile = './norrt_courses.xml'
        elif self.custsel == 'Salem':
            self.url = 'https://salem.alvis.gotit.se/'
            self.cfile = './salem_courses.xml'
        elif self.custsel == 'Järfälla':
            self.url = 'https://jarfalla.alvis.gotit.se/'
            self.cfile = './jarf_courses.xml'

        self.SetSizeHints(wx.Size(1045, 900), wx.Size(1045, 900))

        self.SetFont(
            wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))
        self.SetMinSize(wx.Size(1045, 900))
        self.SetMaxSize(wx.Size(1045, 900))

        elvisFeedBox = wx.BoxSizer(wx.VERTICAL)

        self.elvisScrollable = wx.ScrolledWindow(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                                 wx.HSCROLL | wx.TAB_TRAVERSAL | wx.VSCROLL | wx.EXPAND)
        self.elvisScrollable.SetScrollRate(5, 5)

        elvisGBS = wx.GridBagSizer(20, 20)
        elvisGBS.SetFlexibleDirection(wx.BOTH)
        elvisGBS.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        elvisGBS.SetMinSize(wx.Size(700, 700))
        elvisPrepSB = wx.StaticBoxSizer(wx.StaticBox(self.elvisScrollable, wx.ID_ANY, u"Förberedelser"), wx.HORIZONTAL)

        ElvisBrowserChoices = [u"Google Chrome", u"Mozilla Firefox"]
        self.ElvisBrowser = wx.ComboBox(elvisPrepSB.GetStaticBox(), wx.ID_ANY, u"Välj webbläsare", wx.DefaultPosition,
                                        wx.Size(200, -1), ElvisBrowserChoices, wx.CB_DROPDOWN)
        self.ElvisBrowser.SetFont(
            wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))

        elvisPrepSB.Add(self.ElvisBrowser, 0, wx.ALL, 5)

        elvisPrepSB.Add((0, 0), 1, wx.EXPAND, 5)

        self.ElvisURL = wx.TextCtrl(elvisPrepSB.GetStaticBox(), wx.ID_ANY, u"Internetadress", wx.DefaultPosition,
                                    wx.Size(400, -1), 0)
        self.ElvisURL.SetFont(
            wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))

        elvisPrepSB.Add(self.ElvisURL, 0, wx.ALL, 5)

        elvisGBS.Add(elvisPrepSB, wx.GBPosition(0, 0), wx.GBSpan(1, 3), wx.EXPAND, 5)

        self.ElvisFeedAll = wx.CheckBox(self.elvisScrollable, wx.ID_ANY, u"Kör efter varandra", wx.DefaultPosition, wx.DefaultSize, 0)
        self.ElvisFeedAll.SetFont(
            wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))

        elvisGBS.Add(self.ElvisFeedAll, wx.GBPosition(1, 0), wx.GBSpan(1, 1), wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.ElvisSaveSharp = wx.CheckBox(self.elvisScrollable, wx.ID_ANY, u"Spara i Alvis", wx.DefaultPosition, wx.DefaultSize, 0)
        self.ElvisSaveSharp.SetFont(
            wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))
        self.ElvisSaveSharp.SetToolTip('VARNING! Testa först utan att spara')


        elvisGBS.Add(self.ElvisSaveSharp, wx.GBPosition(1, 1), wx.GBSpan(1, 1), wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.ElvisLogin = wx.Button(self.elvisScrollable, wx.ID_ANY, u"Logga in", wx.DefaultPosition, wx.DefaultSize, 0)
        self.ElvisLogin.SetFont(
            wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))

        elvisGBS.Add(self.ElvisLogin, wx.GBPosition(2, 0), wx.GBSpan(1, 1), wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.elvisTemplSBS = wx.StaticBoxSizer(wx.StaticBox(self.elvisScrollable, wx.ID_ANY, u"Mallar"), wx.HORIZONTAL)

        self.ElvisTemplFile = wx.TextCtrl(self.elvisTemplSBS.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                          wx.Size(150, -1), 0)
        self.ElvisTemplFile.Enable(False)
        self.ElvisTemplFile.SetMinSize(wx.Size(150, -1))
        self.ElvisTemplFile.SetMaxSize(wx.Size(150, -1))

        self.elvisTemplSBS.Add(self.ElvisTemplFile, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.elvisFilePicker = wx.FilePickerCtrl(self.elvisTemplSBS.GetStaticBox(), wx.ID_ANY, u"Välj mallfil",
                                                 u"Välj mallfil", u"*.xml", wx.DefaultPosition, wx.Size(-1, -1),
                                                 wx.FLP_FILE_MUST_EXIST | wx.FLP_OPEN | wx.FLP_SMALL)
        self.elvisFilePicker.SetFont(
            wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))

        self.elvisTemplSBS.Add(self.elvisFilePicker, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.ElvisTemplFeedStart = wx.Button(self.elvisTemplSBS.GetStaticBox(), wx.ID_ANY, u"Börja inmatning av mallar",
                                             wx.DefaultPosition, wx.DefaultSize, 0)
        self.ElvisTemplFeedStart.SetFont(
            wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))

        self.elvisTemplSBS.Add(self.ElvisTemplFeedStart, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.ElvisTemplProgress = wx.Gauge(self.elvisTemplSBS.GetStaticBox(), wx.ID_ANY, 300, wx.DefaultPosition,
                                           wx.Size(-1, 20), wx.GA_HORIZONTAL | wx.GA_SMOOTH)
        self.ElvisTemplProgress.SetValue(0)
        self.ElvisTemplProgress.SetFont(
            wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))
        self.ElvisTemplProgress.SetMinSize(wx.Size(-1, 20))
        self.ElvisTemplProgress.SetMaxSize(wx.Size(-1, 20))

        self.elvisTemplSBS.Add(self.ElvisTemplProgress, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        elvisGBS.Add(self.elvisTemplSBS, wx.GBPosition(3, 0), wx.GBSpan(1, 4), wx.EXPAND, 5)
        
        # Kursinmatning börjar

        self.elvisCourseSBS = wx.StaticBoxSizer(wx.StaticBox(self.elvisScrollable, wx.ID_ANY, u"Kurser"), wx.HORIZONTAL)
        self.elvisCourseB = wx.BoxSizer(wx.VERTICAL)

        # 100 100
        self.elvis100_100SBS = wx.StaticBoxSizer(wx.StaticBox(self.elvisScrollable, wx.ID_ANY, u"100 poäng > heltid"), wx.HORIZONTAL)

        self.Elvis100_100Templ = wx.TextCtrl(self.elvis100_100SBS.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                          wx.Size(180, -1), 0)
        self.Elvis100_100Templ.Enable(False)
        self.Elvis100_100Templ.SetMinSize(wx.Size(180, -1))
        self.Elvis100_100Templ.SetMaxSize(wx.Size(180, -1))

        self.Elvis100_100Btn = wx.Button(self.elvis100_100SBS.GetStaticBox(), wx.ID_ANY, u"Mata in 100 poäng på heltid",
                                             wx.DefaultPosition, wx.Size(250, -1), 0)
        self.Elvis100_100Btn.SetFont(
            wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))
        self.Elvis100_100Btn.Enable(False)
        self.elvisFeedAlt100_100Box = wx.BoxSizer(wx.VERTICAL)
        self.ElvisAPL100_100Btn = wx.Button(self.elvis100_100SBS.GetStaticBox(), wx.ID_ANY, u"APL",
                                             wx.DefaultPosition, wx.Size(50, -1), 0)
        self.ElvisAPL100_100Btn.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString))
        self.ElvisAPL100_100Btn.Enable(False)
        self.ElvisHLR100_100Btn = wx.Button(self.elvis100_100SBS.GetStaticBox(), wx.ID_ANY, u"HLR",
                                             wx.DefaultPosition, wx.Size(50, -1), 0)
        self.ElvisHLR100_100Btn.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString))
        self.ElvisHLR100_100Btn.Enable(False)
        self.ElvisLAB100_100Btn = wx.Button(self.elvis100_100SBS.GetStaticBox(), wx.ID_ANY, u"Lab",
                                             wx.DefaultPosition, wx.Size(50, -1), 0)
        self.ElvisLAB100_100Btn.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString))
        self.ElvisLAB100_100Btn.Enable(False)
        alternBtns100_100 = [self.ElvisAPL100_100Btn, self.ElvisHLR100_100Btn, self.ElvisLAB100_100Btn]
        self.elvisFeedAlt100_100Box.AddMany(alternBtns100_100)
        self.Elvis100_100Progress = wx.Gauge(self.elvis100_100SBS.GetStaticBox(), wx.ID_ANY, 300, wx.DefaultPosition,
                                           wx.Size(-1, 20), wx.GA_HORIZONTAL | wx.GA_SMOOTH)
        self.Elvis100_100Progress.SetValue(0)
        self.Elvis100_100Progress.SetFont(
            wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))
        self.Elvis100_100Progress.SetMinSize(wx.Size(-1, 20))
        self.Elvis100_100Progress.SetMaxSize(wx.Size(-1, 20))

        self.elvis100_100SBS.Add(self.Elvis100_100Templ, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)
        self.elvis100_100SBS.Add(self.Elvis100_100Btn, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)
        self.elvis100_100SBS.Add(self.elvisFeedAlt100_100Box, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 2)
        self.elvis100_100SBS.Add(self.Elvis100_100Progress, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)


        self.elvisCourseB.Add(self.elvis100_100SBS, 0, wx.ALL, 2)


        # 100 50

        self.elvisCourseSBS = wx.StaticBoxSizer(wx.StaticBox(self.elvisScrollable, wx.ID_ANY, u"Kurser"), wx.HORIZONTAL)

        self.elvis100_50SBS = wx.StaticBoxSizer(wx.StaticBox(self.elvisScrollable, wx.ID_ANY, u"100 poäng > halvtid"), wx.HORIZONTAL)

        self.Elvis100_50Templ = wx.TextCtrl(self.elvis100_50SBS.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                          wx.Size(180, -1), 0)
        self.Elvis100_50Templ.Enable(False)
        self.Elvis100_50Templ.SetMinSize(wx.Size(180, -1))
        self.Elvis100_50Templ.SetMaxSize(wx.Size(180, -1))

        self.Elvis100_50Btn = wx.Button(self.elvis100_50SBS.GetStaticBox(), wx.ID_ANY, u"Mata in 100 poäng på halvtid",
                                             wx.DefaultPosition, wx.Size(250, -1), 0)
        self.Elvis100_50Btn.SetFont(
            wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))
        self.Elvis100_50Btn.Enable(False)
        self.elvisFeedAlt100_50Box = wx.BoxSizer(wx.VERTICAL)
        self.ElvisAPL100_50Btn = wx.Button(self.elvis100_50SBS.GetStaticBox(), wx.ID_ANY, u"APL",
                                             wx.DefaultPosition, wx.Size(50, -1), 0)
        self.ElvisAPL100_50Btn.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString))
        self.ElvisAPL100_50Btn.Enable(False)
        self.ElvisHLR100_50Btn = wx.Button(self.elvis100_50SBS.GetStaticBox(), wx.ID_ANY, u"HLR",
                                             wx.DefaultPosition, wx.Size(50, -1), 0)
        self.ElvisHLR100_50Btn.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString))
        self.ElvisHLR100_50Btn.Enable(False)
        self.ElvisLAB100_50Btn = wx.Button(self.elvis100_50SBS.GetStaticBox(), wx.ID_ANY, u"Lab",
                                             wx.DefaultPosition, wx.Size(50, -1), 0)
        self.ElvisLAB100_50Btn.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString))
        self.ElvisLAB100_50Btn.Enable(False)
        alternBtns100_50 = [self.ElvisAPL100_50Btn, self.ElvisHLR100_50Btn, self.ElvisLAB100_50Btn]
        self.elvisFeedAlt100_50Box.AddMany(alternBtns100_50)
        self.Elvis100_50Progress = wx.Gauge(self.elvis100_50SBS.GetStaticBox(), wx.ID_ANY, 300, wx.DefaultPosition,
                                           wx.Size(-1, 20), wx.GA_HORIZONTAL | wx.GA_SMOOTH)
        self.Elvis100_50Progress.SetValue(0)
        self.Elvis100_50Progress.SetFont(
            wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))
        self.Elvis100_50Progress.SetMinSize(wx.Size(-1, 20))
        self.Elvis100_50Progress.SetMaxSize(wx.Size(-1, 20))

        self.elvis100_50SBS.Add(self.Elvis100_50Templ, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)
        self.elvis100_50SBS.Add(self.Elvis100_50Btn, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)
        self.elvis100_50SBS.Add(self.elvisFeedAlt100_50Box, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 2)
        self.elvis100_50SBS.Add(self.Elvis100_50Progress, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)


        self.elvisCourseB.Add(self.elvis100_50SBS, 0, wx.ALL, 2)


        # 100 25
        
        self.elvisCourseSBS = wx.StaticBoxSizer(wx.StaticBox(self.elvisScrollable, wx.ID_ANY, u"Kurser"), wx.HORIZONTAL)

        self.elvis100_25SBS = wx.StaticBoxSizer(wx.StaticBox(self.elvisScrollable, wx.ID_ANY, u"100 poäng > kvartstid"), wx.HORIZONTAL)

        self.Elvis100_25Templ = wx.TextCtrl(self.elvis100_25SBS.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                          wx.Size(180, -1), 0)
        self.Elvis100_25Templ.Enable(False)
        self.Elvis100_25Templ.SetMinSize(wx.Size(180, -1))
        self.Elvis100_25Templ.SetMaxSize(wx.Size(180, -1))
        self.Elvis100_25Btn = wx.Button(self.elvis100_25SBS.GetStaticBox(), wx.ID_ANY, u"Mata in 100 poäng på kvartstid",
                                             wx.DefaultPosition, wx.Size(250, -1), 0)
        self.Elvis100_25Btn.SetFont(
            wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))
        self.Elvis100_25Btn.Enable(False)
        self.elvisFeedAlt100_25Box = wx.BoxSizer(wx.VERTICAL)
        self.ElvisAPL100_25Btn = wx.Button(self.elvis100_25SBS.GetStaticBox(), wx.ID_ANY, u"APL",
                                             wx.DefaultPosition, wx.Size(50, -1), 0)
        self.ElvisAPL100_25Btn.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString))
        self.ElvisAPL100_25Btn.Enable(False)
        self.ElvisHLR100_25Btn = wx.Button(self.elvis100_25SBS.GetStaticBox(), wx.ID_ANY, u"HLR",
                                             wx.DefaultPosition, wx.Size(50, -1), 0)
        self.ElvisHLR100_25Btn.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString))
        self.ElvisHLR100_25Btn.Enable(False)
        self.ElvisLAB100_25Btn = wx.Button(self.elvis100_25SBS.GetStaticBox(), wx.ID_ANY, u"Lab",
                                             wx.DefaultPosition, wx.Size(50, -1), 0)
        self.ElvisLAB100_25Btn.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString))
        self.ElvisLAB100_25Btn.Enable(False)
        alternBtns100_25 = [self.ElvisAPL100_25Btn, self.ElvisHLR100_25Btn, self.ElvisLAB100_25Btn]
        self.elvisFeedAlt100_25Box.AddMany(alternBtns100_25)
        self.Elvis100_25Progress = wx.Gauge(self.elvis100_25SBS.GetStaticBox(), wx.ID_ANY, 300, wx.DefaultPosition,
                                           wx.Size(-1, 20), wx.GA_HORIZONTAL | wx.GA_SMOOTH)
        self.Elvis100_25Progress.SetValue(0)
        self.Elvis100_25Progress.SetFont(
            wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))
        self.Elvis100_25Progress.SetMinSize(wx.Size(-1, 20))
        self.Elvis100_25Progress.SetMaxSize(wx.Size(-1, 20))

        self.elvis100_25SBS.Add(self.Elvis100_25Templ, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)
        self.elvis100_25SBS.Add(self.Elvis100_25Btn, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)
        self.elvis100_25SBS.Add(self.elvisFeedAlt100_25Box, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 2)
        self.elvis100_25SBS.Add(self.Elvis100_25Progress, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)


        self.elvisCourseB.Add(self.elvis100_25SBS, 0, wx.ALL, 2)

        # 200 100
        
        self.elvis200_100SBS = wx.StaticBoxSizer(wx.StaticBox(self.elvisScrollable, wx.ID_ANY, u"200 poäng > heltid"), wx.HORIZONTAL)

        self.Elvis200_100Templ = wx.TextCtrl(self.elvis200_100SBS.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                          wx.Size(180, -1), 0)
        self.Elvis200_100Templ.Enable(False)
        self.Elvis200_100Templ.SetMinSize(wx.Size(180, -1))
        self.Elvis200_100Templ.SetMaxSize(wx.Size(180, -1))
        self.Elvis200_100Btn = wx.Button(self.elvis200_100SBS.GetStaticBox(), wx.ID_ANY, u"Mata in 200 poäng på heltid",
                                             wx.DefaultPosition, wx.Size(250, -1), 0)
        self.Elvis200_100Btn.SetFont(
            wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))
        self.Elvis200_100Btn.Enable(False)
        self.elvisFeedAlt200_100Box = wx.BoxSizer(wx.VERTICAL)
        self.ElvisAPL200_100Btn = wx.Button(self.elvis200_100SBS.GetStaticBox(), wx.ID_ANY, u"APL",
                                             wx.DefaultPosition, wx.Size(50, -1), 0)
        self.ElvisAPL200_100Btn.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString))
        self.ElvisAPL200_100Btn.Enable(False)
        self.ElvisHLR200_100Btn = wx.Button(self.elvis200_100SBS.GetStaticBox(), wx.ID_ANY, u"HLR",
                                             wx.DefaultPosition, wx.Size(50, -1), 0)
        self.ElvisHLR200_100Btn.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString))
        self.ElvisHLR200_100Btn.Enable(False)
        self.ElvisLAB200_100Btn = wx.Button(self.elvis200_100SBS.GetStaticBox(), wx.ID_ANY, u"Lab",
                                             wx.DefaultPosition, wx.Size(50, -1), 0)
        self.ElvisLAB200_100Btn.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString))
        self.ElvisLAB200_100Btn.Enable(False)
        alternBtns200_100 = [self.ElvisAPL200_100Btn, self.ElvisHLR200_100Btn, self.ElvisLAB200_100Btn]
        self.elvisFeedAlt200_100Box.AddMany(alternBtns200_100)
        self.Elvis200_100Progress = wx.Gauge(self.elvis200_100SBS.GetStaticBox(), wx.ID_ANY, 300, wx.DefaultPosition,
                                           wx.Size(-1, 20), wx.GA_HORIZONTAL | wx.GA_SMOOTH)
        self.Elvis200_100Progress.SetValue(0)
        self.Elvis200_100Progress.SetFont(
            wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))
        self.Elvis200_100Progress.SetMinSize(wx.Size(-1, 20))
        self.Elvis200_100Progress.SetMaxSize(wx.Size(-1, 20))

        self.elvis200_100SBS.Add(self.Elvis200_100Templ, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)
        self.elvis200_100SBS.Add(self.Elvis200_100Btn, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)
        self.elvis200_100SBS.Add(self.elvisFeedAlt200_100Box, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 2)
        self.elvis200_100SBS.Add(self.Elvis200_100Progress, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)


        self.elvisCourseB.Add(self.elvis200_100SBS, 0, wx.ALL, 2)

        # 200 50
        
        self.elvis200_50SBS = wx.StaticBoxSizer(wx.StaticBox(self.elvisScrollable, wx.ID_ANY, u"200 poäng > halvtid"), wx.HORIZONTAL)

        self.Elvis200_50Templ = wx.TextCtrl(self.elvis200_50SBS.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                          wx.Size(180, -1), 0)
        self.Elvis200_50Templ.Enable(False)
        self.Elvis200_50Templ.SetMinSize(wx.Size(180, -1))
        self.Elvis200_50Templ.SetMaxSize(wx.Size(180, -1))
        self.Elvis200_50Btn = wx.Button(self.elvis200_50SBS.GetStaticBox(), wx.ID_ANY, u"Mata in 200 poäng på halvtid",
                                             wx.DefaultPosition, wx.Size(250, -1), 0)
        self.Elvis200_50Btn.SetFont(
            wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))
        self.Elvis200_50Btn.Enable(False)
        self.elvisFeedAlt200_50Box = wx.BoxSizer(wx.VERTICAL)
        self.ElvisAPL200_50Btn = wx.Button(self.elvis200_50SBS.GetStaticBox(), wx.ID_ANY, u"APL",
                                             wx.DefaultPosition, wx.Size(50, -1), 0)
        self.ElvisAPL200_50Btn.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString))
        self.ElvisAPL200_50Btn.Enable(False)
        self.ElvisHLR200_50Btn = wx.Button(self.elvis200_50SBS.GetStaticBox(), wx.ID_ANY, u"HLR",
                                             wx.DefaultPosition, wx.Size(50, -1), 0)
        self.ElvisHLR200_50Btn.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString))
        self.ElvisHLR200_50Btn.Enable(False)
        self.ElvisLAB200_50Btn = wx.Button(self.elvis200_50SBS.GetStaticBox(), wx.ID_ANY, u"Lab",
                                             wx.DefaultPosition, wx.Size(50, -1), 0)
        self.ElvisLAB200_50Btn.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString))
        self.ElvisLAB200_50Btn.Enable(False)
        alternBtns200_50 = [self.ElvisAPL200_50Btn, self.ElvisHLR200_50Btn, self.ElvisLAB200_50Btn]
        self.elvisFeedAlt200_50Box.AddMany(alternBtns200_50)
        self.Elvis200_50Progress = wx.Gauge(self.elvis200_50SBS.GetStaticBox(), wx.ID_ANY, 300, wx.DefaultPosition,
                                           wx.Size(-1, 20), wx.GA_HORIZONTAL | wx.GA_SMOOTH)
        self.Elvis200_50Progress.SetValue(0)
        self.Elvis200_50Progress.SetFont(
            wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))
        self.Elvis200_50Progress.SetMinSize(wx.Size(-1, 20))
        self.Elvis200_50Progress.SetMaxSize(wx.Size(-1, 20))

        self.elvis200_50SBS.Add(self.Elvis200_50Templ, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)
        self.elvis200_50SBS.Add(self.Elvis200_50Btn, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)
        self.elvis200_50SBS.Add(self.elvisFeedAlt200_50Box, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 2)
        self.elvis200_50SBS.Add(self.Elvis200_50Progress, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)


        self.elvisCourseB.Add(self.elvis200_50SBS, 0, wx.ALL, 2)

        # 200 25
        
        self.elvis200_25SBS = wx.StaticBoxSizer(wx.StaticBox(self.elvisScrollable, wx.ID_ANY, u"200 poäng > kvartstid"), wx.HORIZONTAL)

        self.Elvis200_25Templ = wx.TextCtrl(self.elvis200_25SBS.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                          wx.Size(180, -1), 0)
        self.Elvis200_25Templ.Enable(False)
        self.Elvis200_25Templ.SetMinSize(wx.Size(180, -1))
        self.Elvis200_25Templ.SetMaxSize(wx.Size(180, -1))
        self.Elvis200_25Btn = wx.Button(self.elvis200_25SBS.GetStaticBox(), wx.ID_ANY, u"Mata in 200 poäng på kvartstid",
                                             wx.DefaultPosition, wx.Size(250, -1), 0)
        self.Elvis200_25Btn.SetFont(
            wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))
        self.Elvis200_25Btn.Enable(False)
        self.elvisFeedAlt200_25Box = wx.BoxSizer(wx.VERTICAL)
        self.ElvisAPL200_25Btn = wx.Button(self.elvis200_25SBS.GetStaticBox(), wx.ID_ANY, u"APL",
                                             wx.DefaultPosition, wx.Size(50, -1), 0)
        self.ElvisAPL200_25Btn.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString))
        self.ElvisAPL200_25Btn.Enable(False)
        self.ElvisHLR200_25Btn = wx.Button(self.elvis200_25SBS.GetStaticBox(), wx.ID_ANY, u"HLR",
                                             wx.DefaultPosition, wx.Size(50, -1), 0)
        self.ElvisHLR200_25Btn.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString))
        self.ElvisHLR200_25Btn.Enable(False)
        self.ElvisLAB200_25Btn = wx.Button(self.elvis200_25SBS.GetStaticBox(), wx.ID_ANY, u"Lab",
                                             wx.DefaultPosition, wx.Size(50, -1), 0)
        self.ElvisLAB200_25Btn.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString))
        self.ElvisLAB200_25Btn.Enable(False)
        alternBtns200_25 = [self.ElvisAPL200_25Btn, self.ElvisHLR200_25Btn, self.ElvisLAB200_25Btn]
        self.elvisFeedAlt200_25Box.AddMany(alternBtns200_25)
        self.Elvis200_25Progress = wx.Gauge(self.elvis200_25SBS.GetStaticBox(), wx.ID_ANY, 300, wx.DefaultPosition,
                                           wx.Size(-1, 20), wx.GA_HORIZONTAL | wx.GA_SMOOTH)
        self.Elvis200_25Progress.SetValue(0)
        self.Elvis200_25Progress.SetFont(
            wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))
        self.Elvis200_25Progress.SetMinSize(wx.Size(-1, 20))
        self.Elvis200_25Progress.SetMaxSize(wx.Size(-1, 20))

        self.elvis200_25SBS.Add(self.Elvis200_25Templ, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)
        self.elvis200_25SBS.Add(self.Elvis200_25Btn, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)
        self.elvis200_25SBS.Add(self.elvisFeedAlt200_25Box, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 2)
        self.elvis200_25SBS.Add(self.Elvis200_25Progress, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)


        self.elvisCourseB.Add(self.elvis200_25SBS, 0, wx.ALL, 2)

        # 150 100

        self.elvis150_100SBS = wx.StaticBoxSizer(wx.StaticBox(self.elvisScrollable, wx.ID_ANY, u"150 poäng > heltid"), wx.HORIZONTAL)

        self.Elvis150_100Templ = wx.TextCtrl(self.elvis150_100SBS.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                          wx.Size(180, -1), 0)
        self.Elvis150_100Templ.Enable(False)
        self.Elvis150_100Templ.SetMinSize(wx.Size(180, -1))
        self.Elvis150_100Templ.SetMaxSize(wx.Size(180, -1))
        self.Elvis150_100Btn = wx.Button(self.elvis150_100SBS.GetStaticBox(), wx.ID_ANY, u"Mata in 150 poäng på heltid",
                                             wx.DefaultPosition, wx.Size(250, -1), 0)
        self.Elvis150_100Btn.SetFont(
            wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))
        self.Elvis150_100Btn.Enable(False)
        self.elvisFeedAlt150_100Box = wx.BoxSizer(wx.VERTICAL)
        self.ElvisAPL150_100Btn = wx.Button(self.elvis150_100SBS.GetStaticBox(), wx.ID_ANY, u"APL",
                                             wx.DefaultPosition, wx.Size(50, -1), 0)
        self.ElvisAPL150_100Btn.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString))
        self.ElvisAPL150_100Btn.Enable(False)
        self.ElvisHLR150_100Btn = wx.Button(self.elvis150_100SBS.GetStaticBox(), wx.ID_ANY, u"HLR",
                                             wx.DefaultPosition, wx.Size(50, -1), 0)
        self.ElvisHLR150_100Btn.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString))
        self.ElvisHLR150_100Btn.Enable(False)
        self.ElvisLAB150_100Btn = wx.Button(self.elvis150_100SBS.GetStaticBox(), wx.ID_ANY, u"Lab",
                                             wx.DefaultPosition, wx.Size(50, -1), 0)
        self.ElvisLAB150_100Btn.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString))
        self.ElvisLAB150_100Btn.Enable(False)
        alternBtns150_100 = [self.ElvisAPL150_100Btn, self.ElvisHLR150_100Btn, self.ElvisLAB150_100Btn]
        self.elvisFeedAlt150_100Box.AddMany(alternBtns150_100)
        self.Elvis150_100Progress = wx.Gauge(self.elvis150_100SBS.GetStaticBox(), wx.ID_ANY, 300, wx.DefaultPosition,
                                           wx.Size(-1, 20), wx.GA_HORIZONTAL | wx.GA_SMOOTH)
        self.Elvis150_100Progress.SetValue(0)
        self.Elvis150_100Progress.SetFont(
            wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))
        self.Elvis150_100Progress.SetMinSize(wx.Size(-1, 20))
        self.Elvis150_100Progress.SetMaxSize(wx.Size(-1, 20))

        self.elvis150_100SBS.Add(self.Elvis150_100Templ, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)
        self.elvis150_100SBS.Add(self.Elvis150_100Btn, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)
        self.elvis150_100SBS.Add(self.elvisFeedAlt150_100Box, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 2)
        self.elvis150_100SBS.Add(self.Elvis150_100Progress, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)


        self.elvisCourseB.Add(self.elvis150_100SBS, 0, wx.ALL, 2)

        # 150 50

        self.elvis150_50SBS = wx.StaticBoxSizer(wx.StaticBox(self.elvisScrollable, wx.ID_ANY, u"150 poäng > halvtid"), wx.HORIZONTAL)

        self.Elvis150_50Templ = wx.TextCtrl(self.elvis150_50SBS.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                          wx.Size(180, -1), 0)
        self.Elvis150_50Templ.Enable(False)
        self.Elvis150_50Templ.SetMinSize(wx.Size(180, -1))
        self.Elvis150_50Templ.SetMaxSize(wx.Size(180, -1))
        self.Elvis150_50Btn = wx.Button(self.elvis150_50SBS.GetStaticBox(), wx.ID_ANY, u"Mata in 150 poäng på halvtid",
                                             wx.DefaultPosition, wx.Size(250, -1), 0)
        self.Elvis150_50Btn.SetFont(
            wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))
        self.Elvis150_50Btn.Enable(False)
        self.elvisFeedAlt150_50Box = wx.BoxSizer(wx.VERTICAL)
        self.ElvisAPL150_50Btn = wx.Button(self.elvis150_50SBS.GetStaticBox(), wx.ID_ANY, u"APL",
                                             wx.DefaultPosition, wx.Size(50, -1), 0)
        self.ElvisAPL150_50Btn.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString))
        self.ElvisAPL150_50Btn.Enable(False)
        self.ElvisHLR150_50Btn = wx.Button(self.elvis150_50SBS.GetStaticBox(), wx.ID_ANY, u"HLR",
                                             wx.DefaultPosition, wx.Size(50, -1), 0)
        self.ElvisHLR150_50Btn.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString))
        self.ElvisHLR150_50Btn.Enable(False)
        self.ElvisLAB150_50Btn = wx.Button(self.elvis150_50SBS.GetStaticBox(), wx.ID_ANY, u"Lab",
                                             wx.DefaultPosition, wx.Size(50, -1), 0)
        self.ElvisLAB150_50Btn.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString))
        self.ElvisLAB150_50Btn.Enable(False)
        alternBtns150_50 = [self.ElvisAPL150_50Btn, self.ElvisHLR150_50Btn, self.ElvisLAB150_50Btn]
        self.elvisFeedAlt150_50Box.AddMany(alternBtns150_50)
        self.Elvis150_50Progress = wx.Gauge(self.elvis150_50SBS.GetStaticBox(), wx.ID_ANY, 300, wx.DefaultPosition,
                                           wx.Size(-1, 20), wx.GA_HORIZONTAL | wx.GA_SMOOTH)
        self.Elvis150_50Progress.SetValue(0)
        self.Elvis150_50Progress.SetFont(
            wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))
        self.Elvis150_50Progress.SetMinSize(wx.Size(-1, 20))
        self.Elvis150_50Progress.SetMaxSize(wx.Size(-1, 20))

        self.elvis150_50SBS.Add(self.Elvis150_50Templ, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)
        self.elvis150_50SBS.Add(self.Elvis150_50Btn, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)
        self.elvis150_50SBS.Add(self.elvisFeedAlt150_50Box, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 2)
        self.elvis150_50SBS.Add(self.Elvis150_50Progress, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)


        self.elvisCourseB.Add(self.elvis150_50SBS, 0, wx.ALL, 2)

        # 150 25
        
        self.elvis150_25SBS = wx.StaticBoxSizer(wx.StaticBox(self.elvisScrollable, wx.ID_ANY, u"150 poäng > kvartstid"), wx.HORIZONTAL)

        self.Elvis150_25Templ = wx.TextCtrl(self.elvis150_25SBS.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                          wx.Size(180, -1), 0)
        self.Elvis150_25Templ.Enable(False)
        self.Elvis150_25Templ.SetMinSize(wx.Size(180, -1))
        self.Elvis150_25Templ.SetMaxSize(wx.Size(180, -1))
        self.Elvis150_25Btn = wx.Button(self.elvis150_25SBS.GetStaticBox(), wx.ID_ANY, u"Mata in 150 poäng på kvartstid",
                                             wx.DefaultPosition, wx.Size(250, -1), 0)
        self.Elvis150_25Btn.SetFont(
            wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))
        self.Elvis150_25Btn.Enable(False)
        self.elvisFeedAlt150_25Box = wx.BoxSizer(wx.VERTICAL)
        self.ElvisAPL150_25Btn = wx.Button(self.elvis150_25SBS.GetStaticBox(), wx.ID_ANY, u"APL",
                                             wx.DefaultPosition, wx.Size(50, -1), 0)
        self.ElvisAPL150_25Btn.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString))
        self.ElvisAPL150_25Btn.Enable(False)
        self.ElvisHLR150_25Btn = wx.Button(self.elvis150_25SBS.GetStaticBox(), wx.ID_ANY, u"HLR",
                                             wx.DefaultPosition, wx.Size(50, -1), 0)
        self.ElvisHLR150_25Btn.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString))
        self.ElvisHLR150_25Btn.Enable(False)
        self.ElvisLAB150_25Btn = wx.Button(self.elvis150_25SBS.GetStaticBox(), wx.ID_ANY, u"Lab",
                                             wx.DefaultPosition, wx.Size(50, -1), 0)
        self.ElvisLAB150_25Btn.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString))
        self.ElvisLAB150_25Btn.Enable(False)
        alternBtns150_25 = [self.ElvisAPL150_25Btn, self.ElvisHLR150_25Btn, self.ElvisLAB150_25Btn]
        self.elvisFeedAlt150_25Box.AddMany(alternBtns150_25)
        self.Elvis150_25Progress = wx.Gauge(self.elvis150_25SBS.GetStaticBox(), wx.ID_ANY, 300, wx.DefaultPosition,
                                           wx.Size(-1, 20), wx.GA_HORIZONTAL | wx.GA_SMOOTH)
        self.Elvis150_25Progress.SetValue(0)
        self.Elvis150_25Progress.SetFont(
            wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))
        self.Elvis150_25Progress.SetMinSize(wx.Size(-1, 20))
        self.Elvis150_25Progress.SetMaxSize(wx.Size(-1, 20))

        self.elvis150_25SBS.Add(self.Elvis150_25Templ, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)
        self.elvis150_25SBS.Add(self.Elvis150_25Btn, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)
        self.elvis150_25SBS.Add(self.elvisFeedAlt150_25Box, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 2)
        self.elvis150_25SBS.Add(self.Elvis150_25Progress, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)


        self.elvisCourseB.Add(self.elvis150_25SBS, 0, wx.ALL, 2)

        # 50 50
        
        self.elvis50_50SBS = wx.StaticBoxSizer(wx.StaticBox(self.elvisScrollable, wx.ID_ANY, u"50 poäng > halvtid"), wx.HORIZONTAL)

        self.Elvis50_50Templ = wx.TextCtrl(self.elvis50_50SBS.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                          wx.Size(180, -1), 0)
        self.Elvis50_50Templ.Enable(False)
        self.Elvis50_50Templ.SetMinSize(wx.Size(180, -1))
        self.Elvis50_50Templ.SetMaxSize(wx.Size(180, -1))
        self.Elvis50_50Btn = wx.Button(self.elvis50_50SBS.GetStaticBox(), wx.ID_ANY, u"Mata in 50 poäng på halvtid",
                                             wx.DefaultPosition, wx.Size(250, -1), 0)
        self.Elvis50_50Btn.SetFont(
            wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))
        self.Elvis50_50Btn.Enable(False)
        self.elvisFeedAlt50_50Box = wx.BoxSizer(wx.VERTICAL)
        self.ElvisAPL50_50Btn = wx.Button(self.elvis50_50SBS.GetStaticBox(), wx.ID_ANY, u"APL",
                                             wx.DefaultPosition, wx.Size(50, -1), 0)
        self.ElvisAPL50_50Btn.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString))
        self.ElvisAPL50_50Btn.Enable(False)
        self.ElvisHLR50_50Btn = wx.Button(self.elvis50_50SBS.GetStaticBox(), wx.ID_ANY, u"HLR",
                                             wx.DefaultPosition, wx.Size(50, -1), 0)
        self.ElvisHLR50_50Btn.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString))
        self.ElvisHLR50_50Btn.Enable(False)
        self.ElvisLAB50_50Btn = wx.Button(self.elvis50_50SBS.GetStaticBox(), wx.ID_ANY, u"Lab",
                                             wx.DefaultPosition, wx.Size(50, -1), 0)
        self.ElvisLAB50_50Btn.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString))
        self.ElvisLAB50_50Btn.Enable(False)
        alternBtns50_50 = [self.ElvisAPL50_50Btn, self.ElvisHLR50_50Btn, self.ElvisLAB50_50Btn]
        self.elvisFeedAlt50_50Box.AddMany(alternBtns50_50)

        self.Elvis50_50Progress = wx.Gauge(self.elvis50_50SBS.GetStaticBox(), wx.ID_ANY, 300, wx.DefaultPosition,
                                           wx.Size(-1, 20), wx.GA_HORIZONTAL | wx.GA_SMOOTH)
        self.Elvis50_50Progress.SetValue(0)
        self.Elvis50_50Progress.SetFont(
            wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))
        self.Elvis50_50Progress.SetMinSize(wx.Size(-1, 20))
        self.Elvis50_50Progress.SetMaxSize(wx.Size(-1, 20))

        self.elvis50_50SBS.Add(self.Elvis50_50Templ, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)
        self.elvis50_50SBS.Add(self.Elvis50_50Btn, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)
        self.elvis50_50SBS.Add(self.elvisFeedAlt50_50Box, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 2)
        self.elvis50_50SBS.Add(self.Elvis50_50Progress, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)


        self.elvisCourseB.Add(self.elvis50_50SBS, 0, wx.ALL, 2)

        # 50 25
        
        self.elvis50_25SBS = wx.StaticBoxSizer(wx.StaticBox(self.elvisScrollable, wx.ID_ANY, u"50 poäng > kvartstid"), wx.HORIZONTAL)

        self.Elvis50_25Templ = wx.TextCtrl(self.elvis50_25SBS.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                          wx.Size(180, -1), 0)
        self.Elvis50_25Templ.Enable(False)
        self.Elvis50_25Templ.SetMinSize(wx.Size(180, -1))
        self.Elvis50_25Templ.SetMaxSize(wx.Size(180, -1))
        self.Elvis50_25Btn = wx.Button(self.elvis50_25SBS.GetStaticBox(), wx.ID_ANY, u"Mata in 50 poäng på kvartstid",
                                             wx.DefaultPosition, wx.Size(250, -1), 0)
        self.Elvis50_25Btn.SetFont(
            wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))
        self.Elvis50_25Btn.Enable(False)
        self.elvisFeedAlt50_25Box = wx.BoxSizer(wx.VERTICAL)
        self.ElvisAPL50_25Btn = wx.Button(self.elvis50_25SBS.GetStaticBox(), wx.ID_ANY, u"APL",
                                             wx.DefaultPosition, wx.Size(50, -1), 0)
        self.ElvisAPL50_25Btn.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString))
        self.ElvisAPL50_25Btn.Enable(False)
        self.ElvisHLR50_25Btn = wx.Button(self.elvis50_25SBS.GetStaticBox(), wx.ID_ANY, u"HLR",
                                             wx.DefaultPosition, wx.Size(50, -1), 0)
        self.ElvisHLR50_25Btn.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString))
        self.ElvisHLR50_25Btn.Enable(False)
        self.ElvisLAB50_25Btn = wx.Button(self.elvis50_25SBS.GetStaticBox(), wx.ID_ANY, u"Lab",
                                             wx.DefaultPosition, wx.Size(50, -1), 0)
        self.ElvisLAB50_25Btn.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString))
        self.ElvisLAB50_25Btn.Enable(False)
        alternBtns50_25 = [self.ElvisAPL50_25Btn, self.ElvisHLR50_25Btn, self.ElvisLAB50_25Btn]
        self.elvisFeedAlt50_25Box.AddMany(alternBtns50_25)

        self.Elvis50_25Progress = wx.Gauge(self.elvis50_25SBS.GetStaticBox(), wx.ID_ANY, 300, wx.DefaultPosition,
                                           wx.Size(-1, 20), wx.GA_HORIZONTAL | wx.GA_SMOOTH)
        self.Elvis50_25Progress.SetValue(0)
        self.Elvis50_25Progress.SetFont(
            wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))
        self.Elvis50_25Progress.SetMinSize(wx.Size(-1, 20))
        self.Elvis50_25Progress.SetMaxSize(wx.Size(-1, 20))

        self.elvis50_25SBS.Add(self.Elvis50_25Templ, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)
        self.elvis50_25SBS.Add(self.Elvis50_25Btn, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)
        self.elvis50_25SBS.Add(self.elvisFeedAlt50_25Box, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 2)
        self.elvis50_25SBS.Add(self.Elvis50_25Progress, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)


        self.elvisCourseB.Add(self.elvis50_25SBS, 0, wx.ALL, 2)

        self.elvisCourseSBS.Add(self.elvisCourseB, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        elvisGBS.Add(self.elvisCourseSBS, wx.GBPosition(4, 0), wx.GBSpan(1, 4), wx.EXPAND, 5)

        self.elvisVariantDescrSBS = wx.StaticBoxSizer(wx.StaticBox(self.elvisScrollable, wx.ID_ANY, u"Avvikande kommentarer"), wx.HORIZONTAL)
        self.elvisVariantDescrB = wx.BoxSizer(wx.VERTICAL)

        self.workExpSBS = wx.StaticBoxSizer(wx.StaticBox(self.elvisScrollable, wx.ID_ANY, u"APL"), wx.HORIZONTAL)

        aplTxt = u"Heltid på distans, APL ingår. Slutprov i skolans lokal. För övrig information se www.nti.se."
        self.ElvisAlternCommentWorkExp = wx.TextCtrl(self.elvisScrollable, wx.ID_ANY, aplTxt, wx.DefaultPosition,
                                       wx.Size(200, 150), wx.TE_MULTILINE)
        self.ElvisAlternCommentWorkExp.SetToolTip(u"Generell kursbeskrivning. Skriv som vid heltid.")
        self.workExpSBS.Add(self.ElvisAlternCommentWorkExp, 0, wx.ALL, 2)

        self.elvisVariantDescrB.Add(self.workExpSBS, 0, wx.ALL, 2)


        self.cprSBS = wx.StaticBoxSizer(wx.StaticBox(self.elvisScrollable, wx.ID_ANY, u"HLR"), wx.HORIZONTAL)

        hlrTxt = u"Heltid på distans, HLR ingår. Slutprov i skolans lokal. För övrig information se www.nti.se."
        self.ElvisAlternCommentCPR = wx.TextCtrl(self.elvisScrollable, wx.ID_ANY, hlrTxt, wx.DefaultPosition,
                                       wx.Size(200, 150), wx.TE_MULTILINE)
        self.ElvisAlternCommentCPR.SetToolTip(u"Generell kursbeskrivning. Skriv som vid heltid.")
        self.cprSBS.Add(self.ElvisAlternCommentCPR, 0, wx.ALL, 2)

        self.elvisVariantDescrB.Add(self.cprSBS, 0, wx.ALL, 2)

        self.labSBS = wx.StaticBoxSizer(wx.StaticBox(self.elvisScrollable, wx.ID_ANY, u"Laboraton"), wx.HORIZONTAL)

        labTxt = u"Heltid på distans. Laboration och slutprov i skolans lokaler. För övrig information se www.nti.se."
        self.ElvisAlternCommentLAB = wx.TextCtrl(self.elvisScrollable, wx.ID_ANY, labTxt, wx.DefaultPosition,
                                       wx.Size(200, 150), wx.TE_MULTILINE)
        self.ElvisAlternCommentLAB.SetToolTip(u"Generell kursbeskrivning. Skriv som vid heltid.")
        self.labSBS.Add(self.ElvisAlternCommentLAB, 0, wx.ALL, 2)

        self.elvisVariantDescrB.Add(self.labSBS, 0, wx.ALL, 2)


        self.elvisVariantDescrSBS.Add(self.elvisVariantDescrB, 0, wx.ALL, 2)
        elvisGBS.Add(self.elvisVariantDescrSBS, wx.GBPosition(4, 5), wx.GBSpan(1, 1), wx.EXPAND, 5)

        # Kursinmatning slutar        

        self.elvisScrollable.SetSizer(elvisGBS)
        self.elvisScrollable.Layout()
        elvisGBS.Fit(self.elvisScrollable)
        elvisFeedBox.Add(self.elvisScrollable, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(elvisFeedBox)
        self.Layout()

        #Special event
        EVT_RESULT(self, self.getNextInChain)

        # Bind events
        self.elvisFilePicker.Bind(wx.EVT_FILEPICKER_CHANGED, self.setTmplFile)
        self.ElvisTemplFeedStart.Bind(wx.EVT_BUTTON, self.feedTemplates)
        self.ElvisLogin.Bind(wx.EVT_BUTTON, self.login)
        self.Elvis100_100Btn.Bind(wx.EVT_BUTTON, self.ElvisCoursesStart)
        self.Elvis100_50Btn.Bind(wx.EVT_BUTTON, self.ElvisCoursesStart)
        self.Elvis100_25Btn.Bind(wx.EVT_BUTTON, self.ElvisCoursesStart)
        self.Elvis200_100Btn.Bind(wx.EVT_BUTTON, self.ElvisCoursesStart)
        self.Elvis200_50Btn.Bind(wx.EVT_BUTTON, self.ElvisCoursesStart)
        self.Elvis200_25Btn.Bind(wx.EVT_BUTTON, self.ElvisCoursesStart)
        self.Elvis150_100Btn.Bind(wx.EVT_BUTTON, self.ElvisCoursesStart)
        self.Elvis150_50Btn.Bind(wx.EVT_BUTTON, self.ElvisCoursesStart)
        self.Elvis150_25Btn.Bind(wx.EVT_BUTTON, self.ElvisCoursesStart)
        self.Elvis50_50Btn.Bind(wx.EVT_BUTTON, self.ElvisCoursesStart)
        self.Elvis50_25Btn.Bind(wx.EVT_BUTTON, self.ElvisCoursesStart)
        self.ElvisAPL100_100Btn.Bind(wx.EVT_BUTTON, self.ElvisAltCourseStart)
        self.ElvisHLR100_100Btn.Bind(wx.EVT_BUTTON, self.ElvisAltCourseStart)
        self.ElvisLAB100_100Btn.Bind(wx.EVT_BUTTON, self.ElvisAltCourseStart)
        self.ElvisAPL100_50Btn.Bind(wx.EVT_BUTTON, self.ElvisAltCourseStart)
        self.ElvisHLR100_50Btn.Bind(wx.EVT_BUTTON, self.ElvisAltCourseStart)
        self.ElvisLAB100_50Btn.Bind(wx.EVT_BUTTON, self.ElvisAltCourseStart)
        self.ElvisAPL100_25Btn.Bind(wx.EVT_BUTTON, self.ElvisAltCourseStart)
        self.ElvisHLR100_25Btn.Bind(wx.EVT_BUTTON, self.ElvisAltCourseStart)
        self.ElvisLAB100_25Btn.Bind(wx.EVT_BUTTON, self.ElvisAltCourseStart)
        self.ElvisAPL200_100Btn.Bind(wx.EVT_BUTTON, self.ElvisAltCourseStart)
        self.ElvisHLR200_100Btn.Bind(wx.EVT_BUTTON, self.ElvisAltCourseStart)
        self.ElvisLAB200_100Btn.Bind(wx.EVT_BUTTON, self.ElvisAltCourseStart)
        self.ElvisAPL200_50Btn.Bind(wx.EVT_BUTTON, self.ElvisAltCourseStart)
        self.ElvisHLR200_50Btn.Bind(wx.EVT_BUTTON, self.ElvisAltCourseStart)
        self.ElvisLAB200_50Btn.Bind(wx.EVT_BUTTON, self.ElvisAltCourseStart)
        self.ElvisAPL200_25Btn.Bind(wx.EVT_BUTTON, self.ElvisAltCourseStart)
        self.ElvisHLR200_25Btn.Bind(wx.EVT_BUTTON, self.ElvisAltCourseStart)
        self.ElvisLAB200_25Btn.Bind(wx.EVT_BUTTON, self.ElvisAltCourseStart)
        self.ElvisAPL150_100Btn.Bind(wx.EVT_BUTTON, self.ElvisAltCourseStart)
        self.ElvisHLR150_100Btn.Bind(wx.EVT_BUTTON, self.ElvisAltCourseStart)
        self.ElvisLAB150_100Btn.Bind(wx.EVT_BUTTON, self.ElvisAltCourseStart)
        self.ElvisAPL150_50Btn.Bind(wx.EVT_BUTTON, self.ElvisAltCourseStart)
        self.ElvisHLR150_50Btn.Bind(wx.EVT_BUTTON, self.ElvisAltCourseStart)
        self.ElvisLAB150_50Btn.Bind(wx.EVT_BUTTON, self.ElvisAltCourseStart)
        self.ElvisAPL150_25Btn.Bind(wx.EVT_BUTTON, self.ElvisAltCourseStart)
        self.ElvisHLR150_25Btn.Bind(wx.EVT_BUTTON, self.ElvisAltCourseStart)
        self.ElvisLAB150_25Btn.Bind(wx.EVT_BUTTON, self.ElvisAltCourseStart)
        self.ElvisAPL50_50Btn.Bind(wx.EVT_BUTTON, self.ElvisAltCourseStart)
        self.ElvisHLR50_50Btn.Bind(wx.EVT_BUTTON, self.ElvisAltCourseStart)
        self.ElvisLAB50_50Btn.Bind(wx.EVT_BUTTON, self.ElvisAltCourseStart)
        self.ElvisAPL50_25Btn.Bind(wx.EVT_BUTTON, self.ElvisAltCourseStart)
        self.ElvisHLR50_25Btn.Bind(wx.EVT_BUTTON, self.ElvisAltCourseStart)
        self.ElvisLAB50_25Btn.Bind(wx.EVT_BUTTON, self.ElvisAltCourseStart)
        self.Elvis100_100Templ.Bind(wx.EVT_TEXT, self.falseOrTrueTempl)
        self.Elvis100_50Templ.Bind(wx.EVT_TEXT, self.falseOrTrueTempl)
        self.Elvis100_25Templ.Bind(wx.EVT_TEXT, self.falseOrTrueTempl)
        self.Elvis200_100Templ.Bind(wx.EVT_TEXT, self.falseOrTrueTempl)
        self.Elvis200_50Templ.Bind(wx.EVT_TEXT, self.falseOrTrueTempl)
        self.Elvis200_25Templ.Bind(wx.EVT_TEXT, self.falseOrTrueTempl)
        self.Elvis150_100Templ.Bind(wx.EVT_TEXT, self.falseOrTrueTempl)
        self.Elvis150_50Templ.Bind(wx.EVT_TEXT, self.falseOrTrueTempl)
        self.Elvis150_25Templ.Bind(wx.EVT_TEXT, self.falseOrTrueTempl)
        self.Elvis50_50Templ.Bind(wx.EVT_TEXT, self.falseOrTrueTempl)
        self.Elvis50_25Templ.Bind(wx.EVT_TEXT, self.falseOrTrueTempl)

        self.Layout()

        self.Centre(wx.BOTH)
        self.Show(True)

        # Set values
        self.ElvisURL.SetValue(self.url)

    def __del__(self):
        pass

    def login(self, evt):
        if self.ef.loggedin == 1:
            dial = wx.MessageDialog(None, 'Du har redan påbörjat en session. Ska den stängas? Logga ut först om nödvändigt.', 'Info', wx.YES_NO)
            re = dial.ShowModal()
            if re == wx.YES:
                self.ef.closeDriver()
        self.ef.login(self.url, self.ElvisBrowser.GetValue())

    def feedTemplates(self, evt):
        if self.ef.loggedin == 0:
            dial = wx.MessageDialog(None, 'Du måste logga in först!', 'Info', wx.OK)
            dial.ShowModal()
            return
        try:
            self.ef.prepareTmplFeed(self.tmplfile)
        except FileNotFoundError:
            dial = wx.MessageDialog(None, 'Du måste välja mallfil', 'Info', wx.OK)
            dial.ShowModal()
            return
        if hasattr(self, 'ftt'):
            self.ftt.Destroy()
        ftt = feedTemplatesThread(self)
        ftt.start()

    def setTmplFile(self, evt):
        self.tmplfile = self.elvisFilePicker.GetPath()
        path, file = os.path.split(self.tmplfile)
        dirs = path.split('\\')
        lasttwo = dirs[-2:]
        lastwostr = ' ... ' + '\\'.join(lasttwo)
        self.elvisTemplSBS.GetStaticBox().SetLabel('Mallar (' + lastwostr + ')')
        self.ElvisTemplFile.SetValue(file)
        templs = open(self.tmplfile, 'rb')
        templstree = ET.parse(templs)
        root = templstree.getroot()
        self.Elvis100_100Templ.Clear()
        self.Elvis100_50Templ.Clear()
        self.Elvis100_25Templ.Clear()
        self.Elvis200_100Templ.Clear()
        self.Elvis200_50Templ.Clear()
        self.Elvis200_25Templ.Clear()
        self.Elvis150_100Templ.Clear()
        self.Elvis150_50Templ.Clear()
        self.Elvis150_25Templ.Clear()
        self.Elvis50_50Templ.Clear()
        self.Elvis50_25Templ.Clear()
        for templ in root.findall('Mall'):
            nm = templ.find('Namn').text
            if '100_100' in nm:
                self.Elvis100_100Templ.SetValue(nm.upper())
            elif '100_50' in nm:
                self.Elvis100_50Templ.SetValue(nm.upper())
            elif '100_25' in nm:
                self.Elvis100_25Templ.SetValue(nm.upper())
            elif '200_100' in nm:
                self.Elvis200_100Templ.SetValue(nm.upper())
            elif '200_50' in nm:
                self.Elvis200_50Templ.SetValue(nm.upper())
            elif '200_25' in nm:
                self.Elvis200_25Templ.SetValue(nm.upper())
            elif '150_100' in nm:
                self.Elvis150_100Templ.SetValue(nm.upper())
            elif '150_50' in nm:
                self.Elvis150_50Templ.SetValue(nm.upper())
            elif '150_25' in nm:
                self.Elvis150_25Templ.SetValue(nm.upper())
            elif '50_50' in nm:
                self.Elvis50_50Templ.SetValue(nm.upper())
            elif '50_25' in nm:
                self.Elvis50_25Templ.SetValue(nm.upper())

    def ElvisCoursesStart(self, evt):
        if self.ef.loggedin == 0:
            dial = wx.MessageDialog(None, 'Du måste logga in först!', 'Info', wx.OK)
            dial.ShowModal()
            return
        caller = evt.GetEventObject()
        btnText = caller.GetLabel()
        pointStr = re.search(r'\d+', btnText).group()
        pacestrings = ['heltid', 'halvtid', 'kvartstid']
        paceStr = ''
        for pacestring in pacestrings:
            if pacestring in btnText:
                paceStr = pacestring
                break
        pacedict = {'heltid': '100', 'halvtid': '50', 'kvartstid': '25'}
        tmpl = eval('self.Elvis' + pointStr + '_' + pacedict[paceStr] + 'Templ').GetValue()
        type = 'Normal'
        ready = self.ef.prepareCourseFeed(self.cfile, pointStr, paceStr, type)
        if ready:
            fct = feedCoursesThread(self, pointStr, pacedict[paceStr], type, tmpl)
            fct.start()
        else:
            dial = wx.MessageDialog(None, 'Inga kurser att markera', 'Info', wx.OK)
            dial.ShowModal()
            caller.Enable(False)
            return

    def ElvisAltCourseStart(self, evt):
        if self.ef.loggedin == 0:
            dial = wx.MessageDialog(None, 'Du måste logga in först!', 'Info', wx.OK)
            dial.ShowModal()
            return
        altBtn = evt.GetEventObject()
        type = altBtn.GetLabel()
        contSiz = altBtn.GetParent()
        cSLabel = contSiz.GetLabel()
        pointStr = re.search(r'\d+', cSLabel).group()
        pacestrings = ['heltid', 'halvtid', 'kvartstid']
        paceStr = ''
        for pacestring in pacestrings:
            if pacestring in cSLabel:
                paceStr = pacestring
                break
        pacedict = {'heltid': '100', 'halvtid': '50', 'kvartstid': '25'}
        tmpl = eval('self.Elvis' + pointStr + '_' + pacedict[paceStr] + 'Templ').GetValue()
        typeStr = type
        if type == 'Lab':
            typeStr = 'Laboration'
        ready = self.ef.prepareCourseFeed(self.cfile, pointStr, paceStr, typeStr)
        if ready:
            fct = feedAltCoursesThread(self, pointStr, pacedict[paceStr], type.upper(), tmpl)
            fct.start()
        else:
            dial = wx.MessageDialog(None, 'Inga kurser att markera', 'Info', wx.OK)
            dial.ShowModal()
            altBtn.Enable(False)
            return

    def getNextInChain(self, msg):
        t = msg.data
        print(t)

    def falseOrTrueTempl(self, evt):
        tOrNot = evt.GetEventObject()
        cont = tOrNot.GetParent()
        litter = cont.GetChildren()
        if len(tOrNot.GetValue()) > 2:
            litter[1].Enable(True)
            litter[2].Enable(True)
            litter[3].Enable(True)
            litter[4].Enable(True)
        else:
            litter[1].Enable(False)
            litter[2].Enable(False)
            litter[3].Enable(False)
            litter[4].Enable(False)

    def isTestRun(self, yes):
        if yes:
            self.cfile = self.testcfile
        else:
            self.cfile = self.sharpcfile
