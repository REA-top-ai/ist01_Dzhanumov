# задание 1
tort = ['торт',1]

household_chemicals = [
    ["стиральный порошок", 1],
    ["средство для мытья посуды", 1]
]

# задание 2

Names=['Ben', 'Holly', 'Ann']
dogs_names= ['Sharik', 'Gab', 'Beethoven']

names_and_dogs_names = zip(Names,dogs_names)

list_of_names_and_dogs_names = list(names_and_dogs_names)

print(list_of_names_and_dogs_names)

# задание 3

orders = ['маргаритки', 'васильки']
print(orders)

orders.append('тюльпаны')
orders.append('розы')

print(orders)

# задание 4

orders = ['маргаритка', 'лютик', 'львиный зев', 'гардения', 'лилия']

new_orders = orders + ['сирень', 'ирис']

broken_prices = [5, 3, 4, 5, 4] + [4]

# задание 5

list1 = [1,8]
list1 = list(range(9))
list2 = list(range(8))

# задание 6

list1 = list(range(5, 16, 3))

list2 = list(range(0, 40, 5))

# задание 7

first_names = ["Эйнсли", "Бен", "Чани", "Депак"]

age = []

age.append(42)

all_ages = [32, 41, 29] + age

name_and_age = zip(first_names, all_ages)

ids = range(4)


