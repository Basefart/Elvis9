from xml.etree.ElementTree import Element, SubElement
from xml.etree import ElementTree as ET
import locale
from xml.dom import minidom
import os.path
from datetime import datetime
from datetime import timedelta
import math
import itertools
import subprocess

locale.setlocale(locale.LC_ALL, '')
locale.setlocale(locale.LC_ALL, 'swedish')

class ExemElvis:

    def __init__(self, parent, dictionary, path):
        self.parent = parent
        self.mydictionary = dictionary
        self.path = path

    def prettify(self, elem):
        rough_string = ET.tostring(elem, 'utf-8')
        reparsed = minidom.parseString(rough_string)
        return reparsed.toprettyxml(indent="\t", encoding="utf-8")

    def splitDict(self):
        n = 10 // 2  # length of smaller half
        i = iter(self.mydictionary.items())  # alternatively, i = d.iteritems() works in Python 2
        d1 = dict(itertools.islice(i, n))  # grab first n items
        d2 = dict(i)  # grab the rest

        return d1, d2

    '''
        'applicationstart'
        'applicationend'
        'coursestart'
    '''

    def saveTemplates2xml(self):
        d1, d2 = self.splitDict()
        file = self.path + "\\" + d1['feedname'] + 'mallar.xml'
        self.top = Element('Mallar')
        i = 0
        while i < len(d2):
            j = 0
            while j < 1:
                tmplName = 'Mall'
                tmpl = SubElement(self.top, tmplName)
                nm = SubElement(tmpl, 'Namn')
                nm.text = list(d2.values())[i]
                period = SubElement(tmpl, 'Period')
                period.text = d1['period']
                applstart = SubElement(tmpl, 'Ansökningsstart')
                applstart.text = d1['applicationstart']
                applend = SubElement(tmpl, 'Ansökningsslut')
                applend.text = d1['applicationend']
                cstart = SubElement(tmpl, 'Kursstart')
                cstart.text = d1['coursestart']
                i += 1
                j += 1
                while j < 4:
                    elemTg = list(d2.keys())[i].replace('courseEnd', 'Kursslut').replace('1', '').replace('2', '').replace('5', '').replace('0', '')
                    elemTg = elemTg.replace('Full', '').replace('Half', '').replace('Quart', '').replace('weeks', 'Veckor').replace('descr', 'Beskrivning')
                    elem = SubElement(tmpl, elemTg)
                    elem.text = list(d2.values())[i]
                    i += 1
                    j += 1
        self.finalxmlstring = self.prettify(self.top)
        self.finalxml = ET.ElementTree(ET.fromstring(self.finalxmlstring))
        self.root = self.finalxml.getroot()
        self.root.set("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")
        self.finalxml.write(file, encoding="utf-8", method="xml")
        line = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        with open(file, 'r+') as f:
            file_data = f.read()
            f.seek(0, 0)
            f.write(line.rstrip('\r\n') + '\n' + file_data)
        subprocess.Popen('explorer ' + self.path)
