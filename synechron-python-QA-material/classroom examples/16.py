import xlwt
wb = xlwt.Workbook()
ws = wb.add_sheet('Marks List')
f=open("c:\\users\\tring\\desktop\\synechron3\\marks.csv","r")
for rowno, line in enumerate(f):
    for colno,data in enumerate(line.rstrip().split(",")):
        ws.write(rowno, colno, data)
wb.save('marks.xls')
f.close()

