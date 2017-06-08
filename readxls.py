# coding=utf-8
from pyh2 import *
import xlrd
import ItemStruct
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
data=xlrd.open_workbook('c:/Identity.xlsx')
data.sheet_names()
table=data.sheet_by_name('Identity')
nrows=table.nrows
ncolos=table.ncols
i=1
dic={}
# FID,POINTID,GRID_CODE,ID
#FID_POINT_dict,FID_GRID_dict,FID_ID_dict,ID_FID_dict
FID_GRID_dict={}
FID_ID_dict={}
ID_FID_dict={}
ID_GRID_dict={}
#求得结构POINT_GRID_dict
POINT_GRID_dict={}
#-----------------------
#先赋值
for i in range(1,nrows,1):
    key=int(table.cell(i,3).value)
    if key in ID_GRID_dict.keys():
        print ""
    else:
        ID_GRID_dict[key]=int(table.cell(i, 2).value)
#遍历
# FID,POINTID,GRID_CODE,ID
for i in range(1,nrows,1):
    FID=int(table.cell(i,0).value)
    POINTID=int(table.cell(i,1).value)
    GRID=int(table.cell(i,2).value)
    ID=int(table.cell(i,3).value)
    if int(table.cell(i,2).value)<=ID_GRID_dict[ID]:
        continue
    else:
        del ID_GRID_dict[ID]
        ID_GRID_dict[ID]=GRID

print ID_GRID_dict.__len__()
f=open(r'f:/222.txt','w')
for i in range(1,nrows,1):
    FID=int(table.cell(i,0).value)
    POINTID=int(table.cell(i,1).value)
    GRID=int(table.cell(i,2).value)
    ID=int(table.cell(i,3).value)
    if (ID in ID_GRID_dict.keys())and(GRID==ID_GRID_dict[ID]):
        f.write(str(FID)+"\t"+str(POINTID)+"\t"+str(GRID)+"\t"+str(ID)+"\n")
f.close()




























