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