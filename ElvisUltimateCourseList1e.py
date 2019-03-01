import wx
import wx.lib.agw.ultimatelistctrl as ULC
from xml.etree import ElementTree as ET
from xml.etree.ElementTree import Element, SubElement
from ElvisCourseDialog2 import ElvisCourseDlg
from xml.dom import minidom
from ListSkeletonFiller import ListSkeletonFiller


class ElvisUltimateCourseList(wx.Panel):

    def __init__(self, parent, custsel):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(-1,-1), style=wx.WANTS_CHARS | wx.TAB_TRAVERSAL)
        self.ClearBackground()
        self.SetBackgroundColour(wx.Colour(255,255,255,120))
        self.exitFlag = 0
        self.custsel = custsel
        self.file = './courses.xml'
        if self.custsel == 'Välj kund':
            self.file = './courses.xml'
        elif self.custsel == 'Södertälje':
            self.file = './sodert_courses.xml'
        elif self.custsel == 'Freja':
            self.file = './freja_courses.xml'
        elif self.custsel == 'Huddinge':
            self.file = './hudd_courses.xml'
        elif self.custsel == 'Norrtälje':
            self.file = './norrt_courses.xml'
        elif self.custsel == 'Salem':
            self.file = './salem_courses.xml'
        elif self.custsel == 'Järfälla':
            self.file = './jarf_courses.xml'
        self.courselist = []
        font = wx.SystemSettings.GetFont(wx.SYS_DEFAULT_GUI_FONT)
        boldfont = wx.SystemSettings.GetFont(wx.SYS_DEFAULT_GUI_FONT)

        font.SetPointSize(11)
        boldfont.SetWeight(wx.FONTWEIGHT_BOLD)
        boldfont.SetPointSize(12)

        agwStyle = (ULC.ULC_HAS_VARIABLE_ROW_HEIGHT | ULC.ULC_REPORT | ULC.ULC_SINGLE_SEL |
                    ULC.ULC_STICKY_HIGHLIGHT | ULC.ULC_VRULES | ULC.ULC_HRULES | ULC.ULC_STICKY_NOSELEVENT)
        self.elvisulc = elvisulc = ULC.UltimateListCtrl(self, wx.ID_ANY, agwStyle=agwStyle)
        elvisulc.ClearBackground()
        elvisulc.SetBackgroundColour(wx.Colour(255, 255, 255, 120))
        elvisulc.SetFont(font)

        def makeheader(text, col):
            info = ULC.UltimateListItem()
            info._format = wx.LIST_FORMAT_LEFT
            info._mask = wx.LIST_MASK_TEXT | wx.LIST_MASK_FORMAT | ULC.ULC_MASK_FONT
            info._text = text
            info._font = boldfont
            elvisulc.InsertColumnInfo(col, info)

        cols = {'Anmälningskod': 0, 'Namn': 1, 'Poäng': 2, 'Heltid': 3, 'Halvtid': 4, 'Kvartstid': 5, 'Kurstyp': 6, 'Redigera': 7}
        for k, v in cols.items():
            makeheader(k, v)

        wx.CallAfter(self.setColWidth, elvisulc)

        rows, self.numrows = self.parsexml()

        i = 0
        self.listSkelly = ListSkeletonFiller(self, rows)

        while i < self.numrows:
            self.listSkelly.insertRowIndex(i)
            i += 1

        gbTotal = wx.GridBagSizer(0, 0)
        gbTotal.SetFlexibleDirection(wx.HORIZONTAL)
        gbTotal.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.newCbtn = wx.Button(self, wx.ID_ANY, u"Ny kurs", wx.DefaultPosition, wx.Size(-1, 40), 0)
        self.newCbtn.SetFont(
            wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString))
        self.newCbtn.SetMinSize(wx.Size(-1, 40))
        self.newCbtn.SetMaxSize(wx.Size(-1, 40))
        gbTotal.Add(self.newCbtn, wx.GBPosition(0, 1), wx.GBSpan(1, 1), wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL | wx.ALL, 8)
        self.newCbtn.Bind(wx.EVT_BUTTON, self.elvisNewCourse)

        listlabelTxt = 'Kurser för ' + self.custsel
        self.listlabel = wx.StaticText(self, wx.ID_ANY, u"", wx.DefaultPosition, wx.Size(-1, 40), 0)
        self.listlabel.Wrap(-1)
        self.listlabel.SetLabelText(listlabelTxt)
        self.listlabel.SetMinSize(wx.Size(-1, 40))
        self.listlabel.SetMaxSize(wx.Size(-1, 40))

        self.listlabel.SetFont(
            wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString))

        gbTotal.Add(self.listlabel, wx.GBPosition(0, 2), wx.GBSpan(1, 1), wx.ALIGN_RIGHT | wx.ALIGN_BOTTOM | wx.ALL, 20)
        gbTotal.Add(elvisulc, wx.GBPosition(1, 0), wx.GBSpan(1, 3), wx.EXPAND | wx.ALL, 8)

        gbTotal.AddGrowableCol(0)
        gbTotal.AddGrowableCol(1)
        gbTotal.AddGrowableRow(1)

        self.SetSizer(gbTotal)

    def setColWidth(self, elvisulc):
        elvisulc.SetColumnWidth(0, 150)
        elvisulc.SetColumnWidth(1, 400)
        elvisulc.SetColumnWidth(2, -2)
        elvisulc.SetColumnWidth(3, -2)
        elvisulc.SetColumnWidth(4, -2)
        elvisulc.SetColumnWidth(5, -2)
        elvisulc.SetColumnWidth(6, 100)
        elvisulc.SetColumnWidth(7, 100)

    def prettify(self, elem):
        rough_string = ET.tostring(elem, 'utf-8')
        reparsed = minidom.parseString(rough_string)
        return reparsed.toprettyxml(indent="\t", encoding="utf-8")

    def xmlsorter(self, col, xmltree):
        def getkey(elem):
            return elem.findtext(col)

        container = xmltree.findall('course')
        root = xmltree.getroot()
        container[:] = sorted(container, key=getkey)

        root.clear()
        for course in container:
            root.append(course)
        prettytreestr = self.prettify(root)
        prettytree = ET.ElementTree(ET.fromstring(prettytreestr))
        return prettytree

    def removeCourse(self, anmkod):
        tree = ET.parse(self.file)
        root = tree.getroot()
        for course in root.findall('course'):
            if course.find('anmkod').text == anmkod:
                root.remove(course)
        fileisclosed = self.xml2file(tree)
        if fileisclosed:
            self.courseDlg.prepReload()

    def appendNewCourse(self, coursed):
        tree = ET.parse(self.file)
        root = tree.getroot()
        c = SubElement(root, 'course')
        for key, value in coursed.items():
            if key is not 'id':
                elem = SubElement(c, key)
                elem.text = str(value)
        newtreebStr = ET.tostring(root, encoding="utf-8", method='xml')
        newtreebStr = newtreebStr.replace(b'\t', b'')
        newtreebStr = newtreebStr.replace(b'\n', b'')
        newtreeStr = newtreebStr.decode('UTF-8')
        newxmltree = ET.ElementTree(ET.fromstring(newtreeStr))
        return newxmltree

    def parsexml(self):
        self.cStarts = open(self.file, 'rb')
        self.starttree = ET.parse(self.cStarts)
        self.root = self.starttree.getroot()
        length = 0
        for course in self.root.findall('course'):
            courselist_inner = [course.find('anmkod').text, course.find('name').text, course.find('points').text,
                                course.find('heltid').text, course.find('halvtid').text,
                                course.find('kvartstid').text, course.find('kurstyp').text]
            self.courselist.append(courselist_inner)
            length += 1
        return self.courselist, length

    def changestate(self, anmkod, speed, state):
        courses = open(self.file, 'rb+')
        tree = ET.parse(courses)
        root = tree.getroot()
        for course in root.findall('course'):
            if course.find('anmkod').text == anmkod:
                course.find(speed).text = str(state)
        return self.xml2file(tree)


    def xml2file(self, tree):
        root = tree.getroot()
        root.set("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")
        tree.write(self.file, encoding="utf-8", method="xml")
        line = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        with open(self.file, 'r+') as f:
            file_data = f.read()
            f.seek(0, 0)
            f.write(line.rstrip('\r\n') + '\n' + file_data)
        return f.closed

    def onClickCourse(self, event):
        btn = event.GetEventObject()
        anmkod = btn.course
        if anmkod == 'Anmälningskoden':
            pass
        else:
            self.courseDlg = ElvisCourseDlg(self, anmkod)
            self.courseDlg.ShowModal()

    def elvisNewCourse(self, event):
        self.courseDlg = ElvisCourseDlg(self, 'Ny')
        self.courseDlg.ShowModal()

    def getDlgValues(self, anmkod):
        courses = open(self.file, 'rb')
        tree = ET.parse(courses)
        root = tree.getroot()
        coursedict = {}
        for course in root.findall('course'):
            if course.find('anmkod').text == anmkod:
                for child in course:
                    coursedict[child.tag] = child.text
        return coursedict

    def resurrectMyGrandfather(self):
        wx.CallLater(800, self.bigReload)

    def bigReload(self):
        self.GetParent().GetParent().onChangeCustomer(wx.EVT_COMBOBOX)

    def processDlgResponse(self, values):
        changed = False
        coursesfile = open(self.file, 'rb+')
        tree = ET.parse(coursesfile)
        root = tree.getroot()
        fileisclosed = False
        if values['id'] == 'Ny':
            # Ny kurs
            unsorted = self.appendNewCourse(values)
            newtree = self.xmlsorter('name', unsorted)
            fileisclosed = self.xml2file(newtree)
            self.courseDlg.prepReload()
        else:
            for course in root.findall('course'):
                if course.find('anmkod').text == values['id']:
                    if course.find('anmkod').text != values['anmkod'] or course.find('name').text != values['name'] \
                        or course.find('points').text != values['points'] or course.find('heltid').text != values['heltid'] \
                          or course.find('halvtid').text != values['halvtid'] or course.find('kvartstid').text != values['kvartstid']\
                            or course.find('kurstyp').text != values['kurstyp']:
                        changed = True
                        course.find('anmkod').text = values['anmkod']
                        course.find('name').text = values['name']
                        course.find('points').text = values['points']
                        course.find('heltid').text = values['heltid']
                        course.find('halvtid').text = values['halvtid']
                        course.find('kvartstid').text = values['kvartstid']
                        course.find('kurstyp').text = values['kurstyp']
                        fileisclosed = self.xml2file(tree)
                    else:
                        return
        if changed:
            self.courseDlg.prepReload()

    def presentSelf(self):
        return self

def __del__(self):
    pass