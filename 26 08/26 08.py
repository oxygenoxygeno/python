import xlsxwriter


def export_check(text):
    workbook = xlsxwriter.Workbook('res.xlsx')
    now = []
    for i in text:
        if i != '---':
            now.append(i)
        else:
            check(now, workbook)
        now = []
    if now:
        check(now, workbook)
    workbook.close()


def check(text, workbook):
    worksheet = workbook.add_worksheet()
    text = text.split('\n')
    for i in range(len(text)):
        text[i] = text.split('\t')
    text.sort(key=lambda xx: xx[0])
    x = 0
    while x != len(text):
        if tuple(text[x][:2]) == tuple(text[x + 1][:2]):
            text[x][2] += text[x + 1][2]
        else:
            x += 1
    for i in range(len(text)):
        name, price, num = text[i]
        worksheet.write(i, 0, name)
        worksheet.write(i, 1, int(price))
        worksheet.write(i, 2, int(num))
        worksheet.write(i, 3, '=B{}*C{}'.format(str(i + 1), str(i + 1)))
    worksheet.write(len(text), 0, 'Итого')
    worksheet.write(len(text), 3, '=SUM(D1:D{})'.format(str(len(text))))