from openpyxl import Workbook
import csv
import glob
path = "*.csv"
for fname in glob.glob(path):
    print(fname)

    fname=fname.split('.')

    workbk = Workbook()
    workSpace = workbk.active

    with open(fname[0]+'.csv', 'r') as f:
        for row in csv.reader(f):
            workSpace.append(row)
    workbk.save(fname[0]+'.xlsx')

