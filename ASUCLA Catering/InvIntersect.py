import xlrd
import re
# Catering/Greenhouse Food inventory List reader
# looks for the intersection between the two lists and will act on said intersection
# Can easily be modified to check other lists and to be more general
#
# InvIntersect.py
# Achille C. Hebert III
# Copyright © Achille. 7/31/19
#

#TODO: Print out col 01234 from old sheet on hit
new = xlrd.open_workbook('C:\\Users\\achil\\Downloads\\205 Inventory\\SSS Inventory 205 FY 19-20.xls')
old = xlrd.open_workbook('C:\\Users\\achil\\Downloads\\205 Inventory\\Period 2 205.xls')

#Indexes for columns and rows etcetc. begins at [0]
##Column that match up for both sheets
newName = 0
newUnit = 1

oldName = 1
oldUnit = 2

##Row Tracker variables for both sheets(set to initial location)
NRow = 7
ORow = 7

#assigning food sheet to respective variables
nFood = new.sheet_by_index(0)
oFood = old.sheet_by_index(1)

while NRow < 849:
    while ORow < 449:
        if ("".join(re.split("[^a-zA-Z]*", oFood.cell_value(NRow, newName)))).upper() == ("".join(re.split("[^a-zA-Z]*", nFood.cell_value(ORow, oldName)))).upper():
            #Line below is for comparing the right neighboring column(unit) column, making the search stricter
            if ("".join(re.split("[^a-zA-Z]*", oFood.cell_value(NRow, newUnit)))).upper() == ("".join(re.split("[^a-zA-Z]*", nFood.cell_value(ORow, oldUnit)))).upper():
                print(oFood.cell_value(NRow, newName))
                break
        ORow += 1
    NRow += 1
#debug statements
#print(oFood.cell_value(7, nameCol))
