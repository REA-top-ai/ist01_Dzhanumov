
def create_spreadsheet(title):
    print('Создание электронной таблицы с именем '+title+'')

create_spreadsheet('Загрузки')


def create_spreadsheet1(title,row_count = 1000):
    row_count = str(row_count)
    print('Создание электронной таблицы с именем '+title+' with '+row_count+' lines')

create_spreadsheet1('Приложения', 10)