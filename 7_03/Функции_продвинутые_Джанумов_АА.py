# task 1

tables = {
    1: ['Jiho', False],
    2: [],
    3: [],
    4: [],
    5: [],
    6: [],
    7: [],
}

def assign_table(table_number: int, name: str, vip_status = False):
    client = [name, vip_status]
    tables[table_number] = client

assign_table(6,'Yoni')
assign_table(4,'Carla')
print('номер стола: [имя гостя, статус vip]')
for i in tables:
    print(f'{i} : {tables[i]}')

# task 2

def print_order(*order_items):
    print(order_items)

print_order('Orange Juice','Apple Juice','Scrambled Eggs','Pancakes')

# task 3 refactoring task 1

tables = {
    1: {
'name': 'Jiho',
'vip_status': False,
'order': 'Orange Juice, Apple Juice'
},
2: {},
3: {},
4: {},
5: {},
6: {},
7: {},
}


def assign_table(table_number: int, name: str, vip_status = False):
    tables[table_number]['name'] = name
    tables[table_number]['vip_status'] = vip_status



def assign_and_print_order(table_number, *order_items):
    order = ''
    for i in order_items:
        order = order + ', ' + i
        print(i)
    tables[table_number]['orders'] = order
    print(tables)

assign_table(2,'Arwa', True)

assign_and_print_order(2,'Стейк','Морской окунь','Бутылка вина')

    