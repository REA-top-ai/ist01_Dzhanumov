# задание 1
from datetime import datetime

current_time = datetime.now()
print(current_time)

# задание 2

import random

random_list = []

random_list = [random.randint(1, 100) for i in range(101)]

print(random_list)

randomer_number = random.choice(random_list)

print(randomer_number)

# задание 3

from matplotlib import pyplot as plt

number_a = range(1, 13)

number_b = random.sample(range(1000), 12)

plt.plot(number_a, number_b)

plt.show()


# задание 4

from datetime import datetime

employees = [
    ["Иванов Иван Иванович", "Менеджер", datetime(2013, 10, 22), 250000],
    ["Сорокина Екатерина Матвеевна", "Аналитик", datetime(2020, 3, 12), 75000],
    ["Струков Иван Сергеевич", "Старший программист", datetime(2012, 4, 23), 150000],
    ["Корнеева Анна Игоревна", "Ведущий программист", datetime(2015, 2, 22), 120000],
    ["Старчиков Сергей Анатольевич", "Младший программист", datetime(2021, 11, 12), 50000],
    ["Бутенко Артем Андреевич", "Архитектор", datetime(2010, 2, 12), 200000],
    ["Савченко Алина Сергеевна", "Старший аналитик", datetime(2016, 4, 13), 100000]
]

def programmer_bonus(employee):
    if "программист" in employee[1]:
        return employee[3] * 0.03
    return 0


def holiday_bonus():
    bonuses = []
    for emp in employees:
        bonuses.append([emp[0], 2000])
    return bonuses


def index_salary():
    today = datetime.now()
    for emp in employees:
        years = (today - emp[2]).days / 365
        if years > 10:
            emp[3] *= 1.07
        else:
            emp[3] *= 1.05


def vacation_list():
    today = datetime.now()
    vacation_employees = []
    for emp in employees:
        months = (today - emp[2]).days / 30
        if months > 6:
            vacation_employees.append(emp[0])
    return vacation_employees


for emp in employees:
    bonus = programmer_bonus(emp)
    if bonus > 0:
        print(emp[0], bonus)

print(holiday_bonus())

index_salary()
print(employees)

print(vacation_list())


# задание 5

admin_number = random.randint(1, 9)
print("Число администрации: ", admin_number)

winners_count = 0
current_number = 1

while winners_count < 5:
    digits_sum = sum(int(digit) for digit in str(current_number))
    if digits_sum % admin_number == 0:
        print("Выигрышный номер:", current_number)
        winners_count += 1
    current_number += 1
    
print("Розыгрыш завершён")

# задание 6 я устал красиво писать


def brosochek(kolvo_or_count_nazivaete_kak_hotit):
    for i in range(kolvo_or_count_nazivaete_kak_hotit):
        a = random.randint(0,1)
        print('орел' if a == 1 else 'решка')

brosochek(int(input('напишите пож колво бросочков - ')))

# задание 7

def opyiat_brosochek(kolvo):
    for i in range(kolvo):
        face_of_cube = random.randint(1,6)
        print(f'вам выпала грань под номером {face_of_cube}')

opyiat_brosochek(int(input('колво пыток - ')))

# задание 8

len_password = int(input("введите длину пароля: "))

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" # нам же нельзя использовать string.ascii_letters

password = ""

for i in range(len_password):
    password += random.choice(letters)

print("Случайный пароль:", password)
