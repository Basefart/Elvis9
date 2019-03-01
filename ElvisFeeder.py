from xml.etree import ElementTree as ET
from xml.etree.ElementTree import ParseError
import locale
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, NoSuchWindowException, WebDriverException, TimeoutException, ElementNotVisibleException,StaleElementReferenceException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import time
import wx

locale.setlocale(locale.LC_ALL, '')
locale.setlocale(locale.LC_ALL, 'swedish')

class anmkod(object):

    def __init__(self, anmkod):
        self.anmkod = anmkod

    def getanmkod(self):
        return self.anmkod

class ElvisFeeder:

    def __init__(self, parent):
        self.parent = parent
        self.loggedin = 0
        self.url = ''
        self.tmplfile = ''
        self.cfile = ''
        self.browser = ''
        self.delay = 0.5
        self.tmplsList = []
        self.courseList = []

    def readysteadygo(self):
        time.sleep(self.delay)
        element = False
        timeout = time.time() + 20
        while not element:
            try:
                element = driver.find_element_by_id('ctl00_Img3')
                if time.time() > timeout:
                    driver.quit()
            except NoSuchElementException:
                pass
        time.sleep(self.delay)
        return True

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


    def choosetemplate(self, template):
        try:
            tmplslc = Select(driver.find_element_by_id('ctl00_cph_tc1_tb3_KursstartMallarDropDownList'))
            if tmplslc.first_selected_option == template:
                return
            else:
                tmplslc.select_by_visible_text(template)
        except NoSuchElementException:
            tmplslc = Select(driver.find_element_by_name('ctl00$cph$tc1$tb3$KursstartMallarDropDownList'))
            if tmplslc.first_selected_option == template:
                return
            else:
                tmplslc.select_by_visible_text(template)

    def prepareTmplFeed(self, file):
        self.file = file
        templs = open(self.file, 'rb')
        try:
            templstree = ET.parse(templs)
        except ParseError:
            dial = wx.MessageDialog(None, 'Är detta verkligen en mallfil?', 'Que?', wx.ICON_QUESTION)
            dial.ShowModal()
            return
        root = templstree.getroot()
        tmplbranches = root.findall('Mall')
        for branch in tmplbranches:
            tmplDict = {}
            for twig in branch:
                tmplDict.update({twig.tag: twig.text})
            self.tmplsList.append(tmplDict)

    def prepareCourseFeed(self, file, points, pace, type):
        self.file = file
        courses = open(self.file, 'rb')
        coursestree = ET.parse(courses)
        root = coursestree.getroot()
        coursebranches = root.findall('course')
        for branch in coursebranches:
            if branch[2].text == str(points) and branch[6].text == type:
                courseDict = {}
                key = ''
                val = ''
                for twig in branch:
                    if twig.tag == 'anmkod':
                        key = twig.text
                    if twig.tag == pace:
                        val = twig.text
                    courseDict.update({key: val})
                self.courseList.append(courseDict)
        if self.courseList:
            return True
        else:
            return False

    def tmplFeeder(self, template):
        cu = driver.current_url.split('/')
        if cu[-2] == 'admin' and cu[-1] == 'AdmKurskatalog.aspx':
            pass
        else:
            besturl =cu[0] + '//' + cu[2] + '/admin/AdmKurskatalog.aspx'
            driver.get(besturl)
        while not self.readysteadygo():
            if self.readysteadygo():
                break
        randominput = driver.find_element_by_id('ctl00_cph_tc1_tb1_SokKursstartkurskodTB')
        actions = ActionChains(driver)
        actions.move_to_element(randominput)
        actions.move_by_offset(0, -73)
        actions.click()
        actions.perform()
        while not self.readysteadygo():
            if self.readysteadygo():
                break
        newTmpl = driver.find_element_by_id('ctl00_cph_tc1_tb4_NyMallButton')
        newTmpl.click()
        time.sleep(0.2)
        nmTxt = driver.find_element_by_id('ctl00_cph_tc1_tb4_MallNamnKursstartTextBox')
        nmTxt.clear()
        nmTxt.send_keys(template['Namn'])
        time.sleep(0.2)
        stateCb = driver.find_element_by_id('ctl00_cph_tc1_tb4_MallAktivKursstartCb')
        if stateCb.is_selected():
            pass
        else:
            stateCb.click()
        time.sleep(0.2)
        perSlc = Select(driver.find_element_by_id('ctl00_cph_tc1_tb4_MallPeriodDropDownList'))
        if perSlc.first_selected_option == template['Period']:
            pass
        else:
            perSlc.select_by_visible_text(template['Period'])
        time.sleep(0.2)
        applyFrom = driver.find_element_by_id('ctl00_cph_tc1_tb4_MallSokbarFromTextBox')
        if applyFrom.get_attribute('value') == template['Ansökningsstart']:
            pass
        else:
            applyFrom.clear()
            applyFrom.send_keys(template['Ansökningsstart'])
        time.sleep(0.2)
        applyTo = driver.find_element_by_id('ctl00_cph_tc1_tb4_MallSokbarTomTextBox')
        if applyTo.get_attribute('value') == template['Ansökningsslut']:
            pass
        else:
            applyTo.clear()
            applyTo.send_keys(template['Ansökningsslut'])
        time.sleep(0.2)
        courseStart = driver.find_element_by_id('ctl00_cph_tc1_tb4_MallKursstartTextBox')
        if courseStart.get_attribute('value') == template['Kursstart']:
            pass
        else:
            courseStart.clear()
            courseStart.send_keys(template['Kursstart'])
        time.sleep(0.2)
        courseEnd = driver.find_element_by_id('ctl00_cph_tc1_tb4_MallKursslutTb')
        if courseEnd.get_attribute('value') == template['Kursslut']:
            pass
        else:
            courseEnd.clear()
            courseEnd.send_keys(template['Kursslut'])
        time.sleep(0.2)
        weeks = driver.find_element_by_id('ctl00_cph_tc1_tb4_MallAntVeckorTb')
        if weeks.get_attribute('value') == template['Veckor']:
            pass
        else:
            weeks.clear()
            weeks.send_keys(template['Veckor'])
        time.sleep(0.2)
        descrBoxLabel = driver.find_element_by_xpath("//div[@id='ctl00_cph_tc1_tb4_KursstartPanel']/div/div[2]/div/label")
        actions = ActionChains(driver)
        actions.move_to_element(descrBoxLabel)
        actions.move_by_offset(10, 80)
        actions.click()
        actions.key_down(Keys.CONTROL)
        actions.send_keys('a')
        actions.key_up(Keys.CONTROL)
        actions.send_keys(template['Beskrivning'])
        actions.perform()
        time.sleep(0.2)
        submitBtn = driver.find_element_by_id('ctl00_cph_tc1_tb4_SparaMallButton')
        submitBtn.click()

    def feedTmplWaitress(self):
        for template in self.tmplsList:
            if self.readysteadygo():
                self.tmplFeeder(template)



    def login(self, url, browser):
        global driver
        self.url = url
        self.browser = browser
        if self.browser == 'Google Chrome':
            driver = webdriver.Chrome()
        elif self.browser == 'Mozilla Firefox':
            driver = webdriver.Firefox()
        elif self.browser == 'Välj webbläsare':
            dial = wx.MessageDialog(None, 'Du måste välja webbläsare!', 'Info', wx.OK)
            dial.ShowModal()
            return
        driver.get(self.url)
        self.loggedin = 1

    def closeDriver(self):
        driver.close()

    def listCourses(self, points, pace, type, tmpl):
        try:
            pointiff = 0
            pointiffcount = 0
            gridtable = driver.find_element_by_id('ctl00_cph_tc1_tb3_FleraAnmkoderGridView')
            trlist = gridtable.find_elements_by_tag_name('tr')
            del trlist[0]
            for tr in trlist:
                tdlist = tr.find_elements_by_tag_name('td')
                pointiff += int(tdlist[2].text)
                pointiffcount += 1

            if int(pointiff/pointiffcount) == int(points):
                self.markAndSave(pace, type, tmpl)
            else:
                self.listCoursesByPoints(points, pace, type, tmpl)
        except NoSuchElementException:
            self.listCoursesByPoints(points, pace, type, tmpl)

    def listCoursesByPoints(self, points, pace, type, tmpl):
        kk = driver.find_element_by_partial_link_text('urskatalog')
        kk.click()
        while not self.readysteadygo():
            if self.readysteadygo():
                break
        anmkod = driver.find_element_by_id('ctl00_cph_tc1_tb1_arbetssattRbtnL_1')
        anmkod.click()
        while not self.readysteadygo():
            if self.readysteadygo():
                break
        schoolclickable = driver.find_element_by_xpath(
            '//div[@id="ctl00_cph_tc1_tb1_pnl29"]/span[@class="ui-dropdownchecklist-wrapper"]')
        ActionChains(driver).move_to_element(schoolclickable).click(schoolclickable).move_by_offset(0,
                                    25).click().move_by_offset(0, -100).click().perform()
        while not self.readysteadygo():
            if self.readysteadygo():
                break
        try:
            txt = driver.find_element_by_id('ctl00_cph_tc1_tb1_SokAnmalningskodPoangTB')
            txt.send_keys(points)
        except ElementNotVisibleException:
            txt = driver.find_element_by_name('ctl00$cph$tc1$tb1$SokAnmalningskodPoangTB')
            txt.send_keys(points)
        while not self.readysteadygo():
            if self.readysteadygo():
                break
        ActionChains(driver).move_to_element(txt).move_by_offset(0, 47).click().move_by_offset(0, 47).click().move_by_offset(0, -100).click().perform()
        while not self.readysteadygo():
            if self.readysteadygo():
                break
        studyformclickable = driver.find_element_by_xpath(
            '//div[@id="ctl00_cph_tc1_tb1_pnl31"]/span[@class="ui-dropdownchecklist-wrapper"]')
        studyformclickable.click()
        dropdowncbs = driver.execute_script('return document.getElementsByClassName("ui-dropdownchecklist-text")')
        for dropdowncb in dropdowncbs:
            if dropdowncb.text == 'Distans':
                dropdowncb.click()

        '''ActionChains(driver).move_to_element(studyformclickable).click(studyformclickable).move_by_offset(0,
                                        25).click().move_by_offset(0, -100).click().perform()'''
        '''
        Man bör kunna få fram med ett javascript eller css selector efter att man har klickat så att den blir synlig. 
        '''

        try:
            packageornotSlc = Select(driver.find_element_by_id('ctl00_cph_tc1_tb1_SokAnmkodKurspaketDDL'))
            packageornotSlc.select_by_visible_text('Nej')
        except (ElementNotVisibleException, NoSuchElementException):
            packageornotSlc = Select(driver.find_element_by_name('ctl00$cph$tc1$tb1$SokAnmkodKurspaketDDL'))
            packageornotSlc.select_by_visible_text('Nej')
        while not self.readysteadygo():
            if self.readysteadygo():
                break
        try:
            activeornotSlc = Select(driver.find_element_by_id('ctl00_cph_tc1_tb1_SokAnmkodAktivDDL'))
            activeornotSlc.select_by_visible_text('Ja')
        except (ElementNotVisibleException, NoSuchElementException):
            activeornotSlc = Select(driver.find_element_by_name('ctl00$cph$tc1$tb1$SokAnmkodAktivDDL'))
            activeornotSlc.select_by_visible_text('Ja')
        nrgridrows = driver.find_element_by_id('ctl00_cph_tc1_tb1_AnmkoderGridRaderPerSida')
        nrgridrows.clear()
        nrgridrows.send_keys('600')
        submitbtn = driver.find_element_by_id('ctl00_cph_tc1_tb1_SokAnmkodBtn')
        submitbtn.click()
        while not self.readysteadygo():
            if self.readysteadygo():
                break
        orderadjust = driver.find_element_by_id('ctl00_cph_tc1_tb1_SokAnmkodGv_ctl01_kursstortlbtn')
        orderadjust.click()
        while not self.readysteadygo():
            if self.readysteadygo():
                break
        try:
            checkall = driver.find_element_by_id('tl00_cph_tc1_tb1_SokAnmkodGv_ctl01_SokanmkodMarkeraAlla')
            checkall.click()
        except NoSuchElementException:
            checkall = driver.find_element_by_name('ctl00$cph$tc1$tb1$SokAnmkodGv$ctl01$SokanmkodMarkeraAlla')
            checkall.click()
        makecoursestarts = driver.find_element_by_id('ctl00_cph_tc1_tb1_arbetaMfleraAnmkoderBtn')
        makecoursestarts.click()
        self.markAndSave(pace, type, tmpl)

    def markAndSave(self, pace, type, tmpl):
        while not self.readysteadygo():
            if self.readysteadygo():
                break
        toclick = []
        toclickid = []
        for course in self.courseList:
            for key, value in course.items():
                if value == 'True':
                    toclick.append(key)
        while not self.readysteadygo():
            if self.readysteadygo():
                break
        # Här rensar jag bort tidigare iklickade
        try:
            checkallornone = driver.find_element_by_id('ctl00_cph_tc1_tb3_FleraAnmkoderGridView_ctl01_MarkeraAllaCheckBox')
            checkallornone.click()
            while not self.readysteadygo():
                if self.readysteadygo():
                    break
            checkallornone = driver.find_element_by_id('ctl00_cph_tc1_tb3_FleraAnmkoderGridView_ctl01_MarkeraAllaCheckBox')
            checkallornone.click()
        except (NoSuchElementException, ElementNotVisibleException):
            checkallornone = driver.find_element_by_name('ctl00$cph$tc1$tb3$FleraAnmkoderGridView$ctl01$MarkeraAllaCheckBox')
            checkallornone.click()
            while not self.readysteadygo():
                if self.readysteadygo():
                    break
            checkallornone = driver.find_element_by_name('ctl00$cph$tc1$tb3$FleraAnmkoderGridView$ctl01$MarkeraAllaCheckBox')
            checkallornone.click()
        gridtable = driver.find_element_by_id('ctl00_cph_tc1_tb3_FleraAnmkoderGridView')
        trlist = gridtable.find_elements_by_tag_name('tr')
        del trlist[0]
        for tr in trlist:
            tdlist = tr.find_elements_by_tag_name('td')
            if tdlist[0].text in toclick:
                cb = tr.find_element_by_tag_name('input')
                toclick.remove(tdlist[0].text)
                cb_id = cb.get_attribute('id')
                toclickid.append(cb_id) 
        for x in toclickid:
            driver.find_element_by_id(x).click()
        # Här verkar det fungera. Finns säkert något säkrare
        processtabsheader = driver.find_element_by_id('ctl00_cph_tc1_header')
        processtabs = processtabsheader.find_elements_by_tag_name('span')
        for processtab in processtabs:
            try:
                if processtab.get_attribute('class') == 'ajax__tab_active':
                    active = processtab.find_element_by_class_name('ajax__tab_tab').text
                    if active.strip() == 'Kursstart (3)':
                        self.choosetemplate(tmpl)
            except StaleElementReferenceException:
                self.choosetemplate(tmpl)
        descr = ''
        if type == 'APL':
            descr = self.parent.ElvisAlternCommentWorkExp.GetValue()
        elif type == 'HLR':
            descr = self.parent.ElvisAlternCommentCPR.GetValue()
        elif type == 'LAB':
            descr = self.parent.ElvisAlternCommentLAB.GetValue()
        if pace == '50':
            descr = self.halfpaceadjust(descr)
        elif pace == '25':
            descr = self.quartpaceadjust(descr)
        actions = ActionChains(driver)
        descrBoxLabel = driver.find_element_by_xpath("//div[@id='ctl00_cph_tc1_tb3_GenerellKursstartPanel']/div/div[2]/div/label")
        actions.move_to_element(descrBoxLabel)
        actions.move_by_offset(515, 51)
        actions.click()
        actions.key_down(Keys.CONTROL)
        actions.send_keys('a')
        actions.key_up(Keys.CONTROL)
        actions.send_keys(descr)
        actions.perform()

        self.courseList = []
        external_link = driver.find_element_by_id('ctl00_cph_tc1_tb3_KursstartExternLankTextBox')
        external_link.clear()
        external_link.send_keys('https://www.nti.se')
        sokbar = driver.find_element_by_id('ctl00_cph_tc1_tb3_KursstartSokbarCheckBox')
        if not sokbar.is_selected():
            sokbar.click()

        # Klicka på sparaknappen.

