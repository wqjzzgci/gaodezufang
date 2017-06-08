#coding:utf-8
#中文
from pyh2 import *
import xlrd
import sys
#reload(sys)
sys.setdefaultencoding('utf-8')
data=xlrd.open_workbook(u'E:/研发部生产问题管理表-2016.xlsx')
data.sheet_names()
table=data.sheet_by_name(u'管理表')
nrows=table.nrows
ncolos=table.ncols
page = PyH('My wonderful PyH page')
page.addCSS('myStylesheet1.css', 'myStylesheet2.css')
page.addJS('myJavascript1.js', 'myJavascript2.js')
myDiv=div(id='myopdiv')
myPar=myDiv<<div(id='myinnerdiv')<<p(id='myPar')
myPar << a('mya111111111111',href='#11')
myDiv.render()
page << myDiv
for k in range(3,nrows):
    tmp = table.cell(k, 7).value
    page << a(str(tmp).decode('utf-8'), href='#'+str(k))
    page <<br()
for i in range(3,nrows):
    page << div(cl='myclass', id=str(i))
    for j in range(1,ncolos):
        tmp1=table.cell(2,j).value
        tmp2=table.cell(3,j).value
        page << h4(str(tmp1).decode('utf-8'),cl='center')
        page<< p(str(tmp2).decode('utf-8'), id='myp')
page.printOut()
'''
for i in range(3,5):
    page << div(cl='myclass', id=str(i))
    for j in range(1,5):
        tmp1=table.cell(2,j)
        tmp2=table.cell(3,j)
        page << h4(str(tmp1).decode('unicode_escape').encode('utf-8'),cl='center')
        page<< p(str(tmp2).decode('unicode_escape').encode('utf-8'), id='myp')
page.printOut()'''