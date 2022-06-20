from xlsxwriter import Workbook
from sys import stdin

workbook = Workbook('res.xlsx')
worksheet = workbook.add_worksheet()

data = []

for i in stdin.read().split('\n')[:-2]:
    i = i.split()
    i = (i[0], int(i[1]))
    data.append(i)

for row, (item, price) in enumerate(data):
    worksheet.write(row, 0, item)
    worksheet.write(row, 1, price)

chart = workbook.add_chart({'type': 'pie'})

chart.add_series({'values': '=Sheet1!B1:{0}'.format('B' + str(len(data))),
                  'categories': '=Sheet1!A1:{0}'.format('A' + str(len(data)))})

worksheet.insert_chart('C3', chart)

workbook.close()