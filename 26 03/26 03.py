from docxtpl import DocxTemplate


def create_training_sheet(class_name, subject_name, name, *marks):
    d = DocxTemplate(name)
    context = {'class_name': class_name,
               'subject_name': subject_name,
               'marks': [{'num': i, 'fio': marks[i][0], 'mark': marks[i][1]}
                         for i in range(len(marks))]}
    d.render(context)
    d.save("res.docx")