import xlsxwriter
import sys


def export_check(text):
    workbook = xlsxwriter.Workbook('res.xlsx')
    worksheet = workbook.add_worksheet()
    text = text.strip('\n').split('\n')
    data = []
    for i in range(len(text)):
        ul = text[i].split('\t')
        data.append((ul[0], ul[1], ul[2]))
    for row in range(len(data)):
        worksheet.write(row, 0, data[row][0])
        worksheet.write(row, 1, data[row][1])
        worksheet.write(row, 2, data[row][2])
        st1 = 'B' + str(row + 1)
        st2 = 'C' + str(row + 1)
        worksheet.write(row, 3, '=' + st1 + '*' + st2)
    # row += 1
    worksheet.write(len(text), 0, 'Итого')
    st1 = 'D' + str(1)
    st2 = 'D' + str(len(text))
    worksheet.write(len(text), 3, '=SUM(' + st1 + ':' + st2 + ')')
    workbook.close()


export_check(sys.stdin.read())